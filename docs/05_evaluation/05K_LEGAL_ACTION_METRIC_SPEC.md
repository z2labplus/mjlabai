# 05K_LEGAL_ACTION_METRIC_SPEC

## Purpose

This document defines the P5 legal-action and invalid-action metric specification.

The goal is to make future offline evaluators use the same counting rules for:

- `legal_action_rate`.
- `invalid_action_rate`.
- parse failures.
- missing actions.
- skipped records.

This specification supports future fixed-position evaluation, wrapper audit reports and baseline adapter validation.

It is P5 evaluation groundwork only. It is not:

- evaluator implementation.
- a legal-action checker implementation.
- an adapter extension.
- a league harness.
- a match runner.
- a CLI.
- a training objective.
- self-play.
- real Tenhou integration.
- Tenhou ranked evidence.
- model-strength proof.

High legal-action rate is necessary for later evaluation, but it is not sufficient to prove strong mahjong play or LuckyJ-level strength.

## Core Definitions

### Decision Record

A decision record is one offline evaluation decision point.

A future record should contain at least:

- `decision_id`.
- `actor`.
- observation or state reference.
- `legal_actions`.
- `proposed_action`.
- source model or tool id.
- ruleset, room and context metadata.

This document defines the fields and counting rules only. It does not implement a reader, parser, canonicalizer or evaluator.

### Legal Actions

`legal_actions` is the legal action set available at a decision point.

It may come from a rule engine, adapter, fixture or hand-authored sample.

Requirements:

- It must be a canonicalized action list before comparison.
- It must not be empty for the record to enter the metric denominator.
- If `legal_actions` is missing or empty, the record is skipped and counted in `skipped_count`.

### Proposed Action

`proposed_action` is the candidate action emitted by the model, wrapper or tool being evaluated.

Evaluation order:

1. Read the proposed action.
2. Parse it into the action schema.
3. Canonicalize it.
4. Compare it with canonical `legal_actions`.

### Legal Action

A proposed action is legal when:

- `proposed_action` parses successfully.
- The canonicalized proposed action exactly matches at least one canonical action in `legal_actions`.
- Required fields match, including actor, action type and action-specific metadata.

### Invalid Action

A proposed action is invalid when:

- `proposed_action` parses successfully.
- The canonicalized proposed action is not present in canonical `legal_actions`.

Invalid action is not the same as parse failure.

Invalid action is not the same as missing output.

### Parse Failure

A parse failure occurs when `proposed_action` cannot be parsed into the action schema.

Parse failures must be counted separately.

Default policy:

- Do not include parse failures in `invalid_action_count`.
- Report `parse_failure_count` and `parse_failure_rate`.

A future strict-mode evaluator may choose to treat parse failures as invalid, but that must be an explicit mode and must be recorded in the result envelope.

### Missing Action

A missing action occurs when a record is evaluable but no `proposed_action` is emitted.

Missing actions must be counted separately.

Default policy:

- Do not include missing actions in `invalid_action_count`.
- Report `missing_action_count` and `missing_action_rate`.

### Skipped Record

A skipped record is excluded before action legality evaluation.

Recommended skipped categories:

- `skipped_no_legal_actions`: `legal_actions` is missing or empty.
- `skipped_not_decision`: the event is not a decision point.
- `skipped_actor_mismatch`: the record actor does not match the evaluated actor.
- `skipped_not_evaluable`: the fixture or dataset explicitly marks the record as not evaluable.

Skipped records do not enter `evaluated_decision_count`.

Skipped records must still be counted and reported.

## Metric Formulas

Definitions:

```text
evaluated_decision_count = records with non-empty legal_actions that are not skipped

legal_action_count = proposed_action parse success AND canonical proposed_action in canonical legal_actions

invalid_action_count = proposed_action parse success AND canonical proposed_action not in canonical legal_actions

parse_failure_count = proposed_action parse failure

missing_action_count = no proposed_action emitted

skipped_count = records excluded before evaluation
```

Invariant:

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

If `evaluated_decision_count == 0`, all rates are undefined.

Do not return `0`, `1` or any fabricated rate when the denominator is zero.

Reports must include:

- `evaluated_decision_count`.
- `legal_action_count`.
- `invalid_action_count`.
- `parse_failure_count`.
- `missing_action_count`.
- `skipped_count`.

`legal_action_rate + invalid_action_rate` is not guaranteed to equal `1.0`, because parse failures and missing actions are separate categories.

## Recommended Outcome Categories

Future evaluators should use this outcome vocabulary:

