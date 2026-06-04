# 05J_OFFLINE_EVALUATION_RESULT_SCHEMA

## Purpose

This document defines the P5 offline evaluation metric registry and result envelope schema.

The goal is to give future offline evaluation outputs a shared shape, including:

- stable-dan reports.
- Akochan wrapper audit results.
- future fixed-position decision evaluation results.
- future legal-action / invalid-action / latency summaries.

This is P5 evaluation groundwork only. It is not:

- a league harness.
- a match runner.
- a CLI.
- a training path.
- a self-play path.
- a real Tenhou integration.
- platform automation.
- a source of model-strength proof.

The envelope records results produced elsewhere. It does not generate results.

## Metric Registry

The current registry lives in:

```text
src/mjlabai/eval/offline_result.py
```

Current metric names:

| Metric | Unit | Higher is better | Current status |
|---|---:|---:|---|
| `stable_dan_point_estimate` | `dan` | true | stable-dan calculator exists |
| `stable_dan_ci_lower` | `dan` | true | bootstrap CI exists |
| `stable_dan_ci_upper` | `dan` | true | bootstrap CI exists |
| `stable_dan_threshold_outcome` | `category` | null | threshold helper exists |
| `stable_dan_sample_size_status` | `category` | null | sample-size guardrail exists |
| `legal_action_rate` | `rate` | true | implemented for synthetic legal-action fixture only |
| `invalid_action_rate` | `rate` | false | implemented for synthetic legal-action fixture only |
| `evaluated_decision_count` | `count` | null | implemented for synthetic legal-action fixture only |
| `legal_action_count` | `count` | null | implemented for synthetic legal-action fixture only |
| `invalid_action_count` | `count` | null | implemented for synthetic legal-action fixture only |
| `missing_action_count` | `count` | null | implemented for synthetic legal-action fixture only |
| `parse_failure_count` | `count` | null | implemented for synthetic legal-action fixture only |
| `skipped_count` | `count` | null | implemented for synthetic legal-action fixture only |
| `missing_action_rate` | `rate` | false | implemented for synthetic legal-action fixture only |
| `parse_failure_rate` | `rate` | false | implemented for synthetic legal-action fixture only |
| `command_exit_code` | `exit_code` | false | schema field only |
| `latency_ms` | `ms` | false | schema field only |
| `parse_success_rate` | `rate` | true | placeholder definition only |
| `wrapper_smoke_success` | `boolean` | true | schema field only |

The stable-dan metrics have existing calculators or helpers.

The legal-action count/rate metrics are implemented only for the project-authored synthetic fixture boundary in:

```text
src/mjlabai/eval/legal_action_metric.py
```

That evaluator is not a broad evaluator, canonicalizer, rule engine, CLI, league, runner, model-output evaluator, Tenhou connector or strength proof. It reads no external logs or real platform data.

The parse-success, latency and wrapper-smoke metrics remain registry definitions for later P5 evaluators. They are not complete evaluation systems yet.

The legal-action / invalid-action metric specification is documented in:

```text
docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md
```

That specification defines the denominator, parse-failure handling, missing-action handling, skipped-record handling, canonical matching principles and result-envelope mapping. It does not implement an evaluator.

The action canonicalization schema for legal-action metric fixtures is documented in:

```text
docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md
```

That schema defines canonical action fields, current minimum `dahai` fixture scope, strict matching, future relaxed matching boundaries and fixture shape. It does not implement a canonicalizer.

The current synthetic legal-action fixture schema smoke test lives at:

```text
tests/eval/test_legal_action_fixture_schema_smoke.py
```

It reads only:

```text
tests/fixtures/eval/legal_action_metric_smoke.json
```

That fixture is synthetic-only and shape-only. It does not calculate legal-action metrics, implement an evaluator, read Tenhou data, read external logs or produce strength evidence.

The future synthetic legal-action evaluator boundary is documented in:

```text
docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md
```

That boundary says legal-action synthetic evaluator output should enter `OfflineEvaluationResultEnvelope` with `evaluation_stage = "P5"` and `evaluation_type = "legal_action_metric"`, all safety flags false for synthetic-only smoke runs, explicit fixture/reproducibility metadata and warnings that the result is synthetic-only, not Tenhou data and not model-strength evidence. The current helper `build_synthetic_legal_action_metric_envelope(...)` implements this mapping only for the project-authored synthetic fixture result.

