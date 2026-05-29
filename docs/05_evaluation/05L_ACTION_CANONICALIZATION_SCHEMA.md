# 05L_ACTION_CANONICALIZATION_SCHEMA

## Purpose

This document defines the P5 action canonicalization schema for future legal-action metric fixtures.

The goal is to give future `proposed_action` and `legal_actions` records a shared structured shape so they can be compared consistently in offline P5 evaluation.

This schema supports:

- future synthetic legal-action metric fixtures.
- future fixed-position evaluation.
- future wrapper / baseline adapter validation.
- future legal-action and invalid-action metric tests.

This document is P5 evaluation groundwork only. It is not:

- a canonicalizer implementation.
- an evaluator implementation.
- a legal-action checker implementation.
- an adapter extension.
- a CLI.
- a league harness.
- a match runner.
- a training path.
- self-play.
- real Tenhou integration.
- model-strength proof.

## Canonical Action Object

The recommended canonical action object fields are:

```text
schema_version
action_id
actor
action_type
tile
tsumogiri
called_tile
consumed_tiles
target
source
reach_declared
kan_type
raw_action
metadata
```

### `schema_version`

Recommended default:

```text
canonical_action_v0.1
```

This field is required in fixtures so future schema migrations can be audited.

### `action_id`

Optional fixture-local identifier.

`action_id` is for fixture references and debugging. It does not participate in default legality matching.

### `actor`

Required.

The actor is the player who executes the action.

Allowed values:

```text
0
1
2
3
```

### `action_type`

Required.

Recommended values:

```text
dahai
reach
chi
pon
kan
hora
ryukyoku
noop
unknown
```

This document defines the schema only. It does not parse action types.

### `tile`

Used by discard, win and other tile-specific actions.

Recommended tile tokens preserve the original canonical tile string, such as:

```text
1m
5pr
E
C
```

This document does not implement tile parsing or tile normalization.

### `tsumogiri`

Used by `dahai`.

Recommended values:

```text
true
false
null
```

If tsumogiri is unknown, use `null`. Do not guess.

Strict matching uses this field when both compared actions provide it.

### `called_tile`

Used by `chi`, `pon` and `kan`.

This document defines the field only. It does not implement call parsing.

### `consumed_tiles`

Used by `chi`, `pon` and `kan`.

This should be a canonical tile list. Future canonicalizer work must define the ordering or normalization rule.

This document does not implement ordering.

### `target` and `source`

Used for called-tile source, target player or action target when relevant.

This document defines the field names only.

### `reach_declared`

Used to represent whether an action contains a riichi declaration.

Reach may be represented as:

- an independent `reach` action.
- metadata on a `dahai` action.
- a two-step decision.

This is a known edge case and is not implemented in this task.

### `kan_type`

Used by `kan`.

Recommended values:

```text
ankan
minkan
kakan
```

This document defines the field only.

### `raw_action`

Raw action payload preserved for audit and debugging.

`raw_action` must not participate in default canonical equality.

### `metadata`

Optional fixture, source, parser or debugging metadata.

`metadata` must not participate in default canonical equality.

## Minimal Supported Fixture Scope

The current minimum supported action type for future P5 legal-action metric fixtures is:

```text
current_minimum_supported_action_type = dahai
```

The minimum fixture scope is:

- `dahai` proposed action.
- `dahai` legal actions.
- `actor`.
- `tile`.
- `tsumogiri`.
- `raw_action` preserved for audit.

Other action types are schema-defined but not required for the first fixture:

- `reach`.
- `chi`.
- `pon`.
- `kan`.
- `hora`.
- `ryukyoku`.

## Dahai Canonical Schema

Example:

```json
{
  "schema_version": "canonical_action_v0.1",
  "actor": 0,
  "action_type": "dahai",
  "tile": "1s",
  "tsumogiri": true,
  "raw_action": {
    "type": "dahai",
    "actor": 0,
    "pai": "1s",
    "tsumogiri": true
  }
}
```

Strict comparison rules:

```text
actor must match
action_type must match
tile must match
tsumogiri must match when both sides provide it
unknown/null tsumogiri should not be guessed
raw_action ignored for equality
metadata ignored for equality
```

Default matching mode:

```text
strict
```

## Matching Modes

### `strict`

Default mode for P5 legal-action metrics.

Compare:

- `actor`.
- `action_type`.
- `tile` when required.
- `tsumogiri` for `dahai` when both sides provide it.
- action-specific required fields for calls, kans and future action types.

### `relaxed_discard_tile`

Future optional mode.

For `dahai`, this mode may compare only:

- `actor`.
- `action_type`.
- `tile`.

This mode is not implemented in this task.

Relaxed behavior must not be used unless the evaluator mode is explicitly recorded in the offline result envelope.

Project default:

```text
strict
```

## Legal-Action Fixture Shape

Future synthetic legal-action metric fixtures should use this minimum shape:

```json
{
  "fixture_id": "synthetic-legal-action-0001",
  "schema_version": "legal_action_fixture_v0.1",
  "decision_id": "synthetic-decision-0001",
  "actor": 0,
  "ruleset": "tenhou_four_player",
  "room": "phoenix",
  "matching_mode": "strict",
  "proposed_action": {
    "schema_version": "canonical_action_v0.1",
    "actor": 0,
    "action_type": "dahai",
    "tile": "1s",
    "tsumogiri": true,
    "raw_action": {
      "type": "dahai",
      "actor": 0,
      "pai": "1s",
      "tsumogiri": true
    }
  },
  "legal_actions": [
    {
      "schema_version": "canonical_action_v0.1",
      "actor": 0,
      "action_type": "dahai",
      "tile": "1s",
      "tsumogiri": true
    }
  ],
  "source_note": "Synthetic fixture only; not Tenhou data; not model strength evidence."
}
```

Fixture rules:

- Fixture data must be synthetic/local only unless a later task explicitly approves another source.
- Fixture data must not come from Tenhou.
- Fixture data must not be real haifu.
- Fixture data must not read external logs.
- Fixture data must not be model-strength evidence.
- `proposed_action` is one canonical action object or missing/null for missing-action tests.
- `legal_actions` is a list of canonical action objects.
- `matching_mode` defaults to `strict`.

## Current Synthetic Smoke Fixture

The current P5 schema smoke fixture is:

```text
tests/fixtures/eval/legal_action_metric_smoke.json
```

The corresponding shape-only smoke test is:

```text
tests/eval/test_legal_action_fixture_schema_smoke.py
```

The fixture contains project-authored synthetic records labeled for evaluator scenarios:

- `legal`.
- `invalid`.
- `missing_action`.
- `parse_failure`.
- `skipped_no_legal_actions`.

`expected_future_outcome` is only a fixture label. The smoke test does not calculate legal/invalid outcomes, does not compare canonical equality and does not implement an evaluator.

## Current Synthetic Evaluator Use

The first narrow evaluator using this schema is:

```text
src/mjlabai/eval/legal_action_metric.py
```

It uses this document's current minimum boundary only:

- `dahai` actions.
- `strict` matching.
- `actor`, `action_type`, `tile` and `tsumogiri` equality.
- `raw_action`, `metadata` and `action_id` ignored for equality.

The synthetic `parse_failure` fixture case still uses `action_type = "dahai"` and only sets `tsumogiri` to `null` on the proposed action to verify the strict evaluator's parse-failure branch. That does not make unknown/null `tsumogiri` a supported strict comparison input.

It does not implement a production canonicalizer. It does not support reach, chi, pon, kan, hora, ryukyoku, red-five normalization, tile notation conversion or relaxed discard matching.

The current minimum action type remains:

```text
dahai
```

The current matching mode remains:

```text
strict
```

The synthetic evaluator boundary before implementation is defined in:

```text
docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md
```

That boundary keeps the current evaluator scope to synthetic/local fixtures, `dahai` actions and strict matching only. It does not implement a canonicalizer or evaluator.

## Outcome Mapping

