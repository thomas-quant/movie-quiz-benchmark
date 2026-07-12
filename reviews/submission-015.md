# Review — submission-015

## Summary

This is a clean, compact Flask knowledge quiz that meets the core 32-question, one-page-per-question brief and completed a fresh headed browser run successfully. Its navy/coral visual system, progress display, feedback pattern, and full answer review are coherent and usable, but the experience remains fairly generic, the linear flow offers no visible back/edit path, the results page is repetitive, and the answer key is notably position-biased.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | The fresh evidence starts the Flask server successfully and records `GET /` as 200. The trace also records one `/favicon.ico` 404, but no page error or failed application route. |
| Full flow completes | Yes | Fresh headed Playwright metadata records 32 steps from `/` through `/question/32` to `/results`; the server log records the final results page as 200. |
| Quiz type | knowledge | The questions ask for definitions and examples of movie genres, subgenres, formats, and related movie types. |
| Questions | 32; four options each | `submission/questions.py` contains 32 question entries, each with a four-item `choices` list; the fresh start page also displays “32 questions.” |
| Page-per-question behavior | Yes | The trace records a distinct GET for each `/question/1` through `/question/32`, with each submitted answer redirecting to the next question or `/results`. |
| State between pages | Yes | The trace carries session cookies between requests, and the completed run produces a score and 32-item review. The source stores answers and score in the Flask session. |
| Meets minimum question count | Yes | 32 questions were supplied, exceeding the 30-question minimum. |
| Content matches movie types/genres | Yes | The question bank covers horror, documentary, noir, western, rom-com, science fiction, thriller, biopic, fantasy, musical, and other movie genres or formats. |
| Scoring/result generation | Yes, for the exercised path | The fresh all-first-option run ends with `8 / 32 (25%)`, and the results review agrees with the selected answers. This is consistent with the eight option-A answer keys. Other answer choices were not exercised in the fresh run. |
| Answer/category leak | No observed before answering | The question screenshot shows only the question and four choices; the question template renders choices but not the answer key. The completed results review intentionally reveals correct answers afterward. |
| Answer-position distribution | A: 8, B: 19, C: 5, D: 0 | Counting the 32 `answer` indexes in `submission/questions.py` shows a strong bias toward option B and no correct option D. |
| Skip/direct-navigation behavior | Unverified | The fresh trace follows only the intended sequence and does not probe an incomplete direct URL or an out-of-order question. The source contains guards intended to redirect to the first unanswered question, but that behavior was not freshly verified. |
| Restart behavior | Unverified | The fresh run does not click “Play again” or “Start over.” The source’s `/start` route calls `session.clear()`, but clearing prior results was not freshly verified. |
| Tests present | No | No test files are present in the staged submission; both available test-result records say “No test files found.” |
| Tests pass | N/A | There are no tests to run; the available test-result record is explicitly `not-run`. |
| Self-testing evidence | Unverified | `submission/notes.txt` claims the agent ran tests, but no test artifacts or agent-run output corroborate that claim. The headed Playwright trace verifies the artifact externally, not the agent’s own testing process. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 3/5 | 40% | 24/40 | The captured start, question, and results states share a coherent navy gradient, white card, coral action color, readable hierarchy, progress bar, and consistent controls. The composition is also a generic single-card/gradient treatment with a weak emoji-like logo, no movie-specific imagery, and a long repetitive results list. |
| UX and interaction design | 3/5 | 40% | 24/40 | The start page sets expectations, the question page exposes count/score/progress and large selectable answer rows, and the results page gives a score plus per-question review. The flow is strictly linear with no visible back/edit control, and 32 consecutive submissions create friction; direct-navigation and restart behavior remain unverified. |
| Code quality and maintainability | 4/5 | 15% | 12/15 | The question bank, routes, templates, and stylesheet are separated cleanly. The small helper functions and session transitions in `submission/app.py` are understandable and straightforward to change. The lack of tests and limited handling evidence keep it below exceptional. |
| Tests and verification evidence | 1/5 | 5% | 1/5 | No test files or pass output are available. The notes claim testing, but the available record says no tests were found and not run. |
| **Quality score** |  | **100%** | **61/100** | Weighted calculation: 24 + 24 + 12 + 1. |

## Strongest aspects

- The core benchmark contract is implemented directly: 32 movie-genre questions, a distinct server-rendered page per question, and session-held progress through the full run.
- The visual language is consistent across the fresh captured states: dark blue background, white content surface, coral primary action, clear question count, and generous answer controls.
- The result experience is concrete rather than just a number: the completed page shows the percentage, a short interpretation, and a question-by-question answer review.

## Main weaknesses

- The visual treatment is competent but generic. A gradient background, white card, system sans, and emoji logo do not create much movie-specific personality, while the 32-item review becomes a tall, repetitive text list rather than a particularly satisfying finale.
- The quiz is a one-way sequence with no visible back/edit affordance. That makes a mistaken answer costly and limits user control during a 32-question session; the fresh evidence did not verify whether direct navigation or restart handling improves this.
- The answer key is heavily position-biased: 19 of 32 correct answers are option B and none are option D. This makes answer position an avoidable shortcut and weakens quiz integrity even though the scoring shown in the exercised run is internally consistent.
- Verification evidence is thin. No tests were present or run, and the notes’ claim of self-testing is not backed by a reproducible test artifact or output.

## Reviewer confidence

Directly verified from the fresh headed evidence: successful launch, the rendered start/question/results states, the complete 32-step navigation trace, the final 8/32 result, and the absence of page errors apart from the favicon 404. Inferred from the staged source: the full question count and four-option consistency, answer distribution, answer-key non-leak in the question template, scoring logic for unexercised choices, sequential guards, and session clearing on restart. Unverified: no-answer handling in the browser, direct URL or skip attempts, restart clearing, runs using non-first options, and the agent’s own self-testing. Overall confidence: **High**.
