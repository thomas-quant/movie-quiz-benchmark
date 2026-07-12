# Scorecard — MiMo v2.5 (`mimo-v2.5-free`)

## Legacy assessment

The pre-publication scorecard content below is retained verbatim. Its historical score uses a different maintainer scale and is not comparable to the canonical automated quality score.

> Factual record, compiled by automated assessment: static code read + live browser run
> (Chromium, fresh Flask launch, Python 3.12). The model's own files in this folder are
> exactly as it produced them. **The qualitative assessment and final score are for the
> repository maintainers** — see the last section.

## Build (opencode session, build turn only)

| Metric | Value |
| --- | --- |
| opencode model id | `mimo-v2.5-free` (variant: high) |
| Provider / lab | Xiaomi MiMo (served via OpenCode Zen) |
| Wall time (build) | 1m 35s (94.9s) |
| Output tokens (build) | 7,055 |
| Reasoning tokens | 443 |

Build turn only (single-turn session).

## Observed facts

| Property | Value |
| --- | --- |
| Runs (fresh Flask launch, Py3.12) | Yes — start → 34 questions → results, no runtime error |
| Questions | 34 |
| Options per question | 4 |
| App layout | Single `app.py` with inline templates (start, question, feedback, results) |
| New page per question | Yes (route `/question/<qnum>`); a separate feedback page follows each question (two pages per question) |
| State across pages | Flask signed session cookie: `current`, `score`, `answers` |
| Correct-answer position distribution | A:2 B:29 C:3 D:0 |
| Answer/category visible before answering | No (a hint shows the *previous* question's context) |
| Anti-skip guard | Radio `required` (client) only; server records a missing answer without blocking; direct GET allowed |
| Live score during quiz | Yes — "Score: N" badge on each question page (browser-confirmed) |
| Restart / Play Again | Yes — "Try Again" → `/` (clears session) |
| Navigation | Forward-only (question → feedback → next) |
| Results page | Score X/34, performance label, per-question review (no percentage figure) |
| Final score correct | Yes — option-A run scored 2/34, equal to the A-count |
| Python test files | None |
| `<meta viewport>` | Present |
| `secret_key` | `os.urandom(24)` (regenerated each process start) |

Factual notes:
- Options not shuffled; question order fixed. 3 routes (`/`, `/question/<qnum>`, `/results`).
- The start page hardcodes the literal "34" question count. `debug=True`.

## Screenshots

| Start | Question | Results |
| --- | --- | --- |
| ![start](../../screenshots/mimo-v2.5-start.webp) | ![question](../../screenshots/mimo-v2.5-question.webp) | ![results](../../screenshots/mimo-v2.5-finish.webp) |

## Maintainer assessment

<!-- Repository maintainers: write the qualitative assessment (UI quality, polish,
     subjective calls) and assign the final score here. -->

**Score:** _TBD_

## Automated blind review

This section is generated from the canonical public aggregation. It is the completed benchmark quality assessment. The Legacy assessment above is retained historical maintainer material on a different scale and is not a competing total.

| Field | Value |
| --- | --- |
| Opaque submission ID | `submission-012` |
| Final review | [`../../reviews/submission-012.md`](../../reviews/submission-012.md) |
| Quiz type | knowledge |
| Questions / options | 34 / 4 |
| Launch / full flow | Yes / Yes |
| Content scope | Yes |
| Scoring/result | Yes |
| Answer leak / position distribution | No / Heavily biased |
| Skip/direct navigation | Bypassable |
| Restart | Yes |
| Tests present / pass status | No / N/A |
| Capture status | completed |
| Reviewer confidence | High |
| Disagreement status | Not assessed: one canonical blind pass; no independent second pass. |
| Build time | 1m 35s |
| Output tokens | 7,055 |

| Category | Rating | Weighted points |
| --- | ---: | ---: |
| Frontend visual quality and polish | 3/5 | 24/40 |
| UX and interaction design | 3/5 | 24/40 |
| Code quality and maintainability | 2/5 | 6/15 |
| Tests and verification evidence | 1/5 | 1/5 |
| **Quality score** |  | **55/100** |

Quality is recalculated from the integer ratings and excludes build time and output tokens.