After the parse-failure fixture coverage update, the synthetic legal-action fixture envelope records `sample_size = 4`, because the skipped empty-`legal_actions` record is excluded from `evaluated_decision_count`. Current metric values include one legal action, one invalid action, one missing action, one parse failure and one skipped record, with all four evaluated rates equal to `1/4`.

The current legal-action synthetic evaluator coverage review is recorded in:

```text
docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md
```

That review confirms only the synthetic `dahai` + strict fixture/evaluator
coverage. It is not model-strength evidence, Tenhou ranked evidence, LuckyJ
comparison evidence or authorization for real-data ingestion.

The future P5 tiny benchmark harness boundary is recorded in:

```text
docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md
```

If a future synthetic/local tiny benchmark result is implemented, it should
enter this envelope schema with `evaluation_stage = "P5"` and an explicit
diagnostic `evaluation_type`, such as `tiny_benchmark_harness`. It may record
legal-action, latency and fixed-position diagnostic metrics only after separate
fixture/schema tasks define those inputs. The boundary remains synthetic/local
only: no real Tenhou, real haifu, external logs, platform data, model-output
integration, third-party binaries, CLI, runner or league behavior is authorized.
Such envelope records are diagnostics, not strength evidence.

The current P5 tiny benchmark harness schema-only smoke fixture lives at:

```text
tests/fixtures/eval/tiny_benchmark_harness_smoke.json
tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
```

It validates the future envelope-facing shape for synthetic/local legal-action,
latency and fixed-position diagnostics. It does not create an
`OfflineEvaluationResultEnvelope`, implement a harness, calculate metrics,
measure latency, call model/evaluator code or read real Tenhou, real haifu,
external logs or platform data. It remains P5 synthetic/local fixture schema
smoke evidence only, not model-strength evidence or LuckyJ `10.68` comparison.

The review for that fixture schema coverage is recorded in:

```text
docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md
```

Future tiny benchmark harness outputs remain envelope-compatible P5 diagnostics
only. Even after implementation, they must remain synthetic/local engineering
diagnostic evidence unless a later task explicitly reviews and authorizes a
broader scope. They are not model-strength evidence, stable-dan evidence,
Tenhou evidence or LuckyJ `10.68` comparison.

## Result Envelope

The envelope type is:

```python
OfflineEvaluationResultEnvelope
```

Core fields:

- `schema_version`: default `offline_evaluation_result_v0.1`.
- `evaluation_id`: unique offline evaluation identifier.
- `evaluation_stage`: current stage label, such as `P5`.
- `evaluation_type`: kind of offline evaluation result.
- `model_or_tool_id`: model, wrapper or tool being evaluated.
- `dataset_or_fixture_id`: dataset, fixture or scenario identifier.
- `room`: optional room label.
- `ruleset`: optional ruleset label.
- `metrics`: one or more `OfflineEvaluationMetricValue` records.
- `sample_size`: optional sample size.
- `confidence_interval`: optional `OfflineConfidenceInterval`.
- `command_status`: optional `OfflineCommandStatus`.
- `latency_ms`: optional wall-clock latency.
- `reproducibility`: `OfflineReproducibilityMetadata`.
- `safety`: `OfflineEvaluationSafetyFlags`.
- `warnings`: warning strings.
- `evidence_refs`: doc, test, commit or run references.
- `source_note`: schema note.

## Metric Values

`OfflineEvaluationMetricValue` records:

- `metric_name`
- `value`
- `metric_unit`
- `higher_is_better`
- `sample_size`
- `source_note`

Values may be simple JSON-compatible scalars only:

- integer.
- float.
- string.
- boolean.
- null.

Complex objects are intentionally not supported.

If the metric exists in the registry, the metric value can inherit its unit and higher-is-better direction.

## Confidence Interval

`OfflineConfidenceInterval` records:

- `lower_bound`
- `upper_bound`
- `confidence_level`
- `method`

Validation requires:

- `lower_bound <= upper_bound`.
- `confidence_level` in `(0, 1)`.
- non-empty method.

## Command Status

`OfflineCommandStatus` records:

- `command_name`
- `exit_code`
- `success`
- `stdout_summary`
- `stderr_summary`

This schema does not run commands.

Stdout and stderr fields are bounded summaries only. Do not store huge logs in the envelope.

## Reproducibility Metadata

`OfflineReproducibilityMetadata` records:

- `code_commit`
- `external_repo`
- `external_commit`
- `fixture_id`
- `seed`
- `environment`
- `source_note`

This is metadata for evidence tracking. It is not a downloader, artifact manager or runner.

