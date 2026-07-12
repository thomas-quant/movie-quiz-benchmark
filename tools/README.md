# Capture tools

These tools prepare anonymized submission copies and capture standardized browser
evidence. They write to caller-supplied directories, so the original submissions
and the benchmark repository are not modified by a capture run.

## Setup on the VPS

Use a dedicated virtual environment for the tools:

```bash
uv venv /path/to/movie-benchmark-review-venv
source /path/to/movie-benchmark-review-venv/bin/activate
uv pip install -r /path/to/movie-benchmark/tools/requirements.txt
python -m playwright install chromium
```

The browser can run headless. If headed capture is preferred, use the VPS display:

```bash
xvfb-run -a python /path/to/movie-benchmark/tools/capture_runner.py \
  --headed \
  --submission /path/to/movie-benchmark-review/submissions/submission-001 \
  --output /path/to/movie-benchmark-review/evidence/submission-001
```

## Stage one submission

```bash
python /path/to/movie-benchmark/tools/stage_submission.py \
  --source /path/to/movie-benchmark/openai/codex/v3-sol \
  --destination /path/to/movie-benchmark-review/submissions/submission-001
```

The staging tool excludes git history, virtual environments, caches,
`README.md`, and `SCORECARD.md`. It keeps the application source, templates,
static assets, requirements, and tests.

## Capture evidence

The default launcher imports `app:app` through the Flask CLI and chooses a free
local port. This avoids hard-coded ports in `app.py` and prevents Flask's debug
reloader from creating extra processes.

```bash
python /path/to/movie-benchmark/tools/capture_runner.py \
  --submission /path/to/movie-benchmark-review/submissions/submission-001 \
  --output /path/to/movie-benchmark-review/evidence/submission-001
```

The runner automatically opens the initial page, starts the quiz if necessary,
selects the first answer on every question, handles intermediate feedback pages,
and stops at the results/profile page. It is deliberately route-agnostic and
uses visible controls rather than assuming a particular URL scheme.

Each evidence directory contains, when available:

- `start.png` — initial screen;
- `question.png` — first question before answering;
- `results.png` — final results/profile screen;
- `trace.zip` — Playwright trace;
- `metadata.json` — flow, URLs, capture settings, and errors;
- `server.log` — application output;
- `failure.png` — last visible page if the flow fails.

The screenshots use a fixed 1440×1000 CSS-pixel viewport, 2× device scale, a
consistent locale, disabled animations, and lossless PNG output. The runner exits
with status 0 only when it reaches a result/profile page.

## Custom server command

If a staged submission cannot be imported through Flask's CLI, provide a command
template. These placeholders are supported:

```bash
python tools/capture_runner.py \
  --submission /path/to/submission \
  --output /path/to/evidence \
  --server-command '{python} app.py'
```

The `{python}`, `{entrypoint}`, `{host}`, and `{port}` placeholders are available.
The custom command must honor `{host}` and `{port}` if it is expected to run on the
runner-selected port.
