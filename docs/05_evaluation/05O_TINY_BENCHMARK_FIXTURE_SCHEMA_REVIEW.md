# 05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW

## Purpose

This document reviews the P5 tiny benchmark harness synthetic fixture schema
smoke coverage.

It is a docs-only review gate. It does not:

- implement a benchmark harness.
- add production code.
- add tests or fixtures.
- add latency measurement code.
- calculate legal-action metrics.
- calculate fixed-position exact-match.
- modify evaluator logic.
- connect model output.
- read real Tenhou, real haifu, external logs or platform data.
- enter P6-P12.

This review supports the north-star target only indirectly. It confirms that a
future P5-only tiny benchmark harness has a controlled synthetic/local input
boundary before any implementation is allowed. It is not model-strength
evidence and is not a LuckyJ `10.68` comparison.

## Evidence Sources

Primary boundary document:

```text
docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md
```

Primary fixture:

```text
tests/fixtures/eval/tiny_benchmark_harness_smoke.json
```

Schema smoke test:

```text
tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
```

Related P5 evaluation documents:

```text
docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md
docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md
docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md
docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md
docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md
```

## Current Fixture Shape

The current fixture has the following top-level fields:

- `schema_version = "tiny_benchmark_harness_fixture_v0.1"`.
- `fixture_id = "tiny_benchmark_harness_smoke_v0.1"`.
- `evaluation_stage = "P5"`.
- `fixture_type = "tiny_benchmark_harness_schema_smoke"`.
- `source_note`.
- `warnings`.
- `intended_safety_flags`.
- `diagnostic_metric_names`.
- `legal_action_diagnostics`.
- `latency_diagnostics`.
- `fixed_position_decision_diagnostics`.
- `related_docs`.
- `evidence_refs`.

The fixture is project-authored synthetic/local only. It is explicitly not:

- Tenhou data.
- real haifu.
- external log data.
- platform data.
- model output.
- model-strength evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- full action-space coverage.

## Current Diagnostic Sections

### Legal-Action Diagnostics

The `legal_action_diagnostics` section:

- references `tests/fixtures/eval/legal_action_metric_smoke.json`.
- is project-authored synthetic/local only.
- keeps the action scope at `dahai` only.
- keeps the matching mode at strict only.
- records diagnostic metric names only.
- does not calculate `legal_action_rate`, `invalid_action_rate`,
  `missing_action_rate` or `parse_failure_rate` in this smoke test.

### Latency Diagnostics

The `latency_diagnostics` section is a synthetic latency plan only.

It records:

- future timing-method field shape.
- future repetition count field shape.
- future sample-count field shape.
- future reproducibility field requirements.
- future latency metric names.

It does not include:

- measured latency.
- `time` / `perf_counter` use.
- benchmark results.
- real Tenhou latency.
- GPU benchmark throughput.
- training throughput.
- self-play throughput.
- league throughput.

### Fixed-Position Decision Diagnostics

The `fixed_position_decision_diagnostics` section:

- is project-authored synthetic fixed-position record shape only.
- uses `matching_mode = "strict"`.
- uses `action_scope = "dahai"`.
- includes at least one synthetic record.
- uses `canonical_action_v0.1` `dahai` shape for `candidate_actions`.
- uses `canonical_action_v0.1` `dahai` shape for `expected_action`.

The `expected_action` field is a future diagnostic expectation only. It is not:

- a supervised label.
- policy-quality evidence.
- strength evidence.
- Tenhou evidence.
- LuckyJ comparison evidence.

## Schema Smoke Test Coverage

The schema smoke test validates:

- required top-level keys.
- `evaluation_stage = "P5"`.
- `fixture_type = "tiny_benchmark_harness_schema_smoke"`.
- `source_note` and `warnings` guardrails.
- all intended safety flags are present and false.
- required diagnostic metric names are present.
- legal-action diagnostic section shape.
- latency diagnostic plan shape.
- absence of measured latency / benchmark result fields.
- fixed-position diagnostic record shape.
- canonical `dahai` action shape.

The schema smoke test does not:

- import or call evaluator code.
- measure latency.
- calculate benchmark metrics.
- calculate fixed-position exact-match.
- run a harness.
- call model code.
- read real Tenhou, real haifu, external logs or platform data.

## Review Conclusion

```text
Current tiny benchmark harness synthetic fixture schema smoke coverage can be
considered complete for the current P5 schema-only boundary.
```

The fixture schema is sufficient as the front-door input boundary for a future
P5-only tiny benchmark harness implementation task.

This conclusion does not mean:

- the harness is implemented.
- latency is measured.
- fixed-position exact-match is computed.
- legal-action metrics are computed by the tiny benchmark fixture smoke test.
- model outputs are supported.
- real data is supported.
- P5 is complete.
- P6-P12 work is authorized.

P5 overall remains open.

## Evidence Grade

Current evidence grade:

```text
P5 synthetic/local fixture schema smoke evidence only.
```

It is not:

- model-strength evidence.
- Tenhou ranked evidence.
- LuckyJ `10.68` comparison.
- stable-dan evidence.
- policy-quality evidence.
- candidate-promotion evidence.
- benchmark harness implementation evidence.
- production evaluator evidence.
- P6-P12 evidence.

## Remaining Gaps

The project still lacks:

- tiny benchmark harness implementation.
- latency measurement.
- fixed-position exact-match calculation.
- model-output adapter.
- real Tenhou log parser.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- CLI.
- broad file ingestion.
- league / runner / match harness.
- self-play.
- training.
- third-party binary integration.
- action-space expansion beyond `dahai` + strict.
- stable-dan evidence from actual ranked games.

## Next P5-Only Task Recommendation

The next narrow P5-only task should be:

```text
Implement P5 tiny benchmark harness for project-authored synthetic fixture only.
```

This is only the next task name. It is not executed in this review.

The next task must remain P5-only and may use only:

- `tests/fixtures/eval/tiny_benchmark_harness_smoke.json`.
- repo-local synthetic/local inputs.
- existing P5 offline result envelope infrastructure.

The next task must not:

- connect model output.
- read real Tenhou.
- read real haifu.
- read external logs.
- read platform data.
- add CLI.
- add broad file ingestion.
- call Akochan `system.exe`.
- call `libai.so`.
- call third-party binaries.
- use model weights.
- train, tune or self-play.
- run league, runner or match harnesses.
- enter P6-P12.

Any future harness output remains at most:

```text
P5 synthetic/local engineering diagnostic evidence.
```

It is still not model-strength evidence, Tenhou evidence, stable-dan evidence or
LuckyJ `10.68` comparison.

## Verification

Recommended validation:

```bash
git diff --check
python3 -m unittest tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_legal_action_metric.py
python3 -m unittest tests/eval/test_offline_result.py
python3 -m unittest tests/eval/test_offline_envelope_smoke.py
```
