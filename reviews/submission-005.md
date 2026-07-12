# Review — submission-005

## Summary

This is a complete, cleanly rendered 32-question knowledge quiz about movie genres, with a consistent dark card-based interface, per-question progress, session-backed answers, and a useful scored review. Its main weaknesses are a linear flow without back navigation, source-visible direct-URL bypasses, a strongly A/B-biased answer key, and no submission-provided tests or self-testing evidence.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | The fresh evidence metadata reports a completed run; `server.log` shows the server starting and `GET /` returning 200. |
| Full flow completes | Yes | The fresh trace records 32 answer steps from `/quiz/0` through `/quiz/31`, ending at `/result`; the server log shows the POST/redirect/GET sequence with no 5xx responses. `metadata.json` reports no page errors. |
| Quiz type | knowledge | The questions have correct genre answers and the result reports a numerical score. |
| Questions | 32; 4 options per question | The `QUESTIONS` list contains 32 entries, each with four options; the start screen also states 32 questions. |
| Page-per-question behavior | Yes | Each step is rendered at a distinct `/quiz/<qid>` URL; the trace and server log cover `/quiz/0` through `/quiz/31`. |
| State between pages | Yes | Answers are stored in the Flask session keyed by question ID, and the fresh run reaches a result consistent with all 32 submitted choices. |
| Meets minimum question count | Yes | 32 questions meets the required minimum of 30. |
| Content matches movie types/genres | Yes | The question set consistently asks about film genres and subgenres such as Comedy, Science Fiction, Horror, Film Noir, and Body Horror, rather than general movie trivia. |
| Scoring/result generation | Yes | The fresh result shows `13/32`, `41%`, and a per-question correct/incorrect review. For the trace's first-option answer run, that score agrees with the 13 questions whose correct answer is option A. |
| Answer/category leak | No | The question template renders only the question and options; the answer key is not sent to the quiz page. Correct answers appear only in the results review after submission. |
| Answer-position distribution | 13 A / 14 B / 5 C / 0 D | The distribution is computed from the staged `QUESTIONS` data. It is materially biased toward A/B, with no correct answer in option D; the first-option trace scored 13/32. |
| Skip/direct-navigation behavior | Yes, direct bypass exists | The normal UI requires a radio selection and initially disables `Next`, but the route renders any in-range question without checking prior progress and accepts a direct POST to it. The supplied fresh trace did not exercise this alternate path; source behavior indicates partial results can contain `None` for unanswered items. |
| Restart behavior | Yes, source-verified | The `Try Again` link goes to `/`, and the index route calls `session.clear()`. This was not separately exercised in the supplied trace. |
| Tests present | No | No test files are staged; `test-results.txt` says `No test files found.` |
| Tests pass | N/A | There were no tests to run; `test-results.txt` reports `not-run`. |
| Self-testing evidence | No | There is no submission-provided test or self-test record. The completed browser trace is fresh benchmark evidence, not evidence of a submission-authored verification routine. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 4/5 | 40% | 32/40 | The start, question, and results states share a coherent dark palette, warm orange-red gradient, rounded cards, readable hierarchy, clear option states, progress indicator, and green/red result feedback. The presentation is polished and free of visible layout defects in the supplied screenshots, but it is fairly generic and has little movie-specific visual identity. |
| UX and interaction design | 3/5 | 40% | 24/40 | The start screen sets expectations, question numbering and progress orient the user, required choices prevent ordinary accidental skips, and the results page explains each answer with a clear Try Again action. The flow is rigidly linear with no back/edit control, asks the user to complete 32 consecutive pages, and the direct URL behavior is not guarded. |
| Code quality and maintainability | 3/5 | 15% | 9/15 | The small Flask app has a straightforward question data structure, separate templates, concise routes, and understandable session state. Maintainability is reduced by duplicated inline CSS, and the quiz route lacks sequence validation, allowing direct question access and incomplete result records. |
| Tests and verification evidence | 1/5 | 5% | 1/5 | No tests are present or run, and there is no submission-authored self-testing evidence. The supplied standardized browser capture is useful coverage of the normal full flow but does not replace tests of alternate paths or restart behavior. |
| **Quality score** |  | **100%** | **66/100** | `(4/5 × 40) + (3/5 × 40) + (3/5 × 15) + (1/5 × 5) = 32 + 24 + 9 + 1 = 66`. |

## Strongest aspects

- Consistent, restrained visual system across the start, question, and results states, with good contrast between the dark surface and warm action/feedback colors.
- Complete multi-page quiz implementation: 32 genre questions, four choices each, visible progress, session-retained answers, and a successful fresh end-to-end trace.
- Results are meaningful and actionable, combining the total score and percentage with a full correct/incorrect answer review and the expected answer for misses.

## Main weaknesses

- The answer key is position-biased: 27 of 32 correct answers are A or B and none are D, making position guessing unusually informative; the standardized first-option run visibly scores 13/32.
- The server does not enforce sequential progress. Directly opening a later `/quiz/<qid>` and posting it can bypass earlier questions, and incomplete result rows can display `None`; the normal UI's required radio control does not cover this server-side path.
- The implementation has no back navigation and no test files or submission-authored verification record; the otherwise polished UI is also generic rather than strongly movie-themed.

## Reviewer confidence

High overall confidence. Directly verified evidence includes the supplied start, question, and results screenshots; the completed 32-step trace; the server log; the staged templates and Flask routes; the 32-question content; and the answer-position calculation. The full normal flow and its `13/32` result are strongly supported by fresh browser evidence. Direct URL bypass and restart clearing are source-verified from the staged route/link logic but were not separate steps in the supplied trace, so those alternate-path claims are identified as not freshly exercised. No tests were available to independently verify them.
