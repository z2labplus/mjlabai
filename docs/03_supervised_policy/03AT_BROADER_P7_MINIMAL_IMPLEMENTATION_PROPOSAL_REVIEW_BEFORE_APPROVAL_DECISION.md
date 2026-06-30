# 03AT Broader P7 Minimal Implementation Proposal Review Before Approval Decision

Date: 2026-06-30

## Scope

This document reviews
`docs/03_supervised_policy/03AS_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_FOR_REVIEW_AFTER_PROPOSAL_BOUNDARY_REVIEW.md`.

This is a docs-only proposal review gate. It reviews the proposal draft only.
It does not approve the proposal, approve broader P7 implementation, make an
approval decision, execute implementation, add production code, add tests, add
fixtures, add data files, approve source approval, approve source ingestion,
approve parser / reader / ingestion, approve actual feature extraction,
approve actual label generation, approve supervised dataset construction,
approve split creation, approve leakage-test implementation, approve training
data, approve a training run, approve training, approve model architecture,
approve trainer implementation, approve checkpoints or weights, approve
evaluation implementation, approve model-output integration, create
model-strength evidence, create Tenhou ranked evidence, create stable-dan
ranked-game evidence, create LuckyJ `10.68` comparison evidence, create
candidate-promotion evidence, approve self-play, approve league or approve
P8-P12 entry.

## Reviewed Artifacts

Primary artifact:

- `docs/03_supervised_policy/03AS_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_FOR_REVIEW_AFTER_PROPOSAL_BOUNDARY_REVIEW.md`

Immediate proposal-boundary artifacts:

- `docs/03_supervised_policy/03AQ_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_AFTER_READINESS_CHECKLIST_REVIEW.md`
- `docs/03_supervised_policy/03AR_BROADER_P7_MINIMAL_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW_AFTER_READINESS_CHECKLIST_REVIEW.md`

Readiness artifacts:

- `docs/03_supervised_policy/03AO_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_AFTER_BOUNDARY_CHAIN_REVIEW.md`
- `docs/03_supervised_policy/03AP_BROADER_P7_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW_AFTER_BOUNDARY_CHAIN_REVIEW.md`

Broader P7 boundary-chain context:

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

Context artifacts were read only for consistency:

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
- current P6/P7 synthetic/local schema helpers, smoke fixtures and tests.

## Scope Review

`03AS` correctly states that it only drafts a broader P7 minimal
implementation proposal for later review.

It is explicit that it is docs-only and is not:

- minimal implementation proposal approval;
- broader P7 implementation approval;
- implementation execution;
- production code;
- tests;
- fixtures;
- data files;
- source approval;
- source ingestion;
- parser / reader / ingestion implementation;
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
- checkpoint / weights;
- evaluation implementation;
- model-output integration;
- model-strength evidence;
- Tenhou ranked evidence;
- stable-dan ranked-game evidence;
- LuckyJ `10.68` comparison;
- candidate promotion evidence;
- self-play / league;
- P8-P12 entry.

Review verdict: sufficient. No blocker found.

## Proposal Summary Review

`03AS` selects:

```text
Project-authored synthetic/local parser-reader smoke proposal
```

This candidate class is conservative and appropriate for the next broader P7
proposal chain because it stays inside project-authored synthetic/local
artifacts, does not require source approval, does not require real data, does
not require model output and does not require feature extraction, label
generation, dataset construction, training or evaluation implementation.

The proposal summary is narrow:

- future behavior would validate only a tiny in-memory parse/read path;
- future behavior would not read real data;
- future behavior would not ingest external files;
- future behavior would not expose CLI paths;
- future behavior would not perform broad file ingestion;
- future behavior would not extract features;
- future behavior would not generate labels;
- future behavior would not construct datasets;
- future behavior would not train;
- future behavior would not evaluate model strength.

It also requires later proposal review, a separate approval decision and an
exact implementation task before execution.

Review verdict: sufficient. No blocker found.

