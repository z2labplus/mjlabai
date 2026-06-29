# 03AI Broader P7 Training-Data Approval And Training-Run Boundary Before Implementation

## Scope

This document defines the broader P7 training-data approval and training-run
boundary before implementation.

It is docs-only boundary definition evidence. It is not training-data
approval, training-run approval, training, training-data construction,
supervised dataset construction, split creation, leakage-test implementation,
source approval, source ingestion, parser / reader / ingestion, actual feature
extraction, actual label generation, model architecture / trainer
implementation, model-output integration or P8-P12 entry. It produces no
model-strength evidence.

## Purpose

The north-star target is a Japanese riichi mahjong AI whose long-term Tenhou
stable dan exceeds LuckyJ `10.68`. P7 supervised learning can only help that
target if future training data and future training runs are approved through
separate, auditable gates instead of inferred from source, parser, feature,
label, dataset, split or leakage planning.

This document defines:

- future broader P7 training-data approval concepts and boundaries.
- future broader P7 training-run approval concepts and boundaries.
- the distinction between training data, training-data construction,
  training-data approval, training run, training-run approval, training
  evidence and model-strength evidence.
- future training-data approval prerequisites.
- future training-run approval prerequisites.
- future training-data approval record fields.
- future training-run approval record fields.
- allowed and forbidden future behavior.
- stop conditions.
- risk controls.
- evidence requirements.

It prevents two failure modes: treating dataset boundary work as permission to
train, and treating a training run as model-strength or LuckyJ-comparison
evidence.

## Current Training-Data / Training-Run Status

Current broader P7 status:

- No training data is approved.
- No training-data construction is approved.
- No training-data source is approved.
- No training run is approved.
- No training implementation is approved.
- No model architecture is approved.
- No dataloader, optimizer, loss or trainer is approved.
- No checkpoint, weights or snapshot is approved.
- No source is approved for P7 training.
- No source ingestion is approved.
- No parser / reader / ingestion is approved.
- No actual feature extraction is approved.
- No actual label generation is approved.
- No supervised dataset construction is approved.
- No split creation is approved.
- No leakage-test implementation is approved.
- No model-output integration is approved.
- No P8-P12 work is approved.

Current smoke artifacts remain non-training artifacts:

- `tests/fixtures/supervised/synthetic_supervised_smoke.json` is a
  project-authored synthetic/local smoke artifact only. It is not training
  data.
- `src/mjlabai/supervised/feature_label_schema.py` validates in-memory
  synthetic/local smoke mappings only. It does not extract features, generate
  labels, build a dataset or train.
- Repository docs are governance context, not training data.
- The P6 synthetic replay fixture is not P7 training data.
- The P7 synthetic feature-label smoke fixture is a smoke artifact only.

## Concept Definitions

`training data`:
Approved data that a training run may consume. It must come from approved
dataset artifacts and must carry source, parser, feature, label, split,
leakage and storage approvals. No training data is approved now.

`training-data construction`:
The future process that prepares training-ready records, manifests or files
from approved supervised dataset artifacts. It remains unapproved.

`training-data approval`:
A future explicit decision that named dataset artifacts may be used for
specified training purposes under specified constraints. It is not training
approval and is not model-strength evidence.

`training-data source`:
A source or dataset artifact proposed for training use. No training-data
source is approved now.

`supervised dataset`:
A collection of approved supervised examples, manifests and split metadata.
No supervised dataset exists or is approved now.

`supervised dataset approval`:
A separate future decision that constructed dataset artifacts satisfy their
schema, source, feature, label, split and leakage constraints. It does not
substitute for training-data approval.

`split approval`:
A future decision that train / validation / test membership and grouping
policy are acceptable. It does not approve training.

`leakage validation`:
A future validation result or report about hidden, future, target, label,
source, duplicate, same-game, temporal or other leakage categories. It does
not approve training by itself.

`training run`:
A future execution of approved training code with approved training data,
model architecture, dataloader, optimizer, loss, trainer, configuration,
runtime and artifact policy. No training run is approved now.

`training-run approval`:
A future explicit decision that a specific training run may execute. It
requires training-data approval and model/trainer approval. It is not model
strength, Tenhou evidence or LuckyJ comparison.

`training configuration`:
The exact configuration for a future training run, including data references,
model settings, loss, optimizer, seeds, runtime, output policy and validation
commands.

`model architecture`:
The future model structure to train. No architecture is approved now.

