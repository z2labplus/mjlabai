# 03BE_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_EXTENSION_CURRENT_SCOPE_ACCEPTANCE_DECISION

## Scope

This document records a docs-only current-scope acceptance decision for the
exact P7 minimal synthetic/local parser-reader smoke extension implementation.

This task only decides whether the exact implementation reviewed in `03BD` can
be accepted as current-scope complete. It does not add production code, modify
implementation logic, add tests, add fixtures, add data files, approve full P7
closure, approve broader P7 implementation, approve source approval, approve
source ingestion, approve broad parser / reader / ingestion, approve actual
feature extraction, approve actual label generation, approve supervised
dataset construction, approve split creation, approve leakage-test
implementation, approve training-data construction, approve training-data
approval, approve training-run approval, approve training, approve model
architecture / trainer implementation, approve evaluation implementation,
approve model-output integration, approve real data, approve self-play, approve
league or approve P8-P12.

North-star relationship: accepting this narrow synthetic/local guardrail helper
keeps the supervised-learning path auditable before any later P7 work can
request broader parser, feature, label, dataset or training approval. It is not
model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

## Acceptance Candidate

Candidate:

```text
P7 minimal synthetic/local parser-reader smoke extension implementation.
```

Exact implementation files:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`
- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`

Exact blocker-fix test file:

- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`

The candidate acceptance may include only:

- the exact implementation module approved in `03BA`.
- the exact test file approved in `03BA`.
- the exact test-only blocker fix approved in `03BC`.
- direct docs / governance synchronization.
- validation evidence for the exact scope.

The candidate acceptance may not include full P7 closure, broader P7
implementation, source approval, source ingestion, broad parser / reader /
ingestion, feature extraction, label generation, supervised dataset
construction, training, evaluation, model-output integration, real data,
self-play, league or P8-P12.

## Reviewed Evidence Chain

Reviewed chain:

- `03AY_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_AFTER_FULL_SCOPE_REVIEW`
  drafted the minimal parser-reader smoke extension proposal.
- `03AZ_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_REVIEW_BEFORE_APPROVAL_DECISION`
  reviewed that proposal and recorded `Review can close`.
- `03BA_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_EXTENSION_IMPLEMENTATION_APPROVAL_DECISION`
  approved only the next exact minimal implementation task.
- Commit `854a8037880b4621023ee45e941bb3e84a400d00` implemented the exact
  approved module and tests.
- `03BB_P7_MINIMAL_SYNTHETIC_LOCAL_PARSER_READER_SMOKE_EXTENSION_IMPLEMENTATION_REVIEW`
  reviewed the implementation and found a test-coverage blocker.
- `03BC_P7_PARSER_READER_SMOKE_EXTENSION_REVIEW_BLOCKER_RESOLUTION_APPROVAL_DECISION`
  approved only the exact test-only blocker fix.
- Commit `188336b3983f042b7e9174f1d9e51da970d92a44` added the exact rejection
  tests.
- `03BD_P7_PARSER_READER_SMOKE_EXTENSION_IMPLEMENTATION_REVIEW_AFTER_BLOCKER_FIX`
  reran the implementation review and recorded `Review can close`.
- Current validation commands pass for the exact reviewed scope.

## Acceptance Decision Options

| option | meaning | current selection |
|---|---|---:|
| A. ACCEPTED as current-scope complete | The exact reviewed implementation is accepted as current-scope complete for this narrow synthetic/local scope only. | yes |
| B. REJECTED due to blockers | The exact implementation is not accepted because blockers remain. | no |
| C. ACCEPTED with constraints | The exact implementation is accepted with additional unresolved constraints. | no |

## Required Acceptance Checks

| check | result | notes |
|---|---|---|
| Exact `03BA` scope respected. | pass | Implementation remains limited to the approved module and test file. |
| Exact `03BC` blocker fix respected. | pass | The fix is limited to explicit top-level `bytes`, `bytearray` and `Mapping` rejection tests. |
| `03BB` blocker resolved. | pass | `03BD` confirms the blocker is resolved. |
| `03BD` review can close. | pass | Review decision is `Review can close`. |
| No production code changed after the exact implementation. | pass | The later blocker fix was test-only. |
| No unapproved tests changed after the blocker fix. | pass | The blocker fix modified only the approved test file. |
| No fixtures or data files added. | pass | The extension uses in-memory synthetic/local records only. |
| No real data, Tenhou, haifu, external logs or platform data. | pass | No real-data path is introduced or approved. |
| No source approval or source ingestion. | pass | Source approval and ingestion remain unapproved. |
| No broad parser / reader / ingestion, arbitrary path input or CLI. | pass | The helper rejects path-like inputs and has no CLI. |
| No feature extraction, label generation, tensors, targets or examples. | pass | Output remains a JSON-safe guardrail manifest. |
| No dataset, split, leakage-test implementation or training data. | pass | Dataset construction remains unapproved. |
| No model, trainer, checkpoint, weights, evaluation or model output. | pass | No model-output integration or evaluation is approved. |
| No model-strength, Tenhou, stable-dan, LuckyJ or promotion evidence. | pass | Evidence grade remains synthetic/local smoke acceptance only. |
| No self-play, league or P8-P12. | pass | Later stages remain closed. |
| Validation passes. | pass | Required commands are recorded below. |
| Governance is synchronized. | pass | Handoff, index, next, evidence, risk, changelog, decisions, stage contract, milestones, backlog and technical plan are updated. |

## Acceptance Decision

```text
A. ACCEPTED as current-scope complete
```

Decision statement:

```text
The exact P7 minimal synthetic/local parser-reader smoke extension
implementation is accepted as current-scope complete. This acceptance is
limited to the exact 03BA-approved synthetic/local smoke extension scope,
including the exact implementation module, exact tests, the exact
03BC-approved test-only blocker fix, validation evidence and direct
docs/governance synchronization. This is not full P7 closure and does not
approve broader P7 implementation, source approval, source ingestion, broad
parser / reader / ingestion, actual feature extraction, actual label
generation, supervised dataset construction, split creation, leakage-test
implementation, training-data approval, training-run approval, training, model
architecture / trainer implementation, evaluation implementation,
model-output integration, model-strength evidence, Tenhou ranked evidence,
stable-dan ranked-game evidence, LuckyJ 10.68 comparison, candidate promotion,
real data, self-play, league or P8-P12 entry.
```

## Accepted Current Scope

Accepted current scope:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke_extension.py`
- `tests/supervised/test_synthetic_parser_reader_smoke_extension.py`
- explicit top-level `bytes` rejection test.
- explicit top-level `bytearray` rejection test.
- explicit top-level `Mapping`-as-records-collection rejection test.
- validation commands for the exact synthetic/local scope.
- direct docs / governance synchronization.

