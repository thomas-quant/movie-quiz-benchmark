#!/usr/bin/env python3
"""Capture standardized browser evidence from one Flask submission.

The runner is intentionally independent of the submission's own dependencies and
launches Flask through the CLI so hard-coded ``app.run(port=...)`` calls do not
affect the capture port. It writes screenshots, a Playwright trace, server output,
and a machine-readable flow record to the caller-supplied output directory.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import socket
import subprocess
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.request import urlopen
from urllib.parse import urlparse

from playwright.sync_api import BrowserContext, Locator, Page, Playwright, TimeoutError


VIEWPORT = {"width": 1440, "height": 1000}
DEVICE_SCALE_FACTOR = 2
MAX_STEPS_DEFAULT = 100

STABILITY_CSS = """
*, *::before, *::after {
  animation: none !important;
  transition: none !important;
  caret-color: transparent !important;
}
"""

RESULT_TEXT_PATTERNS = (
    "your score",
    "your results",
    "quiz complete",
    "quiz completed",
    "review your answers",
    "your movie type",
    "your genre profile",
    "take it again",
    "play it again",
    "play again",
    "try again",
)

START_TEXT_RE = re.compile(r"\b(start|begin|cue|take|launch)\b.*\b(quiz|screening|test)\b|\bstart\b", re.I)
CONTINUE_TEXT_RE = re.compile(
    r"\b(next|continue|finish|submit|confirm|lock it in|see (my )?results?|view results?|show results?)\b",
    re.I,
)


class CaptureError(RuntimeError):
    """Raised when the standardized flow cannot be completed."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submission", type=Path, required=True, help="Staged submission directory")
    parser.add_argument("--output", type=Path, required=True, help="External evidence output directory")
    parser.add_argument("--python", dest="python_executable", default=sys.executable, help="Python used to launch Flask")
    parser.add_argument("--entrypoint", default="app:app", help="Flask application entrypoint")
    parser.add_argument("--server-command", help="Optional command template; supports {python}, {entrypoint}, {host}, and {port}")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, help="Port to use; otherwise choose a free local port")
    parser.add_argument("--entry-path", default="/", help="Initial path to open")
    parser.add_argument("--startup-timeout", type=float, default=30.0)
    parser.add_argument("--step-timeout", type=float, default=12.0)
    parser.add_argument("--max-steps", type=int, default=MAX_STEPS_DEFAULT)
    parser.add_argument("--headed", action="store_true", help="Run headed; use under Xvfb on a VPS")
    parser.add_argument("--force", action="store_true", help="Allow an existing non-empty output directory")
    return parser.parse_args()


def choose_port(host: str) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, 0))
        return int(sock.getsockname()[1])


def build_server_command(args: argparse.Namespace, port: int) -> list[str]:
    template = args.server_command or (
        "{python} -m flask --app {entrypoint} run "
        "--host {host} --port {port} --no-debugger --no-reload"
    )
    values = {
        "python": str(args.python_executable),
        "entrypoint": args.entrypoint,
        "host": args.host,
        "port": str(port),
    }
    try:
        command = template.format(**values)
    except KeyError as exc:
        raise CaptureError(f"Unknown placeholder in --server-command: {exc}") from exc
    return shlex.split(command)


def wait_for_server(process: subprocess.Popen[str], url: str, timeout: float) -> None:
    deadline = time.monotonic() + timeout
    last_error = "server did not respond"
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise CaptureError(f"server exited with code {process.returncode}; see server.log")
        try:
            with urlopen(url, timeout=1.5) as response:
                if response.status < 500:
                    return
        except (OSError, URLError) as exc:
            last_error = str(exc)
        time.sleep(0.25)
    raise CaptureError(f"timed out waiting for {url}: {last_error}")


def terminate_process(process: subprocess.Popen[str]) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def clean_text(value: str) -> str:
    return " ".join(value.split())


def safe_inner_text(locator: Locator) -> str:
    try:
        return clean_text(locator.inner_text(timeout=500))
    except Exception:
        return ""


def visible(locator: Locator) -> bool:
    try:
        return locator.is_visible() and locator.is_enabled()
    except Exception:
        return False


def attr(locator: Locator, name: str) -> str:
    try:
        return (locator.get_attribute(name) or "").lower()
    except Exception:
        return ""


def find_radios(page: Page) -> Locator:
    return page.locator("input[type='radio']:visible")


def button_score(button: Locator, *, allow_navigation: bool = False) -> int:
    text = safe_inner_text(button).lower()
    value = attr(button, "value")
    name = attr(button, "name")
    classes = attr(button, "class")
    identity = " ".join((text, value, name, classes, attr(button, "id")))

    score = 0
    if name in {"answer", "choice", "option", "selected", "selected_answer"}:
        score += 100
    if any(token in classes for token in ("option", "answer", "choice")):
        score += 45
    if re.search(r"\b(next|submit|continue|finish|confirm|lock|result)\b", identity):
        score += 30
    if re.search(r"\b(previous|back|restart|reset|play again)\b", identity):
        score -= 100
    if not allow_navigation and re.search(r"\b(start|begin|cue|launch)\b", identity):
        score -= 100
    return score


