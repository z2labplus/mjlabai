# 05F_ALGORITHM_RANKING_PROTOCOL

Goal: determine which algorithm route is best for the project target, not which one is most famous.

## Final answer criterion

The best algorithm is the one that produces the highest statistically reliable Tenhou-target score under the same evaluation harness.

Minimum target:

```text
Tenhou stable dan estimate > 10.68
with enough sample size and confidence interval to rule out luck.
```

## Evaluation ladder

### Level 0 — Evidence review

Collect public evidence:

- Tenhou dan or stable dan.
- Room type: expert room, phoenix room, private lobby, other.
- Game count and time period.
- Rank distribution: 1st/2nd/3rd/4th.
- Win rate and deal-in rate.
- Whether code/weights/logs are available.

This level can rank research value, but it cannot prove what is best for our implementation.

### Level 1 — Local build and replay compatibility

A candidate must pass:

- Builds on local machine or documented container.
- Can read/write a known replay format or be adapted to one.
- Produces legal actions only.
- Logs every decision with state, candidate actions, selected action, value estimate if available.

### Level 2 — Offline decision evaluation

Evaluate on fixed high-value positions:

- Discard decision.
- Riichi decision.
- Chi/Pon/Kan decision.
- Push/fold decision.
- Dangerous tile defense.
- South-round rank-awareness.
- Oorasu fourth-place avoidance.

Primary score is not imitation accuracy alone. Record expected value, rank impact, risk, and disagreement with strong baselines.

### Level 3 — Controlled self-play / tournament

Use a fixed league:

- Baseline A: current main model.
- Baseline B: Mortal or other first reproducible open-source baseline.
- Baseline C: rule-based sanity bot.
- Candidate: new route/checkpoint.

Run enough games with seat rotation and seed control. Report:

- Average placement.
- 1st/2nd/3rd/4th rates.
- Tenhou pt EV.
- Stable dan estimate.
- Deal-in rate.
- Win rate.
- Riichi EV.
- Open-hand EV.
- Fourth-place rescue rate in South/Oorasu.

### Level 4 — Stable-dan estimate with uncertainty

Use the Tenhou formula for the target room.

For four-player ippan/general-style stable dan:

```text
stable_dan = ((first_count * 20 + second_count * 10) / fourth_count - 20) / 10
```

For four-player joukyu/upper-style stable dan:

```text
stable_dan = ((first_count * 40 + second_count * 10) / fourth_count - 20) / 10
```

For four-player phoenix-style stable dan:

```text
stable_dan = ((first_count * 60 + second_count * 30) / fourth_count - 20) / 10
```

For four-player tokujou/expert-style stable dan:

```text
stable_dan = ((first_count * 50 + second_count * 20) / fourth_count - 20) / 10
```

Always report bootstrap confidence intervals. A model does not beat LuckyJ unless the lower confidence bound is above the required threshold or the project explicitly marks the result as provisional.

Stable-dan CI reporting must include:

- point estimate.
- lower bound.
- upper bound.
- confidence level.
- number of bootstrap resamples.
- successful resamples.
- undefined resamples.
- undefined rate.

Undefined bootstrap resamples occur when the resampled fourth-place count is zero. They must be skipped and reported, not converted into infinite stable dan. If undefined rate is high, treat the interval as unreliable until more games are available.

Stable-dan threshold comparison against LuckyJ 10.68 must use the bootstrap lower bound:

- `clear_pass` only when lower bound is greater than `10.68` and undefined rate is acceptable.
- `point_estimate_only` when point estimate is greater than `10.68` but lower bound is not; do not claim a clear pass.
- `clear_fail` when even upper bound does not exceed `10.68`.
- `unreliable` when undefined resample rate is too high.
- `inconclusive` when confidence interval overlaps the threshold.

Stable-dan reports must also pass sample-size reporting guardrails before project-level threshold review:

- report minimum: `total_games >= 100`.
- report minimum: `fourth_count >= 10`.
- threshold-review minimum: `total_games >= 1000`.
- threshold-review minimum: `fourth_count >= 50`.
- maximum undefined bootstrap resample rate: `0.05`.

These defaults are project-internal governance guardrails, not Tenhou official standards or proof of strength. Low-sample reports may be useful diagnostics, but they cannot support a LuckyJ 10.68 project-level claim.

Stable-dan inputs may be aggregated from offline placement results only through explicit placement values:

- accepted numeric placements: `1`, `2`, `3`, `4`.
- accepted string placements: `"1"`, `"2"`, `"3"`, `"4"`.
- accepted alias placements: `"first"`, `"second"`, `"third"`, `"fourth"`, `"1st"`, `"2nd"`, `"3rd"`, `"4th"`.

Do not accept zero-based placements, fuzzy labels, bools, floats or unknown strings. Invalid placement records must fail loudly instead of being skipped or repaired, because silent correction can bias the stable-dan estimate.

