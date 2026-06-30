# 03AQ Broader P7 Minimal Implementation Proposal Boundary After Readiness Checklist Review

Date: 2026-06-30

## Scope

This document defines the boundary for a future broader P7 minimal
implementation proposal after the readiness checklist review in `03AP`.

This is a docs-only proposal-boundary definition. It is not a minimal
implementation proposal, not a proposal approval decision, not broader P7
implementation approval and not implementation execution.

This document does not add production code, tests, fixtures, data files,
source approval, source ingestion, parser / reader / ingestion, actual feature
extraction, actual label generation, supervised dataset construction, split
creation, leakage-test implementation, training data, a training run, model
architecture, trainer code, checkpoints, weights, evaluation implementation,
metric implementation, a runner, a benchmark harness, model-output
integration, Tenhou evidence, stable-dan evidence, LuckyJ `10.68` comparison,
candidate promotion, self-play, league or P8-P12 work.

## Purpose

The purpose of this boundary is to make any future broader P7 minimal
implementation proposal auditable before it can be reviewed for approval. It
defines the sections, exact-scope requirements, forbidden scope, evidence
requirements, risk controls, rollback expectations and stop conditions that a
future proposal must include.

This boundary separates:

- proposal-boundary definition from proposal drafting;
- proposal drafting from proposal review;
- proposal review from approval decision;
- approval decision from implementation execution;
- implementation execution from implementation review;
- implementation review from current-scope acceptance;
- current-scope acceptance from model-strength evidence or candidate
  promotion.

## Proposal Lifecycle Vocabulary

| Term | Meaning | Not a substitute for |
| --- | --- | --- |
| Proposal boundary | A docs-only rule set that describes what a later proposal must contain. | Proposal draft, approval or execution. |
| Proposal draft | A concrete plan naming exact files, inputs, outputs, validation commands and rollback. | Approval or implementation. |
| Proposal review | A docs-only review of a proposal draft. | Approval or implementation. |
| Approval decision | A separate docs-only decision that may approve one exact task. | Broader approval, training approval or strength evidence. |
| Approved exact task | A narrowly scoped task authorized by an approval decision. | Permission to expand scope. |
| Implementation execution | The later code/docs task, if explicitly approved. | Review, acceptance or promotion. |
| Implementation review | A later review of implemented artifacts. | Acceptance or strength evidence. |
| Current-scope acceptance | A later decision that a narrow implemented scope can close. | Full P7 closure or P8-P12 entry. |
| Model-strength evidence | Evidence from approved evaluation protocols. | Any docs-only boundary, synthetic smoke or proposal artifact. |
| Promotion evidence | Evidence that can support candidate promotion. | Any current broader P7 boundary artifact. |

Boundary definition is not execution permission. Proposal drafting is not
execution permission. Review can close is not execution permission.

## Candidate Proposal Classes

The classes below are allowed to be described by a future proposal, but none is
approved by this document.