def visible_buttons(page: Page) -> list[Locator]:
    candidates = page.locator("button:visible, input[type='submit']:visible")
    return [candidates.nth(i) for i in range(candidates.count()) if visible(candidates.nth(i))]


def find_answer_button(page: Page) -> Locator | None:
    buttons = visible_buttons(page)
    scored = [(button_score(button), button) for button in buttons]
    scored = [(score, button) for score, button in scored if score >= 45]
    if not scored:
        return None
    scored.sort(key=lambda item: item[0], reverse=True)
    return scored[0][1]


def find_start_action(page: Page) -> Locator | None:
    candidates = page.locator("button:visible, input[type='submit']:visible, a:visible")
    matches: list[tuple[int, Locator]] = []
    for index in range(candidates.count()):
        candidate = candidates.nth(index)
        if not visible(candidate):
            continue
        text = " ".join((safe_inner_text(candidate), attr(candidate, "value"), attr(candidate, "aria-label")))
        if "play again" in text.lower() or "restart" in text.lower():
            continue
        if START_TEXT_RE.search(text):
            score = 10 + (20 if "quiz" in text.lower() else 0)
            matches.append((score, candidate))
    return max(matches, key=lambda item: item[0])[1] if matches else None


def find_continue_action(page: Page) -> Locator | None:
    candidates = page.locator("button:visible, input[type='submit']:visible, a:visible")
    matches: list[tuple[int, Locator]] = []
    for index in range(candidates.count()):
        candidate = candidates.nth(index)
        if not visible(candidate):
            continue
        text = " ".join((safe_inner_text(candidate), attr(candidate, "value"), attr(candidate, "aria-label")))
        lowered = text.lower()
        if any(token in lowered for token in ("previous", "back", "restart", "reset", "play again")):
            continue
        if CONTINUE_TEXT_RE.search(text):
            score = 10
            if re.search(r"\b(next|continue|finish|see .*results?|view results?)\b", lowered):
                score += 20
            matches.append((score, candidate))
    return max(matches, key=lambda item: item[0])[1] if matches else None


def body_text(page: Page) -> str:
    try:
        return page.locator("body").inner_text(timeout=1000).lower()
    except Exception:
        return ""


def looks_like_result(page: Page) -> bool:
    path = urlparse(page.url).path.lower()
    if re.search(r"/(result|results|finish|complete|profile)(/|$)", path):
        return True
    text = body_text(page)
    return any(pattern in text for pattern in RESULT_TEXT_PATTERNS) and find_radios(page).count() == 0 and find_answer_button(page) is None


def has_question_controls(page: Page) -> bool:
    return find_radios(page).count() > 0 or find_answer_button(page) is not None


def settle(page: Page, timeout: float) -> None:
    try:
        page.wait_for_load_state("domcontentloaded", timeout=int(timeout * 1000))
    except TimeoutError:
        pass
    try:
        page.wait_for_load_state("networkidle", timeout=min(int(timeout * 1000), 4000))
    except TimeoutError:
        pass
    try:
        page.add_style_tag(content=STABILITY_CSS)
    except Exception:
        pass
    try:
        page.evaluate("document.fonts && document.fonts.ready")
    except Exception:
        pass
    page.wait_for_timeout(500)


def click(locator: Locator, timeout: float) -> None:
    try:
        locator.click(timeout=int(timeout * 1000))
    except Exception:
        locator.click(timeout=int(timeout * 1000), force=True)


def submit_radio_answer(page: Page, timeout: float) -> str:
    radios = find_radios(page)
    if radios.count() == 0:
        raise CaptureError("question page has no radio options")
    radio = radios.nth(0)
    radio.check(force=True)
    form = radio.locator("xpath=ancestor::form[1]")
    buttons = form.locator("button:visible, input[type='submit']:visible")
    action_candidates = [buttons.nth(i) for i in range(buttons.count()) if visible(buttons.nth(i))]
    scored = [(button_score(button, allow_navigation=True), button) for button in action_candidates]
    scored = [(score, button) for score, button in scored if score > 0]
    if scored:
        scored.sort(key=lambda item: item[0], reverse=True)
        click(scored[0][1], timeout)
    else:
        form.evaluate("form => form.requestSubmit()")
    return "radio:first"


def submit_answer(page: Page, timeout: float) -> str:
    if find_radios(page).count() > 0:
        return submit_radio_answer(page, timeout)
    button = find_answer_button(page)
    if button is None:
        raise CaptureError("could not find an answer control")
    click(button, timeout)
    return f"button:{safe_inner_text(button) or attr(button, 'value')}"


def capture(page: Page, path: Path) -> None:
    page.screenshot(path=str(path), type="png", full_page=True, scale="device")


