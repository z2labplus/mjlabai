# 03AR Broader P7 Minimal Implementation Proposal Boundary Review After Readiness Checklist Review

Date: 2026-06-30

## Scope

This document reviews
`docs/03_supervised_policy/03AQ_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_AFTER_READINESS_CHECKLIST_REVIEW.md`.

This is a docs-only review gate. It reviews the proposal-boundary definition
only. It does not draft a minimal implementation proposal for execution,
approve a minimal implementation proposal, approve broader P7 implementation,
add production code, add tests, add fixtures, add data files, approve source
approval, approve source ingestion, approve parser / reader / ingestion,
approve actual feature extraction, approve actual label generation, approve
supervised dataset construction, approve split creation, approve leakage-test
implementation, approve training data, approve a training run, approve
training, approve model architecture, approve trainer implementation, approve
checkpoints or weights, approve evaluation implementation, approve
model-output integration, create model-strength evidence, create Tenhou
ranked evidence, create stable-dan ranked-game evidence, create LuckyJ
`10.68` comparison evidence, create candidate-promotion evidence, approve
self-play, approve league or approve P8-P12 entry.

## Reviewed Artifacts

Primary artifact:

- `docs/03_supervised_policy/03AQ_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_AFTER_READINESS_CHECKLIST_REVIEW.md`

Immediate prerequisites:

- `docs/03_supervised_policy/03AO_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_AFTER_BOUNDARY_CHAIN_REVIEW.md`
- `docs/03_supervised_policy/03AP_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW_AFTER_BOUNDARY_CHAIN_REVIEW.md`

Broader P7 boundary chain:

- `docs/03_supervised_policy/03Y_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03Z_BROADER_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AD_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AF_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AG_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AH_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AI_BROADER_P7_TRAINING_DATA_APPROVAL_AND_TRAINING_RUN_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AJ_BROADER_P7_TRAINING_DATA_APPROVAL_AND_TRAINING_RUN_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AK_BROADER_P7_MODEL_ARCHITECTURE_AND_TRAINER_PLANNING_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AL_BROADER_P7_MODEL_ARCHITECTURE_AND_TRAINER_PLANNING_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AM_BROADER_P7_EVALUATION_DEPENDENCY_AND_MODEL_STRENGTH_EVIDENCE_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AN_BROADER_P7_EVALUATION_DEPENDENCY_AND_MODEL_STRENGTH_EVIDENCE_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`

