# Scorecard — Codex v2

> Author's evaluation. The model's own files in this folder are left exactly as it
> produced them. (Codex v2 did not write its own README.)

| Metric | Value |
| --- | --- |
| Wall time | 6m 40s |
| Output tokens | 41.1k |
| Questions | 30 |
| Layout | single `app.py` (inline templates) |
| Test files | None |
| **Score** | **+2** |

## Notes

Re-run with the tweaked prompt. Everything lives in a single ~960-line `app.py` with
inline (`render_template_string`) templates and 30 questions. Codex **noticed the
every-answer-is-A problem from v1 and fixed it**, distributing correct answers across
positions via an explicit `ANSWER_POSITIONS` table. It tested itself and wrote no Python
test files, as instructed. Keeps the anti-skip guard and the live score.

The finish screen adds a cinema-staircase image for flavor — a creative touch, though it
isn't scaled correctly. Subjectively this is the cleanest-looking of the three, and the
start screen is a standout.

## Screenshots

| Start | Question | Finish | Finish (staircase) |
| --- | --- | --- | --- |
| ![Codex v2 start screen](../../../screenshots/codex-v2-start.webp) | ![Codex v2 question page](../../../screenshots/codex-v2-question.webp) | ![Codex v2 finish screen](../../../screenshots/codex-v2-finish.webp) | ![Codex v2 finish screen with misscaled staircase image](../../../screenshots/codex-v2-finish-stairs.webp) |
