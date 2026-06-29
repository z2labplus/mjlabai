# 03AK Broader P7 Model Architecture And Trainer Planning Boundary Before Implementation

## Scope

This document defines the broader P7 model architecture and trainer planning
boundary before implementation.

It is docs-only boundary definition evidence. It is not model architecture
approval, trainer approval, dataloader approval, optimizer approval, loss
approval, checkpoint approval, weights approval, snapshot approval,
training-data approval, training-run approval, training, source approval,
source ingestion, parser / reader / ingestion, actual feature extraction,
actual label generation, supervised dataset construction, model-output
integration, self-play, league or P8-P12 entry. It produces no model-strength
evidence.

## Purpose

The north-star target is a Japanese riichi mahjong AI whose long-term Tenhou
stable dan exceeds LuckyJ `10.68`. Model architecture and trainer planning can
help that target only if it remains downstream of approved data, feature,
label, dataset, training-data and training-run gates.

This document defines:

- broader P7 model architecture planning boundary.
- broader P7 trainer planning boundary.
- the distinction between model architecture, model config, decision heads,
  dataloader, optimizer, loss, trainer, checkpoint, weights, training run,
  training evidence, engineering training evidence, offline evaluation
  evidence, model-strength evidence and candidate-promotion evidence.
- the dependency relationship between source approval, parser / reader /
  ingestion, feature / label approval, dataset construction, training-data
  approval, model/trainer approval and training-run approval.
- future model architecture approval record fields.
- future trainer approval record fields.
- allowed and forbidden future behavior.
- stop conditions.
- risk controls.
- evidence requirements.

It prevents three failure modes: treating planning as implementation approval,
treating a trainer plan as permission to train, and treating any model/trainer
artifact as Tenhou, stable-dan, LuckyJ-comparison or candidate-promotion
evidence.

## Current Model Architecture / Trainer Status

Current broader P7 status:

- No model architecture is approved.
- No model config is approved.
- No encoder is approved.
- No policy head is approved.
- No value head is approved.
- No auxiliary head is approved.
- No decision head is approved.
- No dataloader is approved.
- No optimizer is approved.
- No loss is approved.
- No trainer is approved.
- No training loop is approved.
- No training run is approved.
- No training is approved.
- No checkpoint is approved.
- No weights are approved.
- No snapshot is approved.
- No source is approved for P7 training.
- No training data is approved.
- No supervised dataset is approved.
- No parser / reader / ingestion is approved.
- No actual feature extraction is approved.
- No actual label generation is approved.
- No model-output integration is approved.
- No P8-P12 work is approved.

Current smoke artifacts remain non-training and non-model artifacts:

- `tests/fixtures/supervised/synthetic_supervised_smoke.json` is a
  project-authored synthetic/local smoke artifact only. It is not training
  data and not model input data.
- `src/mjlabai/supervised/feature_label_schema.py` validates in-memory
  synthetic/local smoke mappings only. It does not extract features, generate
  labels, build a dataset, define an architecture or train.
- Repository docs are governance context, not a training dataset.
- The P6 synthetic replay fixture is not P7 training data.
- The P7 synthetic feature-label smoke fixture is a smoke artifact only.

## Concept Definitions

`model architecture`:
A future trainable model structure, including encoders, heads, masking
interfaces and output conventions. No architecture is approved now.

`model config`:
A future explicit configuration that names architecture id, feature schema
compatibility, heads, dimensions, regularization, initialization and runtime
constraints. No model config is approved now.

`encoder`:
The future module family that maps approved feature inputs into hidden
representations. No encoder is approved now.

`policy head`:
A future output head for supervised action prediction. It cannot be approved
until feature, label, decision-head, training-data and model architecture
approval gates exist.

`value head`:
A future output head for value, rank, point or outcome estimates. It is not
approved now and cannot create model-strength evidence by itself.

`auxiliary head`:
A future helper output head such as danger, riichi, call, shape or other
diagnostic objectives. It is not approved now.

`decision head`:
A future head associated with a specific decision family, such as discard,
riichi, call, kan or win/abort. No decision head is approved now.

`dataloader`:
Future code that feeds approved training data to a trainer. No dataloader is
approved now.

`optimizer`:
Future optimization algorithm and configuration. No optimizer is approved now.

`loss`:
Future supervised objective or weighted objective bundle. No loss is approved
now.

`trainer`:
Future training orchestration code. It may coordinate data loading, forward
passes, losses, optimization, validation, checkpoints and logs only after
separate approval. No trainer is approved now.

`training loop`:
Future executable training behavior. No training loop is approved now.

`checkpoint`:
Future saved training state. No checkpoint is approved now.

