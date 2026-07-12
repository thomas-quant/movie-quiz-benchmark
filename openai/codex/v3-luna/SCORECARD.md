# Scorecard — Codex v3 Luna

> Maintainer record. This run used the original one-shot prompt shared by Claude and
> Codex v1; it is kept as a separate Codex v3 variant rather than renamed to v1.

| Metric | Value |
| --- | --- |
| Wall time | 6m 38s |
| Output tokens | 18.4k |
| Questions | 30 |
| Layout | `app.py` + templates/static |
| Test files | None |
| **Score** | **+3** |

## Observed facts

| Property | Value |
| --- | --- |
| New page per question | Yes — `/quiz` advances one question per POST |
| State across pages | Flask signed session cookie: `session["quiz"]` stores index, score, answer indices, and previous result |
| Correct-answer position distribution | A:30 B:0 C:0 D:0 |
| Answer/category visible before answering | No exact answer leak; broad category labels are shown, but they do not identify the keyed answer |
| Anti-skip guard | Yes — the server controls the current question and validates submitted choices |
| Live score during quiz | No |
| Restart / Play Again | Yes — `Play it again` clears the quiz at `/restart` |
| Results page | Percentage, verdict, category breakdown, explanations, and a per-question answer review |
| Final score correct | Yes — a complete correct-answer flow rendered 30/30 |
| Python test files | None present in the captured submission |
| Self-testing | Yes — tested itself, but wrote no app test file |

## Notes

The frontend is stunning, with a particularly strong finish screen and a nice category
percentage breakdown. It avoided the lookahead issue and tested itself, but wrote no app
test file (−1) and all 30 correct answers are option A, making the answer pattern easy to
exploit (−1). It took the longest of the three runs at 6m 38s and used the most output
tokens at 18.4k, though it is also the cheapest model; overall this is still a very good
result. **Final score: +3.**

## Screenshots

| Start | Question | Finish |
| --- | --- | --- |
| ![start](../../../screenshots/codex-v3-luna-start.webp) | ![question](../../../screenshots/codex-v3-luna-question.webp) | ![finish](../../../screenshots/codex-v3-luna-finish.webp) |
