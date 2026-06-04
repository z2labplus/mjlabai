# 05N_TINY_BENCHMARK_HARNESS_BOUNDARY

## Purpose

This document defines the boundary for a future P5 tiny benchmark harness before
any harness implementation exists.

It is a docs-only boundary definition. It does not add:

- production code.
- benchmark harness implementation.
- evaluator logic.
- canonicalizer logic.
- legal-action checker or rule engine.
- CLI.
- file ingestion.
- league, runner or match harness.
- model-output integration.
- training, tuning or self-play.
- real Tenhou integration.
- real haifu, external-log or platform-data ingestion.

## Scope

The future tiny benchmark harness, if separately approved later, must remain P5
evaluation groundwork. It may serve only controlled, offline, synthetic/local
evaluation smoke infrastructure.

The intended diagnostic areas are:

- legal-action rate diagnostics.
- latency diagnostics.
- fixed-position decision diagnostics.

This boundary supports the north-star target only indirectly. It helps ensure
future candidate evidence is recorded in a uniform and auditable way before any
candidate can be promoted toward training, league play or Tenhou validation. It
is not model-strength evidence and is not a LuckyJ `10.68` comparison.

## Why This Exists

The project already has:

- stable-dan evaluation utilities.
- offline result envelope schema.
- synthetic legal-action metric fixture and evaluator.
- current synthetic-only legal-action coverage review.

Before adding a tiny benchmark harness, the project must first define what such
a harness may and may not consume, measure and report. This prevents an
engineering smoke tool from becoming an unauthorized runner, real-data
ingestion path, model-output evaluator or league harness.

## Allowed Future Inputs

A future P5 tiny benchmark harness may use only:

- project-authored synthetic fixtures.
- repo-local synthetic/local fixtures.
- in-memory fixture mappings.
- fixed synthetic decision records.
- the current legal-action synthetic fixture as an example input:

```text
tests/fixtures/eval/legal_action_metric_smoke.json
```

- deterministic local evaluation functions already inside this repository, only
  as future target categories after a separate task defines their fixture and
  envelope boundaries.

## Forbidden Future Inputs

A future tiny benchmark harness must not consume:

- real Tenhou logs.
- Tenhou account or session data.
- platform automation data.
- scraped data.
- external logs.
- real haifu ingestion.
- Akochan `system.exe` output.
- `libai.so`.
- third-party binary output.
- unknown model checkpoints.
- `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.
- Mortal, Akochan or other model outputs unless a later task explicitly defines
  a safe synthetic adapter boundary.
- training output.
- self-play output.
- league output.

## Metric Boundary

A future tiny benchmark harness may define or record these diagnostics, but this
document does not implement them:

- `legal_action_rate`.
- `invalid_action_rate`.
- `missing_action_rate`.
- `parse_failure_rate`.
- `evaluated_decision_count`.
- `skipped_count`.
- `latency_ms_mean`.
- `latency_ms_p50`.
- `latency_ms_p95`.
- `latency_ms_max`.
- `fixed_position_decision_count`.
- `fixed_position_exact_match_rate` or a similar diagnostic metric, only after a
  future task defines a fixed-position synthetic fixture schema.

Interpretation limits:

- Legal-action metrics are legality diagnostics, not strength metrics.
- Latency metrics are engineering diagnostics, not strength metrics.
- Fixed-position exact-match or decision diagnostics are fixture-level behavior
  diagnostics, not policy-strength evidence.
- These diagnostics must not be used for LuckyJ `10.68` comparison.
- These diagnostics must not promote a candidate in the racing funnel by
  themselves.

## Latency Boundary

Future latency measurement is restricted to local, offline, synthetic/local
evaluation code paths.

It must not measure:

- real Tenhou.
- online platforms.
- third-party binaries.
- Akochan `system.exe`.
- `libai.so`.
- GPU benchmark throughput.
- training throughput.
- self-play throughput.
- league throughput.

Any future latency result must record:

- environment.
- command or in-process test path.
- sample count.
- timing method.
- repetitions.

Latency is an engineering smoke diagnostic only. It is not model-strength
evidence.

## Fixed-Position Decision Boundary

This task defines only the future boundary. It does not add a fixed-position
fixture or harness.

Future fixed-position decision records must be:

- project-authored synthetic records.
- offline and repo-local.
- explicitly marked as synthetic/local.

They must not come from:

- real Tenhou.
- real haifu.
- external logs.
- platform data.

They must not be interpreted as:

- complete Mahjong strategy coverage.
- supervised accuracy evidence.
- policy quality evidence.
- LuckyJ comparison evidence.

If a future task adds fixed-position fixtures, it must first define a schema
smoke test before any evaluator or harness implementation. The current action
scope remains unchanged; this boundary does not add reach, chi, pon, kan, hora
or ryukyoku support.

## Future Output Envelope Boundary

Any future tiny benchmark harness result should enter
`OfflineEvaluationResultEnvelope` or a compatible P5 result envelope.

Minimum expected fields:

- `evaluation_stage = "P5"`.
- `evaluation_type = "tiny_benchmark_harness"` or another explicit P5
  diagnostic type.
- `dataset_or_fixture_id`.
- `model_or_tool_id`; if synthetic-only, this must be an explicit synthetic or
  test id, not a real-model id.
- `sample_size`.
- `metrics`.
- `reproducibility` metadata.
- `safety` flags.
- `warnings`.
- `evidence_refs`.

The envelope records results produced elsewhere. It must not generate results,
run commands, read files broadly or become a runner.

The current synthetic tiny benchmark envelope coverage review is recorded in:

```text
docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md
```

That review confirms the existing envelope is sufficient for the current
synthetic/local diagnostic result. It does not add implementation, schema
fields, latency measurement, fixed-position exact-match or model-output
integration.

## Synthetic Fixture Schema Smoke Coverage

The current P5 schema-only smoke coverage for this boundary lives in:

```text
tests/fixtures/eval/tiny_benchmark_harness_smoke.json
tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
```

The fixture is project-authored synthetic/local only. It is not Tenhou data, not
a real haifu, not an external log, not platform data, not model output, not
model-strength evidence, not LuckyJ `10.68` comparison and not
candidate-promotion evidence.

The schema smoke test validates only:

- top-level fixture shape.
- source-note and warning guardrails.
- all-false intended safety flags.
- future diagnostic metric names.
- legal-action diagnostic reference shape.
- latency diagnostic plan shape.
- fixed-position synthetic decision record shape.

It does not:

- implement the tiny benchmark harness.
- add production code.
- calculate legal-action metrics.
- measure latency.
- use `time` or `perf_counter`.
- calculate fixed-position exact-match.
- call model code.
- call evaluator code.
- add CLI or file ingestion.
- read real Tenhou, real haifu, external logs or platform data.

Evidence grade:

```text
P5 synthetic/local fixture schema smoke evidence only.
```

The review gate for this fixture schema smoke coverage is recorded in:

```text
docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md
```

That review concludes the fixture schema is sufficient as a front-door input
boundary for a future P5-only tiny benchmark harness implementation task. The
review does not implement the harness and does not change this boundary.

## Safety Flags

Future synthetic/local tiny benchmark smoke results must keep these flags false
unless a later task explicitly introduces and re-reviews the higher-risk scope:

```text
training_related = false
self_play_related = false
league_related = false
tenhou_related = false
platform_automation_related = false
uses_real_platform_data = false
uses_external_log = false
uses_third_party_artifact = false
```

## Required Warnings

Future tiny benchmark envelopes must include warnings with these meanings:

- synthetic/local only.
- not Tenhou data.
- not real haifu.
- not external log.
- not model strength evidence.
- not LuckyJ `10.68` comparison.
- not candidate promotion evidence.
- not full action-space coverage.

## Evidence Grade

This boundary is:

```text
P5 docs-only boundary evidence.
```

Future synthetic/local tiny benchmark smoke evidence can be at most:

```text
P5 synthetic/local engineering diagnostic evidence.
```

It is not:

- model-strength evidence.
- Tenhou ranked evidence.
- LuckyJ `10.68` comparison.
- stable-dan evidence.
- policy-quality evidence.
- production evaluator evidence.
- P6-P12 evidence.

## Current Non-Goals and Gaps

This boundary does not solve:

- real model-output adapters.
- real Tenhou log parsing.
- real haifu ingestion.
- league or match harnesses.
- self-play.
- training.
- benchmark harness implementation.
- CLI.
- broad file ingestion.
- third-party binary integration.
- action-space expansion.
- reach, chi, pon, kan, hora or ryukyoku coverage.
- stable-dan evidence from real ranked games.

## Guardrails

- Do not implement the tiny benchmark harness as part of this schema smoke
  coverage.
- Do not modify evaluator logic as part of this schema smoke coverage.
- Do not connect to model code.
- Do not call third-party binaries.
- Do not read real Tenhou, real haifu, external logs or platform data.
- Do not enter P6-P12.

## Next P5-Only Task

After the fixture schema smoke coverage review, the project implemented the
fixed synthetic fixture harness in:

```text
src/mjlabai/eval/tiny_benchmark_harness.py
tests/eval/test_tiny_benchmark_harness.py
docs/05_evaluation/05P_TINY_BENCHMARK_HARNESS_IMPLEMENTATION.md
```

That implementation remains inside this boundary: fixed project-authored
synthetic fixture only, no latency measurement, no fixed-position exact-match,
no model-output integration, no CLI, no broad ingestion, no real data, no
league/runner/training/self-play/Tenhou access and no P6-P12 work.

The next task should be selected through `docs/10_next/10_NEXT.md` and should
review the implementation before any further P5 work.

## Verification

Current schema smoke validation:

Recommended validation:

```bash
git diff --check
python3 -m unittest tests/eval/test_tiny_benchmark_harness.py
python3 -m unittest tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_legal_action_metric.py
python3 -m unittest tests/eval/test_offline_result.py
python3 -m unittest tests/eval/test_offline_envelope_smoke.py
```
