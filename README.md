# Movie Types Quiz — Coding-Agent Benchmark

A benchmark of coding agents. Each is given the **same one-shot prompt** to build a
multi-page Flask quiz on the **types/genres of movies**, then assessed. Two cohorts so far:
the original **Codex vs Claude** head-to-head, and a set of models run via
**[opencode](https://opencode.ai)**. This repo holds every submission side by side, with
screenshots and a per-submission scorecard.

See **[`docs/METHODOLOGY.md`](docs/METHODOLOGY.md)** for the exact prompt, run conditions,
how the metrics are measured, and how scoring works.

## Scoreboard

### Scored — Codex vs Claude

| Submission | Wall time | Output tokens | Questions | Score | Scorecard |
| --- | --- | --- | --- | --- | --- |
| **Codex v2** | 6m 40s | 41.1k | 30 | **+2** | [scorecard](openai/codex/v2/SCORECARD.md) |
| **Claude** | 5m 01s | 28.4k | 32 | **−1** | [scorecard](anthropic/claude/SCORECARD.md) |
| **Codex v1** | 5m 31s | 16.0k | 30 | **−3** | [scorecard](openai/codex/v1/SCORECARD.md) |

### opencode runs — factual records, awaiting maintainer scoring

Build wall time and output tokens come from each model's opencode session, **build turn
only** (the one-shot prompt → files written; later follow-ups like "run on port N" are
excluded). Every app was launched fresh and driven start → results in a real browser; all
eight completed with **no runtime error**. Scores are **not yet assigned** — the scorecards
hold the facts and leave the qualitative call to the maintainers.

| Submission | opencode model | Build time | Output tokens | Questions | Score | Scorecard |
| --- | --- | --- | --- | --- | --- | --- |
| opencode / big-pickle | `big-pickle` | 1m 47s | 6,970 | 32 | _TBD_ | [scorecard](opencode/big-pickle/SCORECARD.md) |
| deepseek / v4-flash | `deepseek-v4-flash-free` | 1m 33s | 6,654 | 34 | _TBD_ | [scorecard](deepseek/v4-flash/SCORECARD.md) |
| xiaomi / mimo-v2.5 | `mimo-v2.5-free` | 1m 35s | 7,055 | 34 | _TBD_ | [scorecard](xiaomi/mimo-v2.5/SCORECARD.md) |
| minimax / m2 | `MiniMax-M2` | 1m 41s | 7,786 | 41 | _TBD_ | [scorecard](minimax/m2/SCORECARD.md) |
| minimax / m2.1 | `MiniMax-M2.1` | 4m 46s | 6,639 | 31 | _TBD_ | [scorecard](minimax/m2.1/SCORECARD.md) |
| minimax / m2.5 | `MiniMax-M2.5` | 3m 51s | 15,396 | 30 | _TBD_ | [scorecard](minimax/m2.5/SCORECARD.md) |
| minimax / m2.7 | `MiniMax-M2.7-highspeed` | 1m 52s | 4,924 | 35 | _TBD_ | [scorecard](minimax/m2.7/SCORECARD.md) |
| minimax / m3 | `MiniMax-M3` | 2m 24s | 8,570 | 30 \* | _TBD_ | [scorecard](minimax/m3/SCORECARD.md) |

\* `minimax/m3` is a personality / genre-match quiz (options map to genres, no correct
answers) rather than a knowledge quiz.

All submissions keep per-question state across pages via Flask's signed `session` cookie.

## Layout

```
docs/METHODOLOGY.md          # the prompt, run conditions, how metrics + scoring work
anthropic/claude/            # Claude's submission (+ SCORECARD.md)
openai/codex/v1/             # Codex, first run (+ SCORECARD.md)
openai/codex/v2/             # Codex, re-run with the tweaked prompt (+ SCORECARD.md)
opencode/big-pickle/         # stealth model, lab undisclosed (+ SCORECARD.md)
deepseek/v4-flash/           # (+ SCORECARD.md)
xiaomi/mimo-v2.5/            # MiMo (+ SCORECARD.md)
minimax/m2/  m2.1/  m2.5/  m2.7/  m3/   # MiniMax family (each + SCORECARD.md)
screenshots/                 # captures used in the scorecards
```

Each submission folder holds the model's output exactly as produced, plus a `SCORECARD.md`.
For the original Codex/Claude entries the scorecard includes the maintainer's notes and
score; for the opencode entries it records facts only and leaves a blank maintainer section.

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
