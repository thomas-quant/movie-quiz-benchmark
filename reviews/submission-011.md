# Review — submission-011

## Summary

Submission-011 is a complete 41-question knowledge quiz with a clean, consistent navy-and-coral card interface, clear per-question progress, retained session state, working scoring, and a play-again path. Its main shortcomings are a severely position-biased answer key, a 40-versus-41 question-count mismatch, generic and occasionally broken visual details, a results review that omits both the chosen and correct answers, direct access to incomplete results, and no test or self-verification evidence.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | Corrected fresh headed evidence records a clean Flask launch, successful `GET /` responses, and `status: completed`. The only console error is a missing favicon (404); there are no page errors. |
| Full flow completes | Yes | The headed trace records 41 answer submissions and navigation to `/results`; the rendered result is `3 / 41` with no runtime or page error. |
| Quiz type | knowledge | Questions ask the user to identify movie genres, subgenres, and film styles, and the app assigns correct/incorrect outcomes. |
| Questions | 41 | `QUESTIONS` contains 41 entries. Every entry has exactly 4 options. The live question and result screens both show a total of 41, although the start screen incorrectly promises 40. |
| Page-per-question behavior | Yes | Each answer is submitted to the server; the fresh server log shows a `POST /question` followed by a redirect and a new `GET /question` for every step. The URL is reused, but each question is a newly server-rendered page. |
| State between pages | Yes | Flask session values retain `question_index`, `score`, and the answer history. The completed headed run reaches a cumulative `3 / 41` result after 41 separate requests. |
| Meets minimum question count | Yes | 41 questions exceeds the required minimum of 30. |
| Content matches movie types/genres | Yes | The content stays focused on genres, subgenres, and film styles such as horror, science fiction, film noir, mumblecore, cyberpunk, and documentary rather than drifting into general movie trivia. |
| Scoring/result generation | Yes | A complete all-option-A run produces `3 / 41`; source inspection independently shows that A is correct for exactly questions 8, 16, and 18. The result therefore agrees with the submitted answers. The page gives a score, percentage, feedback sentence, and per-question right/wrong list, but does not show the selected or correct answer for review. |
| Answer/category leak | No | Correct-answer indices remain server-side and the rendered question exposes only the four choices. Feedback appears only after submission and states correct/incorrect without revealing the right choice when the user was wrong. |
| Answer-position distribution | A: 3, B: 34, C: 4, D: 0 | Source measurement across all 41 questions shows 82.9% of correct answers in position B and none in D, which is a severe position bias. |
| Unanswered-question handling | Yes | The radio group is marked `required` in rendered HTML. A POST without `answer` also leaves the index unchanged and redirects back to the same question. |
| Skip/direct-navigation behavior | No | The same `/question` route prevents URL-based question-index jumps, but `/results` checks only for the existence of `question_index`; immediately after visiting `/`, a user can directly open `/results` and receive an incomplete `0 / 41` result. |
| Restart behavior | Yes | `/restart` redirects to `/`, whose route clears the session and initializes score, index, and answer history. This is verified from source rather than a recorded restart interaction. |
| Tests present | No | The staged submission has no test files. The prompt variant did not prohibit Python test files. |
| Tests pass | N/A | `test-results.txt` reports `command: not run (no test files found)` and `exit_code: not-run`. |
| Self-testing evidence | No | No submission-authored tests or other self-test artifact is staged. The corrected headed screenshots and trace are fresh reviewer evidence, not evidence that the submitting agent tested its own work. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 3/5 | 40% | 24/40 | Start and question states have a coherent dark-navy/coral palette, centered composition, readable hierarchy, generous spacing, consistent controls, and a clear progress treatment. The execution remains generic, however, and the corrected screenshots show the intended movie/trophy emoji as empty box glyphs. The results state is particularly under-polished: it is one very long stack of 41 near-identical rows, uses thick red/green side accents, and prints `7.317073170731707%` rather than a human-friendly value. |
| UX and interaction design | 3/5 | 40% | 24/40 | The start action is obvious, four choices are easy to scan, selection is required, score/progress remain visible, and the next page reports whether the previous response was correct. The experience sets the wrong expectation by advertising 40 questions before presenting 41, the progress bar starts at 0% on question 1, and wrong-answer feedback never teaches the correct answer. The final review repeats each prompt and only says right or wrong, omitting both what the user chose and what was correct; this makes the very long results page much less useful or satisfying than its “Review Your Answers” label promises. |
| Code quality and maintainability | 3/5 | 15% | 9/15 | The Flask implementation is concise and easy to follow: quiz data is structured consistently, routes are small, and session state and scoring are understandable. For this scope it is maintainable, but all three templates duplicate their full page/CSS shell, presentation constants are independently hard-coded, and `question.html` contains unused option styles plus imperative per-element inline styling. That styling also fails to reset a previously selected option's text color when another option is chosen, creating a brittle visual-state bug. |
| Tests and verification evidence | 1/5 | 5% | 1/5 | No tests are present, no test command ran, and there is no staged evidence of submission-authored manual or browser verification. The original prompt variant allowed Python tests. |
| **Quality score** |  | **100%** | **58/100** | **(3/5 × 40) + (3/5 × 40) + (3/5 × 15) + (1/5 × 5) = 24 + 24 + 9 + 1 = 58.** |

## Strongest aspects

- The complete server-rendered quiz flow works across all 41 questions, retaining score and answer history without runtime errors.
- The start and question states are immediately understandable, with a consistent visual system, strong contrast, clear grouping, and prominent primary actions.
- Scoring is internally consistent: the fresh all-A browser run's `3 / 41` outcome exactly matches the measured answer key, and restart logic clears the session cleanly.

## Main weaknesses

- The answer key is severely biased toward option B (34 of 41 answers, with zero answers in D), making the knowledge assessment easy to game and much less credible.
- The results experience is unwieldy and low-information: 41 repeated rows require extensive scrolling but reveal neither the user's selection nor the correct answer, while the percentage is shown at excessive precision.
- The experience contradicts itself about length—40 questions on the start screen versus 41 in the actual quiz—and direct access to `/results` can generate a misleading incomplete result.
- Visible polish is limited by broken emoji glyphs, a generic card-and-gradient treatment, and brittle option-selection styling; no tests or self-testing evidence cover these states or the core flow.

## Reviewer confidence

**High.** The corrected fresh headed metadata, screenshots, server log, and trace directly verify launch, all 41 answer submissions, server-rendered step transitions, the rendered start/question/results states, and successful completion without page errors. Staged source directly establishes the question and option counts, answer distribution, scoring agreement, session design, unanswered-POST behavior, direct-results bypass, restart semantics, and the option-style defect. `test-results.txt` directly establishes that no tests were found or run. Restart, blank submission, and direct `/results` access were not repeated in a new live browser session and are therefore source-verified rather than interaction-verified; no server was started for this re-review, as instructed.
