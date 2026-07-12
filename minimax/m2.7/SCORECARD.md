# Scorecard — MiniMax M2.7 (`MiniMax-M2.7-highspeed`)

## Legacy assessment

The pre-publication scorecard content below is retained verbatim. Its historical score uses a different maintainer scale and is not comparable to the canonical automated quality score.

> Factual record, compiled by automated assessment: static code read + live browser run
> (Chromium, fresh Flask launch, Python 3.12). The model's own files in this folder are
> exactly as it produced them. **The qualitative assessment and final score are for the
> repository maintainers** — see the last section.

## Build (opencode session, build turn only)

| Metric | Value |
| --- | --- |
| opencode model id | `MiniMax-M2.7-highspeed` |
| Provider / lab | MiniMax (served via minimax-coding-plan) |
| Wall time (build) | 1m 52s (112.1s) |
| Output tokens (build) | 4,924 |
| Reasoning tokens | 0 (not exposed by provider) |

Build turn only (single-turn session).

## Observed facts

| Property | Value |
| --- | --- |
| Runs (fresh Flask launch, Py3.12) | Yes — start → 35 questions → results, no runtime error |
| Questions | 35 |
| Options per question | 4 |
| App layout | `app.py` + templates (base, start, question, results) |
| New page per question | Yes (distinct URLs `/question/<q_num>`) |
| State across pages | Flask signed session cookie: `score`, `answers`, `question_index`, `shuffled_questions` |
| Correct-answer position distribution | A:2 B:24 C:9 D:0 (over each question's fixed options array) |
| Answer/category visible before answering | No |
| Anti-skip guard | Missing-session redirects to start; no guard against jumping ahead via direct `/question/<n>` URL; out-of-order answering possible |
| Live score during quiz | No |
| Restart / Play Again | Yes — "Play Again" → `/` (clears session) |
| Navigation | Forward-only (option submit → next/<q_num+1>); URLs not blocked from manipulation |
| Results page | Percentage, grade, "You scored X out of 35", per-question review (your answer vs correct) |
| Final score correct | Yes — option-A run scored 2/35, equal to the A-count |
| Python test files | None |
| `<meta viewport>` | Present |
| `secret_key` | Hardcoded `"movie_quiz_secret_key_123"` |

Factual notes:
- Question order is randomized per session (`random.sample`); option order within a question is fixed.
- Indexing `shuffled_questions[q_num]` is not bounds-checked; a `/question/<n>` with n ≥ 35 would raise an IndexError. Some answer keys are debatable on content grounds (e.g. a question with both "Horror" and "Sci-Fi" options keyed to "Horror"). `debug=True`.

## Screenshots

| Start | Question | Results |
| --- | --- | --- |
| ![start](../../screenshots/minimax-m2.7-start.webp) | ![question](../../screenshots/minimax-m2.7-question.webp) | ![results](../../screenshots/minimax-m2.7-finish.webp) |

## Maintainer assessment

<!-- Repository maintainers: write the qualitative assessment (UI quality, polish,
     subjective calls) and assign the final score here. -->

**Score:** _TBD_

## Automated blind review

This section is generated from the canonical public aggregation. It is the completed benchmark quality assessment. The Legacy assessment above is retained historical maintainer material on a different scale and is not a competing total.

| Field | Value |
| --- | --- |
| Opaque submission ID | `submission-002` |
| Final review | [`../../reviews/submission-002.md`](../../reviews/submission-002.md) |
| Quiz type | knowledge |
| Questions / options | 35 / 4 |
| Launch / full flow | Yes / Yes |
| Content scope | Yes |
| Scoring/result | Yes |
| Answer leak / position distribution | No in the question UI / A: 2, B: 24, C: 9, D: 0 |
| Skip/direct navigation | No sequential guard; edge runtime unverified |
| Restart | Yes, source-verified; fresh restart not exercised |
| Tests present / pass status | No / N/A |
| Capture status | completed |
| Reviewer confidence | High |
| Disagreement status | Not assessed: one canonical blind pass; no independent second pass. |
| Build time | 1m 52s |
| Output tokens | 4,924 |

| Category | Rating | Weighted points |
| --- | ---: | ---: |
| Frontend visual quality and polish | 3/5 | 24/40 |
| UX and interaction design | 3/5 | 24/40 |
| Code quality and maintainability | 3/5 | 9/15 |
| Tests and verification evidence | 1/5 | 1/5 |
| **Quality score** |  | **58/100** |

Quality is recalculated from the integer ratings and excludes build time and output tokens.

### Fresh automated-review captures

These are the fresh headed Chromium captures used for the canonical blind review.

| Start | Question | Results |
| --- | --- | --- |
| ![submission-002 automated review start](../../screenshots/reviewed/submission-002-start.png) | ![submission-002 automated review question](../../screenshots/reviewed/submission-002-question.png) | ![submission-002 automated review results](../../screenshots/reviewed/submission-002-results.png) |
