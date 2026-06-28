# 03AE Broader P7 Feature And Label Boundary Before Implementation

## Scope

This document defines the broader P7 actual feature extraction and label
generation boundary before implementation.

This is a docs-only boundary definition. It is not:

- actual feature extraction implementation.
- actual label generation implementation.
- feature extraction approval.
- label generation approval.
- parser implementation.
- dataset reader implementation.
- ingestion implementation.
- source ingestion approval.
- source approval.
- training-data approval.
- supervised dataset construction.
- model input pipeline construction.
- model architecture, dataloader, optimizer, loss, trainer, checkpoint or
  weights approval.
- real-data use.
- real Tenhou use.
- real haifu use.
- external-log use.
- platform-data use.
- model-output integration.
- self-play.
- league.
- P8-P12 entry.

Boundary definition is not execution permission.

## Purpose

This document exists to define the auditable boundary that must exist before
any future broader P7 actual feature extraction or label generation task can be
considered.

It defines:

- feature extraction vocabulary.
- label generation vocabulary.
- the relationship between feature / label work and source approval, parser /
  reader / ingestion approval, supervised dataset construction and training.
- current feature / label status.
- candidate feature and label families for planning only.
- future approval prerequisites and approval-record fields.
- allowed and forbidden future behavior.
- leakage controls.
- stop conditions.
- evidence requirements and risk controls.

This supports the north-star target indirectly. A future supervised policy may
need lawful, reproducible, public-information-only feature inputs and correctly
separated labels before any later training can support RL, search, league and
Tenhou validation. This document does not generate data, train, evaluate a
model or provide model-strength evidence.

## Current Feature Label Status

Current broader P7 feature / label status:

- no actual feature extraction is approved.
- no actual label generation is approved.
- no source is approved for P7 training.
- no source ingestion is approved.
- no parser / reader / ingestion is approved.
- no broad file ingestion is approved.
- no CLI data path is approved.
- no supervised dataset construction is approved.
- no feature tensor, label, target, example, split or batch may be emitted.
- no model architecture, dataloader, optimizer, loss, trainer, checkpoint,
  weights or snapshot is approved.
- no real Tenhou, real haifu, external logs or platform data may be used.
- no account / session / cookie / token data may be used.
- no model-output, self-play or league output may be used.
- the accepted minimal synthetic/local supervised feature-label smoke helper
  is not training data and is not broader actual feature extraction or label
  generation approval.
- repository docs are planning context, not parseable training data.
- P6 synthetic replay fixtures and P7 smoke fixtures are synthetic/local smoke
  artifacts, not approved training sources.

## Concept Definitions

| concept | definition | approved now |
|---|---|---:|
| feature extraction boundary | The documented limit around future code or process that may produce feature values, feature vectors or tensors from approved decision records. | no |
| actual feature extraction | Producing concrete feature values, vectors, tensors, model inputs or derived feature records from source or normalized decision content. | no |
| feature family | A named planning category of possible feature inputs, such as visible hand, public discard history or decision-time score context. | docs-only planning |
| feature schema | A versioned description of feature fields, visibility, timing and provenance rules. | no broader implementation |
| label generation boundary | The documented limit around future code or process that may produce labels, targets or annotations from approved source content. | no |
| actual label generation | Producing concrete labels, targets, action annotations, value targets, imitation targets or pseudo-labels. | no |
| label family | A named planning category of possible labels, such as action imitation, discard choice or future value target. | docs-only planning |
| label schema | A versioned description of label fields, provenance, source, timing and leakage policy. | no broader implementation |
| feature tensor | Numeric or structured model input produced from features for supervised learning or diagnostics. | no |
| label target | A generated or stored target used for supervised learning or diagnostics. | no |
| supervised example | A paired feature / label record intended for training, validation, testing or diagnostics. | no |
| supervised split | Train / validation / test grouping or split assignment. | no |
| supervised dataset construction | Building examples, manifests, splits, batches or dataset artifacts intended for supervised training or evaluation. | no |
| source approval | Approval that a named source may be used under specific rights, privacy, storage and provenance constraints. It does not approve feature extraction or label generation. | no |
| parser / reader / ingestion approval | Approval that exact parser / reader / ingestion behavior and files may operate within a bounded source or synthetic/local scope. It does not approve feature extraction or label generation. | no |
| training-data approval | Approval that a source, derived data, feature / label products, splits and leakage controls may be used for training. | no |
| public information | Information available to the acting player at the decision time. | planning constraint |
| hidden information | Opponent concealed hands, unrevealed wall order or other private state not visible to the acting player. | forbidden |
| future information | Draws, discards, calls, scores, outcomes or events after the decision timestamp. | forbidden as decision-time input |
| generated label | A label produced by rules, scripts, annotators, models or derived outcomes rather than copied directly from an approved action source. | no |
| human label | A human-authored annotation that requires protocol, rights, provenance and quality review. | no |
| model-output label | A label produced by a model output, pseudo-labeler or baseline policy. | no |