`weights`:
Future trained or initialized model parameters. No weights are approved now.

`snapshot`:
Future model, trainer or run-state artifact captured for later use. No
snapshot is approved now.

`model artifact`:
Any saved architecture config, checkpoint, weights, snapshot, exported model
or derived artifact. No model artifact is approved now.

`training run`:
A future execution of approved training code with approved training data,
model architecture, dataloader, optimizer, loss, trainer, configuration and
artifact policy. No training run is approved now.

`training-run approval`:
A future explicit decision that a specific training run may execute. It is not
model-strength evidence.

`training evidence`:
Evidence that a training run executed according to approval. It does not prove
policy quality or Tenhou strength.

`engineering training evidence`:
Evidence that training infrastructure behaved mechanically as expected. It is
not model-strength evidence.

`offline evaluation evidence`:
Evidence from approved evaluation tasks after training. It is separate from
architecture/trainer planning and from training-run execution.

`model-strength evidence`:
Evidence that a model is stronger under approved evaluation criteria. No
model-strength evidence is produced by this document.

`candidate promotion evidence`:
Evidence that a candidate can move through the racing funnel. It requires
approved evaluation gates and cannot be inferred from model/trainer planning.

These concepts cannot substitute for each other.

## Dependency Map

Future broader P7 model architecture / trainer work must follow this order:

```text
source approval
-> parser / reader / ingestion approval
-> actual feature extraction approval
-> actual label generation approval
-> supervised dataset construction approval
-> split / leakage approval
-> training-data approval
-> model architecture / trainer planning boundary
-> model architecture / trainer approval proposal
-> model architecture / trainer approval decision
-> exact implementation files
-> model / trainer implementation
-> implementation review
-> training-run approval
-> training-run execution
-> training-run review
-> offline evaluation
-> later-stage transition review
```

If any required predecessor is missing, model architecture implementation,
trainer implementation, dataloader, optimizer, loss, checkpoint creation,
weights creation and training must not be approved.

## Model Architecture Planning Boundary

Future model architecture planning may be considered only after separate
proposal, approval decision and exact first unchecked `10_NEXT` scope.

Future model architecture planning rules:

- Candidate model families may be documented as planning candidates only.
- Planning may reference `03A_MODEL_ARCHITECTURE.md`,
  `03C_KEY_DECISION_HEADS.md` and later approved feature/label/schema docs.
- Planning does not approve architecture implementation.
- Planning does not approve model config implementation.
- Planning does not approve training.
- Planning does not approve checkpoints, weights, snapshots or exported
  models.
- Planning does not provide model-strength evidence.
- Future implementation requires exact files, approval decision and explicit
  `10_NEXT` task.
- Future implementation must depend on approved training data and the
  training-run boundary.
- Future architecture must define input schema compatibility before code.
- Future architecture must define output heads only after decision-head
  boundary approval.
- Future architecture must define artifact policy before checkpoint creation.
- The current task defines the boundary only.

This document approves no model architecture.

## Trainer Planning Boundary

Future trainer planning may be considered only after separate proposal,
approval decision and exact first unchecked `10_NEXT` scope.

Future trainer planning rules:

- Candidate trainer components may be documented as planning candidates only.
- Planning may identify dataloader, optimizer, loss, validation, logging and
  artifact-policy concepts.
- Planning does not approve dataloader implementation.
- Planning does not approve optimizer implementation.
- Planning does not approve loss implementation.
- Planning does not approve training-loop implementation.
- Planning does not approve checkpoint or weights creation.
- Planning does not approve training.
- Future trainer implementation requires approved training data and approved
  model architecture.
- Future trainer planning must define randomness, artifact, evaluation and
  validation boundaries.
- Future trainer planning must stop before model-strength claims.
- The current task defines the boundary only.

This document approves no trainer.

## Future Model Architecture Approval Record Fields

A future model architecture approval record must include at least:

- `model_architecture_approval_id`.
- `model_architecture_id`.
- `model_config_id`.
- architecture family.
- encoder family.
- policy head ids.
- value head ids.
- auxiliary head ids.
- decision head ids.
- input feature schema ids.
- label schema ids.
- legal-action mask interface status.
- feature compatibility status.
- label compatibility status.
- training-data approval dependency.
- trainer approval dependency.
- training-run approval dependency.
- exact implementation files.
- allowed outputs.
- forbidden outputs.
- checkpoint / weights policy.
- artifact storage policy.
- validation commands.
- evidence log reference.
- risk register reference.
- decision record reference.
- known exclusions.
- stop conditions.
- human / Web ChatGPT approval reference.
- explicit first unchecked `10_NEXT` model-architecture task requirement.