| Proposal class | Current status | Approved now | May be drafted now | Approval required before execution | Required upstream artifacts | Exact files required before approval | Validation required | Stop conditions | Risk level | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Project-authored synthetic/local parser-reader smoke proposal | proposal-boundary-eligible | No | Yes | Yes | `03AC`, `03AD`, `03AO`, `03AP`, this boundary | Exact module, test and fixture paths; no broad ingestion path | Targeted synthetic/local tests only | Any real data, broad ingestion or CLI path | Medium | Must stay synthetic/local and in-memory. |
| Project-authored synthetic/local feature-label smoke extension proposal | proposal-boundary-eligible | No | Yes | Yes | `03AE`, `03AF`, `03AO`, `03AP`, current smoke artifacts | Exact supervised module/test/fixture paths | Existing and proposed synthetic/local tests | Any training-data, dataset or real-source behavior | Medium | May extend smoke only after approval. |
| Project-authored synthetic/local dataset-shape smoke proposal | proposal-boundary-eligible | No | Yes | Yes | `03AG`, `03AH`, `03AO`, `03AP` | Exact schema/test/fixture paths | Synthetic/local schema tests | Any split/leakage/training-data approval claim | Medium | Shape-only unless later approved otherwise. |
| Docs-only manifest validator proposal | proposal-boundary-eligible | No | Yes | Yes | Source-rights and approval-record boundary docs | Exact validator and docs paths | Local unit tests with synthetic manifests | Any real manifest ingestion or source approval by implication | Low | Validator cannot approve sources. |
| Source-approval record validator proposal | proposal-boundary-eligible | No | Yes | Yes | P6 source-rights docs and P7 source boundary docs | Exact schema/test paths | Synthetic approval-record tests | Any real source approval or ingestion | Medium | Record validator only. |
| Parser / reader approval record validator proposal | proposal-boundary-eligible | No | Yes | Yes | `03AC`, `03AD` | Exact schema/test paths | Synthetic approval-record tests | Any parser, reader or file ingestion execution | Medium | Approval-record shape only. |
| Feature / label approval record validator proposal | proposal-boundary-eligible | No | Yes | Yes | `03AE`, `03AF` | Exact schema/test paths | Synthetic approval-record tests | Any actual feature or label generation | Medium | Record validator only. |
| Dataset / split / leakage approval record validator proposal | proposal-boundary-eligible | No | Yes | Yes | `03AG`, `03AH` | Exact schema/test paths | Synthetic approval-record tests | Any dataset construction, split or leakage implementation | Medium | Must not produce training data. |
| Training-data approval record validator proposal | proposal-boundary-eligible | No | Yes | Yes | `03AI`, `03AJ` | Exact schema/test paths | Synthetic approval-record tests | Any training-data approval or training run | High | Record shape is not approval. |
| Model / trainer approval record validator proposal | proposal-boundary-eligible | No | Yes | Yes | `03AK`, `03AL` | Exact schema/test paths | Synthetic approval-record tests | Any model, trainer, checkpoint or weight creation | High | No architecture implementation. |
| Evaluation evidence envelope validator proposal | proposal-boundary-eligible | No | Yes | Yes | `03AM`, `03AN`, P5 envelope docs | Exact schema/test paths | Synthetic/local evidence-record tests | Any strength, ranking or promotion claim | High | Evidence shape only, not evidence. |
| Approved-source-only parser / reader proposal | not-ready | No | No | Yes | Explicit source approval and reader approval docs | Exact approved source and file paths | Future approved-source local tests | Any missing approval artifact | High | Requires separate approval first. |
| Approved-source-only feature extractor proposal | not-ready | No | No | Yes | Approved source, parser / reader, feature boundary approval | Exact approved source, module and test paths | Future approved-source tests | Any missing parser/reader approval | High | Not eligible now. |
| Approved-source-only label generator proposal | not-ready | No | No | Yes | Approved source, parser / reader, label boundary approval | Exact approved source, module and test paths | Future approved-source tests | Any missing source or label approval | High | Not eligible now. |
| Approved-source-only dataset manifest builder proposal | not-ready | No | No | Yes | Approved source, parser / reader, feature/label, split/leakage approval | Exact manifest, module and test paths | Future approved-source tests | Any missing upstream approval | High | Not eligible now. |
| Approved-training-data-only training dry-run proposal | not-ready | No | No | Yes | Training-data approval and training-run approval | Exact data, model, trainer and test paths | Future training dry-run tests | Any missing training-data or model/trainer approval | Critical | Not eligible now. |
| Approved-model-only evaluation protocol runner proposal | not-ready | No | No | Yes | Model/trainer approval and evaluation protocol approval | Exact model/eval/test paths | Future approved evaluation tests | Any strength claim or model-output path without approval | Critical | Not eligible now. |
| Broad file ingestion proposal | prohibited/later-stage | No | No | Separate future stage decision required | None sufficient now | N/A | N/A | Any attempt under this boundary | Critical | Prohibited now. |
| CLI data ingestion proposal | prohibited/later-stage | No | No | Separate future stage decision required | None sufficient now | N/A | N/A | Any attempt under this boundary | Critical | Prohibited now. |
| Real Tenhou reader proposal before source approval | prohibited/later-stage | No | No | Separate source, compliance and reader approval required | None sufficient now | N/A | N/A | Any real Tenhou path | Critical | Prohibited now. |
| Real-data training proposal | prohibited/later-stage | No | No | Separate source, training-data and training-run approval required | None sufficient now | N/A | N/A | Any training data or model run | Critical | Prohibited now. |
| Model-output evidence proposal before integration approval | prohibited/later-stage | No | No | Separate model-output and evaluation approval required | None sufficient now | N/A | N/A | Any model-output path or evidence claim | Critical | Prohibited now. |
| Self-play / league proposal | prohibited/later-stage | No | No | P8-P10 approval required | None sufficient now | N/A | N/A | Any self-play or league behavior | Critical | P7 cannot approve this. |
| P8 RL implementation proposal under P7 | prohibited/later-stage | No | No | P8 scope / entry approval required | None sufficient now | N/A | N/A | Any P8-P12 work | Critical | Stage jump. |

