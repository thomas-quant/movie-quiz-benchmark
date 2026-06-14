# Movie Types Quiz — Coding-Agent Benchmark

A head-to-head benchmark. Coding agents are each given the **same one-shot prompt** to
build a multi-page Flask quiz on the **types/genres of movies**, then judged on the result.
This repo holds every submission side by side, with the screenshots and scoring used to
compare them.

See **[`docs/METHODOLOGY.md`](docs/METHODOLOGY.md)** for the exact prompt, run conditions,
and how scoring works.

## Scoreboard

| Submission | Wall time | Output tokens | Questions | Score | Scorecard |
| --- | --- | --- | --- | --- | --- |
| **Codex v2** | 6m 40s | 41.1k | 30 | **+2** | [scorecard](openai/codex/v2/SCORECARD.md) |
| **Claude** | 5m 01s | 28.4k | 32 | **−1** | [scorecard](anthropic/claude/SCORECARD.md) |
| **Codex v1** | 5m 31s | 16.0k | 30 | **−3** | [scorecard](openai/codex/v1/SCORECARD.md) |

All submissions keep per-question state across pages via Flask's signed `session` cookie
and run on `http://127.0.0.1:5000`.

## Layout

```
docs/METHODOLOGY.md        # the prompt, run conditions, scoring rubric
anthropic/claude/          # Claude's submission (+ SCORECARD.md)
openai/codex/v1/           # Codex, first run (+ SCORECARD.md)
openai/codex/v2/           # Codex, re-run with the tweaked prompt (+ SCORECARD.md)
screenshots/               # captures used in the scorecards
```

Each submission folder holds the model's output exactly as produced, plus an
author-written `SCORECARD.md` with its metrics, score, and notes.

## Running any submission

Each app is self-contained. From its directory (e.g. `anthropic/claude`):

```bash
uv venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
uv run python app.py             # then open http://127.0.0.1:5000
```

Codex v1 can also be launched with `uv run flask --app app run --debug`, and its tests run
with `uv run python -m pytest -q`.