```text
legal
invalid
parse_failure
missing_action
skipped_no_legal_actions
skipped_not_decision
skipped_actor_mismatch
skipped_not_evaluable
```

This task defines the vocabulary only. It does not implement code.

## Synthetic Fixture Schema Smoke Test

The first schema-level smoke fixture is:

```text
tests/fixtures/eval/legal_action_metric_smoke.json
```

The corresponding test is:

```text
tests/eval/test_legal_action_fixture_schema_smoke.py
```

The fixture is synthetic-only and contains future outcome labels for:

- `legal`.
- `invalid`.
- `missing_action`.
- `parse_failure`.
- `skipped_no_legal_actions`.

These labels are not evaluator output.

The smoke test validates JSON shape, strict `dahai` canonical action shape and source-note guardrails only. It does not:

- calculate `legal_action_rate`.
- calculate `invalid_action_rate`.
- implement canonical equality.
- implement an evaluator.
- read Tenhou data, external logs or platform data.

## Synthetic Evaluator Implementation

The first narrow synthetic evaluator is implemented in:

```text
src/mjlabai/eval/legal_action_metric.py
```

The corresponding tests are:

```text
tests/eval/test_legal_action_metric.py
```

Implemented API:

- `LegalActionMetricResult`.
- `evaluate_synthetic_legal_action_fixture(fixture)`.
- `build_synthetic_legal_action_metric_envelope(...)`.

Scope:

- input is an in-memory project-authored synthetic fixture mapping.
- default fixture is `tests/fixtures/eval/legal_action_metric_smoke.json`.
- current action support is only `dahai`.
- current matching mode is only `strict`.
- strict comparison uses only `actor`, `action_type`, `tile` and `tsumogiri`.
- `raw_action`, `metadata` and `action_id` are ignored for equality.
- `expected_future_outcome` is not used to compute results.

The current fixture includes an explicit synthetic `parse_failure` record. That record keeps `action_type = "dahai"` and uses `tsumogiri: null` only to exercise the current strict evaluator parse-failure branch. It does not add support for unknown/null `tsumogiri`, relaxed matching or broader action types.

The current fixture produces:

```text
total_record_count = 5
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

The current synthetic evaluator coverage review is recorded in:

```text
docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md
```

That review concludes the minimum outcome coverage is complete only for the
current P5 synthetic-only `dahai` + strict scope. It is not model-strength
evidence, Tenhou ranked evidence or LuckyJ comparison evidence.

The evaluator is still not:

- a broad evaluator.
- a canonicalizer.
- a rule engine.
- a legal-action checker.
- a CLI.
- a file ingestion path.
- a league or runner.
- a model output evaluator.
- Tenhou integration.
- model-strength evidence.
- LuckyJ 10.68 comparison evidence.

## P5 Synthetic Evaluator Boundary Before Implementation

This section defines the minimum future boundary for a synthetic legal-action metric evaluator before any implementation is written.

It is a boundary definition only. It does not implement:

- evaluator code.
- canonicalizer code.
- legal-action checker code.
- a CLI.
- file ingestion.
- league, match, self-play or training code.
- real Tenhou integration.
- external-log, real-haifu, platform-data or account reading.

### Allowed Scope

A future synthetic evaluator may use only:

- project-authored synthetic/local fixtures.
- the default fixture `tests/fixtures/eval/legal_action_metric_smoke.json`.
- P5 offline evaluation context.
- current minimum action type `dahai`.
- current default matching mode `strict`.
- explicit fixture records with `proposed_action`, `legal_actions`, `actor`, `room`, `ruleset` and source notes.

It must not use:

- real Tenhou data.
- real haifu.
- platform data.
- online accounts.
- external logs.
- Akochan real executable or any third-party binary.
- model output, model inference, model training or model weights.
- self-play, league, match runner or any Tenhou connector.
- unknown `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.

### Out-of-Scope Actions

The first synthetic evaluator boundary covers only `dahai`.

The following action types and representation issues are explicitly out of scope until later tasks define them:

- reach.
- chi.
- pon.
- kan.
- hora.
- ryukyoku.
- red-five / aka-dora normalization.
- tile notation conversion.
- relaxed discard matching.
- tile parser implementation.
- canonicalizer implementation.

### Minimum Counting Boundary

The future synthetic evaluator may count only:

- `legal_action_count`.
- `invalid_action_count`.
- `missing_action_count`.
- `parse_failure_count`.
- `skipped_count`.
- `evaluated_decision_count`.
- `legal_action_rate`.
- `invalid_action_rate`.
- `missing_action_rate`.
- `parse_failure_rate`.

Denominator:

```text
evaluated_decision_count = non-empty legal_actions records that are not skipped
```

