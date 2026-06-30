# 03AS Broader P7 Minimal Implementation Proposal For Review After Proposal-Boundary Review

Date: 2026-06-30

## Scope

This document drafts a broader P7 minimal implementation proposal for later
review after the proposal-boundary review in `03AR`.

This is a docs-only proposal draft. It is not minimal implementation proposal
approval, not broader P7 implementation approval and not implementation
execution.

This document does not add production code, tests, fixtures, data files,
source approval, source ingestion, parser / reader / ingestion, actual feature
extraction, actual label generation, supervised dataset construction, split
creation, leakage-test implementation, training-data approval, training-run
approval, training, model architecture implementation, trainer implementation,
checkpoint / weights creation, evaluation implementation, metric
implementation, evaluation runner, benchmark harness, model-output
integration, model-strength evidence, Tenhou ranked evidence, stable-dan
ranked-game evidence, LuckyJ `10.68` comparison, candidate promotion,
self-play, league or P8-P12 entry.

## Proposal Summary

Proposal candidate class:

```text
Project-authored synthetic/local parser-reader smoke proposal
```

Exact proposal summary:

- Draft a later-reviewable proposal for a tiny project-authored
  synthetic/local parser-reader smoke implementation.
- The future implementation, if later reviewed and separately approved, would
  validate only a narrow in-memory parse/read path for project-authored
  synthetic/local supervised smoke content.
- It would not read real data, ingest external files, expose CLI paths,
  perform broad file ingestion, extract features, generate labels, construct a
  supervised dataset, train a model or evaluate model strength.

Why this is the safest first broader P7 proposal candidate:

- It stays inside project-authored synthetic/local artifacts.
- It does not require source approval.
- It does not require real Tenhou, real haifu, external logs, platform data,
  accounts, sessions, cookies or tokens.
- It does not require model-output integration.
- It does not require actual feature extraction or actual label generation.
- It does not require dataset construction, split creation, leakage-test
  implementation, training data, training runs, model architecture, trainer
  code or evaluation implementation.
- It can exercise the boundary between P6 synthetic replay shape and P7
  supervised smoke shape without approving a real parser, reader or ingestion
  path.

This proposal must still go through a later proposal review, separate approval
decision and exact implementation task before any file can be created or
edited for implementation.

## Candidate Class and Current Status

| Field | Value |
| --- | --- |
| candidate_class | Project-authored synthetic/local parser-reader smoke proposal |
| current_status | proposal draft only |
| approved_now | No |
| execution_allowed_now | No |
| proposal_review_required | Yes |
| approval_decision_required | Yes |
| implementation_task_required | Yes, only after separate approval decision and exact `10_NEXT` implementation task |

## Exact Goal

The future proposal, if later reviewed and separately approved, would create a
minimal synthetic/local parser-reader smoke implementation that:

- accepts only an in-memory mapping or explicitly approved project-authored
  synthetic/local fixture content;
- validates a tiny parser/reader boundary for synthetic/local supervised smoke
  records;
- returns only a JSON-safe normalized synthetic/local record or validation
  summary;
- records provenance and guardrail flags showing that the input is not real
  Tenhou, real haifu, external log, platform data, model output, training data
  or strength evidence.

The future implementation would not read real data, ingest arbitrary files,
expose CLI paths, extract features, generate labels, construct datasets,
create splits, run leakage checks, train, create model artifacts, evaluate
model outputs or claim progress toward LuckyJ `10.68`.

## Exact Non-Goals

The proposal explicitly excludes:

- source approval;
- source ingestion;
- real data;
- real Tenhou;
- real haifu;
- external logs;
- platform data;
- account / session / cookie / token handling;
- arbitrary-path file reading;
- broad file ingestion;
- CLI data paths;
- actual feature extraction;
- actual label generation;
- feature tensors;
- labels;
- targets;
- supervised examples;
- supervised dataset construction;
- split creation;
- leakage-test implementation;
- training data;
- training-data approval;
- training-run approval;
- training;
- tuning;
- model input pipeline implementation;
- model architecture;
- model config;
- encoder / policy head / value head / auxiliary head / decision head
  implementation;
- dataloader / optimizer / loss / trainer implementation;
- training loop;
- checkpoint / weights / snapshot creation;
- unknown model artifact loading;
- evaluation implementation;
- metric implementation;
- evaluation runner;
- benchmark harness;
- latency measurement;
- fixed-position exact-match computation;
- model-output integration;
- model-strength evidence;
- Tenhou ranked evidence;
- stable-dan ranked-game evidence;
- LuckyJ `10.68` comparison;
- candidate promotion evidence;
- self-play;
- league;
- P8-P12 entry or implementation.

