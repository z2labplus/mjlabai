# 03AD Broader P7 Parser Reader Ingestion Boundary Review Before Implementation

## Scope

This document reviews
`docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`
before any broader P7 parser, reader or ingestion implementation.

This is a docs-only review gate. It does not approve parser, reader,
ingestion, source ingestion, source approval, training-data approval, broad
file ingestion, CLI data paths, real-data use, actual feature extraction,
actual label generation, supervised dataset construction, training, broader
P7 implementation or P8-P12 entry.

## Reviewed Artifacts

Primary reviewed artifact:

- `docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`

Broader P7 context:

- `docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03Z_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`
- `docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`
- `docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md`

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
The 03AC scope is correct.
```

`03AC` clearly states that it only defines the broader P7 parser, reader and
ingestion boundary before implementation. It is docs-only. It is not parser
implementation, reader implementation, ingestion implementation, parser /
reader / ingestion approval, source ingestion approval, source approval,
training-data approval, real-data use, actual feature extraction, actual label
generation, supervised dataset construction, training, broader P7
implementation approval, P8-P12 entry or model-strength evidence.

No blocker was found.

## Purpose Review

The purpose is sufficient for this review gate.

`03AC` makes future broader P7 parser / reader / ingestion work auditable by
defining:

- parser, reader, ingestion and source-ingestion vocabulary.
- the relationship between parser / reader / ingestion, source approval,
  source ingestion approval, feature extraction, label generation and dataset
  construction.
- future approval preconditions.
- future approval-record fields.
- allowed and forbidden future behavior.
- stop conditions.
- evidence requirements and risk controls.

The main guardrail is explicit:

```text
Source readiness and docs context are not parser / reader / ingestion approval.
```

No blocker was found.

## Current Parser Reader Ingestion Status Review

The current status in `03AC` is accurate.

Current broader P7 status remains:

- no parser approved.
- no dataset reader approved.
- no ingestion approved.
- no source ingestion approved.
- no broad file ingestion approved.
- no CLI data path approved.
- no real-data reader approved.
- no Tenhou reader approved.
- no real haifu reader approved.
- no external-log reader approved.
- no platform-data reader approved.
- no account / session / cookie / token reader approved.
- the current synthetic/local supervised smoke fixture helper is not parser /
  reader / ingestion approval.
- the P6 minimal replay schema helper is not broader P7 parser / reader /
  ingestion approval.
- repository docs are not parseable training data.
- source readiness and source-specific approval are not parser / reader /
  ingestion approval.

No blocker was found.

## Concept Definitions Review

`03AC` clearly distinguishes:

- parser.
- dataset reader.
- ingestion.
- source ingestion.
- broad file ingestion.
- CLI data path.
- source-specific approval.
- parser / reader / ingestion approval.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- training data approval.

The review confirms that no concept is written as a substitute for another
approval. Source-specific approval does not approve ingestion. Parser /
reader / ingestion approval does not approve feature extraction, label
generation, dataset construction or training.

No blocker was found.

## Boundary Dependency Map Review

The dependency order is reasonable and conservative:

```text
source readiness
-> source-specific approval
-> parser / reader / ingestion boundary
-> parser / reader / ingestion proposal
-> parser / reader / ingestion approval decision
-> exact implementation files
-> synthetic/local or approved-source-only implementation
-> implementation review
-> feature / label boundary
-> dataset construction boundary
-> training approval
```

`03AC` also correctly allows a synthetic/local replacement for source-specific
approval only when there is an explicit project-authored synthetic/local
boundary, proposal, approval decision and exact first `10_NEXT` implementation
task.

If any required predecessor is missing, parser / reader / ingestion must not
be implemented.

No blocker was found.

## Candidate Classes Review

The candidate classes are complete enough and safely classified for this
boundary.

The table covers:

- synthetic/local fixture reader.
- project-authored synthetic supervised fixture reader.
- approved-source replay reader.
- approved-source metadata reader.
- raw-to-normalized replay parser.
- ingestion manifest validator.
- provenance / checksum validator.
- split manifest reader.
- dataset index reader.
- rejected broad arbitrary file ingestion.
- rejected CLI path ingestion.
- rejected account/session/cookie/token reader.
- rejected platform scraper.
- rejected real Tenhou reader before explicit approval.

For each class, `03AC` records candidate class, current status, approved-now
status, source dependency, source-approval requirement, implementation-approval
requirement, docs-planning allowance, forbidden-until boundary, risk and notes.

No class is currently approved for implementation.

No blocker was found.

## Future Approval Record Fields Review

The future approval-record fields are sufficient for a later parser / reader /
ingestion approval gate.

Required fields include:

- `component_id`.
- `component_type`.
- source id dependency.
- approved source categories.
- forbidden source categories.
- input path policy.
- output path policy.
- raw storage policy.
- derived storage policy.
- `may_enter_git`.
- privacy / platform terms status.
- account / session / cookie / token prohibition.
- parser scope.
- reader scope.
- ingestion scope.
- validation commands.
- exact files.
- dependency versions.
- evidence log reference.
- risk register reference.
- decision record reference.
- stop conditions.
- rollback plan.
- human / Web ChatGPT approval reference.
- `10_NEXT` explicit task requirement.

If any required field is missing, the component must remain unapproved.

No blocker was found.

## Allowed Future Implementation Boundary Review

The allowed future implementation boundary is conservative.

A future parser / reader / ingestion implementation must be exactly one of:

- synthetic/local only.
- approved-source-only.
- docs-only validator.

It must be exact-file scoped, reviewed and approved before implementation, and
must avoid broad file ingestion, CLI unless separately approved, account /
session / cookie / token handling, platform automation, unknown third-party
binaries and real data unless both source approval and reader approval exist.

It must preserve provenance, storage, evidence and risk logs. It must stop
before actual feature extraction, actual label generation and supervised
dataset construction unless those later boundaries are separately approved.

No blocker was found.

## Forbidden Scope Review

The forbidden scope is strict enough.

`03AC` forbids:

- arbitrary filesystem ingestion.
- recursive broad ingestion.
- CLI user-supplied data paths.
- hidden file / dotfile ingestion.
- `.env` / secret / token reading.
- account / session / cookie / token reading.
- real Tenhou, real haifu, external logs and platform data before explicit
  source and reader approval.
- scraping, automation or evasion.
- parsers that emit feature tensors without feature boundary approval.
- readers that emit labels without label boundary approval.
- ingestion that constructs supervised datasets without dataset policy
  approval.
- ingestion that trains or calls a model.
- writing raw real data into the repository.
- vendoring third-party data or artifacts into the repository.
- model-output ingestion before model-output policy.
- self-play / league output ingestion before later-stage approval.

No blocker was found.

## Stop Conditions Review

The stop conditions are sufficient.

Future parser / reader / ingestion work must stop if an unapproved source,
unapproved file type, unapproved real data, unclear path policy, feature
extraction, label generation, dataset construction, training behavior, model
call, CLI / broad ingestion need, account/session/cookie/token data,
third-party binary / weights need, P8-P12 drift, validation failure or evidence
overclaim appears.

No blocker was found.

## Risk Controls Review

The risk controls are complete enough for this boundary.

`03AC` covers:

- parser mistaken as feature extraction.
- reader mistaken as label generation.
- ingestion mistaken as dataset construction.
- source approval mistaken as ingestion approval.
- docs context mistaken as parseable data.
- current smoke fixture mistaken as real dataset.
- broad file ingestion creep.
- CLI ingestion creep.
- secret/token leak.
- platform/account data leak.
- real-data rights violation.
- split/leakage error.
- model-output/self-play/league data too early.
- training creep.
- P8-P12 creep.
- model-strength overclaim.

No blocker was found.

## Evidence Requirements Review

The future parser / reader / ingestion evidence requirements are sufficient.

They require component id, component type, source id, source approval status,
parser / reader / ingestion approval status, exact files, input policy, output
policy, provenance policy, storage policy, privacy / platform status,
validation commands, evidence log reference, risk register reference, decision
record reference, known exclusions and explicit non-evidence warning.

No blocker was found.

## First Task Candidate Review

The `03AC` first task candidate was:

```text
Review broader P7 parser, reader and ingestion boundary before implementation.
```

That candidate was correct and is executed by this document. It did not choose
parser implementation, reader implementation, ingestion implementation, data
reading, source ingestion, feature extraction, label generation, training or
P8-P12.

No blocker was found.

## Planning Decision Review

The planning decision is conservative:

```text
Broader P7 parser, reader and ingestion boundary is defined before
implementation. This does not approve parser, dataset reader, source
ingestion, broad file ingestion, CLI data path, real-data use, actual feature
extraction, actual label generation, supervised dataset construction,
training, model architecture, model-output integration, self-play, league or
P8-P12 entry.
```

No blocker was found.

## Governance Synchronization Review

The governance synchronization requirement is satisfied by this update.

The following docs now record the review and next task:

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

Synchronized status:

- current stage is broader P7 parser / reader / ingestion boundary review
  before implementation.
- full P7 remains open.
- no parser / reader / ingestion is approved.
- no source ingestion is approved.
- no broad file ingestion is approved.
- no CLI data path is approved.
- no source is approved.
- no training data source is approved.
- actual feature extraction and actual label generation remain unapproved.
- P8-P12 remain unapproved.
- no model-strength claim or real-data approval was added.

No blocker was found.

## Validation Results

Required validation commands for this review gate:

```text
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