Context artifacts were read only for boundary consistency:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`
- `src/mjlabai/supervised/feature_label_schema.py`
- `src/mjlabai/data/replay_schema.py`
- current synthetic/local supervised and replay smoke tests / fixtures.

## Scope Review

`03AQ` correctly defines only the broader P7 minimal implementation proposal
boundary after readiness checklist review.

It is explicit that it is docs-only and is not:

- minimal implementation proposal approval;
- broader P7 implementation approval;
- implementation proposal drafting for execution;
- production code;
- tests;
- fixtures;
- data files;
- source approval;
- source ingestion;
- parser / reader / ingestion;
- actual feature extraction;
- actual label generation;
- supervised dataset construction;
- split creation;
- leakage-test implementation;
- training-data approval;
- training-run approval;
- training;
- model architecture implementation;
- trainer implementation;
- checkpoint / weights creation;
- evaluation implementation;
- model-output integration;
- model-strength evidence;
- Tenhou ranked evidence;
- stable-dan ranked-game evidence;
- LuckyJ `10.68` comparison;
- candidate-promotion evidence;
- self-play / league;
- P8-P12 entry.

Review verdict: sufficient. No blocker found.

## Purpose Review

`03AQ` sufficiently defines the future broader P7 minimal implementation
proposal boundary. It states why a proposal boundary is needed before proposal
drafting, review, approval and execution. It separates proposal boundary,
proposal draft, proposal review, approval decision, implementation execution,
implementation review and current-scope acceptance.

It also defines the required proposal sections, exact-scope requirements,
forbidden proposal scope, approval-decision separation, approval
prerequisites, stop conditions, risk controls, evidence requirements, current
proposal-boundary decision and evidence grade.

Review verdict: sufficient. The purpose supports the north-star target only by
making later supervised-learning implementation auditable before resources are
spent; it does not claim model-strength progress.

## Proposal Lifecycle Vocabulary Review

`03AQ` distinguishes:

- proposal boundary;
- proposal draft;
- proposal review;
- approval decision;
- approved exact task;
- implementation execution;
- implementation review;
- current-scope acceptance;
- model-strength evidence;
- promotion evidence.

The review confirms that these concepts cannot substitute for each other.
Boundary definition is not proposal approval. Proposal draft is not
implementation approval. Review can close is not execution permission.
Acceptance is not model-strength evidence or candidate promotion.

Review verdict: sufficient.

## Candidate Proposal Classes Review

`03AQ` safely classifies candidate proposal classes.

Proposal-boundary-eligible but not approved classes are limited to:

- project-authored synthetic/local parser-reader smoke proposal;
- project-authored synthetic/local feature-label smoke extension proposal;
- project-authored synthetic/local dataset-shape smoke proposal;
- docs-only manifest validator proposal;
- source-approval record validator proposal;
- parser / reader approval record validator proposal;
- feature / label approval record validator proposal;
- dataset / split / leakage approval record validator proposal;
- training-data approval record validator proposal;
- model / trainer approval record validator proposal;
- evaluation evidence envelope validator proposal.

These classes all have `Approved now = No` and require later approval before
execution.

Not-ready classes remain not ready:

- approved-source-only parser / reader proposal;
- approved-source-only feature extractor proposal;
- approved-source-only label generator proposal;
- approved-source-only dataset manifest builder proposal;
- approved-training-data-only training dry-run proposal;
- approved-model-only evaluation protocol runner proposal.

Prohibited or later-stage classes remain blocked:

- broad file ingestion proposal;
- CLI data ingestion proposal;
- real Tenhou reader proposal before source approval;
- real-data training proposal;
- model-output evidence proposal before integration approval;
- self-play / league proposal;
- P8 RL implementation proposal under P7.

Review verdict: sufficient. `may_be_drafted_now` is not implementation
approval or execution approval.

## Minimal Proposal Required Sections Review

The required sections in `03AQ` are sufficient for future proposal review.
They require a proposal id, candidate class, exact objective, exact approval
status, exact files, functions/helpers/schemas if any, fixtures/tests/docs if
any, allowed and forbidden inputs, explicit output shape, source dependency,
parser / reader / ingestion dependency, feature / label dependency, dataset /
split / leakage dependency, training-data and training-run dependency, model /
trainer dependency, evaluation and evidence dependency, validation commands,
rollback plan, risk controls, stop conditions, governance updates,
non-evidence warning and next review / approval gate.

Review verdict: sufficient. A missing required section remains a blocker.

## Exact-Scope Requirements Review

`03AQ` requires a future proposal to specify exact file paths, exact modules,
exact tests, exact fixture paths, exact docs/governance paths, exact public
APIs or helpers, exact input/output mappings, exact validation commands, exact
rollback plan and explicit excluded directories, data sources and claims.

It explicitly states that listing exact files in a proposal boundary does not
approve editing those files. Listing a function does not approve
implementation. Listing validation commands does not approve adding tests or
code.

Review verdict: sufficient.

## Forbidden Proposal Scope Review

The forbidden scope is strict enough. `03AQ` blocks broad file ingestion,
arbitrary-path readers, CLI data ingestion, real Tenhou logs, real haifu,
external logs, platform data, account/session data, scraped data, platform
automation, third-party binaries, Akochan `system.exe` / `libai.so`,
unknown model artifacts, model-output integration, real-source feature
extraction, real-source label generation, supervised dataset construction
from real sources, training-data approval, training-run approval, training,
model architecture implementation, trainer implementation, evaluation runner,
benchmark harness, model-strength claims, Tenhou ranked evidence, stable-dan
ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion,
self-play, league and P8-P12.

Review verdict: sufficient.

## Future Approval Decision Separation Review

`03AQ` defines a safe sequence:

1. Boundary definition.
2. Boundary review.
3. Proposal draft.
4. Proposal review.
5. Separate approval decision.
6. Exact implementation execution, if approved.
7. Implementation review.
8. Current-scope acceptance decision, if warranted.

This separation is sufficient. Implementation prompts can only be generated
after an explicit approval decision. Implementation evidence, implementation
review, acceptance and closure must remain separate.

Review verdict: sufficient.

## Future Proposal Approval Decision Prerequisites Review

`03AQ` requires that a future approval decision verify the candidate class,
exact files, exact non-goals, all upstream dependencies, absence of implied
source approval, absence of implied parser / reader / ingestion approval,
absence of implied feature / label / dataset / training / model / trainer /
evaluation approval, local-safe validation commands, rollback, evidence/risk
/ decision-record planning, non-evidence wording and enforceable stop
conditions.

Review verdict: sufficient. Any later source, parser, feature, label,
dataset, training-data, model, trainer, evaluation or model-output behavior
still needs its own approval artifact.

## Stop Conditions Review

The stop conditions are sufficient. They require stopping if a proposal omits
exact files, validation commands, rollback, stop conditions or governance
references; depends on real data or external logs; implies source approval or
parser / reader / ingestion approval; creates training data; runs training;
touches model architecture, trainer, checkpoints or weights; evaluates model
strength; connects Tenhou or platform data; requires CLI or broad file
ingestion; uses third-party binaries or unknown artifacts; makes LuckyJ,
stable-dan, Tenhou or promotion claims; or drifts into P8-P12.

Review verdict: sufficient.

## Risk Controls Review

The risk controls cover the major current risks:

- proposal boundary mistaken for proposal approval;
- proposal draft mistaken for implementation approval;
- proposal-ready candidate mistaken for approved implementation;
- exact file listing mistaken for edit permission;
- validation command listing mistaken for permission to add tests;
- synthetic/local smoke creep;
- source approval gap;
- parser / reader / ingestion creep;
- feature / label creep;
- dataset / split / leakage creep;
- training-data creep;
- training-run creep;
- model / trainer creep;
- evaluation creep;
- model-output creep;
- model-strength overclaim;
- real-data creep;
- account/session/cookie/token risk;
- self-play / league / P8-P12 creep;
- governance mismatch.

Review verdict: sufficient. This review adds governance entries to keep the
same risks visible for the next proposal-drafting step.

## Evidence Requirements Review

The evidence requirements are sufficient. `03AQ` requires:

```text
proposal_boundary_id
proposal_class
readiness_reference
boundary_artifacts
candidate_class
proposal_status
approval_status
exact_files_status
source_dependency_status
parser_reader_ingestion_status
feature_label_status
dataset_split_leakage_status
training_data_status
training_run_status
model_trainer_status
evaluation_status
model_output_status
validation_commands
rollback_plan
stop_conditions
risk_status
blocker_status
evidence_log_reference
risk_register_reference
decision_record_reference
known_exclusions
explicit_non_evidence_warning
```

Review verdict: sufficient.

## Current Proposal-Boundary Decision Review

`03AQ` states:

```text
Broader P7 minimal implementation proposal boundary is defined, but no proposal is approved and no broader P7 implementation is approved.
```

It also states that the next safe step is a docs-only review of the
proposal-boundary definition.

Review verdict: conservative and sufficient.

## First Task Candidate Review

The first task candidate is:

```text
Review broader P7 minimal implementation proposal boundary after readiness checklist review.
```

This is the current task. It is reasonable and safe because it reviews the
boundary before any proposal draft, proposal approval or implementation.

Review verdict: sufficient.

## Planning Decision Review

The planning decision is conservative. It permits defining the proposal
boundary after readiness checklist review but does not approve a proposal or
implementation. It keeps proposal, review, approval decision, implementation,
implementation review and acceptance as separate tasks.

Review verdict: sufficient.

## Evidence Grade / Non-Evidence Review

The correct evidence grade is:

```text
Broader P7 minimal implementation proposal-boundary definition evidence only.
```

This review adds only:

```text
Broader P7 minimal implementation proposal-boundary review evidence only.
```

It is not:

- minimal implementation proposal approval;
- broader P7 implementation approval;
- implementation proposal drafting for execution;
- production code evidence;
- source approval evidence;
- parser / reader / ingestion evidence;
- actual feature extraction evidence;
- actual label generation evidence;
- supervised dataset construction evidence;
- training-data approval evidence;
- training-run evidence;
- training evidence;
- model / trainer implementation evidence;
- evaluation implementation evidence;
- model-output integration evidence;
- model-strength evidence;
- Tenhou ranked evidence;
- stable-dan ranked-game evidence;
- LuckyJ `10.68` comparison;
- candidate-promotion evidence;
- real-data approval;
- self-play evidence;
- league evidence;
- P8-P12 evidence.

Review verdict: sufficient.

## Governance Synchronization Review

The reviewed governance state is consistent:

- current stage is broader P7 minimal implementation proposal-boundary review.
- P7 current scope is closed only for the exact current scope.
- full P7 remains open.
- no minimal implementation proposal is approved.
- no broader P7 implementation is approved.
- no production code, tests, fixtures or data files are approved.
- no source is approved.
- no source ingestion is approved.
- no parser / reader / ingestion is approved.
- no actual feature extraction or label generation is approved.
- no supervised dataset construction is approved.
- no training-data approval exists.
- no training-run approval exists.
- no training is approved.
- no model architecture or trainer is approved.
- no evaluation implementation is approved.
- no model-output integration is approved.
- no model-strength evidence exists.
- no Tenhou / stable-dan / LuckyJ / candidate-promotion evidence exists.
- no P8-P12 work is approved.

This review synchronizes handoff, docs index, `10_NEXT`, technical plan,
evidence log, risk register, changelog, decision record, stage task contract,
milestones and backlog.

Review verdict: sufficient.

## Validation Results

Local validation for this review passed:

```text
git diff --check: pass
python3 -m unittest tests/supervised/test_feature_label_schema.py: pass, 11 tests
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py: pass, 1 test
python3 -m unittest tests/data/test_replay_schema.py: pass, 7 tests
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py: pass, 1 test
```

These commands validate formatting and confirm the current synthetic/local P7
and P6 smoke validation paths remain healthy. They do not access real data,
Tenhou, real haifu, external logs, platform data, model output, training,
self-play, league, third-party binaries or unknown model artifacts.

## Review Decision

```text
Review can close.
```

No blocker was found. The reviewed proposal boundary is sufficient as a
boundary for a future broader P7 minimal implementation proposal.

This review does not approve a proposal or broader P7 implementation.

## Next Task Recommendation

If validation passes and governance remains synchronized, the next first
unchecked task should be:

```text
Draft broader P7 minimal implementation proposal for review after proposal-boundary review.
```

That next task must still be docs-only proposal drafting. It must not approve
the proposal, approve broader P7 implementation, execute implementation, add
production code, tests, fixtures, data files, approve source, approve
ingestion, implement parser / reader / ingestion, implement actual feature
extraction, implement actual label generation, construct supervised datasets,
create splits, implement leakage tests, approve training data, approve a
training run, train, implement model architecture / trainer, create
checkpoints or weights, implement evaluation, integrate model output, create
model-strength evidence, read real data, self-play, run league or enter
P8-P12.

## Evidence Grade

Broader P7 minimal implementation proposal-boundary review evidence only.

## Explicit Non-Evidence

This review is not:

- minimal implementation proposal approval;
- broader P7 implementation approval;
- implementation proposal drafting for execution approval;
- production code;
- tests;
- fixtures;
- data files;
- source approval;
- source ingestion;
- parser;
- dataset reader;
- ingestion;
- actual feature extraction;
- actual label generation;
- supervised dataset construction;
- split creation;
- leakage-test implementation;
- training-data approval;
- training-run approval;
- training;
- model architecture implementation;
- trainer implementation;
- dataloader;
- optimizer;
- loss;
- checkpoint;
- weights;
- evaluation implementation;
- metric implementation;
- evaluation runner;
- benchmark harness;
- model-output integration;
- model-strength evidence;
- Tenhou ranked evidence;
- stable-dan ranked-game evidence;
- LuckyJ `10.68` comparison;
- candidate-promotion evidence;
- real Tenhou ingestion;
- real haifu ingestion;
- external-log ingestion;
- platform-data ingestion;
- self-play;
- league;
- P8-P12 entry approval.
