# Methodology

A head-to-head benchmark: each coding agent gets the **same one-shot prompt** to build a
multi-page Flask quiz on the **types/genres of movies**, then the result is judged. No
iteration, no follow-ups — whatever the model ships on the first pass is what gets scored.

## The prompt

**Claude** and **Codex v1** received the same prompt:

> Using flask, make a quiz that spans across multiple pages. New page per question,
> while keeping context of what happened last page. Quiz topic is types of movies.
> minimum 30 questions. Don't invoke any of your skills, this is a one-shot prompt.

**Codex v3 Luna, Sol, and Terra** received that same original prompt. They are recorded
as separate v3 variants rather than renamed to v1, even though they share its prompt.

**Codex v2** was a re-run with a tweaked prompt that added a test-yourself instruction
and banned test files:

> …Make the app first, and then test it yourself. Do not make python test files.

## Run conditions

- One shot per run — no retries or follow-up turns. Codex was simply run a second time as
  v2 with the tweaked prompt; that re-run is its own submission, not an iteration on v1.
- No skills invoked.
- Each app is self-contained Flask, serving on `http://127.0.0.1:5000`.
- Per-question state is kept across pages via Flask's signed `session` cookie.

## Scoring

Scores are the benchmark author's judgement, anchored where possible to **falsifiable**
properties — things that are objectively right or wrong (does every question render, is
state kept, is the score correct, can the answer be seen before picking). Qualitative
factors such as frontend polish and token efficiency are called out explicitly; the v3
maintainer scores below include those factors where noted.

### Final tally

| Submission | Score | Why |
| --- | --- | --- |
| **Codex v2** | **+2** | Caught and fixed v1's answer leak; cleanest UI of the three (start screen especially); staircase creativity offset by bad scaling. |
| **Claude** | **−1** | Worked on the first try, but minor UI rendering issues. |
| **Codex v1** | **−3** | Answer-lookahead leak (every answer A + category shown on the card) and tests written before the app. |
| **Codex v3 / Sol** | **+5** | Gorgeous frontend, no lookahead or all-A issue, app test file plus self-testing, and an efficient 14.0k-token build. |
| **Codex v3 / Luna** | **+3** | Stunning frontend and finish screen with category percentages; no test file (−1) and all answers A (−1), offset by the strong overall result from the cheapest model. |
| **Codex v3 / Terra** | **−1** | Fixed the lookahead issue, but the frontend was weak, A was correct 26/30, and there was no test file; notably fast and token-efficient. |

Per-submission detail, metrics, and screenshots live in each submission's `SCORECARD.md`.

The Codex v3 scorecards preserve the same factual fields as the expanded cohort and include
the maintainer's final scores and rationale.

## Expanded cohort: opencode runs

A second cohort of models (`opencode/big-pickle`, `deepseek/v4-flash`, `xiaomi/mimo-v2.5`,
and the `minimax/` family) was run through **[opencode](https://opencode.ai)**. Each
received the **same one-shot prompt** as Claude/Codex v1 (verified verbatim against the
opencode session transcripts).

### How the metrics are measured

opencode stores each run as a session of *turns* (a user message plus the assistant
messages it triggers). Metrics are taken from the **build turn only** — the one-shot prompt
through the assistant finishing writing files. Later turns in the same session (e.g. "run
on port 3000", "run for me") are **excluded**, so they don't inflate the figures.

- **Build wall time** = last assistant completion in the build turn − prompt submission time.
- **Output tokens** = sum of completion tokens across the build turn's assistant messages
  (reasoning tokens are reported separately in each scorecard, not in the headline number).

### How the scorecards are produced

The opencode scorecards record **facts only**; the qualitative call and final score are
left to the maintainers (each has a blank "Maintainer assessment" section). Facts come from
two passes:

1. **Static read** of each `app.py` and its templates — question count, answer-position
   distribution, state mechanism, anti-skip behaviour, live-score presence, restart, etc.
2. **Live browser run** (Chromium via Playwright): each app is launched fresh on a clean
   port and driven start → results. This confirms it runs without error and produces a
   results page. The crawler always picks option A, so the final score should equal the
   static **A-count** — a cross-check that held for all eight knowledge quizzes, verifying
   both the answer-distribution reading and that scoring works.

(`north_mini_code` and `nemotron_3_ultra` are not in this cohort: the former is pending a
re-run, the latter was dropped.)
