# Benchmark results

This document records the completed publication dataset for the Movie Types Quiz coding-agent benchmark. The canonical machine-readable source is [`data/reviews.json`](../data/reviews.json). The blind review files and evidence exports remain keyed by opaque submission IDs.

## Methodology

Each coding agent received a one-shot Flask task: build a multi-page quiz about movie types or genres, render a new page or server-rendered step per question, retain context between pages, and provide at least 30 questions. The artifact produced in that run was the artifact reviewed. The original and test-yourself/no-Python-tests prompt variants are documented in [`docs/METHODOLOGY.md`](METHODOLOGY.md).

The benchmark reports two separate dimensions: objective baseline behavior (launch, completion, content scope, scoring/integrity, navigation, restart, and tests) and a rubric-weighted quality score. The public aggregation does not replace those baseline facts with a single score.

## Reviewer model and configuration

- Reviewer rubric: [`REVIEWER.md`](../REVIEWER.md).
- Reviewer model/configuration: `gpt-5.6-luna` subagents dispatched with `xhigh` reasoning. This configuration was fixed for the blind review pass; the reviewer identity is not added to raw review files.
- Review passes: one canonical blind review per submission; no second independent pass was completed.
- Submission-006: the corrected Luna/xhigh review-1.md replaced the flawed earlier draft in place. It is the sole canonical review and was not averaged as a second rating.
- Review context: each reviewer received only its anonymized staged submission, fresh evidence, benchmark task context, and rubric. Model, provider, source path, ranking, and existing scorecard context were excluded.

## Fresh capture setup

The fresh evidence used headed Chromium through Playwright under Xvfb. The standard capture settings were:

| Setting | Value |
| --- | --- |
| Viewport | 1440 × 1000 CSS pixels |
| Device scale factor | 2 |
| Locale | `en-GB` |
| Browser | Chromium via Playwright |
| Display | Headed browser under `xvfb-run`/Xvfb |
| Animation handling | CSS animations and transitions disabled for stable captures |
| Screenshot format | Full-page, lossless PNG |
| App runtime | Fresh staged Flask process, Python 3.12 review environments |

The corrected crawler was an external patched copy of the capture runner. It changed radio discovery so visually hidden native radio inputs could still be selected and submitted. That patched copy was not committed, so no runner commit SHA is claimed. The repository runner remains the original tool; this publication does not rerun captures.

## Capture and retry process

The standardized runner opened each clean staged app, captured start/question/results PNGs, and drove the ordinary answer flow to completion. Three earlier capture sets were rerun after the crawler fix, then the two newly added runs were captured with the same corrected external runner; their initial host-library launch issue was resolved by supplying the configured browser-library path, and all 16 final sets completed. Publication copied only the final fresh PNGs and sanitized metadata. Trace archives, server logs, install logs, environments, staged source copies, and test-result files are excluded from the public export.

## REVIEWER.md rubric and weights

Quality uses integer ratings and exactly these weights:

| Category | Weight |
| --- | ---: |
| Frontend visual quality and polish | 40% |
| UX and interaction design | 40% |
| Code quality and maintainability | 15% |
| Tests and verification evidence | 5% |

`Quality = (frontend / 5 × 40) + (UX / 5 × 40) + (code / 5 × 15) + (verification / 5 × 5)`. Build time and output-token counts never enter this calculation.

## Anonymization and blind-context rules

Raw reviews and the external export use only `submission-001` through `submission-016`. The public manifest contains opaque IDs and artifact paths only. Sanitized metadata removes absolute filesystem paths, server commands, host/port details, private environments, caches, source paths, and provider mappings. The private manifest was consulted only after the blind reviews were complete to create the repository's post-review leaderboard and model-specific scorecard additions; no private source paths are published.

## Objective baseline results