`dataloader`:
Future code that feeds approved training data to a trainer. No dataloader is
approved now.

`optimizer`:
Future optimization algorithm and configuration. No optimizer is approved now.

`loss`:
Future supervised objective. No loss is approved now.

`trainer`:
Future training orchestration code. No trainer is approved now.

`checkpoint`:
Future saved training state or model snapshot. No checkpoint is approved now.

`weights`:
Future trained model parameters. No weights are approved now.

`training evidence`:
Evidence that a training run executed according to approval. It may include
logs, configs, checksums and validation outputs. It is not model-strength
evidence by itself.

`engineering training evidence`:
Evidence that training infrastructure executed or reproduced mechanically. It
does not prove policy quality.

`offline evaluation evidence`:
Evidence from approved evaluation tasks after training. It is separate from
training-run evidence.

`model-strength evidence`:
Evidence that a model is stronger under approved evaluation criteria. A
training run alone is not this evidence.

`candidate promotion evidence`:
Evidence that a candidate can move through the racing funnel. It requires
approved evaluation gates and cannot be inferred from training execution.

These concepts cannot substitute for each other.

## Dependency Map

Future broader P7 training-data approval and training-run approval must follow
this order:

```text
source readiness
-> source-specific approval
-> parser / reader / ingestion approval
-> actual feature extraction approval
-> actual label generation approval
-> supervised dataset construction approval
-> split / leakage approval
-> training-data approval boundary
-> training-data approval proposal
-> training-data approval decision
-> model architecture / trainer boundary
-> training-run boundary
-> training-run approval proposal
-> training-run approval decision
-> exact training implementation
-> training-run review
-> offline evaluation
-> later-stage transition review
```

If any required predecessor is missing, training data or a training run must
not be approved.

## Training-Data Approval Boundary

Future training-data approval may be considered only after separate proposal,
approval decision and exact first unchecked `10_NEXT` scope.

Future training-data approval rules:

- Training data may only come from approved supervised dataset artifacts.
- The supervised dataset must have source approvals.
- The supervised dataset must have parser / reader / ingestion approvals.
- The supervised dataset must have approved feature outputs.
- The supervised dataset must have approved label outputs.
- The supervised dataset must have approved split / leakage policy.
- Training-data approval must reference exact dataset id and manifest id.
- Training-data approval must define allowed model/training use.
- Training-data approval must define forbidden use.
- Training-data approval must define storage and retention policy.
- Training-data approval must define whether artifacts may enter git.
- Training-data approval must stop before any training-run approval.
- Training-data approval is not training approval.
- Training-data approval is not model-strength evidence.

This document grants none of those approvals.

## Training-Run Boundary

Future training-run approval may be considered only after training-data
approval, model/trainer planning boundary, proposal, approval decision and
exact first unchecked `10_NEXT` scope.

Future training-run rules:

- A training run requires training-data approval.
- A training run requires model architecture / trainer planning boundary and
  approval.
- A training run requires exact configuration.
- A training run requires exact code and file approval.
- A training run requires deterministic or recorded randomness policy.
- A training run requires validation commands.
- A training run requires artifact storage policy.
- A training run requires checkpoint / weights policy.
- A training run requires evaluation dependency plan.
- A training run must not claim model strength by itself.
- A training run must stop before P8 / P10 / P12 evidence claims.
- Training-run approval is not P8 approval.
- Training-run approval is not Tenhou evidence.
- Training-run approval is not LuckyJ comparison.

This document approves no training run.

## Future Training-Data Approval Record Fields

A future training-data approval record must include at least:

- `approval_id`.
- `dataset_id`.
- `dataset_manifest_id`.
- `source_ids`.
- source approval references.
- parser / reader / ingestion approval references.
- feature extraction approval references.
- label generation approval references.
- dataset construction approval reference.
- split / leakage approval reference.
- dataset schema version.
- feature schema versions.
- label schema versions.
- split policy id.
- leakage validation status.
- allowed training use.
- forbidden use.
- storage policy.
- retention policy.
- `may_enter_git`.
- privacy / platform terms status.
- evidence log reference.
- risk register reference.
- decision record reference.
- validation commands.
- known exclusions.
- stop conditions.
- human / Web ChatGPT approval reference.
- explicit first unchecked `10_NEXT` training-data approval task requirement.

## Future Training-Run Approval Record Fields

A future training-run approval record must include at least:

- `training_run_approval_id`.
- `training_data_approval_id`.
- `model_architecture_id`.
- `model_config_id`.
- `trainer_id`.
- `dataloader_id`.
- `optimizer_id`.
- `loss_id`.
- random seed policy.
- hardware / runtime policy.
- dependency versions.
- exact implementation files.
- allowed outputs.
- forbidden outputs.
- checkpoint / weights policy.
- artifact storage policy.
- evaluation dependency plan.
- validation commands.
- evidence log reference.
- risk register reference.
- decision record reference.
- rollback plan.
- stop conditions.
- human / Web ChatGPT approval reference.
- explicit first unchecked `10_NEXT` training-run task requirement.

## Candidate Training-Data / Training-Run Classes

| candidate_class | current_status | approved_now | source_dependency | dataset_dependency | model_dependency | implementation_approval_required | allowed_for_docs_planning | forbidden_until | risk | notes |
|---|---|---:|---|---|---|---:|---:|---|---|---|
| Project-authored synthetic/local training-data-shape smoke | Candidate only | No | Explicit synthetic/local boundary | Synthetic shape artifact only | None | Yes | Yes | Exact proposal and approval decision | Medium | Must never be treated as meaningful training data. |
| Approved-source-only training-data manifest approval | Candidate only | No | Source-specific approval | Approved dataset / split / leakage artifacts | None | Yes | Yes | Source, parser, feature, label, dataset, split and leakage approvals | High | Must reference exact dataset and manifest ids. |
| Approved-source-only training-run dry-run planning | Candidate only | No | Training-data approval | Approved training data | Model/trainer boundary | Yes | Yes | Training-data approval and model/trainer approval | High | Planning only until exact training-run approval. |
| Model-free training config validator | Candidate only | No | None or approved synthetic/local config | None | No model execution | Yes | Yes | Exact proposal and no-training guardrails | Medium | May validate config shape only if separately approved. |
| Training evidence envelope draft | Candidate only | No | Depends on approved training run plan | Depends on training-data approval | Depends on model/trainer plan | Yes | Yes | Training-run approval boundary and proposal | Medium | Evidence envelope only, not strength evidence. |
| Real-data training before source/dataset/training approval | Rejected | No | Missing | Missing | Missing | Not eligible | No | Never without source, dataset, training-data and training-run approvals | Very High | Forbidden. |
| Model-output training data before model-output policy | Rejected | No | Model-output policy missing | Missing | Model-output dependency | Not eligible | No | Later explicit model-output policy and approvals | High | Forbidden now. |
| Self-play / league training data before later-stage approval | Rejected | No | P8/P10 approvals missing | Missing | Later-stage dependency | Not eligible | No | P8/P10 approvals | High | Not P7 boundary work. |
| Arbitrary checkpoint / weights training run | Rejected | No | Unknown | Unknown | Unknown checkpoint/weights | Not eligible | No | Never without provenance and approval | Very High | Forbidden artifact path. |
| Third-party artifact training run | Rejected | No | Unknown or third-party | Unknown | Third-party binary/weights | Not eligible | No | Rights/provenance review and explicit approval | Very High | Forbidden now. |
| P8 RL training under P7 | Rejected | No | P8 not approved | Not applicable | RL model/trainer | Not eligible | No | P8 transition and approval | Very High | P7 cannot approve P8 work. |

## Allowed Future Boundary

Future work may be considered only after a separate proposal, approval decision
and first unchecked `10_NEXT` task. Allowed future work must be exactly one of:

- docs-only training-data approval record draft.
- docs-only training-run approval record draft.
- project-authored synthetic/local training-data-shape smoke.
- approved-source-only training-data approval decision.
- approved-source-only training-run approval decision.
- model-free validator.

Future work must:

- be exact-file scoped.
- use only approved dataset artifacts.
- require training-data approval before training-run approval.
- require model/trainer approval before a training run.
- preserve source / feature / label / dataset / split provenance.
- preserve evidence and risk references.
- avoid raw real data unless explicitly approved.
- avoid account, session, cookie and token content.
- avoid model-output, self-play and league data unless later approved.
- stop before model-strength claims.
- stop before P8-P12.

## Forbidden Training-Data / Training-Run Scope

The following remain forbidden now:

