# Scorecard — MiniMax M2.1 (`MiniMax-M2.1`)

> Factual record, compiled by automated assessment: static code read + live browser run
> (Chromium, fresh Flask launch, Python 3.12). The model's own files in this folder are
> exactly as it produced them. **The qualitative assessment and final score are for the
> repository maintainers** — see the last section.

## Build (opencode session, build turn only)

| Metric | Value |
| --- | --- |
| opencode model id | `MiniMax-M2.1` |
| Provider / lab | MiniMax (served via minimax-coding-plan) |
| Wall time (build) | 4m 46s (286.2s) |
| Output tokens (build) | 6,639 |
| Reasoning tokens | 0 (not exposed by provider) |

Build turn only (single-turn session).

## Observed facts

| Property | Value |
| --- | --- |
| Runs (fresh Flask launch, Py3.12) | Yes — start → 31 questions → results, no runtime error |
| Questions | 31 |
| Options per question | 4 |
| App layout | `app.py` + templates (start, question, result) |
| New page per question | Yes — single `/quiz` route re-rendered as full pages (server-driven index) |
| State across pages | Flask signed session cookie: `score`, `question_index` |
| Correct-answer position distribution | A:10 B:14 C:6 D:1 |
| Answer/category visible before answering | No |
| Anti-skip guard | Radio `required` (client); server defaults a missing answer to -1 (counts incorrect) and advances anyway |
| Live score during quiz | No |
| Restart / Play Again | Yes — "Play Again" → `/` (clears session) |
| Navigation | Forward-only |
| Results page | Score X/31, performance message (no percentage, no per-question review) |
| Final score correct | Yes — option-A run scored 10/31, equal to the A-count |
| Python test files | None |
| `<meta viewport>` | Present |
| `secret_key` | `os.urandom(24)` (regenerated each process start) |

Factual notes:
- Question content is movie trivia (directors, actors, release facts, studios) rather than genre/type classification.
- Start submits via a GET form to `/quiz`. Start copy and the top result tier reference "30 questions" while the bank has 31. `debug=True`.

## Screenshots

| Start | Question | Results |
| --- | --- | --- |
| ![start](../../screenshots/minimax-m2.1-start.webp) | ![question](../../screenshots/minimax-m2.1-question.webp) | ![results](../../screenshots/minimax-m2.1-finish.webp) |

## Maintainer assessment

<!-- Repository maintainers: write the qualitative assessment (UI quality, polish,
     subjective calls) and assign the final score here. -->

**Score:** _TBD_