Current implementation status:

- `src/mjlabai/eval/stable_dan.py` implements deterministic point estimates for general/ippan, upper/joukyu, expert/tokujou and phoenix/houou.
- `bootstrap_stable_dan_ci(...)` implements percentile empirical multinomial bootstrap confidence intervals using Python standard library only.
- `compare_stable_dan_to_threshold(...)` compares bootstrap CI results against LuckyJ stable dan `10.68` using lower-bound logic.
- `build_stable_dan_evaluation_report(...)` produces an offline report schema with point estimate, CI, threshold outcome and sample-size assessment.
- `aggregate_placement_counts(...)` and `aggregate_placement_records(...)` convert offline placement inputs into validated first/second/third/fourth counts.
- `calculate_stable_dan_from_placements(...)` composes placement aggregation with the deterministic stable-dan calculator only.
- `tests/fixtures/eval/stable_dan_placements_smoke.json` is a project-authored synthetic 100-record placement fixture (`30/30/20/20`) used only for code-path smoke testing.
- `tests/eval/test_stable_dan_report_smoke.py` verifies the CLI-free path from synthetic placements to placement aggregation, deterministic point estimate, bootstrap CI, threshold comparison, report schema and JSON serialization.
- `docs/05_evaluation/05H_STABLE_DAN_EVALUATION_API.md` documents the API-only usage path from synthetic placement records to a serialized report.
- `docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md` records that the stable-dan evaluation subtrack is complete for the current P5 scope.
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md` defines the offline metric registry and result envelope schema for future P5 outputs.
- `tests/eval/test_offline_envelope_smoke.py` verifies that a synthetic stable-dan report can be represented in the offline result envelope.
- `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md` defines legal-action and invalid-action metric denominators, parse-failure and missing-action handling, skipped-record rules, canonical action matching principles and result-envelope mapping.
- `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md` defines canonical action fields, minimum `dahai` fixture scope, strict matching, future relaxed matching boundary, legal-action fixture shape and action outcome mapping.
- `tests/fixtures/eval/legal_action_metric_smoke.json` and `tests/eval/test_legal_action_fixture_schema_smoke.py` validate a project-authored synthetic legal-action fixture shape with labels for `legal`, `invalid`, `missing_action`, `parse_failure` and `skipped_no_legal_actions`.
- `src/mjlabai/eval/legal_action_metric.py` implements a narrow synthetic-only legal-action metric evaluator for the project-authored fixture. It supports only strict `dahai` comparison over actor/action_type/tile/tsumogiri and builds an `OfflineEvaluationResultEnvelope` with all-false safety flags.
- `tests/eval/test_legal_action_metric.py` verifies the current fixture counts/rates, denominator invariant, skipped/missing behavior, parse-failure counting through inline synthetic records, that `expected_future_outcome` is not used for computation and that the envelope warnings remain synthetic-only.
- `fourth_count == 0` is undefined and raises `StableDanUndefinedError`; do not report infinite stable dan.
- Bootstrap resamples with `fourth_count == 0` are recorded as undefined; if all resamples are undefined, `StableDanBootstrapUndefinedError` is raised.
- The synthetic smoke fixture is not model-strength evidence, Tenhou data, an external log, a league result or a LuckyJ comparison claim.
- `src/mjlabai/eval/offline_result.py` defines `EvaluationMetricDefinition`, `OfflineEvaluationMetricValue`, `OfflineConfidenceInterval`, `OfflineCommandStatus`, `OfflineReproducibilityMetadata`, `OfflineEvaluationSafetyFlags` and `OfflineEvaluationResultEnvelope`.
- P5 overall is still in progress. The next required evaluation-foundation task is to add a synthetic legal-action metric fixture schema smoke test before implementing broader evaluator logic.

### Legal-action / invalid-action metrics

Legal-action metrics are P5 legality checks, not strength metrics.

The specification lives in:

```text
docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md
```

Core denominator:

```text
evaluated_decision_count = records with non-empty legal_actions that are not skipped
```

Core count invariant:

```text
evaluated_decision_count
= legal_action_count
+ invalid_action_count
+ parse_failure_count
+ missing_action_count
```

Rates:

```text
legal_action_rate = legal_action_count / evaluated_decision_count
invalid_action_rate = invalid_action_count / evaluated_decision_count
parse_failure_rate = parse_failure_count / evaluated_decision_count
missing_action_rate = missing_action_count / evaluated_decision_count
```

If `evaluated_decision_count == 0`, all rates are undefined. Do not report fabricated `0` or `1` values.

Skipped records do not enter the denominator, but must be reported through `skipped_count` and a skipped category such as `skipped_no_legal_actions`, `skipped_not_decision`, `skipped_actor_mismatch` or `skipped_not_evaluable`.

`legal_action_rate + invalid_action_rate` is not required to equal `1.0`, because parse failures and missing actions are separate outcomes.

High `legal_action_rate` and low `invalid_action_rate` show only basic output legality. They are not LuckyJ comparison evidence and not proof of strong mahjong decisions.

The current minimum canonical fixture scope is `dahai` only. Default matching mode is `strict`: actor, action type, tile and known `tsumogiri` fields must match, while `raw_action` and metadata are preserved for audit but ignored for equality.

The current synthetic legal-action fixture smoke test validates schema shape only. It does not calculate `legal_action_rate`, calculate `invalid_action_rate`, implement canonical equality or implement an evaluator.

The first implemented legal-action evaluator is synthetic-only and fixture-only. It computes the current project fixture as:

```text
legal_action_count = 1
invalid_action_count = 1
missing_action_count = 1
parse_failure_count = 1
skipped_count = 1
evaluated_decision_count = 4
legal_action_rate = 1 / 4
invalid_action_rate = 1 / 4
missing_action_rate = 1 / 4
parse_failure_rate = 1 / 4
```

The parse-failure fixture case uses `dahai` with `tsumogiri: null` only to exercise the strict evaluator's parse-failure branch; it does not expand action scope or support unknown/null `tsumogiri` for matching. It must not be used as model-strength or LuckyJ comparison evidence. It does not implement a broad evaluator, canonicalizer, legal-action checker, CLI, league, runner, model-output path, Tenhou integration or external-data ingestion.

The coverage review for this synthetic evaluator is:

```text
docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md
```

This is a Level 1 / diagnostic-style P5 artifact. It can check that the
project-authored synthetic fixture covers the current legality branches, but it
must not be used for model ranking, LuckyJ comparison or candidate promotion.

The tiny benchmark harness boundary is documented in:

```text
docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md
```

That boundary is also Level 1 / diagnostic-style P5 work only. Future
legal-action rate, latency and fixed-position diagnostics may help organize
engineering evidence, but they must not be used for model ranking, candidate
promotion, Tenhou evidence or LuckyJ comparison.

The tiny benchmark harness synthetic fixture schema smoke coverage is:

```text
tests/fixtures/eval/tiny_benchmark_harness_smoke.json
tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
```

It is also Level 1 / diagnostic-style P5 evidence only. It validates
synthetic/local fixture shape, safety flags, warning text and future diagnostic
metric names; it does not implement a benchmark harness, measure latency,
calculate fixed-position exact-match, rank models, promote candidates or support
LuckyJ comparison.

The fixture schema coverage review is:

```text
docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md
```

That review confirms the fixture schema is a front-door input boundary for a
future P5-only synthetic harness implementation, but it remains Level 1 /
diagnostic-style P5 evidence only. It must not be used for model ranking,
candidate promotion, Tenhou evidence or LuckyJ comparison.

The implemented tiny benchmark harness is:

```text
src/mjlabai/eval/tiny_benchmark_harness.py
tests/eval/test_tiny_benchmark_harness.py
docs/05_evaluation/05P_TINY_BENCHMARK_HARNESS_IMPLEMENTATION.md
```

It remains Level 1 / diagnostic-style P5 evidence only. Its
`wrapper_smoke_success` envelope metric only says the fixed synthetic fixture
was validated and summarized; it must not be used for model ranking, candidate
promotion, Tenhou evidence, stable-dan evidence or LuckyJ comparison.

The implementation review is recorded in
`docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md`; it
does not change the evidence grade or authorize candidate promotion.

### Level 5 — Promotion gate

A candidate can enter the mainline only if:

- It improves the primary metric over current main model.
- It does not hide a fourth-place-rate regression.
- It passes legality and reproducibility checks.
- It has a rollback path.
- It is recorded in experiment log, evidence log, risk register, and changelog.

## Best-algorithm decision template

```text
Candidate:
Version / commit / checkpoint:
Evaluation date:
Evaluation environment:
Rules:
Game count:
Seat rotation:
Baselines:

Results:
- Average placement:
- 1st / 2nd / 3rd / 4th:
- Tenhou pt EV:
- Stable dan estimate:
- Bootstrap CI:
- Win rate:
- Deal-in rate:
- Latency:

Decision:
- Promote / Continue / Pivot / Stop
Why:
Next task:
Docs updated:
```

## Current answer to “which is best?”

We do not decide from names. Current working assumption:

- LuckyJ is the performance target.
- Suphx is the strongest public methodology blueprint.
- Mortal is the likely first reproducible baseline.
- Archer may be strong but needs verification.
- Akochan and Kanachan are useful comparative references.

The best route becomes the one that wins our same-harness evaluation and pushes stable-dan estimate toward `> 10.68`.