## Minimal Proposal Required Sections

A future broader P7 minimal implementation proposal must include all sections
below before it can be reviewed:

1. Proposal id and linked boundary documents.
2. Exact objective and north-star contribution.
3. Candidate proposal class from this document.
4. Current approval status, explicitly `not approved for execution` unless a
   separate approval decision exists.
5. Exact file paths proposed for edit or creation.
6. Exact functions, dataclasses, helpers or schemas proposed, if any.
7. Exact fixtures, tests or docs proposed, if any.
8. Allowed inputs and forbidden inputs.
9. Explicit output shape and non-output claims.
10. Source dependency status.
11. Parser / reader / ingestion dependency status.
12. Feature / label dependency status.
13. Dataset / split / leakage dependency status.
14. Training-data and training-run dependency status.
15. Model / trainer dependency status.
16. Evaluation and evidence dependency status.
17. Validation commands.
18. Rollback plan.
19. Risk controls and stop conditions.
20. Evidence log, risk register and decision record updates required.
21. Explicit non-evidence warning.
22. Next review gate and required approval gate.

Missing any section is a blocker for approval review.

## Exact-Scope Requirements

A future proposal must name exact paths before approval. It must distinguish
between files it may edit, files it may read, files it must not touch, and
files that are only referenced as context.

The exact-scope block must include:

- exact module paths, if any;
- exact test paths, if any;
- exact fixture paths, if any;
- exact docs / governance paths;
- exact public APIs or helpers, if any;
- exact input mappings and output mappings;
- exact validation commands;
- exact rollback command or manual revert plan;
- explicit excluded directories, data sources and claims.

Naming a file in a proposal boundary does not approve editing that file.
Naming a function in a proposal boundary does not approve implementation.
Naming validation commands does not approve adding tests or code.

## Forbidden Proposal Scope

A future proposal under this boundary must not include:

- broad file ingestion;
- arbitrary-path readers;
- CLI data ingestion;
- real Tenhou logs;
- real haifu ingestion;
- external logs;
- platform data;
- account/session data;
- scraped data;
- platform automation;
- third-party binaries;
- Akochan `system.exe` or `libai.so` execution;
- unknown model checkpoints, `*.pth`, `*.pt`, `checkpoint` or `snapshot`
  files;
- model-output integration;
- feature extraction from real sources;
- label generation from real sources;
- supervised dataset construction from real sources;
- training-data approval;
- training-run approval;
- training;
- model architecture implementation;
- trainer implementation;
- evaluation runner or benchmark harness;
- model-strength claims;
- Tenhou ranked evidence;
- stable-dan ranked-game evidence;
- LuckyJ `10.68` comparison;
- candidate promotion;
- self-play;
- league;
- P8-P12 work.

If any of these appear in a future proposal, the proposal review must stop.

## Future Approval Decision Separation

The required sequence is:

1. Boundary definition.
2. Boundary review.
3. Proposal draft.
4. Proposal review.
5. Separate approval decision.
6. Exact implementation execution, if approved.
7. Implementation review.
8. Current-scope acceptance decision, if warranted.

This document only completes step 1 for the broader P7 minimal implementation
proposal boundary. It does not approve steps 3-8.

