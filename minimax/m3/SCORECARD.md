# Scorecard — MiniMax M3 (`MiniMax-M3`)

## Legacy assessment

The pre-publication scorecard content below is retained verbatim. Its historical score uses a different maintainer scale and is not comparable to the canonical automated quality score.

> Factual record, compiled by automated assessment: static code read + live browser run
> (Chromium, fresh Flask launch, Python 3.12). The model's own files in this folder are
> exactly as it produced them. **The qualitative assessment and final score are for the
> repository maintainers** — see the last section.

## Build (opencode session, build turn only)

| Metric | Value |
| --- | --- |
| opencode model id | `MiniMax-M3` |
| Provider / lab | MiniMax (served via minimax-coding-plan) |
| Wall time (build) | 2m 24s (144.2s) |
| Output tokens (build) | 8,570 |
| Reasoning tokens | 0 (not exposed by provider) |

Build turn only (single-turn session).

## Observed facts

| Property | Value |
| --- | --- |
| Runs (fresh Flask launch, Py3.12) | Yes — 30 questions → result, no runtime error |
| Quiz type | Personality / genre-match — options map to genre categories; **there are no correct/incorrect answers** |
| Questions | 30 |
| Options per question | 4 |
| App layout | Single `app.py` with inline templates (question, result) |
| New page per question | Yes (route `/question/<q>`); `/` redirects to `/question/1` (no separate landing page) |
| State across pages | Flask signed session cookie: `answers` (list of chosen genre categories) |
| Correct-answer position distribution | N/A (no correct answers) |
| Answer/category visible before answering | The genre each option maps to is present in the radio `value` attribute in page markup (not in the visible option text); there is no correct answer to leak |
| Anti-skip guard | Yes — `/result` redirects to the first unanswered question; q-range and category validated server-side; radio `required` (client) |
| Live score during quiz | No (progress indicator + previous answer shown) |
| Restart / Play Again | Yes — "Take it again" → home (clears session) |
| Navigation | Forward-only |
| Results page | Profile title, tagline, summary, recommended films, genre breakdown (count/total per category, top highlighted), collapsible per-question review. No X/N correctness score (preference quiz) |
| Final result | Top-tallied genre category; the option-A traversal produced "The Comedy Lover" (comedy 24/30) |
| Python test files | None |
| `<meta viewport>` | Present |
| `secret_key` | Hardcoded `"movie-quiz-secret-key-change-me"` |

Factual notes:
- 9 result categories defined (comedy, drama, thriller, fantasy, scifi, action, romance, horror, musical).
- Visiting `/` clears the session and restarts at question 1. `debug=True`.

## Screenshots

| Start (= Question 1) | Question | Result |
| --- | --- | --- |
| ![start](../../screenshots/minimax-m3-start.webp) | ![question](../../screenshots/minimax-m3-question.webp) | ![result](../../screenshots/minimax-m3-finish.webp) |

## Maintainer assessment

<!-- Repository maintainers: write the qualitative assessment (UI quality, polish,
     subjective calls) and assign the final score here. -->

**Score:** _TBD_

## Automated blind review

This section is generated from the canonical public aggregation. It is the completed benchmark quality assessment. The Legacy assessment above is retained historical maintainer material on a different scale and is not a competing total.

| Field | Value |
| --- | --- |
| Opaque submission ID | `submission-007` |
| Final review | [`../../reviews/submission-007.md`](../../reviews/submission-007.md) |
| Quiz type | personality/genre-match |
| Questions / options | 30 / 4 |
| Launch / full flow | Yes / Yes |
| Content scope | Yes |
| Scoring/result | Yes |
| Answer leak / position distribution | Yes / N/A |
| Skip/direct navigation | Unverified |
| Restart | Unverified |
| Tests present / pass status | No / N/A |
| Capture status | completed |
| Reviewer confidence | Medium |
| Disagreement status | Not assessed: one canonical blind pass; no independent second pass. |
| Build time | 2m 24s |
| Output tokens | 8,570 |

| Category | Rating | Weighted points |
| --- | ---: | ---: |
| Frontend visual quality and polish | 4/5 | 32/40 |
| UX and interaction design | 3/5 | 24/40 |
| Code quality and maintainability | 3/5 | 9/15 |
| Tests and verification evidence | 1/5 | 1/5 |
| **Quality score** |  | **66/100** |

Quality is recalculated from the integer ratings and excludes build time and output tokens.