## Safety Flags

`OfflineEvaluationSafetyFlags` records:

- `training_related`
- `self_play_related`
- `league_related`
- `tenhou_related`
- `platform_automation_related`
- `uses_real_platform_data`
- `uses_external_log`
- `uses_third_party_artifact`

P5 offline groundwork should usually keep all flags false.

If a flag is true, the envelope records a warning. The schema still does not execute anything.

## Guardrails

The envelope must stay narrow:

- Do not train.
- Do not tune.
- Do not self-play.
- Do not run league or match harnesses.
- Do not connect to real Tenhou.
- Do not create platform automation, scraping, accounts, evasion or anti-detection tools.
- Do not read external logs or real platform data in this task.
- Do not save third-party source, binaries, model weights or build artifacts.
- Do not treat an envelope as model-strength proof.

The envelope only records offline evaluation results. It does not authorize those results as sufficient for LuckyJ claims.

## Synthetic Example

This example is synthetic/local only. It does not use Tenhou data and does not claim model strength.

```python
from mjlabai.eval import (
    OfflineConfidenceInterval,
    OfflineEvaluationMetricValue,
    OfflineEvaluationResultEnvelope,
    OfflineEvaluationSafetyFlags,
    OfflineReproducibilityMetadata,
)

envelope = OfflineEvaluationResultEnvelope(
    evaluation_id="synthetic-stable-dan-smoke-001",
    evaluation_stage="P5",
    evaluation_type="stable_dan_report_smoke",
    model_or_tool_id="synthetic-smoke-model",
    dataset_or_fixture_id="tests/fixtures/eval/stable_dan_placements_smoke.json",
    room="phoenix",
    ruleset="tenhou_four_player_phoenix",
    metrics=(
        OfflineEvaluationMetricValue(
            metric_name="stable_dan_point_estimate",
            value=11.5,
            sample_size=100,
        ),
        OfflineEvaluationMetricValue(
            metric_name="stable_dan_threshold_outcome",
            value="point_estimate_only",
            sample_size=100,
        ),
    ),
    sample_size=100,
    confidence_interval=OfflineConfidenceInterval(
        lower_bound=8.0,
        upper_bound=14.0,
        confidence_level=0.95,
        method="empirical_multinomial_percentile_bootstrap",
    ),
    reproducibility=OfflineReproducibilityMetadata(
        code_commit="example-only",
        fixture_id="tests/fixtures/eval/stable_dan_placements_smoke.json",
        seed=12345,
        environment="local-unit-test",
    ),
    safety=OfflineEvaluationSafetyFlags(),
    warnings=("synthetic only; not strength evidence",),
    evidence_refs=("tests/eval/test_offline_result.py",),
)

envelope_dict = envelope.to_dict()
```

## Verification

Run:

```bash
python3 -m unittest tests/eval/test_offline_envelope_smoke.py
python3 -m unittest tests/eval/test_offline_result.py
```

`test_offline_result.py` verifies schema validation and JSON serialization.

`test_offline_envelope_smoke.py` verifies that the project-authored synthetic stable-dan placement fixture can flow through stable-dan report generation, then be wrapped in `OfflineEvaluationResultEnvelope` with:

- stable-dan point estimate metric.
- stable-dan CI lower and upper metrics.
- stable-dan threshold outcome metric.
- stable-dan sample-size status metric.
- confidence interval.
- reproducibility metadata.
- all-false safety flags.
- synthetic / not-strength-evidence warnings.
- JSON serialization.

These tests do not run a league, command runner, Tenhou connector, training job or external-data reader.

## Tiny Benchmark Harness Envelope Note

The P5 tiny benchmark harness implementation can wrap its fixed synthetic
fixture smoke result in `OfflineEvaluationResultEnvelope` with:

- `evaluation_stage = "P5"`.
- `evaluation_type = "tiny_benchmark_harness"`.
- `dataset_or_fixture_id = "tests/fixtures/eval/tiny_benchmark_harness_smoke.json"`.
- metric `wrapper_smoke_success = true`.
- `sample_size = 1`.
- all safety flags false.
- synthetic/local warnings.

This envelope is synthetic/local engineering diagnostic evidence only. It does
not record latency measurement, fixed-position exact-match, model output, real
Tenhou, real haifu, external logs, platform data, model strength, stable-dan
evidence or LuckyJ `10.68` comparison.

`docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md`
reviews that current envelope-producing implementation boundary and keeps the
evidence grade at P5 synthetic/local review evidence only.