- training-data approval implementation.
- training-data construction.
- training-run implementation.
- model architecture implementation.
- dataloader implementation.
- optimizer / loss / trainer implementation.
- checkpoint / weights creation.
- arbitrary training data.
- real-data training without approvals.
- training from repository docs.
- training from smoke fixtures.
- training from the P6 synthetic replay fixture.
- training from the P7 synthetic feature-label smoke fixture.
- model-output training data.
- self-play / league training data.
- third-party binaries, weights, params or checkpoints.
- claims that a training run equals model strength.
- P8-P12 entry.

## Stop Conditions

Stop before commit if any of these appear:

- unapproved source.
- unapproved dataset.
- unapproved feature or label outputs.
- unapproved split / leakage policy.
- training data constructed without approval.
- training behavior without approval.
- model architecture / trainer without approval.
- checkpoint / weights created without approval.
- real data without approval.
- model-output, self-play or league data.
- account, session, cookie or token content.
- third-party binary or weights requirement.
- validation failure.
- evidence overclaim.
- P8-P12 drift.

## Risk Controls

| Risk | Control | Status |
|---|---|---|
| Training-data boundary is mistaken for training-data approval. | State that this is docs-only boundary definition and requires a later explicit approval decision. | Open |
| Training-data approval is mistaken for training-run approval. | Keep approval records separate and require a training-data approval id before training-run approval. | Open |
| Training run is mistaken for model-strength evidence. | Classify training-run evidence as execution evidence only until approved evaluation exists. | Open |
| Smoke fixtures are mistaken as training data. | Reaffirm synthetic/local smoke artifacts are not training data. | Open |
| Docs context is mistaken as training data. | Mark repository docs as governance context only. | Open |
| Synthetic data overfit / meaningless signal risk. | Require explicit warnings and prevent synthetic smoke from supporting strength claims. | Open |
| Source approval gap. | Require source approval references before training-data approval. | Open |
| Dataset leakage gap. | Require dataset, split and leakage approval references before training-data approval. | Open |
| Split leakage gap. | Require split policy id and leakage validation status. | Open |
| Feature / label leakage gap. | Require feature and label approval references and leakage status. | Open |
| Model-output data enters too early. | Keep model-output data rejected until a later model-output policy exists. | Open |
| Self-play / league data enters too early. | Keep self-play and league data rejected until later-stage approval. | Open |
| Third-party artifact creep. | Forbid third-party binaries, weights, params and checkpoints without explicit review. | Open |
| Checkpoint / weights provenance risk. | Require checkpoint / weights policy and provenance before any training run. | Open |
| Training creep. | Stop if training behavior appears before approval. | Open |
| P8-P12 creep. | Require separate transition reviews and first-task approvals. | Open |
| Model-strength overclaim. | Evidence grade is boundary definition only and explicit non-evidence is listed below. | Open |

## Evidence Requirements

Future training-data / training-run evidence must record:

- `approval_id`.
- `component_type`.
- `source_ids`.
- `dataset_id`.
- `dataset_approval_status`.
- `training_data_approval_status`.
- `training_run_approval_status`.
- `model_architecture_status`.
- `trainer_status`.
- exact files.
- `config_id`.
- random seed policy.
- validation commands.
- artifact policy.
- checkpoint policy.
- evaluation dependency status.
- evidence log reference.
- risk register reference.
- decision record reference.
- known exclusions.
- explicit non-evidence warning.

For this docs-only task, evidence is limited to documentation consistency and
existing synthetic/local schema tests.

## First Task Candidate

The next safe task is:

```text
Review broader P7 training-data approval and training-run boundary before implementation.
```

That next task must be docs-only. It must not approve training data, construct
training data, approve a training run, train, implement model architecture,
implement a trainer, create checkpoints or weights, approve source ingestion,
implement parser / reader / ingestion, implement feature extraction or label
generation, build supervised datasets, create splits, implement leakage tests
or enter P8-P12.

## Planning Decision

```text
Broader P7 training-data approval and training-run boundary is defined before implementation. This does not approve training data, training-data construction, training-run approval, training, source approval, source ingestion, parser, dataset reader, ingestion, actual feature extraction, actual label generation, supervised dataset construction, split creation, leakage-test implementation, model architecture, trainer, checkpoint, weights, model-output integration, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
Broader P7 training-data approval and training-run boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not:

- training-data approval.
- training-data construction.
- training-run approval.
- training.
- model architecture.
- dataloader.
- optimizer.
- loss.
- trainer.
- checkpoint.
- weights.
- source approval.
- source ingestion.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- split creation.
- leakage-test implementation.
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
- candidate-promotion evidence.