## Future Proposal Approval Decision Prerequisites

A future approval decision must verify:

- the proposal class is allowed and not prohibited;
- exact files are named;
- exact non-goals are named;
- all upstream dependency statuses are explicit;
- there is no implied source approval;
- there is no implied parser / reader / ingestion approval;
- there is no implied feature extraction or label generation approval beyond
  the exact proposal;
- there is no implied dataset, split, leakage, training data, training run,
  model, trainer or evaluation approval;
- validation commands are local and safe;
- rollback is possible;
- evidence log, risk register and decision record entries are planned;
- non-evidence wording is explicit;
- stop conditions are enforceable.

## Stop Conditions

Stop before drafting, approval or execution if:

- a proposal omits exact files;
- a proposal omits validation commands;
- a proposal depends on real data or external logs;
- a proposal implies source approval;
- a proposal implies parser / reader / ingestion approval without an upstream
  approval artifact;
- a proposal creates training data;
- a proposal runs training;
- a proposal touches model architecture, trainer, checkpoints or weights;
- a proposal evaluates model strength;
- a proposal connects to Tenhou or platform data;
- a proposal requires a CLI or broad file ingestion;
- a proposal uses third-party binaries or unknown artifacts;
- a proposal makes LuckyJ, stable-dan, Tenhou or candidate-promotion claims;
- a proposal drifts into P8-P12.

## Risk Controls

| Risk | Control |
| --- | --- |
| Proposal boundary is mistaken for approval. | Every section states that this document does not approve proposals or execution. |
| Exact file names are mistaken for edit permission. | Exact-scope section says named files require later approval before edits. |
| Synthetic smoke artifacts are mistaken for training data. | Evidence wording separates smoke evidence from dataset / training-data approval. |
| Validation commands are mistaken for test-creation approval. | Validation section only names future required checks and current safe checks. |
| Candidate classes are mistaken for approved implementation classes. | Matrix has `Approved now = No` for every class. |
| Real-data work sneaks into P7 boundary tasks. | Forbidden scope and stop conditions block real Tenhou, haifu, external logs and platform data. |
| Strength claims appear too early. | Non-evidence warning blocks Tenhou, stable-dan, LuckyJ and candidate-promotion claims. |
| Stage jump into P8-P12. | P8-P12 items are classified as prohibited/later-stage. |

## Evidence Requirements

A future proposal or approval record must include an evidence record with these
fields:

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

## Current Proposal-Boundary Decision

Broader P7 minimal implementation proposal boundary is defined, but no
proposal is approved and no broader P7 implementation is approved.

The next safe step is a docs-only review of this proposal-boundary definition.

## First Task Candidate

```text
Review broader P7 minimal implementation proposal boundary after readiness checklist review.
```

This candidate is a docs-only review gate. It must not approve a proposal,
approve broader P7 implementation, add code, add tests, add fixtures, add data
files, approve source ingestion, implement parser / reader / ingestion,
implement feature extraction, implement label generation, build a dataset,
train, evaluate model strength, connect model output, connect Tenhou, run
self-play, run league or enter P8-P12.

## Planning Decision

Broader P7 may now define the minimal implementation proposal boundary after
the readiness checklist review, but this boundary does not approve a proposal
or implementation. Any later proposal, review, approval decision,
implementation, review of implementation and acceptance must be separate
tasks.

## Evidence Grade

This document is broader P7 minimal implementation proposal-boundary
definition evidence only.

It is not:

- a minimal implementation proposal;
- proposal approval;
- broader P7 implementation approval;
- source approval;
- source ingestion approval;
- parser / reader / ingestion approval;
- feature extraction approval;
- label generation approval;
- dataset construction approval;
- training-data approval;
- training-run approval;
- training evidence;
- model architecture approval;
- trainer approval;
- evaluation implementation approval;
- model-output integration evidence;
- model-strength evidence;
- Tenhou ranked evidence;
- stable-dan ranked-game evidence;
- LuckyJ `10.68` comparison;
- candidate-promotion evidence;
- self-play evidence;
- league evidence;
- P8-P12 evidence.
