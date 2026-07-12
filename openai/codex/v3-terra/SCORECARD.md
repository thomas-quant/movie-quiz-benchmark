# Scorecard — Codex v3 Terra

> Maintainer record. This run used the original one-shot prompt shared by Claude and
> Codex v1; it is kept as a separate Codex v3 variant rather than renamed to v1.

| Metric | Value |
| --- | --- |
| Wall time | 4m 28s |
| Output tokens | 11.4k |
| Questions | 30 |
| Layout | `app.py` + templates/static |
| Test files | None |
| **Score** | **−1** |

## Observed facts

| Property | Value |
| --- | --- |
| New page per question | Yes — `/question/<number>` |
| State across pages | Flask signed session cookie: question index, score, answers, and previous response |
| Correct-answer position distribution | A:26 B:3 C:1 D:0 |
| Answer/category visible before answering | No |
| Anti-skip guard | Yes — the server requires the expected question number and validates submitted choices |
| Live score during quiz | No |
| Restart / Play Again | Yes — `Play again` resets the session at `/restart` |
| Results page | Score, performance message, and a full answer review |
| Final score correct | Yes — a complete correct-answer flow rendered 30/30 |
| Python test files | None |
| Self-testing | Unconfirmed |

## Notes

The model noticed an implementation issue during generation and fixed it mid-run, and it
did not reproduce the earlier lookahead problem. However, option A is correct for 26 of
30 questions (86.67%), which makes the answer pattern highly guessable. It created no app
test file, and self-testing is unconfirmed. The frontend is pretty meh, though the run is
both fast and exceptionally token-efficient at 4m 28s and 11.4k output tokens. **Final
score: −1.**

## Screenshots

| Start | Question | Finish |
| --- | --- | --- |
| ![start](../../../screenshots/codex-v3-terra-start.webp) | ![question](../../../screenshots/codex-v3-terra-question.webp) | ![finish](../../../screenshots/codex-v3-terra-finish.webp) |
