# Scorecard — MiniMax M2 (`MiniMax-M2`)

## Legacy assessment

The pre-publication scorecard content below is retained verbatim. Its historical score uses a different maintainer scale and is not comparable to the canonical automated quality score.

> Factual record, compiled by automated assessment: static code read + live browser run
> (Chromium, fresh Flask launch, Python 3.12). The model's own files in this folder are
> exactly as it produced them. **The qualitative assessment and final score are for the
> repository maintainers** — see the last section.

## Build (opencode session, build turn only)

| Metric | Value |
| --- | --- |
| opencode model id | `MiniMax-M2` |
| Provider / lab | MiniMax (served via minimax-coding-plan) |
| Wall time (build) | 1m 41s (100.7s) |
| Output tokens (build) | 7,786 |
| Reasoning tokens | 0 (not exposed by provider) |

Build turn only (single-turn session).

## Observed facts

| Property | Value |
| --- | --- |
| Runs (fresh Flask launch, Py3.12) | Yes — start → 41 questions → results, no runtime error |
| Questions | 41 |
| Options per question | 4 |
| App layout | `app.py` + templates (index, question, results) + `requirements.txt` |
| New page per question | Yes — single `/question` route re-rendered (server-driven index) |
| State across pages | Flask signed session cookie: `score`, `question_index`, `answers` |
| Correct-answer position distribution | A:3 B:34 C:4 D:0 |
| Answer/category visible before answering | No (a "last answer" block shows Correct/Incorrect for the previous question) |
| Anti-skip guard | Empty POST re-renders the same question (index not incremented); radio `required` (client) |
| Live score during quiz | Yes — "Score: N" on each question page (browser-confirmed) |
| Restart / Play Again | Yes — `/restart` (clears session) |
| Navigation | Forward-only |
| Results page | Score X/41, percentage, performance message, per-question review (correct/incorrect flag) |
| Final score correct | Yes — option-A run scored 3/41, equal to the A-count |
| Python test files | None |
| `<meta viewport>` | Present |
| `secret_key` | Hardcoded `"moviequizsecretkey123"` |

Factual notes:
- Landing copy states "40 questions" while the bank has 41 entries; results uses the dynamic total (41).
- `int(request.form["answer"])` would raise on a non-integer POST value (not reachable via the UI). `debug=True`.

## Screenshots

| Start | Question | Results |
| --- | --- | --- |
| ![start](../../screenshots/minimax-m2-start.webp) | ![question](../../screenshots/minimax-m2-question.webp) | ![results](../../screenshots/minimax-m2-finish.webp) |

## Maintainer assessment

<!-- Repository maintainers: write the qualitative assessment (UI quality, polish,
     subjective calls) and assign the final score here. -->

**Score:** _TBD_

## Automated blind review

This section is generated from the canonical public aggregation. It is the completed benchmark quality assessment. The Legacy assessment above is retained historical maintainer material on a different scale and is not a competing total.

| Field | Value |
| --- | --- |
| Opaque submission ID | `submission-011` |
| Final review | [`../../reviews/submission-011.md`](../../reviews/submission-011.md) |
| Quiz type | knowledge |
| Questions / options | 41 / 4 |
| Launch / full flow | Yes / Yes |
| Content scope | Yes |
| Scoring/result | Yes |
| Answer leak / position distribution | No / A: 3, B: 34, C: 4, D: 0 |
| Skip/direct navigation | Yes |
| Restart | Yes |
| Tests present / pass status | No / N/A |
| Capture status | completed |
| Reviewer confidence | High |
| Disagreement status | Not assessed: one canonical blind pass; no independent second pass. |
| Build time | 1m 41s |
| Output tokens | 7,786 |

| Category | Rating | Weighted points |
| --- | ---: | ---: |
| Frontend visual quality and polish | 3/5 | 24/40 |
| UX and interaction design | 3/5 | 24/40 |
| Code quality and maintainability | 3/5 | 9/15 |
| Tests and verification evidence | 1/5 | 1/5 |
| **Quality score** |  | **58/100** |

Quality is recalculated from the integer ratings and excludes build time and output tokens.
