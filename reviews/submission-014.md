# Review — submission-014

## Summary

This is a functional 31-step Flask knowledge quiz with a clean, consistent card-based interface and a clearly visible question counter. The corrected headed run completes successfully and its 10/31 result matches the submitted all-first-option answers, but the experience is generic and thin: the landing page promises the wrong question count, the content is broad film trivia rather than a quiz about movie types or genres, at least one answer key is plainly wrong, there is no answer feedback or review, and no testing evidence is present.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | Corrected fresh headed evidence is marked `completed`; the server log records successful 200 responses for the start page and quiz route. |
| Full flow completes | Yes | Evidence metadata records one start action followed by 31 answer actions without an error, and the final screenshot renders “Quiz Complete!” with a 10/31 score. |
| Quiz type | Knowledge | Questions have server-side correct-answer indexes and the result is a correctness score. |
| Questions | 31 | `QUESTIONS` contains 31 entries; the question and result screenshots both show a total of 31. The start page incorrectly says 30. |
| Options per question | 4 | Every staged question contains four options, and the rendered question shows four radio-label choices. |
| Page-per-question behavior | Yes | Each answer POST to `/quiz` returns a newly server-rendered question step. The URL is reused, but the corrected run records 31 sequential answer submissions. |
| State between pages | Yes | Flask session fields `question_index` and `score` carry progress and score between requests. |
| Meets minimum question count | Yes | 31 questions exceeds the required minimum of 30. |
| Content matches movie types/genres | No | The landing copy and question set focus on general movie trivia—directors, actors, quotations, awards, studios, and release history—rather than movie types or genres. |
| Scoring/result generation | Yes, mechanically; correctness is flawed | The all-first-option run scores 10/31, exactly matching the ten answer keys at index 0. However, question 1 assigns index 2 (“Queer”) as correct even though “The Story of the Kelly Gang” is the matching answer among its options. |
| Final result agrees with submitted answers | Yes, against the embedded key | Evidence records first-option selections throughout and shows 10/31; the source contains ten index-0 keys. The result therefore agrees with the app’s key, despite the key defect noted above. |
| Answer/category leak | No | Answer indexes remain in server-side `QUESTIONS` data and are not passed to or rendered by the question template. |
| Answer-position distribution | A: 10, B: 14, C: 6, D: 1 | Measured from the 31 embedded answer indexes. B is most common and D is notably underused, but answers are not all in one position. |
| Unanswered-question behavior | Browser blocks; server does not | Each radio group is `required`, so ordinary blank submission is prevented. A missing or invalid `answer` POST becomes `-1` and still advances to the next question as incorrect. |
| Skip/direct-navigation behavior | Direct question jumping: No; crafted POST bypass: Yes | A fresh `/quiz` request without session state redirects to `/`, and there is no question number in the URL. Repeated crafted POSTs can nevertheless advance because the server does not validate that an answer index was supplied or is in range. |
| Restart behavior | Yes | “Play Again” links to `/`; the index route calls `session.clear()` and reinitializes score and question index. |
| Results page outcome/review | Minimal | It provides a numerical score and one threshold-based message, but no correct-answer review, explanations, missed-question list, percentage, or other useful recap. |
| Tests present | No | The submission contains only `app.py` and three templates; `test-results.txt` says no test files were found. Python tests were not prohibited for this prompt variant. |
| Tests pass | N/A | The staged test result is `not-run` because there were no tests. |
| Self-testing evidence | No | No submission-authored test or manual self-test record is present. The corrected headed run is benchmark evidence, not evidence that the submitting agent tested its own work. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 3/5 | 40% | 24/40 | The start, question, and result states share a clear Georgia-serif hierarchy, navy background, pale central panel, coral actions, generous spacing, and consistent rounded controls. The headed screenshots show no broken assets or overflow. The presentation is nevertheless a very generic gradient-and-card treatment with little movie-specific identity, large areas of unused space, only a text counter for progress, and a particularly bare result state. |
| UX and interaction design | 2/5 | 40% | 16/40 | Starting, selecting a required radio option, submitting, seeing orientation text, and restarting are straightforward, and the complete headed flow works. Repeated “Submit Answer” steps offer no correctness feedback or explanation, no back/review navigation, and little reward across a long 31-question run. The start screen’s 30-question promise conflicts with the actual 31, the content misses the requested types/genres focus, the first key is visibly nonsensical, and the final screen gives only a generic band message. |
| Code quality and maintainability | 3/5 | 15% | 9/15 | The small Flask implementation is readable: question data is centralized, routes are short, templates are separated, and session state is easy to follow. Maintainability is reduced by near-total CSS duplication across templates, an inline-styled submit button, unvalidated integer form parsing, and fragile completion state: the final response does not advance or clear `question_index`, so a later GET can render the last question again and a repeated final POST can rescore it. |
| Tests and verification evidence | 1/5 | 5% | 1/5 | No tests or submission-authored verification evidence exist, and the allowed Python-test route was available for this prompt variant. The external headed evidence establishes runtime behavior but does not show that the submission was self-verified. |
| **Quality score** |  | **100%** | **50/100** | **(3/5 × 40) + (2/5 × 40) + (3/5 × 15) + (1/5 × 5) = 50.** |

## Strongest aspects

- The core multi-request flow is complete: 31 server-rendered question steps retain score and position in the Flask session and reach a rendered result without runtime errors.
- The corrected all-first-option browser run produces 10/31, exactly matching the embedded answer-position distribution, which demonstrates that the basic accumulation logic works.
- The three primary screens are visually consistent and easy to scan, with clear headings, large answer targets, a visible question count, and an obvious restart action.

## Main weaknesses

- The submission does not follow the requested subject closely: it is explicitly a general “Movie Trivia Quiz,” and most questions test actors, directors, quotations, awards, or individual films rather than types or genres.
- Quiz integrity is compromised by the first answer key, which declares the unrelated option “Queer” correct for the first feature-length motion-picture question; the absence of answer feedback or review hides such defects from the user.
- The experience lacks depth across 31 repetitive steps: there is no per-answer feedback, explanation, meaningful progress visualization, backward review, or useful final breakdown, while the landing page also understates the length as 30 questions.
- Server-side flow validation is incomplete: crafted blank/invalid POSTs advance, and completion does not finalize the session index, allowing the last question to reappear or be rescored.
- No tests or credible self-testing evidence cover scoring, invalid submissions, completion state, or restart behavior.

## Reviewer confidence

**High.** Launch, the complete 31-answer flow, rendered start/question/result states, HTTP success, and the final 10/31 outcome were directly verified from the corrected fresh headed metadata, screenshots, and server log. Question count, answer distribution, session handling, restart behavior, validation gaps, completion-state bug, and the incorrect first key were verified from the complete staged source; test absence was verified from the staged file set and `test-results.txt`. I did not independently rerun the server, as instructed, and the factual accuracy of every remaining trivia item was not externally researched; those points remain unverified beyond the clear source-level defects identified above.