No concept above can substitute for another approval.

## Dependency Map

The future dependency order is:

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

For a future synthetic/local-only task, source-specific approval may be
replaced only by an explicit project-authored synthetic/local boundary,
proposal, approval decision and exact first `10_NEXT` implementation task.
That replacement still does not approve training data or real-data use.

## Relationship To Parser Reader Ingestion

Parser / reader / ingestion work may only produce approved source records,
normalized records, manifests or validation summaries within its approved
scope. It must stop before feature extraction and label generation unless a
separate feature / label approval exists.

Feature extraction consumes approved synthetic/local or approved-source records
and emits feature values. Label generation consumes approved synthetic/local or
approved-source records and emits labels or targets. Both are downstream of
parser / reader / ingestion and upstream of supervised dataset construction.

Approval separation:

- source approval is not source ingestion approval.
- source ingestion approval is not parser / reader / ingestion approval.
- parser / reader / ingestion approval is not feature extraction approval.
- feature extraction approval is not label generation approval.
- label generation approval is not supervised dataset approval.
- supervised dataset approval is not training approval.

## Current Synthetic Local Smoke Boundary

The accepted minimal synthetic/local supervised feature-label smoke path is a
schema / guardrail smoke artifact only. It validates JSON-safe synthetic/local
mappings, candidate feature / label family names, public-information-only
placeholders and non-evidence guardrails.

It is not:

- training data.
- actual broader P7 feature extraction.
- actual broader P7 label generation.
- parser / reader / ingestion approval.
- source approval.
- supervised dataset construction.
- model input pipeline construction.
- model-strength evidence.

## Candidate Feature Families

The following candidate feature families may be discussed for planning only.
None are approved for extraction now.

| candidate_feature_family | allowed_for_docs_planning | implementation_allowed_now | source_dependency | leakage_risk | required_before_implementation | status |
|---|---:|---:|---|---|---|---|
| project-authored synthetic/local smoke features | yes | no | explicit synthetic/local boundary | medium if mistaken for training data | exact proposal, approval decision and non-training warning | planning only |
| approved-source decision-time table context | yes | no | approved source and approved reader | medium if timestamp wrong | source approval, reader approval, timing policy | planning only |
| visible hand features | yes | no | approved acting-player hand source | high if hidden tiles leak | public-info policy, hidden-info tests | planning only |
| public discard / call / riichi event features | yes | no | approved event source | high if future events leak | event-order validation and timing policy | planning only |
| visible dora / score / round context | yes | no | approved decision source | medium | visibility and timestamp policy | planning only |
| legal-action mask features | yes | no | approved legal-action source or synthetic fixture | high if generated from future state | legal-action source boundary and rule-source review | planning only |
| provenance / source metadata features | yes | no | approved metadata policy | high if model learns source shortcut | split policy and shortcut-risk review | planning only |
| model-output-derived features | no | no | future model-output policy | high | separate model-output boundary | blocked |
| self-play / league-derived features | no | no | P8/P10 approval | high | later-stage approval | blocked |
| real Tenhou / real haifu features | no | no | explicit source and reader approval | high | rights/privacy/platform review plus reader approval | blocked |

