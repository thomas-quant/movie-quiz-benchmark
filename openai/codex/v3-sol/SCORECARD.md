# Scorecard — Codex v3 Sol

## Legacy assessment

The pre-publication scorecard content below is retained verbatim. Its historical score uses a different maintainer scale and is not comparable to the canonical automated quality score.

> Maintainer record. This run used the original one-shot prompt shared by Claude and
> Codex v1; it is kept as a separate Codex v3 variant rather than renamed to v1.

| Metric | Value |
| --- | --- |
| Wall time | 6m 14s |
| Output tokens | 14.0k |
| Questions | 30 |
| Layout | `app.py` + templates/static + `test_app.py` |
| Test files | `test_app.py` (pytest-style) |
| **Score** | **+5** |

## Observed facts

| Property | Value |
| --- | --- |
| New page per question | Yes — `/quiz/<number>` |
| State across pages | Flask signed session cookie: `session["answers"]` stores the selected answers and results |
| Correct-answer position distribution | A:9 B:14 C:7 D:0 |
| Answer/category visible before answering | No |
| Anti-skip guard | Yes — missing/invalid answers are rejected server-side, and future question URLs redirect to the first unanswered question |
| Live score during quiz | No |
| Restart / Play Again | Yes — `Begin a fresh screening` / `Play it again` resets the session |
| Navigation | Sequential, with a previous-scene link; revisiting a completed question replaces its saved answer |
| Results page | Score and percentage, rank/message, and a full scene-by-scene review |
| Final score correct | Yes — the complete correct-answer flow rendered 30/30; the included test suite also passed |
| Python test files | Yes — `test_app.py` covers question count, full flow/scoring, anti-skip, and invalid answers |
| Self-testing | Yes — tested itself |

## Notes

This is a genuinely strong result: the answer key is comparatively well distributed (A is
correct for 9 of 30 questions, 30%), there is no lookahead issue, and the model wrote a
test file and tested the app itself. The frontend is gorgeous, and the 14.0k output-token
build is notably efficient. **Final score: +5.**

## Screenshots

| Start | Question | Finish |
| --- | --- | --- |
| ![start](../../../screenshots/codex-v3-sol-start.webp) | ![question](../../../screenshots/codex-v3-sol-question.webp) | ![finish](../../../screenshots/codex-v3-sol-finish.webp) |

## Automated blind review

This section is generated from the canonical public aggregation. It is the completed benchmark quality assessment. The Legacy assessment above is retained historical maintainer material on a different scale and is not a competing total.

| Field | Value |
| --- | --- |
| Opaque submission ID | `submission-003` |
| Final review | [`../../../reviews/submission-003.md`](../../../reviews/submission-003.md) |
| Quiz type | knowledge |
| Questions / options | 30 / 4 |
| Launch / full flow | Yes / Yes |
| Content scope | Yes |
| Scoring/result | Yes |
| Answer leak / position distribution | No / A: 9, B: 14, C: 7, D: 0 |
| Skip/direct navigation | No for normal GET navigation |
| Restart | Unverified |
| Tests present / pass status | Yes / Yes, according to supplied results |
| Capture status | completed |
| Reviewer confidence | High |
| Disagreement status | Not assessed: one canonical blind pass; no independent second pass. |
| Build time | 6m 14s |
| Output tokens | 14.0k |

| Category | Rating | Weighted points |
| --- | ---: | ---: |
| Frontend visual quality and polish | 5/5 | 40/40 |
| UX and interaction design | 4/5 | 32/40 |
| Code quality and maintainability | 4/5 | 12/15 |
| Tests and verification evidence | 4/5 | 4/5 |
| **Quality score** |  | **88/100** |

Quality is recalculated from the integer ratings and excludes build time and output tokens.