## Future Trainer Approval Record Fields

A future trainer approval record must include at least:

- `trainer_approval_id`.
- `trainer_id`.
- `model_architecture_approval_id`.
- `training_data_approval_id`.
- dataloader id.
- optimizer id.
- loss id.
- training loop id.
- validation plan id.
- logging policy.
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
- known exclusions.
- stop conditions.
- human / Web ChatGPT approval reference.
- explicit first unchecked `10_NEXT` trainer task requirement.

## Candidate Model / Trainer Classes

| candidate_class | current_status | approved_now | training_data_dependency | model_dependency | implementation_approval_required | allowed_for_docs_planning | forbidden_until | risk | notes |
|---|---|---:|---|---|---:|---:|---|---|---|
| Docs-only model architecture record draft | Candidate only | No | None | None | Yes | Yes | Separate approval decision and exact `10_NEXT` task | Medium | May define fields only. |
| Docs-only trainer approval record draft | Candidate only | No | None | Model architecture approval boundary | Yes | Yes | Separate approval decision and exact `10_NEXT` task | Medium | May define fields only. |
| Model-free config validator | Candidate only | No | None or approved synthetic/local config | No model execution | Yes | Yes | Exact proposal and no-training guardrails | Medium | May validate config shape only if separately approved. |
| Synthetic/local model-config smoke | Candidate only | No | Project-authored synthetic/local config only | No trainable model | Yes | Yes | Exact proposal and approval decision | Medium | Must not create checkpoint or weights. |
| Tiny model architecture smoke | Candidate only | No | Approved synthetic/local shape only | Approved model architecture implementation task | Yes | Yes | Model architecture approval decision | Medium-High | Must not train or claim strength. |
| Dataloader-shape validator | Candidate only | No | Approved training-data shape only | None | Yes | Yes | Training-data approval and dataloader proposal | High | Shape validation only if approved later. |
| Optimizer/loss config validator | Candidate only | No | None | Approved trainer planning | Yes | Yes | Trainer approval decision | Medium | Config validation only, no training step. |
| Checkpoint policy validator | Candidate only | No | None | Approved artifact policy | Yes | Yes | Checkpoint policy approval | Medium | Must not create or load checkpoints. |
| Rejected real training model architecture implementation | Rejected | No | Missing approved training data | Trainable model | Not eligible | No | Source, dataset, training-data and architecture approvals | Very High | Forbidden now. |
| Rejected real trainer implementation | Rejected | No | Missing approved training data | Missing approved model | Not eligible | No | Training-data, model and trainer approvals | Very High | Forbidden now. |
| Rejected arbitrary checkpoint/weights usage | Rejected | No | Unknown | Unknown checkpoint/weights | Not eligible | No | Never without provenance and approval | Very High | Forbidden artifact path. |
| Rejected third-party artifact/binary usage | Rejected | No | Unknown or third-party | Third-party binary/weights | Not eligible | No | Rights/provenance review and explicit approval | Very High | Forbidden now. |
| Rejected model-output integration | Rejected | No | Model-output policy missing | Model output dependency | Not eligible | No | Later explicit model-output policy and approvals | High | Forbidden now. |
| Rejected P8 RL policy architecture under P7 | Rejected | No | P8 not approved | RL policy dependency | Not eligible | No | P8 transition and approval | Very High | P7 cannot approve P8 work. |

## Allowed Future Boundary

Future work may be considered only after a separate proposal, approval
decision and first unchecked `10_NEXT` task. Allowed future work must be
exactly one of:

- docs-only model architecture approval record draft.
- docs-only trainer approval record draft.
- docs-only decision-head compatibility review.
- model-free config schema planning.
- project-authored synthetic/local model-config shape smoke.
- project-authored synthetic/local trainer-config shape smoke.
- approved-source-only model architecture proposal.
- approved-source-only trainer proposal.

Future work must:

- be exact-file scoped.
- use only approved synthetic/local or approved training-data artifacts.
- require training-data approval before training-run approval.
- require model architecture approval before trainer approval can execute.
- require trainer approval before training-run approval can execute.
- preserve source / feature / label / dataset / split provenance.
- preserve evidence and risk references.
- avoid raw real data unless explicitly approved.
- avoid account, session, cookie and token content.
- avoid model-output, self-play and league data unless later approved.
- stop before checkpoint / weights creation unless explicitly approved.
- stop before model-strength claims.
- stop before P8-P12.

## Forbidden Model Architecture / Trainer Scope

The following remain forbidden now:

