# 03Q Minimal P7 Synthetic/Local Supervised Feature-Label Smoke Current-Scope Acceptance Decision

## Scope

This document records a docs-only current-scope acceptance decision for the
exact minimal P7 synthetic/local supervised fixture and feature-label smoke
implementation.

This decision only decides whether the exact implementation can be accepted as
current-scope complete. It does not add implementation, modify implementation
logic, add tests, add fixtures, add data files, approve broader P7
implementation, approve training, approve source ingestion, approve parser /
dataset reader / ingestion, approve actual feature extraction, approve actual
label generation, approve model architecture / trainer work, approve real
data, approve model-output integration or approve P8-P12.

North-star relationship: accepting this current-scope smoke implementation
keeps the supervised-learning path auditable before any real training work. It
is not model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

## Reviewed Acceptance Inputs

Acceptance inputs reviewed:

- `docs/03_supervised_policy/03O_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_APPROVAL_DECISION.md`
  completed the approval decision for the exact minimal implementation task.
- Commit `c63338957e96b22038ac934b152f28d80c4754de` implemented the exact
  approved files:
  - `src/mjlabai/supervised/feature_label_schema.py`
  - `tests/fixtures/supervised/synthetic_supervised_smoke.json`
  - `tests/supervised/test_feature_label_schema.py`
  - `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `docs/03_supervised_policy/03P_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_IMPLEMENTATION_REVIEW.md`
  reviewed the exact implementation and records `Review can close`.
- Required validation passed.
- Governance records are synchronized.
- No blocker was found for this acceptance decision.

## Acceptance Decision Options

| option | meaning | current selection |
|---|---|---:|
| Accepted as current-scope complete. | The exact minimal implementation is accepted as complete for the current synthetic/local smoke scope only. | yes |
| Not accepted because blockers exist. | Acceptance is rejected because blockers were found. | no |
| Deferred pending human/Web ChatGPT decision. | Acceptance is deferred because Codex should not decide yet. | no |

## Acceptance Decision

```text
Accepted as current-scope complete.
```

This acceptance is narrow. It accepts only the exact current-scope
synthetic/local feature-label smoke implementation reviewed in `03P`. It does
not approve any broader P7 supervised-learning implementation.

## Accepted Current Scope

Accepted current scope:

- exact minimal helper / schema smoke in
  `src/mjlabai/supervised/feature_label_schema.py`.
- exact project-authored synthetic/local fixture in
  `tests/fixtures/supervised/synthetic_supervised_smoke.json`.
- exact smoke tests in:
  - `tests/supervised/test_feature_label_schema.py`
  - `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- direct docs / governance synchronization.

Accepted behavior is limited to:

- JSON-safe synthetic/local smoke mapping validation.
- candidate feature family validation.
- candidate label family validation.
- public-information-only placeholder checks.
- hidden/future information rejection.
- unsafe provenance / unsafe claim rejection.
- non-evidence guardrails.

## Not Accepted Scope

This acceptance does not accept or approve:

- broader P7 implementation.
- P7 training.
- P7 training data source.
- source ingestion.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction from logs.
- actual label generation.
- supervised dataset construction.
- model architecture.
- dataloader.
- optimizer.
- loss.
- trainer.
- checkpoint.
- weights.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account, session, cookie or token handling.
- model-output integration.
- CLI.
- broad ingestion.
- self-play.
- league.
- P8-P12.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ comparison.
- candidate promotion.

## Validation Results

Validation commands for this acceptance decision:

```bash
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Results:

- `git diff --check`: passed.
- `python3 -m unittest tests/supervised/test_feature_label_schema.py`: passed, 11 tests.
- `python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py`: passed, 1 test.
- `python3 -m unittest tests/data/test_replay_schema.py`: passed, 7 tests.
- `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`: passed, 1 test.

## Next Task Recommendation

Because this decision is accepted, the next task should be:

```text
Define next P7 current-scope supervised-learning task after minimal synthetic feature-label smoke acceptance.
```

The next-task definition is now recorded in
`docs/03_supervised_policy/03R_P7_NEXT_CURRENT_SCOPE_SUPERVISED_LEARNING_TASK_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
It selects:

```text
Define P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance.
```

That follow-up task must remain docs-only. It may define closure criteria,
deferred / blocked / not accepted items, an exit readiness checklist,
validation commands and P8-P12 non-entry conditions. It must not directly
enter implementation, training, parser, dataset reader, ingestion, feature
extraction, label generation, real data, model-output integration, CLI,
self-play, league or P8-P12.

The closure criteria definition is now recorded in
`docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
It keeps the acceptance boundary unchanged: P7 current scope is not closed by
the criteria definition, and broader P7 implementation, training, source
ingestion, parser / reader / ingestion, actual feature extraction, actual label
generation, real data, model-output integration, self-play, league and P8-P12
remain unapproved.

The closure criteria review is now recorded in
`docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
It records `Review can close` for the criteria only. It does not close P7
current scope or approve broader P7 implementation, training, source
ingestion, parser / reader / ingestion, actual feature extraction, actual label
generation, real data, model-output integration, self-play, league or P8-P12.

## Evidence Grade

```text
P7 minimal synthetic/local supervised feature-label smoke current-scope acceptance decision evidence only.
```

## Explicit Non-Evidence

This acceptance decision is not:

- broader P7 implementation.
- P7 training.
- source approval.
- training-data approval.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction from logs.
- actual label generation.
- supervised dataset construction.
- model architecture.
- trainer.
- model-output integration.
- CLI.
- broad file ingestion.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- self-play.
- league.
- P8-P12 entry approval.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
