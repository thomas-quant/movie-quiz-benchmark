# Review — submission-003

## Summary

submission-003 is a polished, genre-focused knowledge quiz with 30 server-rendered question pages, a clear visual identity, and a useful scene-by-scene results review. The supplied browser trace completes the full run and the supplied test results report four passing tests; the main weaknesses are the missing D answer position, limited edge-case test coverage, and a small favicon 404 recorded in the browser evidence.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | `evidence/metadata.json` reports a completed run from the Flask server, and `evidence/server.log` shows the app serving the start page with HTTP 200. |
| Full flow completes | Yes | The supplied browser trace records start plus 30 answer steps, ending at `/results`; the results screenshot renders a complete scorecard. |
| Quiz type | knowledge | The UI asks the user to identify a movie genre from each premise and reports correct/incorrect answers. |
| Questions | 30; 4 options per question consistently | `submission/app.py` contains 30 genre prompts, each with four options; the start and question evidence both display 30 scenes and four choices. |
| Page-per-question behavior | Yes | The trace and server log show POST `/quiz/n` followed by a new GET `/quiz/n+1` for each step, ending with `/quiz/30` to `/results`. |
| State between pages | Yes | The app stores answers in the Flask session; the trace’s all-first-option run produces 9 hits and 21 misses in the results review, and the source/test flow includes prior-scene feedback. |
| Meets minimum question count | Yes | The benchmark minimum is 30 and the staged app contains exactly 30 questions. |
| Content matches movie types/genres | Yes | All 30 premises and answer choices concern recognizable movie genres or types, without drifting into general movie trivia. |
| Scoring/result generation | Yes | The complete trace produces 9/30 and 30%, with a rank, message, hits/misses summary, and scene-by-scene review. This agrees with the submitted first-option answers and the measured answer-key positions: 9 A answers were correct and the other 21 first-option submissions were incorrect. |
| Answer/category leak | No | The initial question screenshot shows the premise and choices but no correctness indicator. The answer and explanatory fact appear only after submission in the prior-scene feedback or results review. |
| Answer-position distribution | A: 9, B: 14, C: 7, D: 0 | Counted from the staged question data. The distribution is not all-A, but no question has D as the correct answer and B is overrepresented. |
| Skip/direct-navigation behavior | No for normal GET navigation | The supplied test result covers a direct GET to question 12 redirecting to question 1, and the source guards later unanswered pages. A crafted POST to a later question is accepted before the next GET, though the subsequent sequence returns to the first unanswered page. Missing/invalid answers are rejected with “Choose one answer to continue.”; the supplied test covers the invalid-value case. |
| Restart behavior | Unverified | The results page has a `Play it again` POST to `/quiz/start`, and that route clears session answers in source, but the supplied browser trace does not exercise the restart action and the local environment could not rerun the app. |
| Tests present | Yes | `submission/test_app.py` contains four tests covering the minimum count, full scoring flow, skip prevention, and invalid-answer rejection. |
| Tests pass | Yes, according to supplied results | `test-results.txt` reports `pytest -q`, 4 passed in 0.13s. An independent rerun was unavailable because this review shell has neither Flask nor pytest installed. |
| Self-testing evidence | Yes | `evidence/metadata.json` records a headed browser run with start, 30 answer transitions, screenshots, and no page errors; the only recorded console issue is the `/favicon.ico` 404 also shown in `evidence/server.log`. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 5/5 | 40% | 40/40 | The start, question, and results screenshots show a distinctive, unusually coherent cream/red/gold identity, disciplined Playfair Display/DM Sans typography, strong spacing and alignment, a custom poster/reel motif, polished answer cards, progress treatment, score ring, and review list. The recorded favicon 404 is a minor finish issue rather than a visible page failure. |
| UX and interaction design | 4/5 | 40% | 32/40 | The start screen sets expectations, the scene counter and progress bar orient the user, radio-card selection is clear, previous-scene navigation and last-scene feedback support continuity, and results provide percentage, rank, hits/misses, and per-scene review. The premises are somewhat formulaic and the supplied run does not verify the play-again path. |
| Code quality and maintainability | 4/5 | 15% | 12/15 | The implementation keeps question data and route logic understandable in `app.py`, separates templates and CSS, uses a small helper for prior-answer feedback, validates submitted options, and replaces answers cleanly when revisiting. The template hardcodes four option letters and the larger edge-case surface is not covered by tests. |
| Tests and verification evidence | 4/5 | 5% | 4/5 | Four focused tests pass in the supplied result, and the fresh browser evidence covers the complete main flow. Coverage is still light for restart, revisiting with changed answers, empty submissions specifically, and mixed-score/result edge cases. |
| **Quality score** |  | **100%** | **88/100** | **40 + 32 + 12 + 4 = 88/100** |

## Strongest aspects

- The visual system is highly coherent and memorable: the poster, reel, editorial typography, restrained palette, and repeated header/footer treatment carry through all three major states.
- The main quiz flow is clear and well-oriented, combining scene numbering, progress, selectable answer cards, prior-scene feedback, and a detailed final scorecard.
- The staged code is appropriately simple for the task, with readable Flask routes, explicit genre data, separated templates/styles, and verification evidence for the main path.

## Main weaknesses

- The answer key has no correct D option and is unevenly distributed as A 9, B 14, C 7, D 0, creating a predictable positional cue.
- Verification does not cover restart, answer revision, empty submissions as a distinct case, or other edge paths; the reviewer could not independently rerun because the local shell lacks the app’s Flask/pytest dependencies.
- One small polish gap remains in the supplied run: the browser records a missing `/favicon.ico` request, and the implementation’s option-letter rendering assumes exactly four options.

## Reviewer confidence

Overall confidence: **High**.

Directly verified from the supplied evidence: the app launch, rendered start/question/results states, the complete 30-step browser path, the final 9/30 result, the server request sequence, and the supplied four-test pass result. Inferred or source-verified from the staged submission: the 30-question/four-option inventory, answer-position distribution, session-state and navigation guards, invalid/missing-answer branch, and restart clearing logic. Remained unverified: an independent local rerun and an actual click-through of the play-again action. The fresh complete trace and rendered evidence are strong enough to support the ratings despite those limits.