| Opaque ID | Type | Questions | Launch | Full flow | Content scope | Scoring/result | Answer leak | Position distribution | Skip/direct navigation | Restart | Tests pass | Capture | Confidence |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| submission-001 | knowledge | 30 | Yes | Yes | Yes | Yes | No | Balanced: A 8, B 7, C 8, D 7 | Sensibly handled | Yes | N/A | completed | High |
| submission-002 | knowledge | 35 | Yes | Yes | Yes | Yes | No in the question UI | A: 2, B: 24, C: 9, D: 0 | No sequential guard; edge runtime unverified | Yes, source-verified; fresh restart not exercised | N/A | completed | High |
| submission-003 | knowledge | 30 | Yes | Yes | Yes | Yes | No | A: 9, B: 14, C: 7, D: 0 | No for normal GET navigation | Unverified | Yes, according to supplied results | completed | High |
| submission-004 | knowledge | 30 | Yes | Yes | No — substantial drift | Yes | No | A: 6, B: 16, C: 7, D: 1 | No — only guarded in the normal UI | Unverified | N/A | completed | High |
| submission-005 | knowledge | 32 | Yes | Yes | Yes | Yes | No | 13 A / 14 B / 5 C / 0 D | Yes, direct bypass exists | Yes, source-verified | N/A | completed | High |
| submission-006 | knowledge | 32 | Yes | Yes | Yes | Yes | No | A=16, B=12, C=4, D=0 | No | Yes | Unverified | completed | High |
| submission-007 | personality/genre-match | 30 | Yes | Yes | Yes | Yes | Yes | N/A | Unverified | Unverified | N/A | completed | Medium |
| submission-008 | knowledge | 30 | Yes | Yes | Yes | Yes | Yes | A: 30, B: 0, C: 0, D: 0 | Yes — prevented | Unverified | Yes | completed | High |
| submission-009 | knowledge | 30 | Yes | Yes | Yes | Yes | No | A: 30, B: 0, C: 0, D: 0 | Sensibly handled; no bypass found | Yes | N/A | completed | High |
| submission-010 | knowledge | 34 | Yes | Yes | Yes | Yes | No | B-heavy: A=7, B=20, C=7, D=0 | No intended-flow enforcement | Unverified | N/A | completed | High |
| submission-011 | knowledge | 41 | Yes | Yes | Yes | Yes | No | A: 3, B: 34, C: 4, D: 0 | Yes | Yes | N/A | completed | High |
| submission-012 | knowledge | 34 | Yes | Yes | Yes | Yes | No | Heavily biased | Bypassable | Yes | N/A | completed | High |
| submission-013 | knowledge | 30 | Yes | Yes | Yes | Yes | No | A: 26, B: 3, C: 1, D: 0 | Unverified | Unverified | N/A | completed | High |
| submission-014 | knowledge | 31 | Yes | Yes | No | Yes, mechanically; correctness is flawed | No | A: 10, B: 14, C: 6, D: 1 | Direct question jumping: No; crafted POST bypass: Yes | Yes | N/A | completed | High |
| submission-015 | knowledge | 32 | Yes | Yes | Yes | Yes, for the exercised path | No observed before answering | A: 8, B: 19, C: 5, D: 0 | Unverified | Unverified | N/A | completed | High |
| submission-016 | knowledge | 32 | Yes | Yes | Yes | Yes | No | 27 A / 3 B / 2 C / 0 D | Unverified | Unverified | N/A | completed | High |

## Quality ratings and aggregation

