# 05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW

## Purpose

This document reviews the current P5 synthetic legal-action evaluator coverage.

It is a documentation-only review gate. It does not add:

- production code.
- evaluator logic.
- canonicalizer logic.
- legal-action checker or rule engine.
- CLI.
- file ingestion.
- benchmark harness implementation.
- league, runner or match harness.
- training, tuning or self-play.
- real Tenhou integration.
- real haifu, external-log or platform-data ingestion.

## Review Scope

The review covers only the current P5 synthetic-only legal-action evaluator path:

```text
tests/fixtures/eval/legal_action_metric_smoke.json
-> tests/eval/test_legal_action_fixture_schema_smoke.py
-> src/mjlabai/eval/legal_action_metric.py
-> tests/eval/test_legal_action_metric.py
-> OfflineEvaluationResultEnvelope
```

This supports the north-star target only indirectly: it builds controlled legality
diagnostic infrastructure so future candidates cannot be compared or promoted
without explicit legality metrics and evidence records.

## Evidence Sources

Primary fixture:

```text
tests/fixtures/eval/legal_action_metric_smoke.json
```

Schema smoke test:

```text
tests/eval/test_legal_action_fixture_schema_smoke.py
```

Evaluator implementation:

```text
src/mjlabai/eval/legal_action_metric.py
```

Evaluator tests:

```text
tests/eval/test_legal_action_metric.py
```

Related schema and metric documents:

```text
docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md
docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md
docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md
```

## Current Implementation Boundary

The current evaluator is intentionally narrow:

- project-authored synthetic fixture only.
- in-memory fixture mapping only.
- no general file ingestion.
- current action type: `dahai` only.
- current matching mode: `strict` only.
- equality fields: `actor`, `action_type`, `tile`, `tsumogiri`.
- `raw_action`, `metadata` and `action_id` are ignored for equality.
- no canonicalizer.
- no broad evaluator.
- no legal-action rule engine.
- no real model-output path.
- no CLI.
- no Tenhou.
- no real haifu.
- no external logs.
- no platform data.
- no third-party binary or artifact path.

The parse-failure fixture record uses `dahai` with `tsumogiri: null` only to
exercise the strict evaluator parse-failure branch. It does not mean null or
unknown `tsumogiri` is accepted for strict matching.

## Minimum Outcome Coverage

The current project-authored fixture covers the minimum outcome categories for
the current synthetic-only `dahai` + strict scope:

```text
legal
invalid
missing_action
parse_failure
skipped_no_legal_actions
```

This is complete only for the current P5 synthetic scope. It is not complete
coverage of real mahjong actions or real model behavior.

## Current Fixture Counts

The current fixture result is:

```text
total_record_count = 5
evaluated_decision_count = 4
legal_action_count = 1
invalid_action_count = 1
missing_action_count = 1
parse_failure_count = 1
skipped_count = 1

legal_action_rate = 1 / 4
invalid_action_rate = 1 / 4
missing_action_rate = 1 / 4
parse_failure_rate = 1 / 4
```

The denominator is:

```text
evaluated_decision_count = non-empty legal_actions records that are not skipped
```

The invariant remains:

```text
evaluated_decision_count
= legal_action_count
+ invalid_action_count
+ missing_action_count
+ parse_failure_count
```

## Envelope Boundary

The synthetic legal-action evaluator maps into `OfflineEvaluationResultEnvelope`
with:

- `evaluation_stage = "P5"`.
- `evaluation_type = "legal_action_metric"`.
- `sample_size = evaluated_decision_count`.
- metrics for legal, invalid, missing, parse-failure and skipped counts/rates.
- reproducibility metadata for fixture and environment.
- all safety flags false.
- evidence references to fixture, tests and docs.

Required warning semantics:

- synthetic only.
- not Tenhou data.
- not real haifu.
- not model strength evidence.
- not LuckyJ 10.68 comparison.

## Evidence Grade

Evidence grade:

```text
P5 synthetic fixture / evaluator smoke evidence only.
```

It verifies:

- schema shape for the project-authored fixture.
- narrow strict `dahai` evaluator flow.
- counts and rates for the synthetic fixture.
- skipped, missing and parse-failure branches.
- `expected_future_outcome` is not used for computation.
- envelope mapping with all-false safety flags.

## Not Evidence Of

This review and the current evaluator are not evidence of:

- model strength.
- Tenhou ranked performance.
- LuckyJ 10.68 comparison.
- policy quality.
- real-game legality.
- complete mahjong action-space coverage.
- candidate promotion in the racing funnel.

## Remaining Gaps

The current synthetic evaluator does not cover:

- reach.
- chi.
- pon.
- kan.
- hora.
- ryukyoku.
- red-five / aka-dora normalization.
- tile notation conversion.
- relaxed discard matching.
- real model-output adapters.
- real Tenhou log parsers.
- league or match harnesses.
- sample-size guardrails for real model evaluation.
- stable-dan evidence from actual ranked games.

## Review Conclusion

```text
Legal-action synthetic evaluator minimum outcome coverage is complete for the
current P5 synthetic-only dahai + strict scope.
```

P5 overall remains open.

Do not promote this result into:

- P6 data system work.
- supervised learning.
- reinforcement learning.
- search/risk modeling.
- league execution.
- large-scale training.
- Tenhou target validation.
- LuckyJ 10.68 claims.

## Next P5-Only Task

The next boundary step is documented in:

```text
docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md
```

That document defines the future tiny benchmark harness boundary for
legal-action rate, latency and fixed-position diagnostics before any harness
implementation. It does not change the coverage conclusion in this review and
does not expand evaluator scope.

The tiny benchmark harness synthetic fixture schema smoke coverage now lives at:

```text
tests/fixtures/eval/tiny_benchmark_harness_smoke.json
tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
```

That fixture/test pair remains synthetic/local schema coverage only. It does
not implement a harness, runner, CLI, file ingestion, league, real Tenhou,
model-output integration or P6-P12 work.

The next narrow P5-only task is to review that schema smoke coverage and define
the next P5-only task.

## Verification

Recommended validation after this review update:

```bash
git diff --check
python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_legal_action_metric.py
python3 -m unittest tests/eval/test_offline_result.py
python3 -m unittest tests/eval/test_offline_envelope_smoke.py
```