The final command outputs are recorded in the task response. Passing validation
is required before commit.

## Review Decision

```text
Review can close.
```

Conditions satisfied:

- scope correct.
- purpose sufficient.
- current status accurate.
- concept definitions clear.
- dependency map safe.
- candidate classes complete and safely classified.
- approval record fields sufficient.
- allowed future boundary safe.
- forbidden scope strict.
- stop conditions sufficient.
- risk controls sufficient.
- evidence requirements sufficient.
- first task candidate safe.
- planning decision conservative.
- evidence grade conservative.
- governance synchronized.
- no blocker.
- no overclaim.

## Next Task Recommendation

Recommended next P7-only task:

```text
Define broader P7 actual feature extraction and label generation boundary before implementation.
```

The next task must remain docs-only boundary definition. It is not actual
feature extraction implementation, actual label generation implementation,
feature extraction approval, label generation approval, parser / reader /
ingestion implementation, source ingestion, supervised dataset construction,
training, model architecture / trainer work, real-data use, model-output
integration, self-play, league or P8-P12 entry.

## Evidence Grade

```text
Broader P7 parser, reader and ingestion boundary review evidence only.
```

## Explicit Non-Evidence

This review is not:

- parser implementation.
- reader implementation.
- ingestion implementation.
- parser / reader / ingestion approval.
- source approval.
- source ingestion approval.
- training-data approval.
- broad file ingestion.
- CLI.
- real-data use.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- training.
- model architecture.
- trainer.
- model-output integration.
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
