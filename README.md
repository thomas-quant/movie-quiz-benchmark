# Movie Types Quiz — Coding-Agent Benchmark

Completed benchmark publication for one-shot coding agents building multi-page Flask quizzes about movie types or genres.

The canonical public aggregation is [`data/reviews.json`](data/reviews.json). Full methodology and results are in [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) and [`docs/RESULTS.md`](docs/RESULTS.md). The raw published reviews remain keyed by opaque submission IDs; the model-level leaderboard and gallery are post-review joins.

## Automated review leaderboard

<details open>
<summary>Quality leaderboard — rubric score, objective flow, and efficiency</summary>

Quality is the rubric-weighted score only: `(frontend / 5 × 40) + (UX / 5 × 40) + (code / 5 × 15) + (verification / 5 × 5)`. Build time and output tokens are separate build-turn efficiency facts and never affect Quality. Flow and Integrity are compact objective-baseline labels; the full evidence rows live in [`data/reviews.json`](data/reviews.json).

| Submission | Quiz type | Quality | Frontend | UX | Code | Verification | Flow | Integrity | Build time | Output tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | ---: |
| [codex/v3-sol](openai/codex/v3-sol/SCORECARD.md) (`submission-003`) | knowledge | **88/100** | 5/5 | 4/5 | 4/5 | 4/5 | Pass | Biased | 6m 14s | 14.0k |
| [v1-opus-4.8](anthropic/v1-opus-4.8/SCORECARD.md) (`submission-006`) | knowledge | **78/100** | 4/5 | 4/5 | 4/5 | 2/5 | Pass | Biased | 5m 01s | 28.4k |
| [codex/v2](openai/codex/v2/SCORECARD.md) (`submission-001`) | knowledge | **78/100** | 4/5 | 4/5 | 4/5 | 2/5 | Pass | Balanced | 6m 40s | 41.1k |
| [codex/v3-luna](openai/codex/v3-luna/SCORECARD.md) (`submission-009`) | knowledge | **77/100** | 5/5 | 3/5 | 4/5 | 1/5 | Pass | Biased | 6m 38s | 18.4k |
| [codex/v3-terra](openai/codex/v3-terra/SCORECARD.md) (`submission-013`) | knowledge | **69/100** | 4/5 | 3/5 | 4/5 | 1/5 | Pass | Biased | 4m 28s | 11.4k |
| [big-pickle](opencode/big-pickle/SCORECARD.md) (`submission-005`) | knowledge | **66/100** | 4/5 | 3/5 | 3/5 | 1/5 | Pass | Biased | 1m 47s | 6,970 |
| [m3](minimax/m3/SCORECARD.md) (`submission-007`) | personality/genre-match | **66/100** | 4/5 | 3/5 | 3/5 | 1/5 | Pass | Category imbalance; prior-category leak | 2m 24s | 8,570 |
| [m2](minimax/m2/SCORECARD.md) (`submission-011`) | knowledge | **58/100** | 3/5 | 3/5 | 3/5 | 1/5 | Pass | Biased | 1m 41s | 7,786 |
| [m2.5](minimax/m2.5/SCORECARD.md) (`submission-004`) | knowledge | **58/100** | 3/5 | 3/5 | 3/5 | 1/5 | Pass | Biased | 3m 51s | 15,396 |
| [m2.7](minimax/m2.7/SCORECARD.md) (`submission-002`) | knowledge | **58/100** | 3/5 | 3/5 | 3/5 | 1/5 | Pass | Biased | 1m 52s | 4,924 |
| [v4-flash](deepseek/v4-flash/SCORECARD.md) (`submission-010`) | knowledge | **58/100** | 3/5 | 3/5 | 3/5 | 1/5 | Pass | Biased | 1m 33s | 6,654 |
| [codex/v1](openai/codex/v1/SCORECARD.md) (`submission-008`) | knowledge | **56/100** | 3/5 | 2/5 | 4/5 | 4/5 | Pass | Answer leak | 5m 31s (done ~4m 30s) | 16.0k |
| [mimo-v2.5](xiaomi/mimo-v2.5/SCORECARD.md) (`submission-012`) | knowledge | **55/100** | 3/5 | 3/5 | 2/5 | 1/5 | Pass | Severely biased | 1m 35s | 7,055 |
| [m2.1](minimax/m2.1/SCORECARD.md) (`submission-014`) | knowledge | **50/100** | 3/5 | 2/5 | 3/5 | 1/5 | Pass | Biased | 4m 46s | 6,639 |

