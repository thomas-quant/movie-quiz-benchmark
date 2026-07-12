# Movie Types Quiz — Coding-Agent Benchmark

Completed benchmark publication for one-shot coding agents building multi-page Flask quizzes about movie types or genres.

The canonical public aggregation is [`data/reviews.json`](data/reviews.json). Methodology and review details are in [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md), [`docs/RESULTS.md`](docs/RESULTS.md), and [`REVIEWER.md`](REVIEWER.md). Fresh reviewed screenshots are in [`screenshots/reviewed/`](screenshots/reviewed/).

## Automated review leaderboard

Quality is the rubric-weighted score only: `(frontend / 5 × 40) + (UX / 5 × 40) + (code / 5 × 15) + (verification / 5 × 5)`. Build time and output tokens are separate build-turn efficiency facts and never affect Quality. Flow and Integrity are compact objective-baseline labels; see `data/reviews.json` for the full evidence rows.

| Submission | Quiz type | Quality | Frontend | UX | Code | Verification | Flow | Integrity | Build time | Output tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | ---: |
| [codex/v3-sol](openai/codex/v3-sol/SCORECARD.md) (`submission-003`) | knowledge | **88/100** | 5/5 | 4/5 | 4/5 | 4/5 | Pass | Biased | 6m 14s | 14.0k |
| [claude](anthropic/claude/SCORECARD.md) (`submission-006`) | knowledge | **78/100** | 4/5 | 4/5 | 4/5 | 2/5 | Pass | Biased | 5m 01s | 28.4k |
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

Build-time and output-token values are shown only when retained in the benchmark run records; approximate legacy timings are labeled as such. The automated blind review is the canonical quality assessment. Historical maintainer scorecards are preserved under their Legacy assessment sections for provenance and use a different, non-comparable scale.

## Publication layout

- `data/reviews.json` — canonical public aggregation and post-review leaderboard join.
- `reviews/submission-XXX.md` — one canonical anonymized review per opaque ID.
- `screenshots/reviewed/` — fresh lossless PNG start/question/results captures.
- `docs/RESULTS.md` — methodology, setup, objective baseline, ratings, limitations, and publication notes.
- `export/` in the private review workspace — sanitized external public export containing only permitted artifacts.

No submission source code, captures, reviews, or repository history were rerun or modified as part of publication.