def run_flow(page: Page, base_url: str, output: Path, args: argparse.Namespace) -> dict[str, Any]:
    flow: dict[str, Any] = {
        "status": "failed",
        "base_url": base_url,
        "start_url": None,
        "question_url": None,
        "results_url": None,
        "steps": [],
        "console_errors": [],
        "page_errors": [],
    }

    def record(action: str, before: str, after: str, **extra: Any) -> None:
        flow["steps"].append({"action": action, "before_url": before, "after_url": after, **extra})

    page.on("console", lambda message: flow["console_errors"].append(message.text) if message.type == "error" else None)
    page.on("pageerror", lambda error: flow["page_errors"].append(str(error)))

    start_url = base_url.rstrip("/") + "/" + args.entry_path.lstrip("/")
    page.goto(start_url, wait_until="domcontentloaded", timeout=int(args.step_timeout * 1000))
    settle(page, args.step_timeout)
    flow["start_url"] = page.url
    capture(page, output / "start.png")

    started = has_question_controls(page)
    if not started:
        starter = find_start_action(page)
        if starter is None:
            if looks_like_result(page):
                raise CaptureError("initial page is a result page")
            raise CaptureError("could not find a start action or question controls")
        before = page.url
        click(starter, args.step_timeout)
        settle(page, args.step_timeout)
        record("start", before, page.url, label=safe_inner_text(starter))
        started = True

    question_captured = False
    for step in range(args.max_steps):
        if looks_like_result(page):
            flow["results_url"] = page.url
            capture(page, output / "results.png")
            flow["status"] = "completed"
            flow["steps_taken"] = step
            return flow

        if has_question_controls(page):
            if not question_captured:
                flow["question_url"] = page.url
                capture(page, output / "question.png")
                question_captured = True
            before = page.url
            control = submit_answer(page, args.step_timeout)
            settle(page, args.step_timeout)
            record("answer", before, page.url, control=control, option_index=0)
            continue

        continuation = find_continue_action(page)
        if continuation is not None:
            before = page.url
            label = safe_inner_text(continuation) or attr(continuation, "value")
            click(continuation, args.step_timeout)
            settle(page, args.step_timeout)
            record("continue", before, page.url, label=label)
            continue

        raise CaptureError(f"stalled after {step} steps at {page.url}")

    raise CaptureError(f"exceeded --max-steps={args.max_steps} without reaching results")


def prepare_output(output: Path, force: bool) -> None:
    output.mkdir(parents=True, exist_ok=True)
    existing = list(output.iterdir())
    if existing and not force:
        names = ", ".join(item.name for item in existing[:5])
        raise CaptureError(f"output directory is not empty ({names}); use --force or a new directory")


def run(args: argparse.Namespace) -> int:
    submission = args.submission.resolve()
    output = args.output.resolve()
    if not submission.is_dir():
        raise CaptureError(f"submission directory does not exist: {submission}")
    prepare_output(output, args.force)

    port = args.port or choose_port(args.host)
    base_url = f"http://{args.host}:{port}"
    server_log = output / "server.log"
    command = build_server_command(args, port)
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    process: subprocess.Popen[str] | None = None
    metadata: dict[str, Any] = {
        "submission": submission.name,
        "server_command": command,
        "host": args.host,
        "port": port,
        "viewport": VIEWPORT,
        "device_scale_factor": DEVICE_SCALE_FACTOR,
        "headed": args.headed,
        "screenshots": ["start.png", "question.png", "results.png"],
        "status": "failed",
    }

    try:
        with server_log.open("w", encoding="utf-8") as log:
            process = subprocess.Popen(
                command,
                cwd=submission,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
                start_new_session=True,
            )
        wait_for_server(process, base_url + "/", args.startup_timeout)

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=not args.headed,
                args=["--disable-dev-shm-usage"],
            )
            context = browser.new_context(
                viewport=VIEWPORT,
                device_scale_factor=DEVICE_SCALE_FACTOR,
                locale="en-GB",
            )
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            try:
                flow = run_flow(page, base_url, output, args)
            except Exception as exc:
                flow = {
                    "status": "failed",
                    "error": str(exc),
                    "url": page.url,
                    "console_errors": [],
                    "page_errors": [],
                }
                try:
                    capture(page, output / "failure.png")
                except Exception:
                    pass
            finally:
                try:
                    context.tracing.stop(path=str(output / "trace.zip"))
                finally:
                    context.close()
                    browser.close()

        metadata.update(flow)
        metadata["status"] = flow.get("status", "failed")
    except Exception as exc:
        metadata.update({"status": "failed", "error": str(exc)})
    finally:
        if process is not None:
            terminate_process(process)
        (output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({"status": metadata["status"], "output": str(output)}, indent=2))
    return 0 if metadata["status"] == "completed" else 1


def main() -> int:
    args = parse_args()
    try:
        return run(args)
    except CaptureError as exc:
        print(f"capture failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