Accepted behavior is limited to:

- already-loaded in-memory project-authored synthetic/local smoke records.
- per-record delegation to the existing synthetic parser-reader smoke
  validation path.
- path-like input rejection.
- real-data, model-output, source-approval, hidden-information and
  future-information guardrail rejection through the delegated path.
- JSON-safe manifest output.
- non-evidence guardrail summary.

## Not Accepted Scope

This acceptance does not accept or approve:

- full P7 closure.
- broader P7 implementation.
- source approval.
- source ingestion.
- broad parser / reader / ingestion.
- arbitrary file ingestion.
- CLI.
- actual feature extraction.
- actual label generation.
- feature tensors.
- labels.
- targets.
- supervised examples.
- supervised dataset construction.
- split creation.
- leakage-test implementation.
- training-data construction.
- training-data approval.
- training-run approval.
- training.
- model architecture.
- trainer.
- checkpoint.
- weights.
- evaluation implementation.
- metric implementation.
- evaluation runner.
- benchmark harness.
- model-output integration.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account, session, cookie or token handling.
- third-party binary integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- self-play.
- league.
- P8-P12.

## Validation Results

Validation commands for this acceptance decision:

```text
git diff --check
```

Result: pass.

```text
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
```

Result: pass, 15 tests.

```text
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
```

Result: pass, 11 tests.

```text
python3 -m unittest tests/supervised/test_feature_label_schema.py
```

Result: pass, 11 tests.

```text
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
```

Result: pass, 1 test.

```text
python3 -m unittest tests/data/test_replay_schema.py
```

Result: pass, 7 tests.

```text
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Result: pass, 1 test.

No real-data, Tenhou, haifu, external-log, platform-data, training, tuning,
self-play, league, model-output integration, evaluation implementation,
model-strength evidence, LuckyJ comparison, Akochan `system.exe`, `libai.so`,
third-party binary or unknown model-artifact command was run.

## Governance Synchronization

Governance records now state:

- the exact parser-reader smoke extension is accepted as current-scope
  complete.
- the acceptance is limited to the exact `03BA` and `03BC` scope.
- the `03BB` blocker is resolved and `03BD` can close.
- full P7 remains open.
- broader P7 implementation remains unapproved.
- source approval and source ingestion remain unapproved.
- broad parser / reader / ingestion remains unapproved.
- actual feature extraction and actual label generation remain unapproved.
- supervised dataset construction, split creation and leakage-test
  implementation remain unapproved.
- training, model architecture / trainer and evaluation remain unapproved.
- model-output integration remains unapproved.
- model-strength evidence was not produced.
- real data, self-play, league and P8-P12 remain unapproved.

## Next Task Recommendation

Because this exact scope is accepted, the next task should be:

```text
Define next P7 full-scope planning step after parser-reader smoke extension current-scope acceptance.
```

The next task must be docs-only planning. It must not add implementation,
approve full P7 closure, approve broader P7 implementation, approve source
approval, approve source ingestion, approve broad parser / reader / ingestion,
approve actual feature extraction, approve actual label generation, approve
supervised dataset construction, approve split creation, approve
leakage-test implementation, approve training, approve model architecture /
trainer, approve evaluation, approve model-output integration, create
model-strength evidence, approve real data, approve self-play, approve league
or approve P8-P12.

## Evidence Grade

```text
P7 minimal synthetic/local parser-reader smoke extension current-scope acceptance decision evidence only.
```

## Explicit Non-Evidence

This acceptance decision is not:

- full P7 closure.
- broader P7 implementation.
- source approval.
- source ingestion.
- broad parser / reader / ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- split creation.
- leakage-test implementation.
- training-data approval.
- training-run approval.
- training.
- model architecture.
- trainer.
- checkpoint.
- weights.
- evaluation implementation.
- metric implementation.
- evaluation runner.
- benchmark harness.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- real data.
- self-play.
- league.
- P8-P12 entry approval.
