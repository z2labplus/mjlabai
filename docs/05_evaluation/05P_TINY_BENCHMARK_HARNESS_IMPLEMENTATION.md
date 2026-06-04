# 05P_TINY_BENCHMARK_HARNESS_IMPLEMENTATION

## Purpose

This document records the P5 tiny benchmark harness implementation for the
project-authored synthetic fixture only.

The implementation supports the north-star target only indirectly: it improves
the evaluation plumbing that future candidate evidence must pass through before
training, league work or Tenhou validation can be considered. It is not
model-strength evidence and is not a LuckyJ `10.68` comparison.

## Implemented Scope

Implemented files:

```text
src/mjlabai/eval/tiny_benchmark_harness.py
tests/eval/test_tiny_benchmark_harness.py
```

The harness uses only this fixed project-authored synthetic/local fixture:

```text
tests/fixtures/eval/tiny_benchmark_harness_smoke.json
```

It does not accept arbitrary paths, scan directories, expose a CLI, ingest files
broadly or read external data.

## API

Public API:

```python
load_project_tiny_benchmark_harness_fixture()
evaluate_tiny_benchmark_harness_fixture(fixture)
run_project_tiny_benchmark_harness()
build_tiny_benchmark_harness_envelope(result, ...)
TinyBenchmarkHarnessResult
```

`load_project_tiny_benchmark_harness_fixture()` loads only the fixed repo-local
fixture path.

`evaluate_tiny_benchmark_harness_fixture(...)` validates and summarizes an
in-memory fixture mapping. It does not calculate legal-action metrics, measure
latency or compute fixed-position exact-match.

`run_project_tiny_benchmark_harness()` runs the fixed project fixture path and
has no path parameter.

`build_tiny_benchmark_harness_envelope(...)` wraps the deterministic smoke result
in `OfflineEvaluationResultEnvelope`.

## Result Boundary

The current result records:

- fixture id.
- fixture schema version.
- P5 evaluation stage.
- fixture type.
- smoke success boolean.
- diagnostic metric names present in the fixture.
- legal-action diagnostic metric names.
- latency diagnostic metric names.
- fixed-position diagnostic metric names.
- fixed-position synthetic record count.
- synthetic/local warnings.
- evidence references.

The current project fixture result is deterministic and records:

```text
fixture_id = tiny_benchmark_harness_smoke_v0.1
evaluation_stage = P5
fixture_type = tiny_benchmark_harness_schema_smoke
smoke_success = true
fixed_position_record_count = 1
```

## Envelope Boundary

The envelope helper records:

- `evaluation_stage = "P5"`.
- `evaluation_type = "tiny_benchmark_harness"`.
- `model_or_tool_id = "synthetic-tiny-benchmark-harness"`.
- `dataset_or_fixture_id = "tests/fixtures/eval/tiny_benchmark_harness_smoke.json"`.
- `sample_size = fixed_position_record_count`.
- one metric: `wrapper_smoke_success`.
- all safety flags false.
- no latency measurement (`latency_ms = None`).
- synthetic/local warnings.
- evidence references to the fixture, schema smoke test, implementation test and
  boundary/review docs.

The envelope is a P5 synthetic/local engineering diagnostic record only.

## Not Implemented

This task does not implement:

- benchmark latency measurement.
- legal-action metric calculation inside the tiny benchmark harness.
- fixed-position exact-match calculation.
- model-output integration.
- broad evaluator behavior.
- canonicalizer behavior.
- legal-action checker or rule engine.
- CLI.
- broad file ingestion.
- runner, match harness or league harness.
- training, tuning or self-play.
- real Tenhou connection.
- real haifu, external-log or platform-data ingestion.
- third-party binary, `system.exe`, `libai.so`, model-weight or artifact use.

## Evidence Grade

Current evidence grade:

```text
P5 synthetic/local engineering diagnostic evidence.
```

It is not:

- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan evidence.
- LuckyJ `10.68` comparison.
- policy-quality evidence.
- candidate-promotion evidence.
- P6-P12 evidence.

## Implementation Review

The implementation review is recorded in:

```text
docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md
```

That review closes the current implementation for the project-authored
synthetic/local fixture scope and keeps the evidence grade limited to P5
synthetic/local implementation review evidence.

## Validation

Expected validation commands:

```bash
git diff --check
python3 -m unittest tests/eval/test_tiny_benchmark_harness.py
python3 -m unittest tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_legal_action_fixture_schema_smoke.py
python3 -m unittest tests/eval/test_legal_action_metric.py
python3 -m unittest tests/eval/test_offline_result.py
python3 -m unittest tests/eval/test_offline_envelope_smoke.py
```
