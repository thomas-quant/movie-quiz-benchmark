# Scorecard — MiniMax M2.5 (`MiniMax-M2.5`)

> Factual record, compiled by automated assessment: static code read + live browser run
> (Chromium, fresh Flask launch, Python 3.12). The model's own files in this folder are
> exactly as it produced them. **The qualitative assessment and final score are for the
> repository maintainers** — see the last section.

## Build (opencode session, build turn only)

| Metric | Value |
| --- | --- |
| opencode model id | `MiniMax-M2.5` |
| Provider / lab | MiniMax (served via minimax-coding-plan) |
| Wall time (build) | 3m 51s (230.9s) |
| Output tokens (build) | 15,396 |
| Reasoning tokens | 0 (not exposed by provider) |

Build turn only (single-turn session).

## Observed facts

| Property | Value |
| --- | --- |
| Runs (fresh Flask launch, Py3.12) | Yes — start → 30 questions → results, no runtime error |
| Questions | 30 |
| Options per question | 4 |
| App layout | `app.py` + templates (index, question, feedback, results); a `SPEC.md` is also present in the folder |
| New page per question | Yes (route `/question`); a separate feedback page follows each question (two pages per question) |
| State across pages | Flask signed session cookie: `current_question`, `answers`, `score` |
| Correct-answer position distribution | A:6 B:16 C:7 D:1 |
| Answer/category visible before answering | No (correct answer shown afterward on the feedback page) |
| Anti-skip guard | No server guard; radio `required` and submit hidden until a radio is selected (client) |
| Live score during quiz | No |
| Restart / Play Again | Yes — "PLAY AGAIN" → `/reset` (clears session) |
| Navigation | Forward-only (question → feedback → next) |
| Results page | Score X/30, percentage, performance message, full per-question review (green/red) |
| Final score correct | Yes — option-A run scored 6/30, equal to the A-count |
| Python test files | None |
| `<meta viewport>` | Present |
| `secret_key` | Hardcoded `"movie-quiz-secret-key-change-in-production"` |

Factual notes:
- The results template indexes `answers[i]` for every question; reaching `/results` before all answers are recorded would raise an IndexError (not reached in normal forward play).
- Option-text typos exist in the data (e.g. "The Texas Chainaw Massacre", "Darryn"). Source binds `port=5001`, `debug=True`.

## Screenshots

| Start | Question | Results |
| --- | --- | --- |
| ![start](../../screenshots/minimax-m2.5-start.webp) | ![question](../../screenshots/minimax-m2.5-question.webp) | ![results](../../screenshots/minimax-m2.5-finish.webp) |

## Maintainer assessment

<!-- Repository maintainers: write the qualitative assessment (UI quality, polish,
     subjective calls) and assign the final score here. -->

**Score:** _TBD_