## Candidate Label Families

The following candidate label families may be discussed for planning only.
None are approved for generation now.

| candidate_label_family | allowed_for_docs_planning | implementation_allowed_now | source_dependency | leakage_risk | required_before_implementation | status |
|---|---:|---:|---|---|---|---|
| project-authored synthetic smoke labels | yes | no | explicit synthetic/local boundary | medium if mistaken for training data | exact proposal, approval decision and non-training warning | planning only |
| action imitation labels | yes | no | approved decision/action source | high | source approval, reader approval, observation boundary | planning only |
| discard-choice labels | yes | no | approved dahai source | high | action schema, legal-action context policy | planning only |
| call / no-call labels | yes | no | approved call-decision source | high | call decision schema and source approval | planning only |
| riichi / no-riichi labels | yes | no | approved riichi-decision source | high | riichi timing schema and leakage review | planning only |
| legal-action diagnostic labels | yes | no | approved legal-action fixture/source | medium | legal-action metric boundary and evaluator approval | planning only |
| future value / reward targets | yes | no | approved outcome source | very high | future-outcome target policy and stage review | deferred |
| final rank / placement targets | yes | no | approved outcome source | very high | outcome source approval and leakage/split policy | deferred |
| human-authored annotation labels | yes | no | approved annotation protocol | high | rights, protocol, annotator provenance and quality review | blocked |
| generated pseudo-labels | yes | no | approved generator and source | high | generator version, deterministic settings and validation | blocked |
| model-output labels | no | no | future model-output policy | high | separate model-output label boundary | blocked |
| self-play / league labels | no | no | P8/P10 approval | high | later-stage approval | blocked |

## Feature Boundary Rules

Future actual feature extraction must be limited to information available to
the acting player at the decision time.

Required future controls:

- source id and approval reference.
- parser / reader / ingestion approval reference, or explicit synthetic/local
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

Forbidden as decision-time features:

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
- account, session, cookie, token or platform-private content.

## Label Boundary Rules

Labels must remain separate from features. A future action source or outcome
source may become a label target only after explicit approval, but it must not
leak into decision-time feature inputs.

Required future controls:

- label source id and approval reference.
- parser / reader / ingestion approval reference, or explicit synthetic/local
  not-required rationale.
- label schema version.
- label family allowlist.
- label generation method.
- target timestamp and observation timestamp separation.
- provenance and generator / annotator metadata, if any.
- split and leakage policy.
- validation commands.
- evidence and risk references.

Forbidden as labels until separate approval:

- labels from unapproved real Tenhou or real haifu.
- labels from external logs or platform data.
- labels from model outputs.
- labels from self-play or league outputs.
- labels generated by unknown third-party binaries, weights or checkpoints.
- labels that require hidden information without an oracle-diagnostic policy.
- labels that imply training-data approval.

## Future Approval Record Fields

Any future actual feature extraction or label generation approval record must
include:

- `component_id`.
- `component_type`: feature_extractor / label_generator.
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

If any required field is missing, the component is not approved.

## Allowed Future Implementation Boundary

A future implementation may be considered only after a separate proposal,
approval decision and first unchecked `10_NEXT` task. It must be exactly one
of:

- project-authored synthetic/local-only feature / label smoke.
- approved-source-only feature extraction.
- approved-source-only label generation.
- docs-only validator.

It must:

- be exact-file scoped.
- use only approved synthetic/local fixtures or approved sources.
- require approved parser / reader / ingestion, unless explicitly not needed
  for a synthetic/local-only task.
