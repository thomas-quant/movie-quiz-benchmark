# Review — submission-002

## Summary

submission-002 is a functioning 35-question Flask knowledge quiz with a clear dark glass-card interface, visible progress, and a useful score-and-answer review at the end. The supplied run completes all questions cleanly, but the presentation is fairly generic and the quiz has important integrity gaps: correct answers are heavily concentrated in a few option positions, and source-level routing does not enforce sequential progress. There is also no test suite or evidence of agent-authored self-testing.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | Fresh evidence reports `status: completed`; `server.log` shows the Flask server starting and `GET /` returning 200. The only logged browser error is a missing `/favicon.ico` (404), not an application page failure. |
| Full flow completes | Yes | The supplied metadata records 35 answer steps from `/question/0` through `/question/34` and a final `/results` load; `server.log` records the same progression with 200 responses for each question page and results. |
| Quiz type | knowledge | The start screen says it tests knowledge of film genres and classifications, and the app computes correct/incorrect answers and a score. |
| Questions | 35 | The start screenshot states 35 questions, and `QUESTIONS` contains 35 entries (`submission/app.py:7-43`). |
| Options per question | 4, consistently | Each question entry has four options, and the supplied question screenshot shows four answer buttons (`submission/app.py:7-43`; `submission/templates/question.html:14-18`). |
| Page-per-question behavior | Yes | Each question is rendered at its own `/question/<q_num>` URL; the fresh trace shows each POST redirecting to the next question URL (`submission/app.py:57-71, 74-96`). |
| State between pages | Yes | The completed trace preserves the randomized question sequence and produces a 2/35 result; source stores score, answers, question index, total, and shuffled questions in the session (`submission/app.py:48-53, 80-96`). |
| Meets minimum question count | Yes | 35 questions meets the required minimum of 30. |
| Content matches movie types/genres | Yes | The questions cover genres and movie classifications such as Horror, Sci-Fi, Western, Musical, Documentary, Thriller, and Superhero; the content does not drift into general movie trivia. |
| Scoring/result generation | Yes | The fresh results screenshot shows `5%`, `Cinema Newbie`, `2 out of 35`, and a per-question review. The score and percentage are generated from submitted answers (`submission/app.py:80-88, 104-122`). |
| Result agrees with submitted answers | Yes | The trace records the first option selected on all 35 steps, and the source answer positions make only two of those first options correct; the displayed result is 2/35. |
| Answer/category leak | No in the question UI | The question screenshot exposes only the prompt and four options; correctness is shown only on the results page after submission (`submission/templates/question.html:11-18`; `submission/templates/results.html:10-18`). |
| Answer-position distribution | A: 2, B: 24, C: 9, D: 0 | Counted from the 35 source entries. Answer options are not shuffled, so the correct position is strongly biased toward B and never D (`submission/app.py:7-43`). |
| Skip/direct-navigation behavior | No sequential guard; edge runtime unverified | The question route checks only that a shuffled session exists and indexes directly into the requested `q_num`; it does not compare against `session['question_index']`. The results route accepts the empty `answers` list initialized at start. This establishes a source-level bypass, though a separate direct-URL run was not available. |
| Unanswered-question handling | No robust handling; source-level | The normal UI has no skip control, but the POST handler accepts a missing `answer`, treats it as incorrect, stores `None`, and advances; the resulting browser rendering was not independently exercised (`submission/app.py:74-96`). |
| Restart behavior | Yes, source-verified; fresh restart not exercised | `/` calls `session.clear()` and reinitializes score, answers, question index, total, and shuffle; the results page links to `/` as “Play Again” (`submission/app.py:46-54`; `submission/templates/results.html:20`). |
| Results meaningfulness | Yes | Results provide a percentage, score, qualitative grade, per-question correctness/correction text, and a Play Again action (`submission/templates/results.html:4-20`). |
| Tests present | No | `test-results.txt` states `command: not run (no test files found)`. |
| Tests pass | N/A | There are no test files to execute; the supplied result is `not-run`. |
| Self-testing evidence | Unverified (none supplied) | The evidence package contains a fresh evaluator run, but no test files or agent-authored verification report; `test-results.txt` explicitly reports no tests found. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 3/5 | 40% | 24/40 | Start, question, and results states share a coherent dark gradient, translucent rounded card, pink accent, teal result state, clear typography, progress bar, and consistent controls. The visual identity is clean but generic, with no movie-specific visual language or imagery; the 35-item results review is a long, repetitive vertical list. |
| UX and interaction design | 3/5 | 40% | 24/40 | The start screen sets the topic and length, question pages have a clear count/progress indicator and one-click answers, and results explain the score with corrections and Play Again. The flow has no answer confirmation or correction path, and the unguarded direct routes plus highly predictable answer positions weaken the intended quiz experience. |
| Code quality and maintainability | 3/5 | 15% | 9/15 | The implementation is small and readable: question data is centralized, routes are easy to follow, and shared styling is in `base.html`. It is adequate for the task, but presentation includes inline styles and the compact route/session logic leaves little abstraction for future changes. |
| Tests and verification evidence | 1/5 | 5% | 1/5 | No tests are present or run, and no agent-authored self-test evidence is supplied. The evaluator trace verifies the happy path but does not replace a broader verification suite. |
| **Quality score** |  | **100%** | **58/100** | `(3/5 × 40) + (3/5 × 40) + (3/5 × 15) + (1/5 × 5) = 24 + 24 + 9 + 1 = 58`. |

## Strongest aspects

- The core baseline flow is complete and confirmed by a full 35-step fresh run, including state retention, scoring, and results rendering.
- The interface is visually consistent and easy to scan, with a restrained palette, prominent question hierarchy, four large answer controls, and clear progress orientation.
- The results state is more useful than a bare score: it includes a percentage, grade, total, per-question corrections, and an obvious Play Again action.

## Main weaknesses

- The answer key is heavily position-biased: A appears twice, B 24 times, C nine times, and D never appears. Because options are not shuffled, users can exploit the pattern rather than their genre knowledge.
- Progression is not enforced at the route level. A session can request later question URLs directly, and `/results` is allowed after only the initial session setup; malformed or missing-answer requests are also not handled gracefully.
- The visual treatment is competent but generic, and the results page becomes a long stack of nearly identical answer cards without a concise breakdown of missed genres or other higher-level feedback.
- No test files were found or run, so edge cases such as restart, direct navigation, and unanswered submissions lack execution evidence.

## Reviewer confidence

Overall confidence: **High**. The start, question, and results screenshots, completed metadata trace, and server log directly verify the main launch and completion path. Source inspection directly verifies the question count, four-option structure, session fields, scoring/result templates, restart reset, and answer-position distribution. Direct-URL edge behavior, missing-answer handling, and restart were not independently rerun in the reviewer environment and are identified as source-based or unverified above; there is also no supplied evidence of agent-authored tests.
