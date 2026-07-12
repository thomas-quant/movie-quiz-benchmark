# Review — submission-009

## Summary

Reel Types is a complete 30-question knowledge quiz with unusually strong editorial art direction, a clear server-rendered question flow, reliable session state, and a detailed final answer review. Its principal weakness is a severe quiz-integrity flaw: all 30 correct answers are option A, making the experience predictable despite otherwise polished interaction design. No submission-authored tests or self-testing evidence are present.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | Launched successfully from a clean process using the staged Flask environment and served `/`, `/quiz`, and `/results` without runtime errors. The existing browser run also has `status: completed`, and its server log contains successful responses through the results page. |
| Full flow completes | Yes | Independently completed two fresh 30-answer HTTP flows. Both reached `/results` without an error; the staged browser trace likewise records a complete run. |
| Quiz type | knowledge | Every question asks for the correct movie genre, type, format, or hybrid, and the app computes correctness and a numeric score. |
| Questions | 30; 4 options each | Runtime/source measurement found 30 unique prompts, with four choices for every prompt. |
| Page-per-question behavior | Yes | Each answer is submitted to the server, followed by a redirect and a newly rendered `/quiz` response for the next numbered scene. The URL is shared, but each question is a distinct server-rendered step. |
| State between pages | Yes | A 30-step fresh run retained the current index, score, answer indices, and last-answer feedback in the Flask session through to results. |
| Meets minimum question count | Yes | Exactly 30 questions meets the at-least-30 requirement. |
| Content matches movie types/genres | Yes | All 30 prompts concern genres/types such as superhero, western, documentary, film noir, mockumentary, slasher, and space opera; there is no drift into general movie trivia. |
| Scoring/result generation | Yes | Selecting the first option for all questions produced 30/30 and 30 correct review rows; selecting the fourth option throughout produced 0/30 and 30 missed rows. The results page reconstructs each selection, correct answer, explanation, overall verdict, percentage, and category scores consistently. |
| Answer/category leak | No | The rendered question page shows the broad section label and four choices, but does not expose the correct choice or its explanation before submission. The position bias below still makes the key readily predictable once noticed. |
| Answer-position distribution | A: 30, B: 0, C: 0, D: 0 | Measured across all 30 source questions: every correct answer is the first option. This is extreme position bias. |
| Skip/direct-navigation behavior | Sensibly handled; no bypass found | A blank answer submission redisplayed scene 1 with “Choose an answer before continuing.” Direct `/results` access before completion redirected to the current quiz/home state. There is no question-number URL with which to jump ahead. |
| Restart behavior | Yes | Posting “Play it again” removed the quiz session, returned to the start page, and a subsequent `/quiz` request redirected home. Starting from the home page also creates a fresh state. |
| Tests present | No | The permitted file inventory contains no test files; `test-results.txt` says “No test files found.” The original prompt variant did not prohibit Python tests. |
| Tests pass | N/A | No tests were available to run; `test-results.txt` records `not-run`. |
| Self-testing evidence | No | No submission-authored test, test command, or documented manual/self-test was found. The supplied screenshots, trace, metadata, and server log are benchmark evidence, not evidence that the submitting agent tested its own work. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 5/5 | 40% | 40/40 | The rendered start, question, and results states share a distinctive, highly finished cinema-editorial identity: disciplined paper/orange/yellow color, strong grotesk/serif/mono typography, precise grid alignment, custom ticket artwork, restrained grain and rules, clear button and selection states, and consistent “scene/reel/final cut” details. Hierarchy remains excellent from the oversized hero through the question sidebar and score stamp to the dense answer review. No broken assets, overflow, or visibly unfinished areas appear in the supplied 1440×1000 captures. |
| UX and interaction design | 3/5 | 40% | 24/40 | The start page clearly promises 30 multiple-choice questions and an instant score; numbered scene progress, a progress track, selected-radio styling, blank-answer validation, previous-answer feedback, and guarded results make the core flow easy to understand. Results are especially useful, with a verdict, percentage, category breakdown, all 30 answers, corrections, explanations, and an obvious replay control. However, the 30/30 A-only key is a major experiential flaw: after the pattern becomes apparent, choosing answers no longer tests genre knowledge and the polished 30-step flow loses credibility. Also, a wrong answer gets only “Plot twist” plus the user’s selection on the next page; the correction is deferred until the long final review. |
| Code quality and maintainability | 4/5 | 15% | 12/15 | The small Flask implementation is clear and proportionate: data is consistently structured, routes have focused responsibilities, templates separate the three states, CSS is centralized with reusable tokens/components, and session data stores compact choice indices while rebuilding the detailed review from the canonical question set. Validation, redirects, restart, scoring tiers, and category aggregation are easy to follow. The implementation is straightforward to change, though the large inline question bank and lack of automated integrity checks allowed the all-A key defect to pass unnoticed. |
| Tests and verification evidence | 1/5 | 5% | 1/5 | No tests or credible submission-authored verification evidence are present even though the original prompt allowed Python test files. The benchmark’s later completed browser trace verifies behavior for review purposes, but it does not demonstrate agent self-verification. |
| **Quality score** |  | **100%** | **77/100** | `(5/5 × 40) + (3/5 × 40) + (4/5 × 15) + (1/5 × 5) = 77`. |

## Strongest aspects

- The interface has a coherent, distinctive cinema-publication identity carried through every state, with exceptionally strong typography, spacing, illustration, and visual hierarchy.
- The quiz is easy to orient within: each server-rendered scene shows redundant question numbering, a progress bar, clear answer controls, validation, and concise last-answer feedback.
- The results experience is comprehensive and satisfying, combining an overall verdict with category-level scores and a full answer-by-answer review including corrections and explanations.

## Main weaknesses

- All 30 correct answers are option A. This extreme distribution undermines the integrity and replay value of the entire knowledge quiz.
- Wrong-answer feedback between questions does not provide the correct answer or explanation; learning feedback is postponed until the end of a 30-question run.
- There are no submission-authored tests or self-testing notes, despite the prompt variant allowing tests; even a small distribution/flow check would likely have caught the central answer-key defect.

## Reviewer confidence

**High.** I directly launched the staged app, performed complete fresh all-first-choice and all-fourth-choice runs, checked blank submissions, premature results access, scoring/review consistency, and restart behavior, and visually inspected the supplied full-page start, question, and results captures. Question count, choice count, answer-position distribution, state design, and result construction were confirmed from runtime/source inspection. The existing completed browser metadata, trace listing, screenshots, and server log corroborate the full UI flow. No required fact remains unverified; hover/focus animation quality was assessed from CSS rather than a fresh headed-browser interaction.