## Candidate Future Exact Files

The following files are candidate future files only. They are not approved for
editing, creation or execution by this document.

- `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
- `tests/supervised/test_synthetic_parser_reader_smoke.py`
- `tests/fixtures/supervised/synthetic_parser_reader_smoke.json`

The fixture candidate is optional and would require explicit justification in
a later approval decision. A future implementation may choose to use only
in-memory project-authored synthetic/local mappings if that is safer.

Candidate future API names, if later approved, may include:

- `SYNTHETIC_PARSER_READER_SMOKE_SCHEMA_VERSION`
- `SyntheticParserReaderSmokeError`
- `validate_synthetic_parser_reader_smoke_mapping(...)`
- `normalize_synthetic_parser_reader_smoke_mapping(...)`
- `collect_synthetic_parser_reader_smoke_errors(...)`

These names are proposal-draft candidates only. They are not implementation
approval.

## Explicitly Excluded Files

This task must not edit or create implementation files. Future implementation
must also exclude these files unless a separate approval decision names them
exactly:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`
- any real-data directory;
- any broad ingestion module;
- any CLI file;
- any model, trainer, dataloader, optimizer, loss, checkpoint, weight or
  evaluation file;
- any P8-P12 file;
- any third-party source, binary, params or build artifact;
- any account / session / cookie / token file;
- `.env`, dotfiles or secret files.

## Allowed Inputs

Future allowed inputs, only if later reviewed and separately approved, are
limited to:

- project-authored synthetic/local fixture content;
- JSON-safe in-repo synthetic/local smoke records;
- in-memory mappings created inside tests;
- explicit synthetic/local provenance and non-evidence flags;
- exact fixture paths named by a later approval decision.

Allowed inputs must not be broad filesystem paths and must not come from real
or external sources.

## Forbidden Inputs

Forbidden inputs include:

- real Tenhou;
- real haifu;
- external logs;
- platform data;
- account / session / cookie / token;
- hidden files / dotfiles;
- `.env` or secrets;
- model outputs;
- generated labels;
- human labels from real play;
- self-play outputs;
- league outputs;
- third-party binaries;
- third-party weights, checkpoints, params or snapshots;
- arbitrary user-supplied paths;
- broad directories;
- source files not explicitly approved;
- real data from outside the repository.

## Allowed Outputs

Future allowed outputs, only if later approved, are limited to:

- in-memory normalized synthetic/local records;
- JSON-safe validation summaries;
- schema-safe smoke objects;
- provenance / guardrail flags;
- local unit-test pass/fail evidence;
- docs/governance evidence entries.

These outputs are engineering smoke outputs only.

## Forbidden Outputs

Forbidden outputs include:

- feature tensors;
- labels;
- targets;
- supervised examples;
- splits;
- datasets;
- training data;
- model inputs;
- model outputs;
- evaluation results;
- model-strength evidence;
- Tenhou ranked evidence;
- stable-dan ranked-game evidence;
- LuckyJ `10.68` comparison;
- candidate-promotion evidence.

## Dependency Status

| Dependency area | Status |
| --- | --- |
| Source dependency | None beyond project-authored synthetic/local fixtures. |
| Source approval | Not required for project-authored synthetic/local smoke; any real or approved-source use is out of scope. |
| Parser / reader / ingestion | This is only a candidate future parser-reader smoke proposal; parser / reader / ingestion approval is not granted. |
| Feature / label | No actual feature or label output. |
| Dataset / split / leakage | Out of scope. |
| Training data | Out of scope. |
| Training run | Out of scope. |
| Model / trainer | Out of scope. |
| Evaluation | Out of scope. |
| Model output | Out of scope. |
| P8-P12 | Out of scope. |

## Candidate Future Validation Commands

Future validation command candidates, if a later implementation is approved,
may include:

