# Review — submission-008

## Summary

This is a complete, cleanly implemented 30-question knowledge quiz with a coherent teal-and-neutral interface, clear progress, per-answer feedback, and a thorough final answer history. Its central weakness is severe quiz-integrity damage: every correct answer is the first option, and the current answer is displayed as the question's category before the user answers, making the otherwise smooth experience trivially solvable; the visual treatment is also generic rather than distinctly cinematic.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | Fresh evidence records a completed Flask launch; `/`, `/static/styles.css`, and the first question returned successful responses. The only console error was a non-blocking missing favicon (404), with no page errors. |
| Full flow completes | Yes | The fresh browser trace submitted 30 answers, moved from `/quiz/1` through `/quiz/30`, and reached `/result` without a runtime or page error. |
| Quiz type | knowledge | Each prompt asks the user to identify a movie genre/type and is evaluated against a defined correct answer. |
| Questions | 30; 4 options each | The staged question bank contains 30 entries, each with four options; the start and question screens also render “30 questions” and “Question 1 of 30.” |
| Page-per-question behavior | Yes | Fresh trace URLs advance one server-rendered route at a time (`/quiz/1`, `/quiz/2`, …, `/quiz/30`), and the question template renders one prompt. |
| State between pages | Yes | The 30-step browser run retained answers through the 30/30 result and complete answer history. Source stores index, score, answers, and last feedback in the Flask session; passing tests also inspect retained session state. |
| Meets minimum question count | Yes | 30 questions meets the requirement of at least 30. |
| Content matches movie types/genres | Yes | All prompts concern genres, formats, or recognizable movie types such as action, documentary, film noir, heist, and road movie rather than general film trivia. |
| Scoring/result generation | Yes | Selecting the first option for all 30 questions produced 30/30, consistent with the staged key in which every correct answer is first. The result page shows the score and all 30 submitted/correct-answer pairs. |
| Answer/category leak | Yes | Before an answer is submitted, the question header prints `question.category`; on question 1 it visibly says “Action,” exactly matching the correct option. In the staged data, `category` equals `answer` for all questions. |
| Answer-position distribution | A: 30, B: 0, C: 0, D: 0 | Every staged `answer` is `options[0]`; the fresh all-first-option run scoring 30/30 independently confirms the pattern. |
| Skip/direct-navigation behavior | Yes — prevented | A passing test confirms that requesting `/quiz/3` at the beginning redirects to `/quiz/1`; route logic similarly redirects to the session's expected question. Missing/invalid answers are rejected with a 400 response and “Choose one of the listed answers,” and the radio group is browser-required. |
| Restart behavior | Unverified | The supplied browser trace did not activate Restart/Try again after completion. Source posts both controls to `/start`, calls `session.clear()`, and a passing test confirms `/start` initializes empty state, but completed-session clearing was not directly exercised by the supplied evidence. |
| Tests present | Yes | `submission/tests/test_quiz.py` contains 8 tests covering question count/shape, start state, one-question rendering and progress, answer/state advancement, direct-URL skipping, invalid answers, full completion/history, and result access before starting. |
| Tests pass | Yes | Supplied `test-results.txt` reports `8 passed in 0.15s` for `pytest -q`. |
| Self-testing evidence | Unverified | Meaningful staged tests exist and pass in the supplied fresh run, but the available artifacts do not establish that the submitting agent itself ran them during its one-shot build. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 3/5 | 40% | 24/40 | Start, question, and result screenshots show consistent typography, alignment, spacing, controls, progress treatment, and a restrained teal palette with no broken layout. The large headings and generous whitespace are readable, but the oversized white-card treatment, plain system typography, and near-total lack of movie-specific imagery or styling make the identity generic. The results page becomes a long, visually repetitive list, and the missing favicon is a small finishing omission. |
| UX and interaction design | 2/5 | 40% | 16/40 | Expectations, question count, current position, click targets, required selection, last-answer feedback/explanations, final score, review history, and replay control are all clear. However, the experience fails as a meaningful knowledge test because every screen labels the answer in advance and every correct choice occupies the first position. That repeated flaw removes uncertainty from all 30 questions. Feedback also appears on the following question rather than before advancing, while the final page offers no percentage, performance interpretation, or focused takeaway beyond a very long answer list. |
| Code quality and maintainability | 4/5 | 15% | 12/15 | The small Flask implementation is easy to follow: structured question data, an app factory, focused routes, shared templates/styles, explicit session state, validation, orderly redirects, and a reusable question template. The uniform first-option key and answer-revealing `category` field are serious content-model/design mistakes, but the code itself is compact and straightforward to change. |
| Tests and verification evidence | 4/5 | 5% | 4/5 | Eight passing tests meaningfully cover the main flow, persisted state, invalid input, URL skipping, completion, and premature results access, and fresh browser evidence completes all 30 steps. Coverage stops short of replay clearing after a completed run, wrong-answer score totals, and browser-visible feedback states. |
| **Quality score** |  | **100%** | **56/100** | Weighted calculation: 24 + 16 + 12 + 4. |

## Strongest aspects

- The supplied browser evidence demonstrates a stable full 30-question server-rendered flow with clear progress and no page errors.
- The visual system is consistent and readable across start, question, and result states, with well-sized controls and a clean answer layout.
- The implementation is unusually well verified for this task: its focused tests cover state, invalid input, flow enforcement, and full completion, and all eight pass.

## Main weaknesses

- Displaying each question's category exposes the correct answer before selection, so the core quiz interaction cannot test knowledge.
- The answer key is maximally position-biased (30/30 correct answers in position A), a pattern visibly confirmed by the fresh 30/30 all-first-option run.
- The presentation has little movie-specific personality, and the result experience is a repetitive 30-item transcript without a performance label, summary insight, or targeted learning guidance.

## Reviewer confidence

**High.** The supplied fresh evidence directly verifies launch, the rendered start/question/results states at 1440×1000, a complete 30-answer browser run, URL progression, the final 30/30 score/history, server responses, and absence of page errors. The staged source and passing tests establish the full question bank, four-option structure, session/scoring logic, invalid-answer handling, and direct-navigation enforcement. Restart after a completed run and whether the submitting agent personally executed its tests remain **Unverified**.