| Opaque ID | Frontend | UX | Code | Verification | Weighted points | Quality |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| submission-001 | 4/5 | 4/5 | 4/5 | 2/5 | frontend 32/40, ux 32/40, code 12/15, verification 2/5 | 78/100 |
| submission-002 | 3/5 | 3/5 | 3/5 | 1/5 | frontend 24/40, ux 24/40, code 9/15, verification 1/5 | 58/100 |
| submission-003 | 5/5 | 4/5 | 4/5 | 4/5 | frontend 40/40, ux 32/40, code 12/15, verification 4/5 | 88/100 |
| submission-004 | 3/5 | 3/5 | 3/5 | 1/5 | frontend 24/40, ux 24/40, code 9/15, verification 1/5 | 58/100 |
| submission-005 | 4/5 | 3/5 | 3/5 | 1/5 | frontend 32/40, ux 24/40, code 9/15, verification 1/5 | 66/100 |
| submission-006 | 4/5 | 4/5 | 4/5 | 2/5 | frontend 32/40, ux 32/40, code 12/15, verification 2/5 | 78/100 |
| submission-007 | 4/5 | 3/5 | 3/5 | 1/5 | frontend 32/40, ux 24/40, code 9/15, verification 1/5 | 66/100 |
| submission-008 | 3/5 | 2/5 | 4/5 | 4/5 | frontend 24/40, ux 16/40, code 12/15, verification 4/5 | 56/100 |
| submission-009 | 5/5 | 3/5 | 4/5 | 1/5 | frontend 40/40, ux 24/40, code 12/15, verification 1/5 | 77/100 |
| submission-010 | 3/5 | 3/5 | 3/5 | 1/5 | frontend 24/40, ux 24/40, code 9/15, verification 1/5 | 58/100 |
| submission-011 | 3/5 | 3/5 | 3/5 | 1/5 | frontend 24/40, ux 24/40, code 9/15, verification 1/5 | 58/100 |
| submission-012 | 3/5 | 3/5 | 2/5 | 1/5 | frontend 24/40, ux 24/40, code 6/15, verification 1/5 | 55/100 |
| submission-013 | 4/5 | 3/5 | 4/5 | 1/5 | frontend 32/40, ux 24/40, code 12/15, verification 1/5 | 69/100 |
| submission-014 | 3/5 | 2/5 | 3/5 | 1/5 | frontend 24/40, ux 16/40, code 9/15, verification 1/5 | 50/100 |
| submission-015 | 3/5 | 3/5 | 4/5 | 1/5 | frontend 24/40, ux 24/40, code 12/15, verification 1/5 | 61/100 |
| submission-016 | 3/5 | 3/5 | 4/5 | 1/5 | frontend 24/40, ux 24/40, code 12/15, verification 1/5 | 61/100 |

Every published quality value was recalculated from the integer ratings and checked against the canonical review table. The model-level public leaderboard in `README.md` is a post-review join; it is not used to alter the blind review records.

## Reviewer confidence and disagreement handling

Confidence is reported per canonical review: 15 submissions are High and submission-007 is Medium because several alternate paths and a question screenshot anomaly remained unverified. A second independent pass was not completed, so inter-reviewer disagreement was not measured. The submission-006 corrected review is a replacement of the canonical review, not an additional vote or competing score.

## Build-time and output-token separation

The following are build-turn efficiency facts retained separately from Quality. Original-cohort times are reported as displayed in the legacy run records where the exact completion timestamp was rounded or described approximately; no unavailable precision is invented.

| Opaque ID | Build time | Output tokens |
| --- | --- | ---: |
| submission-001 | 6m 40s | 41.1k |
| submission-002 | 1m 52s | 4,924 |
| submission-003 | 6m 14s | 14.0k |
| submission-004 | 3m 51s | 15,396 |
| submission-005 | 1m 47s | 6,970 |
| submission-006 | 5m 01s | 28.4k |
| submission-007 | 2m 24s | 8,570 |
| submission-008 | 5m 31s (done ~4m 30s) | 16.0k |
| submission-009 | 6m 38s | 18.4k |
| submission-010 | 1m 33s | 6,654 |
| submission-011 | 1m 41s | 7,786 |
| submission-012 | 1m 35s | 7,055 |
| submission-013 | 4m 28s | 11.4k |
| submission-014 | 4m 46s | 6,639 |
| submission-015 | 4m 25s | 11.7k |
| submission-016 | 3m 25s | 10.2k |

## Limitations and known capture/runtime caveats

- The reviewer evaluates the captured artifact and authorized staged evidence; it does not establish every possible runtime path or the factual accuracy of every question.
- The capture crawler selects the first answer option for standardized knowledge-quiz runs. That is an integrity cross-check, not a measure of user performance.
- All final metadata records no page errors; most captures record a non-blocking console 404 for a missing favicon. Console warnings do not imply a page failure.
- Some reviews identify source-level or unexercised behavior as Unverified. Those labels are preserved in the canonical baseline rather than upgraded by publication.
- The public export omits traces, logs, test reports, source copies, environments, and private mapping data by design.