```bash
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

These are candidate future validation commands only. This task does not create
the future test, must not run a future non-existing test and does not approve
test creation. Current validation remains limited to existing tests.

## Rollback Plan

If a later implementation is approved and then must be rolled back:

- revert the exact implementation commit;
- remove only exact files added by the future approved implementation;
- leave unrelated P6/P7 synthetic smoke artifacts intact;
- update governance docs to record the rollback and evidence status;
- no real-data deletion should be needed because no real data may be used;
- stop and document a blocker if rollback would touch unrelated files.

## Stop Conditions

Stop before approval or implementation if:

- this proposal starts approving itself;
- this proposal implies implementation can start immediately;
- exact future files are unclear;
- rollback is unclear;
- governance sync is unclear;
- source approval is required;
- real data is required;
- broad file ingestion is required;
- CLI paths are required;
- account / session / cookie / token handling appears;
- parser / reader smoke drifts into source ingestion;
- reader behavior drifts into actual feature extraction;
- any output emits feature tensors, labels, targets or supervised examples;
- dataset construction, split creation or leakage-test implementation appears;
- training data, training runs or training appear;
- model / trainer / checkpoint / weights appear;
- evaluation implementation, metric implementation or benchmark harness
  appears;
- model-output integration appears;
- model-strength, Tenhou, stable-dan, LuckyJ or promotion claims appear;
- P8-P12 work appears;
- validation requires non-existing code in this task.

## Risk Controls

| Risk | Control |
| --- | --- |
| Proposal draft mistaken for approval | State `approved_now = No`, require later review and separate approval decision. |
| Candidate files mistaken for edit permission | Mark all candidate future files as not approved for editing now. |
| Synthetic/local smoke mistaken for real parser | Restrict inputs to project-authored synthetic/local mappings and require non-evidence warnings. |
| Parser-reader smoke drifts into ingestion | Forbid arbitrary paths, CLI, broad directories and external files. |
| Reader drifts into feature extraction | Forbid feature tensors, labels, targets and supervised examples. |
| Normalized records mistaken for training data | Mark allowed outputs as validation summaries / smoke objects only. |
| Fixture paths mistaken for broad ingestion | Require exact fixture paths and separate approval before use. |
| Validation commands mistaken for test creation approval | Label commands as future candidates only and run only existing tests now. |
| Real data creep | Forbid real Tenhou, real haifu, external logs and platform data. |
| CLI creep | Forbid CLI data paths and broad file ingestion. |
| Model-output creep | Forbid model outputs and model-output integration. |
| Dataset / training creep | Forbid datasets, splits, training data, training runs and training. |
| P8-P12 creep | Keep self-play, league and P8-P12 out of scope. |
| Model-strength overclaim | Assign proposal-draft evidence grade only. |
| Governance mismatch | Update handoff, index, 10_NEXT, evidence log, risk register, changelog, decision record, stage contract, milestones, backlog and technical plan together. |

## Evidence Requirements

Any later implementation approval must require an evidence plan that records:

- exact proposal id and linked boundary docs;
- exact approved file paths;
- exact synthetic/local input boundary;
- exact output boundary;
- validation commands;
- non-evidence warnings;
- rollback plan;
- evidence log entry;
- risk register update;
- decision record update.

For this task, the evidence grade is:

```text
Broader P7 minimal implementation proposal draft evidence only.
```

## Approval Separation

The required lifecycle is:

1. proposal draft;
2. proposal review;
3. separate approval decision;
4. exact implementation prompt only if approved;
5. implementation execution;
6. implementation review;
7. current-scope acceptance decision if warranted.

This task performs only step 1.

## Current Proposal Decision

The proposal is drafted for review, but not approved.

Broader P7 implementation remains unapproved. The next safe step is a
docs-only review of this proposal draft.

## First Task Candidate

If no blocker is found, the next first task should be:

```text
Review broader P7 minimal implementation proposal before approval decision.
```

That next task must be a docs-only proposal review gate. It must not be
proposal approval, implementation approval, implementation execution, code,
tests, fixtures, data files, source approval, ingestion approval, parser /
reader / ingestion, actual feature extraction, actual label generation,
dataset construction, training-data approval, training-run approval, training,
model / trainer implementation, evaluation implementation, model-output
integration, strength evidence, real-data use, self-play, league or P8-P12.

## Planning Decision

The selected candidate class is `Project-authored synthetic/local
parser-reader smoke proposal` because it is the smallest proposal-boundary
eligible class that can move broader P7 forward without requiring real data,
source approval, ingestion approval, actual feature extraction, label
generation, dataset construction, model code, training or evaluation
implementation.

This planning decision does not approve the proposal or implementation.

## Evidence Grade

Current evidence grade:

```text
Broader P7 minimal implementation proposal draft evidence only.
```

This is useful for governance sequencing and north-star alignment because it
reduces the chance of uncontrolled supervised-learning implementation before
evidence controls exist. It is not model-strength progress.

## Explicit Non-Evidence

This document is not:

- proposal approval;
- broader P7 implementation approval;
- production code;
- tests;
- fixtures;
- data files;
- source approval;
- source ingestion;
- parser;
- reader;
- ingestion;
- actual feature extraction;
- actual label generation;
- feature tensors;
- labels;
- targets;
- supervised examples;
- supervised dataset construction;
- split creation;
- leakage-test implementation;
- training-data approval;
- training-run approval;
- training;
- tuning;
- model architecture;
- trainer;
- checkpoint / weights;
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
- account / session / cookie / token handling;
- self-play;
- league;
- P8-P12 entry approval.