- model architecture implementation.
- model config implementation.
- encoder implementation.
- policy head implementation.
- value head implementation.
- auxiliary head implementation.
- decision head implementation.
- dataloader implementation.
- optimizer implementation.
- loss implementation.
- trainer implementation.
- training-loop implementation.
- checkpoint creation.
- weights creation.
- snapshot creation.
- model artifact creation.
- model artifact loading from unknown source.
- training-data approval.
- training-data construction.
- training-run approval.
- training.
- source approval.
- source ingestion.
- parser / reader / ingestion implementation.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- split creation.
- leakage-test implementation.
- real Tenhou, real haifu, external logs or platform data.
- repository docs as training data.
- smoke fixtures as training data.
- model-output integration.
- self-play or league integration.
- third-party binaries, weights, params or checkpoints.
- claims that architecture or trainer planning equals model strength.
- P8-P12 entry.

## Stop Conditions

Stop before commit if any of these appear:

- architecture implementation.
- trainer implementation.
- dataloader, optimizer or loss implementation.
- training-loop behavior.
- checkpoint, weights or snapshot creation.
- model artifact loading.
- training-data approval by implication.
- training-run approval by implication.
- training behavior.
- source approval or source ingestion by implication.
- parser / reader / ingestion behavior.
- actual feature extraction or actual label generation.
- dataset construction, split creation or leakage-check implementation.
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
| Model architecture planning is mistaken for architecture implementation approval. | State that this is docs-only boundary definition and requires a later explicit approval decision. | Open |
| Trainer planning is mistaken for permission to train. | Keep trainer approval, training-run approval and training separate. | Open |
| Dataloader / optimizer / loss planning drifts into implementation. | Forbid production code, tests, fixtures and exact training-loop behavior in this task. | Open |
| Checkpoint / weights policy is mistaken for artifact approval. | Forbid checkpoint, weights and snapshot creation or loading until separate approval. | Open |
| Synthetic/local smoke artifacts are mistaken as model input training data. | Reaffirm smoke fixtures are schema / guardrail smoke only. | Open |
| Docs context is mistaken as training data. | Mark repository docs as governance context only. | Open |
| Source, parser, feature, label, dataset or training-data approvals are inferred from model/trainer planning. | Preserve dependency order and explicit non-substitution wording. | Open |
| Real Tenhou, real haifu, external logs or platform data enter architecture/trainer planning. | Block real/external/platform data until source-specific and implementation approvals exist. | Open |
| Model-output data enters too early. | Keep model-output integration rejected until a later model-output policy exists. | Open |
| Self-play / league work enters too early. | Keep self-play and league rejected until later-stage approval. | Open |
| Third-party artifact creep. | Forbid third-party binaries, weights, params and checkpoints without explicit review. | Open |
| Model-strength overclaim. | Evidence grade is boundary definition only and explicit non-evidence is listed below. | Open |
| P8-P12 creep. | Require separate transition reviews and first-task approvals. | Open |

## Evidence Requirements

Future model architecture / trainer evidence must record:

- `approval_id`.
- `component_type`.
- `model_architecture_id`.
- `model_config_id`.
- `trainer_id`.
- `dataloader_id`.
- `optimizer_id`.
- `loss_id`.
- `training_data_approval_status`.
- `training_run_approval_status`.
- source approval status.
- parser / reader / ingestion approval status.
- feature extraction approval status.
- label generation approval status.
- supervised dataset approval status.
- split / leakage approval status.
- exact files.
- config ids.
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
Review broader P7 model architecture and trainer planning boundary before implementation.
```

That next task must be docs-only. It must not approve model architecture,
trainer, dataloader, optimizer, loss, checkpoint, weights, training data,
training-data construction, training-run approval, training, source approval,
source ingestion, parser / reader / ingestion, actual feature extraction,
actual label generation, supervised dataset construction, split creation,
leakage-test implementation, model-output integration, self-play, league or
P8-P12.

## Planning Decision

```text
Broader P7 model architecture and trainer planning boundary is defined before implementation. This does not approve model architecture implementation, trainer implementation, dataloader, optimizer, loss, checkpoint, weights, training-run approval, training, source approval, source ingestion, parser, dataset reader, ingestion, actual feature extraction, actual label generation, supervised dataset construction, model-output integration, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
Broader P7 model architecture and trainer planning boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not:

- model architecture approval.
- model architecture implementation.
- model config implementation.
- encoder implementation.
- policy head implementation.
- value head implementation.
- auxiliary head implementation.
- decision head implementation.
- trainer approval.
- dataloader.
- optimizer.
- loss.
- trainer.
- training loop.
- checkpoint.
- weights.
- snapshot.
- model artifact.
- training-data approval.
- training-data construction.
- training-run approval.
- training.
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