The canonical schema maps to `05K_LEGAL_ACTION_METRIC_SPEC.md` outcomes as follows:

| Condition | Outcome |
|---|---|
| `proposed_action` matches one `legal_actions` item | `legal` |
| `proposed_action` parses but does not match | `invalid` |
| `proposed_action` cannot parse | `parse_failure` |
| `proposed_action` missing | `missing_action` |
| `legal_actions` missing or empty | `skipped_no_legal_actions` |
| event is not a decision | `skipped_not_decision` |
| record actor does not match evaluated actor | `skipped_actor_mismatch` |
| fixture is explicitly not evaluable | `skipped_not_evaluable` |

This document defines mapping only. It does not implement an evaluator.

## Edge Cases

### Reach

Reach can be represented as an independent action, a discard flag or a two-step decision.

Future schema work must decide how reach fixtures represent:

- declaration.
- following discard.
- actor.
- timing.

The minimum fixture scope does not require reach.

### Chi and Pon

Call actions must compare more than `action_type`.

Future canonical matching must include:

- `actor`.
- `called_tile`.
- `consumed_tiles`.
- `source` or `target` player where relevant.

### Kan

Kan actions must distinguish:

- `ankan`.
- `minkan`.
- `kakan`.

The `kan_type` field is reserved for this purpose.

### Hora and Ryukyoku

Future evaluator work must decide whether hora or ryukyoku are decision actions for legal-action metrics.

They are not part of the minimum fixture scope.

### Red Fives / Aka Dora

Tile tokens must preserve red-five indicators.

Examples may include:

```text
5pr
5mr
5sr
```

This task does not implement tile normalization.

### Tile Notation Mismatch

Different tools may use different raw fields or tokens:

- `pai`.
- `tile`.
- `5pr`.
- `5p*`.

Future canonicalizer work must define conversions explicitly.

For now, fixtures should use one canonical tile string and preserve the original value under `raw_action`.

## Result Envelope Mapping

Future legal-action fixture evaluation should use:

```text
evaluation_stage = P5
evaluation_type = legal_action_metric
```

Recommended envelope fields:

- `dataset_or_fixture_id`.
- `model_or_tool_id`.
- `ruleset`.
- `room`.
- `sample_size = evaluated_decision_count`.
- `metrics`.
- `reproducibility`.
- `safety`.
- `warnings`.
- `evidence_refs`.

Recommended metrics:

- `legal_action_rate`.
- `invalid_action_rate`.
- `parse_failure_rate`.
- `missing_action_rate`.
- `evaluated_decision_count`.
- `skipped_count`.

Recommended reproducibility metadata:

- fixture id.
- code commit.
- environment.

Required safety expectations for synthetic fixtures:

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

## Guardrails

- This schema is an evaluation input specification only.
- It is not an action parser.
- It is not a canonicalizer implementation.
- It is not a legal-action evaluator.
- It is not a Tenhou connector.
- It is not model-strength evidence.
- `legal_action_rate` is not a LuckyJ `10.68` comparison.
- Do not read real Tenhou data in this task.
- Do not read external logs in this task.
- Do not enter P6-P12 from this task.

## Coverage Review Reference

The current synthetic legal-action evaluator coverage review is recorded in:

```text
docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md
```

That review keeps the current scope at synthetic-only `dahai` + strict
matching. The fixture's `parse_failure` record uses `tsumogiri: null` only as
branch coverage for the strict evaluator; it does not make unknown or null
`tsumogiri` valid for strict matching.

## Future Implementation Boundary

The next likely P5 task is:

```text
Define P5 tiny benchmark harness boundary for legal-action rate, latency and fixed-position decisions before implementation.
```

That future task must remain:

- documentation / boundary definition first.
- no benchmark harness implementation yet.
- no broad evaluator implementation.
- no real Tenhou.
- no league.
- no training.
- no self-play.
- no external logs.
- no CLI.
- no file ingestion.

## Verification

This is a documentation-only schema task.

Run:

```bash
git diff --check
```

No Python test is required for this document-only task.
