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

- `legal_action_rate` and `invalid_action_rate` already exist as placeholder registry names.
- Additional count/rate names above are specification-level recommendations for the next registry update task.
- This document does not implement metric calculation.

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

- synthetic legal-action metric fixture schema smoke tests.
- synthetic fixture based legal-action metric smoke tests.
- fixed decision records with hand-authored `legal_actions`.
- parser and canonicalizer unit tests.
- offline envelope smoke tests for legal-action metrics.
- registry additions for legal-action count/rate metric names.

Future tasks still must not directly implement:

- real Tenhou connector.
- live platform automation.
- league runner.
- model training.
- broad replay ingestion.
- scraping or account automation.

## Verification

This is a documentation-only specification task.

Run:

```bash
git diff --check
```

No Python test is required for this document-only task.
