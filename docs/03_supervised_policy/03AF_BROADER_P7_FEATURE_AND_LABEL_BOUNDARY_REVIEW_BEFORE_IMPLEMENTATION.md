# 03AF Broader P7 Feature And Label Boundary Review Before Implementation

## Scope

This document reviews
`docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
before any broader P7 actual feature extraction or label generation
implementation.

This is a docs-only review gate. It does not approve actual feature
extraction, actual label generation, feature tensors, labels, targets,
examples, splits, supervised dataset construction, source approval, source
ingestion, parser / reader / ingestion, broad file ingestion, CLI data paths,
training, model architecture / trainer, real-data use, model-output
integration, self-play, league or P8-P12 entry.

## Reviewed Artifacts

Primary reviewed artifact:

- `docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md`

Broader P7 context:

- `docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AD_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03Z_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`

Read-only implementation context:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

Governance and tracking context:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

## Scope Review

Review finding:

```text
The 03AE scope is correct.
```

`03AE` clearly states that it only defines the broader P7 actual feature
extraction and label generation boundary before implementation. It is
docs-only. It is not actual feature extraction implementation, actual label
generation implementation, feature extraction approval, label generation
approval, parser implementation, dataset reader implementation, ingestion
implementation, source ingestion approval, source approval, training-data
approval, supervised dataset construction, model input pipeline construction,
model architecture / dataloader / optimizer / loss / trainer / checkpoint /
weights approval, real-data use, real Tenhou use, real haifu use,
external-log use, platform-data use, model-output integration, self-play,
league, P8-P12 entry or model-strength evidence.

No blocker was found.

## Purpose Review

The purpose is sufficient for this review gate.

`03AE` defines:

- actual feature extraction boundary.
- actual label generation boundary.
- feature / label vocabulary.
- feature / label relationships to source approval.
- feature / label relationships to parser / reader / ingestion approval.
- feature / label relationships to supervised dataset construction.
- feature / label relationships to training.
- current feature / label status.
- candidate feature and label families.
- future approval prerequisites.
- future approval-record fields.
- allowed and forbidden future behavior.
- leakage controls.
- stop conditions.
- risk controls.
- evidence requirements.
- why the current synthetic/local smoke path is not training data or broader
  feature / label approval.

No blocker was found.

## Current Feature Label Status Review

The current feature / label status in `03AE` is accurate.

Current broader P7 status remains:

- no actual feature extraction approved.
- no actual label generation approved.
- no source approved for P7 training.
- no source ingestion approved.
- no parser / reader / ingestion approved.
- no broad file ingestion approved.
- no CLI data path approved.
- no supervised dataset construction approved.
- no feature tensor, label, target, example, split or batch may be emitted.
- no model architecture, dataloader, optimizer, loss, trainer, checkpoint,
  weights or snapshot approved.
- no real Tenhou, real haifu, external logs or platform data use.
- no account / session / cookie / token data use.
- no model-output, self-play or league output use.
- the accepted minimal synthetic/local smoke helper is not training data.
- repository docs are not parseable training data.
- P6 and P7 synthetic fixtures are smoke artifacts, not training sources.

No blocker was found.

## Concept Definitions Review

`03AE` clearly distinguishes:

- feature extraction boundary.
- actual feature extraction.
- feature family.
- feature schema.
- label generation boundary.
- actual label generation.
- label family.
- label schema.
- feature tensor.
- label target.
- supervised example.
- supervised split.
- supervised dataset construction.
- source approval.
- parser / reader / ingestion approval.
- training-data approval.
- public information.
- hidden information.
- future information.
- generated label.
- human label.
- model-output label.

No concept is written as a substitute for another approval. In particular,
source approval, parser / reader / ingestion approval, feature extraction
approval, label generation approval, supervised dataset approval and training
approval remain separate.

No blocker was found.

## Dependency Map Review

The dependency order is safe and conservative:

```text
source readiness
-> source-specific approval or explicit synthetic/local boundary
-> parser / reader / ingestion boundary and review
-> parser / reader / ingestion proposal
-> parser / reader / ingestion approval decision
-> exact parser / reader / ingestion implementation
-> implementation review
-> actual feature / label boundary
-> feature / label proposal
-> feature / label approval decision
-> exact feature / label implementation
-> feature / label implementation review
-> supervised dataset construction boundary
-> split and leakage policy
-> training-data approval
-> training approval
```

If any required predecessor is missing, actual feature extraction and actual
label generation must not be implemented.

No blocker was found.

## Parser Reader Ingestion Relationship Review

`03AE` correctly states that parser / reader / ingestion may only produce
approved source records, normalized records, manifests or validation summaries
within approved scope. Parser / reader / ingestion must stop before feature
extraction and label generation unless a separate feature / label approval
exists.

The approval separation is correct:

- source approval is not source ingestion approval.
- source ingestion approval is not parser / reader / ingestion approval.
- parser / reader / ingestion approval is not feature extraction approval.
- feature extraction approval is not label generation approval.
- label generation approval is not supervised dataset approval.
- supervised dataset approval is not training approval.

No blocker was found.

## Current Synthetic Local Smoke Boundary Review

`03AE` correctly classifies the accepted minimal synthetic/local supervised
feature-label smoke path as a schema / guardrail smoke artifact only.

It validates:

- JSON-safe synthetic/local mappings.
- candidate feature / label family names.
- public-information-only placeholders.
- non-evidence guardrails.

It is not:

- training data.
- actual broader P7 feature extraction.
- actual broader P7 label generation.
- parser / reader / ingestion approval.
- source approval.
- supervised dataset construction.
- model input pipeline construction.
- model-strength evidence.

No blocker was found.

## Candidate Feature Families Review

The candidate feature families are safely classified. None are approved for
extraction now.

`03AE` covers:

- project-authored synthetic/local smoke features.
- approved-source decision-time table context.
- visible hand features.
- public discard / call / riichi event features.
- visible dora / score / round context.
- legal-action mask features.
- provenance / source metadata features.
- model-output-derived features.
- self-play / league-derived features.
- real Tenhou / real haifu features.

Each row records planning allowance, implementation allowance, source
dependency, leakage risk, requirements before implementation and current
status. Unsafe categories remain blocked or later-stage only.

No blocker was found.

## Candidate Label Families Review

The candidate label families are safely classified. None are approved for
generation now.

`03AE` covers:

- project-authored synthetic smoke labels.
- action imitation labels.
- discard-choice labels.
- call / no-call labels.
- riichi / no-riichi labels.
- legal-action diagnostic labels.
- future value / reward targets.
- final rank / placement targets.
- human-authored annotation labels.
- generated pseudo-labels.
- model-output labels.
- self-play / league labels.

Each row records planning allowance, implementation allowance, source
dependency, leakage risk, requirements before implementation and current
status. Unsafe categories remain blocked, deferred or later-stage only.

No blocker was found.

## Feature Boundary Rules Review

`03AE` sufficiently defines future feature extraction rules.

Required future controls include:

- source id and approval reference.
- parser / reader / ingestion approval reference or synthetic/local
  not-required rationale.
- feature schema version.
- decision timestamp and observation timestamp.
- public-information-only policy.
- hidden-information exclusion.
- future-information exclusion.
- derived feature provenance.
- feature family allowlist.
- exact implementation files.
- validation commands.
- evidence and risk references.

Forbidden decision-time features include:

- opponent concealed hands.
- unrevealed wall order.
- future draws.
- future discards.
- future calls.
- future riichi declarations.
- final score.
- final placement.
- future rank delta.
- model output unless separately approved.
- source ids or provenance shortcuts unless explicitly reviewed.
- account / session / cookie / token or platform-private content.

No blocker was found.

## Label Boundary Rules Review

`03AE` sufficiently defines future label generation rules.

It states that labels remain separate from features and may not leak into
decision-time feature inputs. A future action source or outcome source may
become a label target only after explicit approval.

Required future controls include:

- label source id and approval reference.
- parser / reader / ingestion approval reference or synthetic/local rationale.
- label schema version.
- label family allowlist.
- label generation method.
- target timestamp and observation timestamp separation.
- provenance and generator / annotator metadata, if any.
- split and leakage policy.
- validation commands.
- evidence and risk references.

Forbidden labels include:

- labels from unapproved real Tenhou or real haifu.
- labels from external logs or platform data.
- labels from model outputs.
- labels from self-play or league outputs.
- labels generated by unknown third-party binaries, weights or checkpoints.
- labels requiring hidden information without an oracle-diagnostic policy.
- labels implying training-data approval.

No blocker was found.

## Future Approval Record Fields Review

The future approval-record fields are sufficient.

`03AE` requires:

- `component_id`.
- `component_type`.
- `source_id`.
- source approval reference or synthetic/local boundary reference.
- parser / reader / ingestion approval reference.
- approved input record categories.
- forbidden input categories.
- feature family allowlist.
- label family allowlist.
- public-information policy.
- hidden-information exclusion policy.
- future-information exclusion policy.
- observation timestamp policy.
- target timestamp policy.
- raw input storage policy.
- derived feature storage policy.
- derived label storage policy.
- `may_enter_git`.
- privacy / platform terms status.
- account / session / cookie / token prohibition.
- exact implementation files.
- dependency versions.
- validation commands.
- leakage validation plan.
- split policy status.
- supervised dataset construction status.
- evidence log reference.
- risk register reference.
- decision record reference.
- rollback plan.
- stop conditions.
- human / Web ChatGPT approval reference.
- explicit first unchecked `10_NEXT` implementation task.

No blocker was found.

## Allowed Future Implementation Boundary Review

The allowed future implementation boundary is conservative.

Future implementation may be considered only after a separate proposal,
approval decision and first unchecked `10_NEXT` task. The implementation must
be exactly one of:

- project-authored synthetic/local-only feature / label smoke.
- approved-source-only feature extraction.
- approved-source-only label generation.
- docs-only validator.

It must be exact-file scoped, use only approved synthetic/local fixtures or
approved sources, require approved parser / reader / ingestion unless
explicitly not needed for synthetic/local-only scope, emit only approved
feature / label fields, preserve provenance and schema versions, stop before
supervised dataset construction and training unless separately approved, avoid
broad file ingestion and CLI data paths, avoid account/session/cookie/token
handling, and avoid model-output, self-play or league sources unless a later
stage review approves them.

No blocker was found.

## Forbidden Feature Label Scope Review

The forbidden scope is sufficiently strict.

`03AE` forbids:

- actual feature extraction implementation.
- actual label generation implementation.
- feature tensors, labels, targets, examples, splits or batches.
- supervised dataset construction.
- model input pipeline construction.
- source approval.
- source ingestion.
- parser / reader / ingestion implementation.
- broad file ingestion.
- CLI data paths.
- real Tenhou, real haifu, external logs or platform data.
- account / session / cookie / token access.
- hidden opponent hands as features.
- future information as decision-time features.
- final results as decision-time features.
- labels from unapproved sources.
- model-output labels or features.
- self-play / league output labels or features.
- third-party binaries, params, checkpoints, weights or snapshots as feature /
  label sources.
- training, tuning, model architecture, dataloader, optimizer, loss, trainer,
  checkpoint or weights.
- P8-P12 entry.

No blocker was found.

## Stop Conditions Review

The stop conditions are sufficient.

Future feature / label work must stop if:

- an unapproved source appears.
- an unapproved parser / reader / ingestion dependency appears.
- real data appears without approval.
- feature extraction begins in a parser / reader / ingestion task.
- label generation begins in a parser / reader / ingestion task.
- labels are used as decision-time features.
- hidden information appears in feature inputs.
- future information appears in decision-time feature inputs.
- supervised examples, splits or batches are created without dataset
  construction approval.
- training behavior appears.
- model calls appear.
- CLI or broad ingestion is needed.
- account / session / cookie / token data appears.
- third-party binaries, weights, params, checkpoints or snapshots are needed.
- validation fails.
- evidence is overclaimed.
- P8-P12 drift appears.

No blocker was found.

## Risk Controls Review

Risk controls are complete enough for this boundary.

Covered risks include:

- boundary mistaken for approval.
- feature families mistaken as implemented features.
- label families mistaken as generated labels.
- source approval mistaken as feature extraction approval.
- parser / reader / ingestion mistaken as feature extraction.
- label generation mistaken as supervised dataset construction.
- labels leaking into features.
- hidden information leakage.
- future information leakage.
- split leakage.
- current smoke fixture mistaken as training data.
- docs context mistaken as training data.
- model-output labels too early.
- self-play / league labels too early.
- third-party artifact creep.
- training creep.
- P8-P12 creep.
- model-strength overclaim.

No blocker was found.

## Evidence Requirements Review

The evidence requirements are sufficient.

Future feature / label evidence must record component id, component type,
source id, source approval status, parser / reader / ingestion approval
status, exact files, feature schema version, label schema version, feature
family allowlist, label family allowlist, public-information policy,
hidden-information exclusion, future-information exclusion, input policy,
output policy, provenance policy, storage policy, validation commands, leakage
validation results, evidence log reference, risk register reference, decision
record reference and explicit non-evidence warning.

For later implementation reviews, the next dataset / split / leakage boundary
should add explicit fields for feature extraction status, label generation
status, timestamp-policy validation, split-policy status, supervised dataset
construction status and known exclusions. That is a follow-up boundary task,
not a blocker for closing this `03AE` review.

No blocker was found.

## First Task Candidate Review

The first task candidate in `03AE` was:

```text
Review broader P7 actual feature extraction and label generation boundary before implementation.
```

That is the correct task. It keeps the project in docs-only review mode and
does not select actual feature extraction implementation, label generation
implementation, dataset construction, training or P8-P12.

No blocker was found.

## Planning Decision Review

The planning decision is conservative:

```text
Broader P7 actual feature extraction and label generation boundary is defined before implementation.
```

It explicitly does not approve actual feature extraction, actual label
generation, feature extraction implementation, label generation implementation,
source approval, source ingestion, parser / reader / ingestion, broad file
ingestion, CLI data paths, supervised dataset construction, training, model
architecture / trainer, real-data use, model-output integration, self-play,
league or P8-P12 entry.

No blocker was found.

## Evidence Grade / Non-Evidence Review

The evidence grade is correct:

```text
Broader P7 actual feature extraction and label generation boundary definition
evidence only.
```

This review is not:

- actual feature extraction implementation evidence.
- actual label generation implementation evidence.
- feature extraction approval.
- label generation approval.
- source approval evidence.
- parser / reader / ingestion evidence.
- supervised dataset construction evidence.
- training evidence.
- model-strength evidence.
- P8-P12 evidence.

No blocker was found.

## Governance Synchronization Review

The governance docs now record this review gate and next task:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

They keep:

- current stage as broader P7 supervised dataset construction / split /
  leakage boundary definition planning after this feature / label boundary
  review.
- full P7 open.
- actual feature extraction unapproved.
- actual label generation unapproved.
- source approval unapproved.
- training-data approval unapproved.
- source ingestion unapproved.
- parser / reader / ingestion unapproved.
- supervised dataset construction unapproved.
- training unapproved.
- P8-P12 unapproved.
- model-strength claims forbidden.
- real-data approval absent.

No blocker was found.

## Validation Results

Required validation for this review:

```text
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Results:

- `git diff --check`: pass.
- `python3 -m unittest tests/supervised/test_feature_label_schema.py`: pass,
  11 tests.
- `python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py`:
  pass, 1 test.
- `python3 -m unittest tests/data/test_replay_schema.py`: pass, 7 tests.
- `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`:
  pass, 1 test.

## Review Decision

```text
Review can close.
```

No blocker was found. The `03AE` scope, purpose, current status, concept
definitions, dependency map, parser / reader / ingestion relationship,
synthetic/local smoke boundary, candidate feature families, candidate label
families, feature boundary rules, label boundary rules, approval-record fields,
allowed future boundary, forbidden scope, stop conditions, risk controls,
evidence requirements, first task candidate, planning decision, evidence grade
and governance synchronization are sufficient for this review gate.

## Next Task Recommendation

Recommended next P7-only task:

```text
Define broader P7 supervised dataset construction, split and leakage boundary before implementation.
```

The next task must remain docs-only boundary definition. It must not approve
or implement supervised dataset construction, training-data approval, training,
actual feature extraction, actual label generation, parser / reader /
ingestion, source ingestion, source approval, production code, tests, fixtures,
data files, real-data use, model-output integration, self-play, league or
P8-P12.

## Evidence Grade

```text
Broader P7 actual feature extraction and label generation boundary review
evidence only.
```

## Explicit Non-Evidence

This review is not:

- actual feature extraction implementation.
- actual label generation implementation.
- feature extraction approval.
- label generation approval.
- source approval.
- source ingestion approval.
- parser implementation.
- reader implementation.
- ingestion implementation.
- supervised dataset construction.
- training.
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
- broader P7 implementation.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