## Candidate Class and Current Status Review

`03AS` records:

| Field | Review |
| --- | --- |
| candidate_class | `Project-authored synthetic/local parser-reader smoke proposal`; safe and proposal-boundary-eligible. |
| current_status | `proposal draft only`; safe. |
| approved_now | `No`; safe. |
| execution_allowed_now | `No`; safe. |
| proposal_review_required | `Yes`; safe. |
| approval_decision_required | `Yes`; safe. |
| implementation_task_required | `Yes, only after separate approval decision and exact 10_NEXT implementation task`; safe. |

These fields are not written as execution approval.

Review verdict: sufficient. No blocker found.

## Exact Goal Review

The future goal in `03AS` is appropriately narrow. It permits only:

- an in-memory mapping or explicitly approved project-authored
  synthetic/local fixture content;
- a tiny parser / reader boundary for synthetic/local supervised smoke
  records;
- a JSON-safe normalized synthetic/local record or validation summary;
- provenance and guardrail flags.

It excludes real Tenhou, real haifu, external logs, platform data, model
output, training data, strength evidence, arbitrary file reading, CLI, broad
ingestion, feature extraction, label generation, dataset construction, split
creation, leakage tests, training, model artifacts, evaluation and LuckyJ
progress evidence.

Review verdict: sufficient. No blocker found.

## Exact Non-Goals Review

The non-goals in `03AS` are complete for this proposal-review gate. They cover:

- no source approval;
- no source ingestion;
- no real data;
- no real Tenhou;
- no real haifu;
- no external logs;
- no platform data;
- no account / session / cookie / token;
- no arbitrary-path reading;
- no broad file ingestion;
- no CLI;
- no feature extraction;
- no label generation;
- no feature tensors;
- no labels;
- no targets;
- no supervised examples;
- no dataset;
- no splits;
- no leakage tests;
- no training data;
- no training;
- no model / trainer;
- no checkpoint / weights;
- no evaluation;
- no model output;
- no strength evidence;
- no P8-P12.

Review verdict: sufficient. No blocker found.

## Candidate Future Exact Files Review

`03AS` names the following candidate future files only:

- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`
- `tests/fixtures/supervised/synthetic_parser_reader_smoke.json`

It clearly states that these files are not approved for editing, creation or
execution by the proposal draft. It also states that the fixture candidate is
optional, requires later explicit justification, and may be avoided if
in-memory mappings are safer. Candidate API names are also marked as proposal
draft candidates only.

Review verdict: sufficient. No blocker found.

## Explicitly Excluded Files Review

The excluded-file list is sufficient for this stage. It protects existing
implementation and fixture artifacts unless a later approval decision names
them exactly:

- `src/mjlabai/supervised/feature_label_schema.py`;
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`;
- `tests/supervised/test_feature_label_schema.py`;
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`;
- `src/mjlabai/data/replay_schema.py`;
- `tests/fixtures/data/synthetic_replay_smoke.json`;
- `tests/data/test_replay_schema.py`;
- `tests/data/test_synthetic_replay_fixture_schema.py`;
- real-data directories;
- broad ingestion modules;
- CLI files;
- model / trainer / evaluation files;
- P8-P12 files;
- third-party artifacts;
- account/session/cookie/token files;
- `.env`, dotfiles and secrets.

Review verdict: sufficient. No blocker found.

## Allowed / Forbidden Inputs Review

Allowed inputs are restricted to project-authored synthetic/local fixture
content, JSON-safe in-repo synthetic/local smoke records, in-memory test
mappings, synthetic/local provenance and non-evidence flags, and exact fixture
paths named later by approval decision.

Forbidden inputs include real Tenhou, real haifu, external logs, platform
data, account/session/cookie/token data, hidden/dotfiles, `.env` / secrets,
model outputs, generated labels, human labels from real play, self-play
outputs, league outputs, third-party binaries / weights / checkpoints / params,
arbitrary user-supplied paths, broad directories, unapproved sources and real
external data.

Review verdict: sufficient. No blocker found.

## Allowed / Forbidden Outputs Review

Allowed outputs are limited to:

- in-memory normalized synthetic/local records;
- JSON-safe validation summaries;
- schema-safe smoke objects;
- provenance / guardrail flags;
- local unit-test pass/fail evidence;
- docs/governance evidence entries.

Forbidden outputs include feature tensors, labels, targets, supervised
examples, splits, datasets, training data, model inputs, model outputs,
evaluation results, model-strength evidence, Tenhou ranked evidence,
stable-dan ranked-game evidence, LuckyJ `10.68` comparison and candidate
promotion evidence.

Review verdict: sufficient. No blocker found.

## Dependency Status Review

The dependency status table in `03AS` is clear:

- source dependency is none beyond project-authored synthetic/local fixtures;
- source approval is not required for synthetic/local smoke;
- any real or approved-source use remains out of scope;
- parser / reader / ingestion approval is not granted;
- feature / label output is out of scope;
- dataset / split / leakage is out of scope;
- training data is out of scope;
- training run is out of scope;
- model / trainer is out of scope;
- evaluation is out of scope;
- model output is out of scope;
- P8-P12 is out of scope.

Review verdict: sufficient. No blocker found.

## Candidate Validation Commands Review

`03AS` lists candidate future validation commands safely. It marks the future
`test_synthetic_parser_reader_smoke.py` command as a candidate only and states
that this task must not create tests, must not run future non-existing tests
and does not approve test creation.

Existing smoke tests remain valid current validation commands.

Review verdict: sufficient. No blocker found.

## Rollback Plan Review

The rollback plan is sufficient:

- revert the exact implementation commit;
- remove only exact files added by the future approved implementation;
- preserve unrelated P6/P7 synthetic smoke artifacts;
- update governance docs;
- require no real-data deletion because no real data may be used;
- stop if rollback would touch unrelated files.

Review verdict: sufficient. No blocker found.

## Stop Conditions Review

The stop conditions cover the required blockers, including self-approval,
implied immediate implementation, unclear exact files, unclear rollback,
unclear governance, source approval, real data, broad ingestion, CLI paths,
account/session/cookie/token handling, ingestion drift, feature/label drift,
dataset / split / leakage drift, training-data and training drift,
model/trainer/checkpoint drift, evaluation/metric/harness drift, model-output
integration, strength / Tenhou / stable-dan / LuckyJ / promotion claims,
P8-P12 work and validation that requires non-existing code in the current
task.

Review verdict: sufficient. No blocker found.

## Risk Controls Review

The risk controls are complete for this stage. They cover:

- proposal draft mistaken for approval;
- candidate files mistaken for edit permission;
- synthetic/local smoke mistaken for real parser;
- parser-reader smoke drifting into ingestion;
- reader drifting into feature extraction;
- normalized records mistaken for training data;
- fixture paths mistaken for broad ingestion;
- validation commands mistaken for test creation approval;
- real data creep;
- CLI creep;
- model-output creep;
- dataset / training creep;
- P8-P12 creep;
- model-strength overclaim;
- governance mismatch.

Review verdict: sufficient. No blocker found.

## Evidence Requirements Review

`03AS` defines enough evidence requirements for a later approval decision. It
requires exact proposal id, linked boundary docs, exact approved file paths,
synthetic/local input boundary, output boundary, validation commands,
non-evidence warnings, rollback plan, evidence log entry, risk register update
and decision record update.

For this review, the evidence grade remains:

```text
Broader P7 minimal implementation proposal review evidence only.
```

Review verdict: sufficient. No blocker found.

## Approval Separation Review

The lifecycle is explicit and safe:

1. proposal draft;
2. proposal review;
3. separate approval decision;
4. exact implementation prompt only if approved;
5. implementation execution;
6. implementation review;
7. current-scope acceptance decision if warranted.

`03AS` performs step 1. This review performs step 2. It does not perform step
3 or later.

Review verdict: sufficient. No blocker found.

## Current Proposal Decision Review

`03AS` states:

```text
The proposal is drafted for review, but not approved.
Broader P7 implementation remains unapproved.
The next safe step is a docs-only review of this proposal draft.
```

Review verdict: sufficient. No blocker found.

## First Task Candidate Review

The first task candidate in `03AS` is:

```text
Review broader P7 minimal implementation proposal before approval decision.
```

This is exactly the current task. It is a review gate, not approval,
implementation, code, training, evaluation, P8-P12 or strength evidence.

Review verdict: sufficient. No blocker found.

## Planning Decision Review

The planning decision is conservative. It selects the smallest
proposal-boundary-eligible class that can move broader P7 forward without real
data, source approval, ingestion approval, actual feature extraction, label
generation, dataset construction, model code, training or evaluation
implementation.

Review verdict: sufficient. No blocker found.

## Evidence Grade / Non-Evidence Review

The evidence grade in `03AS` is correct:

```text
Broader P7 minimal implementation proposal draft evidence only.
```

This review evidence is:

```text
Broader P7 minimal implementation proposal review evidence only.
```

It is not proposal approval, implementation approval, production code
evidence, source approval evidence, parser / reader / ingestion evidence,
actual feature extraction evidence, actual label generation evidence,
supervised dataset construction evidence, training-data approval evidence,
training-run evidence, training evidence, model/trainer implementation
evidence, evaluation implementation evidence, model-output integration
evidence, model-strength evidence or P8-P12 evidence.

Review verdict: sufficient. No blocker found.

## Governance Synchronization Review

The governance documents are updated by this review to keep the current stage
consistent:

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

These updates keep current stage as broader P7 minimal implementation
approval-decision preparation after proposal review, keep full P7 open, keep
the proposal unapproved, keep broader P7 implementation unapproved and keep
source approval, source ingestion, parser / reader / ingestion, actual feature
extraction, actual label generation, supervised dataset construction,
training-data approval, training-run approval, training, model / trainer,
evaluation, model-output integration, model-strength evidence, Tenhou /
stable-dan / LuckyJ evidence, real data and P8-P12 unapproved.

Review verdict: sufficient. No blocker found.

## Validation Results

Required validation commands for this review:

```text
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