The automated blind review is the canonical quality assessment. Historical maintainer scorecards are preserved under their `Legacy assessment` sections and use a different, non-comparable scale.

</details>

## Reviewer methodology

<details>
<summary>Blind review model, rubric, anonymization, and aggregation</summary>

- Each coding agent received a one-shot Flask task: build a multi-page quiz about movie types or genres, render a new page or server-rendered step per question, retain context between pages, and provide at least 30 questions.
- Each submission received one canonical blind review using [`REVIEWER.md`](REVIEWER.md) and the fixed blind reviewer configuration recorded in the benchmark policy.
- Reviewer contexts contained only the anonymized staged submission, fresh evidence, benchmark task context, and rubric. Model, provider, source path, ranking, and existing scorecard context were excluded.
- Submission-006’s corrected Luna/xhigh review replaced the flawed draft in place; it is not a second independent rating.
- Quality uses integer ratings with weights of Frontend 40%, UX 40%, Code 15%, and Verification 5%.
- Build time and output tokens are reported separately and never affect Quality.
- The public export keeps raw reviews opaque. The model-level join is used only after blind review for the leaderboard and scorecard gallery.

See [`docs/RESULTS.md`](docs/RESULTS.md) for the complete objective baseline, confidence handling, limitations, and capture caveats.

</details>

## Automated testing and capture

<details>
<summary>Fresh headed Playwright/Chromium flow verification</summary>

The fresh evidence was produced by an automated Playwright runner that launched each staged Flask app, opened the initial page, selected answers through the rendered controls, completed the ordinary flow, and captured start/question/results states.

| Setting | Value |
| --- | --- |
| Browser | Headed Chromium via Playwright under Xvfb |
| Viewport | 1440 × 1000 CSS pixels |
| Device scale factor | 2 |
| Locale | `en-GB` |
| Screenshot output | Full-page, lossless PNG |
| Stability | CSS animations/transitions disabled |

All 14 final capture sets completed. The crawler was corrected to discover visually hidden radio inputs; the corrected runner was an external patched copy and was not committed, so no runner SHA is claimed. The publication process did not rerun captures or reviews. Most captures recorded only a non-blocking missing-favicon console 404; final metadata recorded no page errors.

The capture outputs used here are the fresh files in [`screenshots/reviewed/`](screenshots/reviewed/), not the repository’s legacy `screenshots/` files.

</details>

## Fresh screenshot gallery

Each model has a collapsible gallery of the three fresh automated-review captures. Use the scorecard link for the full objective baseline, rubric evidence, and legacy assessment.

<details>
<summary>codex/v3-sol — submission-003 — Quality 88/100</summary>

