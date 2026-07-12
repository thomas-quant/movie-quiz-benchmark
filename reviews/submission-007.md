# Review — submission-007

## Summary

This is a complete 30-question personality/genre-match quiz with a cohesive dark cinema-adjacent presentation, clear progress, and an unusually substantive results page containing profile copy, film recommendations, a category tally, and a collapsible history. The supplied browser run completes all 30 steps and its final tally agrees with the submitted first options. Its largest weaknesses are experiential and structural: there is no introductory start screen, the next page reveals the category assigned to the previous answer, category opportunities are so unbalanced that some authored profiles cannot win, and no tests or self-verification evidence are present.

## Objective baseline

| Fact | Result | Evidence |
| --- | --- | --- |
| Launches | Yes | Fresh metadata reports `status: completed`; the server log shows `/` redirecting to `/question/1`, which returns 200. |
| Full flow completes | Yes | The supplied fresh trace records 30 successful answer steps from `/question/1` through `/question/30` and arrival at `/result`, with no page errors or runtime error. The only console error is an irrelevant missing favicon (404). |
| Quiz type | personality/genre-match | Every option maps a preference to one of nine genre categories; the outcome is a dominant genre profile rather than a correctness score. There are no claims that an answer is right or wrong. |
| Questions | 30 | `QUESTIONS` contains 30 entries, consistently with four options each; the rendered progress says “Question 1 of 30,” and the trace completes 30 submissions. |
| Page-per-question behavior | Yes | Each answer POST receives a 302 and is followed by a distinct server-rendered GET at `/question/<n>`; the log and trace show this sequence for all 30 questions. |
| State between pages | Yes | The browser-visible text on question 2 says “Last page, you leaned comedy,” and the final result aggregates all 30 stored category selections. Source uses Flask `session["answers"]`. |
| Meets minimum question count | Yes | The submission contains and serves exactly 30 questions, meeting the at-least-30 requirement. |
| Content matches movie types/genres | Yes | Questions ask about film mood, pacing, settings, subgenres, directors, endings, tropes, and viewing preferences, and map them to movie genres. It does not drift into a general movie-fact quiz. |
| Scoring/result generation | Yes | The fresh run chose the first option on every question. The rendered result reports Comedy 24/30, Action 2/30, and Musical, Thriller, Fantasy, and Romance 1/30 each, exactly matching the staged mappings. Every option has a category value and the result gives an explained profile, recommendations, breakdown, and history. However, mapping opportunities are severely unbalanced: Comedy appears in 29 of 120 options, Drama 24, Thriller 25, Action 13, Fantasy 10, Sci-Fi 9, Romance 6, Horror 3, and Musical 1. Musical and Horror therefore cannot win a 30-answer plurality. Ties are resolved by first insertion order rather than an explained rule. |
| Answer/category leak | Yes | From question 2 onward, the interface explicitly names the prior selection’s hidden category (for example, “Last page, you leaned comedy”). Current option categories are not printed before selection, but this repeated disclosure lets users infer and steer the mapping. |
| Answer-position distribution | N/A | A personality quiz has no correct-answer key. Category placement is nevertheless strongly positional: 24 of 30 A options are Comedy, 16 of 30 B options are Thriller, and 13 of 30 C options are Drama. |
| Skip/direct-navigation behavior | Unverified | The fresh run followed only the intended sequence. Source accepts a GET for any in-range `/question/<n>` and only guards incomplete state at `/result`; a direct jump was not exercised, so the browser-visible outcome remains Unverified. Unanswered submission is also Unverified in the browser run, although source includes both `required` radios and server-side invalid-choice handling. |
| Restart behavior | Unverified | The rendered result has a “Take it again” link to `/`, and the `/` route calls `session.clear()`, but the supplied interaction did not click it; clearing the previous session is therefore Unverified behaviorally. |
| Tests present | No | `test-results.txt` says “No test files found,” and the staged submission contains only `app.py`. This cohort did not prohibit Python tests. |
| Tests pass | N/A | No tests existed, so the test command was not run. |
| Self-testing evidence | No | No submission-authored tests or other credible self-testing record are supplied. The fresh benchmark browser trace verifies the artifact for review but is not evidence that the submitting agent tested it. |