The future non-existing `tests/supervised/test_synthetic_parser_reader_smoke.py`
test was not run.

## Review Decision

```text
Review can close.
```

No blocker was found. This review does not approve the proposal, approve
broader P7 implementation or permit implementation execution.

## Next Task Recommendation

If this review is accepted, the next first task should be:

```text
Prepare approval decision for broader P7 minimal synthetic/local parser-reader smoke implementation.
```

That task must be docs-only approval-decision preparation. It must not be
implementation, code, tests, fixtures, data files, source approval, source
ingestion, real data, real Tenhou, real haifu, external logs, platform data,
broad file ingestion, CLI, actual feature extraction, actual label generation,
supervised dataset construction, split creation, leakage-test implementation,
training-data approval, training-run approval, training, model architecture,
trainer, checkpoint / weights, evaluation implementation, model-output
integration, model-strength evidence, Tenhou evidence, stable-dan evidence,
LuckyJ `10.68` comparison, candidate-promotion evidence, self-play, league or
P8-P12.

## Evidence Grade

```text
Broader P7 minimal implementation proposal review evidence only.
```

## Explicit Non-Evidence

This review is not:

- proposal approval;
- broader P7 implementation approval;
- implementation execution;
- production code;
- tests;
- fixtures;
- data files;
- source approval;
- source ingestion;
- parser implementation;
- reader implementation;
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
- candidate promotion evidence;
- real Tenhou ingestion;
- real haifu ingestion;
- external-log ingestion;
- platform-data ingestion;
- self-play;
- league;
- P8-P12 entry approval.