[Open scorecard](openai/codex/v3-sol/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![codex/v3-sol start](screenshots/reviewed/submission-003-start.png) | ![codex/v3-sol question](screenshots/reviewed/submission-003-question.png) | ![codex/v3-sol results](screenshots/reviewed/submission-003-results.png) |

</details>

<details>
<summary>v1-opus-4.8 — submission-006 — Quality 78/100</summary>

[Open scorecard](anthropic/v1-opus-4.8/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![v1-opus-4.8 start](screenshots/reviewed/submission-006-start.png) | ![v1-opus-4.8 question](screenshots/reviewed/submission-006-question.png) | ![v1-opus-4.8 results](screenshots/reviewed/submission-006-results.png) |

</details>

<details>
<summary>codex/v2 — submission-001 — Quality 78/100</summary>

[Open scorecard](openai/codex/v2/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![codex/v2 start](screenshots/reviewed/submission-001-start.png) | ![codex/v2 question](screenshots/reviewed/submission-001-question.png) | ![codex/v2 results](screenshots/reviewed/submission-001-results.png) |

</details>

<details>
<summary>codex/v3-luna — submission-009 — Quality 77/100</summary>

[Open scorecard](openai/codex/v3-luna/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![codex/v3-luna start](screenshots/reviewed/submission-009-start.png) | ![codex/v3-luna question](screenshots/reviewed/submission-009-question.png) | ![codex/v3-luna results](screenshots/reviewed/submission-009-results.png) |

</details>

<details>
<summary>codex/v3-terra — submission-013 — Quality 69/100</summary>

[Open scorecard](openai/codex/v3-terra/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![codex/v3-terra start](screenshots/reviewed/submission-013-start.png) | ![codex/v3-terra question](screenshots/reviewed/submission-013-question.png) | ![codex/v3-terra results](screenshots/reviewed/submission-013-results.png) |

</details>

<details>
<summary>big-pickle — submission-005 — Quality 66/100</summary>

[Open scorecard](opencode/big-pickle/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![big-pickle start](screenshots/reviewed/submission-005-start.png) | ![big-pickle question](screenshots/reviewed/submission-005-question.png) | ![big-pickle results](screenshots/reviewed/submission-005-results.png) |

</details>

<details>
<summary>m3 — submission-007 — Quality 66/100</summary>

[Open scorecard](minimax/m3/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![m3 start](screenshots/reviewed/submission-007-start.png) | ![m3 question](screenshots/reviewed/submission-007-question.png) | ![m3 results](screenshots/reviewed/submission-007-results.png) |

</details>

<details>
<summary>m2 — submission-011 — Quality 58/100</summary>

[Open scorecard](minimax/m2/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![m2 start](screenshots/reviewed/submission-011-start.png) | ![m2 question](screenshots/reviewed/submission-011-question.png) | ![m2 results](screenshots/reviewed/submission-011-results.png) |

</details>

<details>
<summary>m2.5 — submission-004 — Quality 58/100</summary>

[Open scorecard](minimax/m2.5/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![m2.5 start](screenshots/reviewed/submission-004-start.png) | ![m2.5 question](screenshots/reviewed/submission-004-question.png) | ![m2.5 results](screenshots/reviewed/submission-004-results.png) |

</details>

<details>
<summary>m2.7 — submission-002 — Quality 58/100</summary>

[Open scorecard](minimax/m2.7/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![m2.7 start](screenshots/reviewed/submission-002-start.png) | ![m2.7 question](screenshots/reviewed/submission-002-question.png) | ![m2.7 results](screenshots/reviewed/submission-002-results.png) |

</details>

<details>
<summary>v4-flash — submission-010 — Quality 58/100</summary>

[Open scorecard](deepseek/v4-flash/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![v4-flash start](screenshots/reviewed/submission-010-start.png) | ![v4-flash question](screenshots/reviewed/submission-010-question.png) | ![v4-flash results](screenshots/reviewed/submission-010-results.png) |

</details>

<details>
<summary>codex/v1 — submission-008 — Quality 56/100</summary>

[Open scorecard](openai/codex/v1/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![codex/v1 start](screenshots/reviewed/submission-008-start.png) | ![codex/v1 question](screenshots/reviewed/submission-008-question.png) | ![codex/v1 results](screenshots/reviewed/submission-008-results.png) |

</details>

<details>
<summary>mimo-v2.5 — submission-012 — Quality 55/100</summary>

[Open scorecard](xiaomi/mimo-v2.5/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![mimo-v2.5 start](screenshots/reviewed/submission-012-start.png) | ![mimo-v2.5 question](screenshots/reviewed/submission-012-question.png) | ![mimo-v2.5 results](screenshots/reviewed/submission-012-results.png) |

</details>

<details>
<summary>m2.1 — submission-014 — Quality 50/100</summary>

[Open scorecard](minimax/m2.1/SCORECARD.md)

| Start | Question | Results |
| --- | --- | --- |
| ![m2.1 start](screenshots/reviewed/submission-014-start.png) | ![m2.1 question](screenshots/reviewed/submission-014-question.png) | ![m2.1 results](screenshots/reviewed/submission-014-results.png) |

</details>

## Publication layout

- `data/reviews.json` — canonical public aggregation and post-review leaderboard join.
- `reviews/submission-XXX.md` — one canonical anonymized review per opaque ID.
- `screenshots/reviewed/` — fresh lossless PNG start/question/results captures.
- `docs/RESULTS.md` — methodology, setup, objective baseline, ratings, limitations, and publication notes.
- `export/` in the private review workspace — sanitized external public export containing only permitted artifacts.

No submission source code, captures, reviews, or repository history were rerun or modified as part of publication.