Boundary rules:

- `skipped_no_legal_actions` does not enter `evaluated_decision_count`.
- `missing_action` enters `evaluated_decision_count` when `legal_actions` is non-empty and the record is otherwise evaluable.
- `parse_failure` enters `evaluated_decision_count` when `legal_actions` is non-empty and the record is otherwise evaluable.
- The evaluator must preserve this invariant:

```text
evaluated_decision_count
= legal_action_count
+ invalid_action_count
+ parse_failure_count
+ missing_action_count
```

- `legal_action_rate + invalid_action_rate` is not required to equal `1.0`, because parse failures and missing actions are independent categories.
- If `evaluated_decision_count == 0`, all rates are undefined. Do not fabricate `0`, `1` or any other numeric rate.

### Current Fixture Boundary

The current fixture contains these labels:

```text
legal
invalid
missing_action
parse_failure
skipped_no_legal_actions
```

`expected_future_outcome` is only a fixture label for future smoke expectations.

It is not:

- evaluator output.
- a model prediction.
- model-strength evidence.
- LuckyJ comparison evidence.

If a future evaluator uses the current fixture, it should skip the empty-`legal_actions` record and calculate only over synthetic/local records. That future computation is not implemented in this task.

Expected future smoke expectations for the current fixture, without implementing them here:

- one `legal` label.
- one `invalid` label.
- one `missing_action` label.
- one `parse_failure` label.
- one `skipped_no_legal_actions` label.
- `evaluated_decision_count` should exclude the skipped empty-`legal_actions` record.

### Canonical Comparison Boundary

Current matching boundary:

```text
action_type = dahai
matching_mode = strict
```

Strict `dahai` comparison may compare only:

- `actor`.
- `action_type`.
- `tile`.
- `tsumogiri`.

Rules:

- `raw_action` is audit/debug data and does not participate in default equality.
- `metadata` does not participate in default equality.
- Do not normalize tile notation.
- Do not guess unknown or null `tsumogiri`.
- Do not use `relaxed_discard_tile` unless a future task explicitly approves it and records that mode in the offline result envelope.
- Do not implement a canonicalizer in this boundary task.

### Offline Result Envelope Boundary

A future synthetic evaluator result should map into `OfflineEvaluationResultEnvelope` with:

- `evaluation_stage = "P5"`.
- `evaluation_type = "legal_action_metric"`.
- `dataset_or_fixture_id` recording the fixture id or fixture path.
- `model_or_tool_id` using an explicit synthetic/test id for synthetic-only smoke runs, not a real model id.
- `sample_size = evaluated_decision_count`.
- metric values for counts and rates when implemented.
- reproducibility metadata containing the code commit, fixture id, test path, environment or command.
- evidence references to the fixture, test, docs and commit.

Required safety flags for this synthetic-only boundary:

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

Required warnings:

- synthetic only.
- not Tenhou data.
- not real haifu.
- not model strength evidence.
- not LuckyJ 10.68 comparison.

### Claim Boundary

Legal-action metrics are legality diagnostics only.

They are not:

- model-strength evidence.
- Tenhou ranked evidence.
- LuckyJ 10.68 comparison.
- sufficient to promote a candidate in the racing funnel.
- permission to start training, self-play, league, runner, real Tenhou or P6-P12 work.

## Canonical Action Matching

Canonical matching compares structured action fields, not raw text.

The action canonicalization schema is defined in:

```text
docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md
```

Recommended canonical action fields:

- `actor`.
- `action_type`.
- `tile`.
- `tsumogiri`.
- target player or consumed tiles for chi/pon/kan when applicable.
- reach flag when applicable.
- raw action preserved separately for audit.

### Dahai

For discard actions:

- `actor` must match.
- `action_type` must be `dahai`.
- `tile` must match.
- `tsumogiri` behavior depends on evaluator mode.

Default mode:

```text
strict
```

Strict mode requires `tsumogiri` to match.

Future relaxed mode may allow tile-only discard matching if the rules and evaluator documentation explicitly permit it.

### Reach

Riichi declaration and the subsequent discard can be represented differently across engines.

Future action schemas must specify whether reach is:

- a separate `reach` action.
- a flag on the discard action.
- a two-step decision.

This document records reach as a future edge case and does not implement it.

### Chi, Pon and Kan

For calls and kans, do not compare only `action_type`.

Future canonical comparison must include:

- actor.
- called tile.
- consumed tiles.
- call type.
- target/source player when relevant.

This task defines the principle only.

### Hora and Ryukyoku

