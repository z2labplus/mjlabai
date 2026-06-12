# 03O Minimal P7 Synthetic/Local Supervised Fixture And Feature-Label Smoke Implementation Approval Decision

## Scope

This document records a docs-only approval decision for the minimal P7
synthetic/local supervised fixture and feature-label smoke implementation task.

This document does not implement P7. It does not create a fixture, add tests,
add production code, add data files, generate an implementation prompt, train,
approve real data, approve parser / dataset reader / ingestion, approve
actual feature extraction, approve actual label generation, approve model
architecture / trainer work, or approve P8-P12.

North-star relationship: the decision supports the long-term Tenhou stable dan
`> 10.68` target only by allowing the next narrowly bounded synthetic/local
smoke implementation task to become auditable. This decision is not
model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

## Reviewed Approval Inputs

The following inputs were reviewed for this approval decision:

- `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
  defines P7 scope, entry criteria and first task before implementation.
- `docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`
  records `Review can close` for the P7 scope chain.
- `docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
  defines P7 data/source readiness with no approved training source.
- `docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`
  records `Review can close` for the data/source readiness chain.
- `docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`
  defines feature / label readiness boundaries before implementation.
- `docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`
  records `Review can close` for the feature / label boundary chain.
- `docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`
  defines risk and evidence taxonomy before implementation.
- `docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md`
  records `Review can close` for the risk / evidence taxonomy chain.
- `docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md`
  defines the minimal proposal.
- `docs/03_supervised_policy/03N_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_REVIEW.md`
  records `Review can close` for the proposal review.
- Governance docs are synchronized.
- Existing validation commands pass.
- No blocker was found for making an approval decision.

## Decision Options

| option | meaning | current selection |
|---|---|---:|
| Approved for next minimal implementation task. | A later exact minimal synthetic/local implementation task may become the first unchecked `10_NEXT` item. | yes |
| Not approved because blockers exist. | Implementation is not allowed because blockers were found. | no |
| Deferred pending human/Web ChatGPT decision. | Implementation approval is deferred because Codex should not decide yet. | no |

## Approval Decision

```text
Approved for next minimal implementation task.
```

This approval is narrow. It approves only placing the exact next minimal
synthetic/local smoke implementation task into `docs/10_next/10_NEXT.md`. It
does not execute implementation, create any file, generate an implementation
prompt, approve training data, approve source ingestion, approve parser /
reader / ingestion, approve actual feature extraction, approve actual label
generation, approve model architecture / trainer work, approve real data or
approve P8-P12.

## Exact Allowed Files If Approved

The next implementation task may touch only these exact implementation files:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`

Directly related docs / governance updates are allowed only as necessary to
record the implementation evidence, validation, risks and next task.

No other production code, tests, fixtures or data files are approved. Any
additional file requires separate approval.

## Exact Allowed Implementation Scope If Approved

The next implementation task may only:

- define a minimal schema / validation helper for synthetic/local
  feature-label smoke.
- validate project-authored synthetic/local supervised fixture shape.
- validate candidate feature family names.
- validate candidate label family names.
- validate public-information-only placeholder fields.
- reject hidden-information fields.
- reject future-information fields.
- reject training-use claims.
- reject source-approval claims.
- reject real-data provenance.
- reject model-output, self-play and league provenance.
- ensure JSON-safe fixture content.
- provide minimal unittest smoke coverage for the exact fixture and helper.
- update directly related docs / governance records.

The implementation must remain standard-library-only unless a later explicit
approval says otherwise.

## Exact Forbidden Implementation Scope If Approved

The next implementation task must not add or approve:

- parser.
- dataset reader.
- ingestion.
- feature extraction from logs.
- actual label generation.
- supervised dataset construction.
- training.
- tuning.
- model architecture.
- dataloader.
- optimizer.
- loss.
- trainer.
- checkpoint.
- weights.
- model-output integration.
- CLI.
- broad file ingestion.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account, session, cookie or token handling.
- self-play.
- league.
- runner.
- P8-P12.
- model-strength claims.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.

## Validation Commands For Future Implementation If Approved

The next exact implementation task must run at least:

```bash
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

The current approval-decision task validates only existing tests:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

## Stop Conditions

Stop a future implementation attempt before commit if any of these occur:

- an unapproved file is needed.
- parser, reader or ingestion is needed.
- feature extraction expands beyond schema smoke validation.
- label generation expands beyond schema smoke validation.
- real data appears.
- account, session, cookie or token handling appears.
- model-output path appears.
- training behavior appears.
- model architecture, dataloader, optimizer, loss, trainer, checkpoint,
  weights or snapshot behavior appears.
- third-party artifact usage appears.
- P8-P12 drift appears.
- validation fails.
- evidence wording overclaims the synthetic/local smoke artifact.

## Next Task Recommendation

Because the decision is approved, the next task should be:

```text
Implement minimal P7 synthetic/local supervised fixture and feature-label smoke only.
```

This is a next-task recommendation only. It is not executed by this approval
decision, and this document does not generate an implementation prompt.

## Evidence Grade

```text
P7 minimal synthetic/local supervised fixture and feature-label smoke implementation approval-decision evidence only.
```

## Explicit Non-Evidence

This approval decision is not:

- P7 implementation.
- P7 first-task execution.
- fixture creation.
- tests creation.
- production code.
- data file creation.
- P8-P12 entry approval.
- training.
- tuning.
- self-play.
- league.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- parser.
- dataset reader.
- data ingestion.
- actual feature extraction.
- actual label generation.
- source approval.
- training-data approval.
- model-output integration.
- CLI.
- broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
