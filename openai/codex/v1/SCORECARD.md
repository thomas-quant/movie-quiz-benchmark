# Scorecard — Codex v1

> Author's evaluation. The model's own files in this folder are left exactly as it
> produced them; see [`README.md`](README.md) for the model's own writeup.

| Metric | Value |
| --- | --- |
| Wall time | 5m 31s (done ~4m 30s) |
| Output tokens | 16.0k |
| Questions | 30 |
| Layout | `app.py` + templates/static + `tests/` |
| Test files | pytest |
| **Score** | **−3** |

## Notes

30 questions, templates + external stylesheet, and a `tests/` directory — Codex wrote the
**pytest tests before the app**. It includes a nice **Restart** control and shows a running
score during the quiz, plus an anti-skip guard that stops you advancing past an unanswered
question.

The fatal flaw: it set **every correct answer to option A** and rendered the question's
**category in the top-right of the card** — so the answer is visible before you pick. That
lookahead leak is what triggered the v2 re-run.

## Screenshots

| Start | Question (note the leaked "Action" label) | Finish |
| --- | --- | --- |
| ![Codex v1 start screen](../../../screenshots/codex-v1-start.webp) | ![Codex v1 question page with category leak](../../../screenshots/codex-v1-question.webp) | ![Codex v1 finish screen](../../../screenshots/codex-v1-finish.webp) |
