# Scorecard — MiniMax M2.1 (`MiniMax-M2.1`)

## Legacy assessment

The pre-publication scorecard content below is retained verbatim. Its historical score uses a different maintainer scale and is not comparable to the canonical automated quality score.

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

## Automated blind review

This section is generated from the canonical public aggregation. It is the completed benchmark quality assessment. The Legacy assessment above is retained historical maintainer material on a different scale and is not a competing total.

| Field | Value |
| --- | --- |
| Opaque submission ID | `submission-014` |
| Final review | [`../../reviews/submission-014.md`](../../reviews/submission-014.md) |
| Quiz type | knowledge |
| Questions / options | 31 / 4 |
| Launch / full flow | Yes / Yes |
| Content scope | No |
| Scoring/result | Yes, mechanically; correctness is flawed |
| Answer leak / position distribution | No / A: 10, B: 14, C: 6, D: 1 |
| Skip/direct navigation | Direct question jumping: No; crafted POST bypass: Yes |
| Restart | Yes |
| Tests present / pass status | No / N/A |
| Capture status | completed |
| Reviewer confidence | High |
| Disagreement status | Not assessed: one canonical blind pass; no independent second pass. |
| Build time | 4m 46s |
| Output tokens | 6,639 |

| Category | Rating | Weighted points |
| --- | ---: | ---: |
| Frontend visual quality and polish | 3/5 | 24/40 |
| UX and interaction design | 2/5 | 16/40 |
| Code quality and maintainability | 3/5 | 9/15 |
| Tests and verification evidence | 1/5 | 1/5 |
| **Quality score** |  | **50/100** |

Quality is recalculated from the integer ratings and excludes build time and output tokens.

### Fresh automated-review captures

These are the fresh headed Chromium captures used for the canonical blind review.

| Start | Question | Results |
| --- | --- | --- |
| ![submission-014 automated review start](../../screenshots/reviewed/submission-014-start.png) | ![submission-014 automated review question](../../screenshots/reviewed/submission-014-question.png) | ![submission-014 automated review results](../../screenshots/reviewed/submission-014-results.png) |