- emit only the approved feature / label fields.
- preserve provenance, schema version and evidence references.
- stop before supervised dataset construction unless separately approved.
- stop before training unless separately approved.
- avoid broad file ingestion.
- avoid CLI data paths unless separately approved.
- avoid account / session / cookie / token handling.
- avoid model-output, self-play or league sources unless later-stage review
  approves them.

## Forbidden Feature Label Scope

The following are forbidden now:

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

## Stop Conditions

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

## Risk Controls

| risk | mitigation | current_status |
|---|---|---|
| Feature boundary is mistaken for feature extraction approval. | Mark this document and `10_NEXT` as docs-only and require later proposal / approval / exact first task. | open |
| Label boundary is mistaken for label generation approval. | Keep labels as planning-only and require approval record fields before generation. | open |
| Parser / reader output becomes feature tensors. | Require feature extraction approval after parser / reader / ingestion review. | open |
| Reader output becomes labels. | Require label generation approval after parser / reader / ingestion review. | open |
| Synthetic smoke fixture becomes training data. | Repeat that current synthetic/local smoke artifacts are not training data. | open |
| Hidden-information leakage. | Require public-information-only feature policy and hidden-info exclusion. | open |
| Future-information leakage. | Require timestamp policy and future-event exclusion. | open |
| Final outcomes leak into decision features. | Forbid final score / placement as decision-time features. | open |
| Labels leak into features. | Require separate observation and target timestamp policies. | open |
| Source approval is mistaken for training-data approval. | Keep source, ingestion, feature, label, dataset and training approvals separate. | open |
| Dataset construction starts too early. | Stop before examples, splits and batches unless dataset construction is approved. | open |
| Model-output pseudo-labels enter too early. | Keep model-output labels blocked until later policy. | open |
| Broad file / CLI ingestion creep. | Keep arbitrary file loading and CLI data paths unapproved. | open |
| Real-data rights or platform terms violation. | Require source-specific rights, privacy and platform review before use. | open |
| Evidence overclaim. | Evidence grade remains boundary definition evidence only. | open |
| P8-P12 creep. | Require separate transition reviews and first-task approval. | open |

## Evidence Requirements

Future actual feature extraction or label generation evidence must record:

- `component_id`.
- `component_type`.
- source id and source approval status.
- parser / reader / ingestion approval status.
- exact files.
- feature schema version.
- label schema version.
- feature family allowlist.
- label family allowlist.
- public-information policy.
- hidden-information exclusion.
- future-information exclusion.
- input policy.
- output policy.
- provenance policy.
- storage policy.
- validation commands.
- leakage validation results.
- evidence log reference.
- risk register reference.
- decision record reference.
- explicit non-evidence warning.

## First Task Candidate

The next safe task is:

```text
Review broader P7 actual feature extraction and label generation boundary before implementation.
```

That review must remain docs-only. It must not implement feature extraction or
label generation, approve feature / label work, create tensors, labels,
examples or splits, construct a supervised dataset, train, read real data or
enter P8-P12.

## Planning Decision

```text
Broader P7 actual feature extraction and label generation boundary is defined
before implementation.
```

This does not approve actual feature extraction, actual label generation,
feature extraction implementation, label generation implementation, source
approval, source ingestion, parser / reader / ingestion, broad file ingestion,
CLI data paths, supervised dataset construction, training, model architecture
/ trainer, real-data use, model-output integration, self-play, league or
P8-P12 entry.

## Evidence Grade

```text
Broader P7 actual feature extraction and label generation boundary definition
evidence only.
```

This is not:

- feature extraction implementation evidence.
- label generation implementation evidence.
- feature extraction approval.
- label generation approval.
- source approval evidence.
- source ingestion evidence.
- parser / reader / ingestion evidence.
- supervised dataset construction evidence.
- training evidence.
- model architecture or trainer evidence.
- model-output integration evidence.
- real-data evidence.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- P8-P12 evidence.