## Quality ratings

| Category | Rating | Weight | Weighted points | Evidence |
| --- | ---: | ---: | ---: | --- |
| Frontend visual quality and polish | 4/5 | 40% | 32/40 | The question state has a strong, legible hierarchy: restrained violet/black background, consistently styled card, prominent question, large labeled answer targets, numeric and bar progress, and a clear coral CTA. The results state preserves the same visual system while organizing profile title, explanatory copy, film chips, tally rows, review disclosure, and restart action cleanly. Spacing and alignment are controlled, with no demonstrated overflow or broken asset. It falls short of exceptional because the system-font/glass-card treatment is fairly familiar, movie-specific identity is limited, selection feedback is mostly the native radio, and there is no distinct designed start state. |
| UX and interaction design | 3/5 | 40% | 24/40 | The primary flow is simple, the four choices are easy to scan, progress remains explicit over a long 30-step quiz, and the final profile is useful and satisfying rather than just a label. Against that, `/` drops the user directly into question 1 with no title, explanation, duration expectation, or start consent; there is no back/edit control; the prior category disclosure makes the result gameable; and the extreme category imbalance makes Musical and Horror outcomes unreachable. The collapsed history lists category labels and question text rather than the actual chosen option text, weakening review value. Restart, unanswered handling, and direct-jump behavior were not interaction-verified. |
| Code quality and maintainability | 3/5 | 15% | 9/15 | The single module is readable for this scope: question and result data are explicit, the routes are short, session state is understandable, invalid categories are checked server-side, and templates are separated into named constants. Maintainability is only competent because 710 lines combine content, routing, markup, and duplicated page CSS; `random` and a computed GET-side `last_answer` are unused; the template is instead always passed `answers[-1]`, which can show the wrong context after backward/direct navigation; jumping ahead pads the session with `None`; and plurality ties depend on dictionary insertion order. |
| Tests and verification evidence | 1/5 | 5% | 1/5 | No tests are present, the test command was not run, and there is no evidence of submission-authored manual or browser verification. The externally supplied fresh trace establishes that the main happy path works but does not improve the submission’s own verification evidence. |
| **Quality score** |  | **100%** | **66/100** | `(4/5 × 40) + (3/5 × 40) + (3/5 × 15) + (1/5 × 5) = 66`. |

## Strongest aspects

- The fresh browser evidence demonstrates a reliable full 30-page happy path with retained state and a result tally that exactly matches the submitted options.
- The question UI is visually consistent, readable, and well paced through clear option rows, a question count, a progress bar, and an obvious primary action.
- The results page is notably substantive: it combines an explained genre identity, tailored film recommendations, the complete category breakdown, an answer-history disclosure, and a replay affordance.

## Main weaknesses

- There is no real start screen: the root route clears state and immediately redirects to question 1, so users receive no quiz framing, time/length expectation, or explanation of how the match is determined.
- The genre model is materially biased. Comedy, Drama, and Thriller dominate the option pool, while Musical appears once and Horror three times; those two finished result profiles are mathematically unreachable as plurality winners.
- Each subsequent page reveals the raw genre category assigned to the prior selection, making the supposedly implicit personality mapping easy to reverse-engineer and steer.
- Navigation and review are underdeveloped: there is no back/edit control, the answer history omits the actual selected option text, and direct navigation, empty submission, and restart were not covered by supplied interaction evidence or tests.

## Reviewer confidence

Overall confidence: **Medium**. Launch, the complete 30-answer happy path, per-question URL transitions, retained state, the all-first-option tally, and the rendered question/results visuals were directly verified by the supplied fresh log, metadata, trace, and screenshots. Question count, category opportunity distribution, validation intent, direct-route structure, restart implementation, tie behavior, and maintainability findings came from the staged source. Unanswered submission, direct URL jumping, backward navigation, expansion of the answer history, and restart/session clearing were not exercised and remain **Unverified** as browser behavior. The supplied `question.png` is anomalously almost blank, but its contemporaneous trace records the full question body and four visible radios on the same URL, while the separate question-1 screenshot renders normally and the flow completes; the cause of that capture anomaly remains **Unverified**, so it was not treated as a demonstrated application rendering failure.