If future evaluators include win or draw declarations, they must explicitly decide whether those events are decision actions for this metric.

This task does not implement that policy.

## Result Envelope Mapping

The offline result envelope should record legal-action metrics using:

```text
evaluation_type = "legal_action_metric"
```

Recommended metric names:

- `legal_action_rate`.
- `invalid_action_rate`.
- `evaluated_decision_count`.
- `legal_action_count`.
- `invalid_action_count`.
- `parse_failure_count`.
- `missing_action_count`.
- `skipped_count`.
- `parse_failure_rate`.
- `missing_action_rate`.

Current registry status:

- `legal_action_rate` and `invalid_action_rate` now have registry definitions used by the synthetic fixture evaluator.
- The synthetic evaluator task added registry definitions for:
  - `evaluated_decision_count`.
  - `legal_action_count`.
  - `invalid_action_count`.
  - `missing_action_count`.
  - `parse_failure_count`.
  - `skipped_count`.
  - `missing_action_rate`.
  - `parse_failure_rate`.
- Count metrics are descriptive and have `higher_is_better = null`.
- `missing_action_rate` and `parse_failure_rate` have `higher_is_better = false`.
- These metrics are implemented only for the project-authored synthetic fixture boundary. They are not broad evaluator metrics yet.

Recommended envelope fields:

- `evaluation_stage = "P5"`.
- `evaluation_type = "legal_action_metric"`.
- `model_or_tool_id`: model, wrapper or tool being evaluated.
- `dataset_or_fixture_id`: fixture or scenario set.
- `sample_size`: `evaluated_decision_count`.
- `metrics`: legal-action metric values.
- `command_status`: present if output came from a wrapper or external tool.
- `reproducibility`: code commit, fixture id, external repo/commit if used, seed if any and environment.
- `safety`: explicit safety flags.
- `warnings`: denominator, parse and skipped-record warnings.
- `evidence_refs`: fixture, test, doc, commit or workflow references.

Safety flags should normally be:

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

Any true flag must be explicitly audited in a future task.

## Tiny Benchmark Harness Boundary Reference

Legal-action metrics may feed a future P5 tiny benchmark harness only as
diagnostics. The boundary for that future harness is documented in:

```text
docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md
```

That boundary does not change the legal-action metric rules in this document.
It does not authorize a runner, CLI, file ingestion, real Tenhou, real haifu,
external logs, platform data, model-output integration, third-party binaries,
league execution, training or self-play. Legal-action rates remain legality
diagnostics only and are not strength evidence or LuckyJ `10.68` comparison
evidence.

The current tiny benchmark harness schema smoke fixture may reference
legal-action diagnostic metric names and the project-authored legal-action
fixture path, but it does not calculate `legal_action_rate` or
`invalid_action_rate`. That fixture lives at:

```text
tests/fixtures/eval/tiny_benchmark_harness_smoke.json
tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py
```

It is shape-only coverage for future P5 harness inputs, not an evaluator, not
model-strength evidence and not LuckyJ `10.68` comparison.

The fixture schema coverage review is recorded in:

```text
docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md
```

That review does not change the legal-action denominator, outcome categories,
synthetic evaluator rules or current `dahai` + strict scope.

## Guardrails

- `legal_action_rate` only measures basic legality.
- `invalid_action_rate` only measures illegal structured outputs.
- Low invalid-action rate is not a LuckyJ comparison.
- High legal-action rate is not model-strength proof.
- Akochan `legal_action` checker output is not model-strength proof.
- This specification cannot be used to claim Tenhou ranked performance.
- Do not connect to real Tenhou.
- Do not read platform data or real external logs unless a future replay or dataset task explicitly approves it.
- Do not implement an evaluator in this task.
- Do not implement a CLI in this task.
- Do not implement a league or match runner in this task.
- Do not train or self-play in this task.

## Future Implementation Boundary

Future P5 tasks may implement:

- synthetic fixture based legal-action metric smoke tests.
- a synthetic parse-failure fixture case and smoke coverage for the existing narrow evaluator.
- fixed decision records with hand-authored `legal_actions`.
- parser and canonicalizer unit tests.
- offline envelope smoke tests for legal-action metrics.

Future tasks still must not directly implement:

- real Tenhou connector.
- live platform automation.
- league runner.
- model training.
- broad replay ingestion.
- scraping or account automation.

## Verification

Current implementation verification:

Run:

```bash
git diff --check
python3 -m unittest tests/eval/test_legal_action_metric.py
```

The implemented synthetic evaluator remains limited to project-authored synthetic fixtures and does not read real Tenhou, real haifu, external logs, platform data or model outputs.
