# 03AW_P7_FULL_SCOPE_EXPANSION_PLAN_AFTER_CURRENT_SCOPE_ACCEPTANCE

## Purpose

This document defines the full P7 expansion plan after accepting the exact
broader P7 minimal synthetic/local parser-reader smoke implementation as
current-scope complete.

It is a docs-only planning artifact. It does not approve or implement any
additional P7 work.

## Current Accepted P7 Scope

The following P7 work is accepted as current-scope complete:

- The docs-only supervised-learning readiness chain through `03V`.
- The exact minimal synthetic/local supervised feature-label smoke
  implementation approved in `03O`, reviewed in `03P` and accepted in `03Q`.
- The broader P7 boundary chain from `03Y` through `03AT`.
- The exact broader P7 minimal synthetic/local parser-reader smoke task
  approved in `03AU`, implemented only in:
  - `src/mjlabai/supervised/synthetic_parser_reader_smoke.py`
  - `tests/supervised/test_synthetic_parser_reader_smoke.py`
- The exact parser-reader smoke implementation review in `03AV`.
- The 2026-07-01 acceptance decision that marks the exact parser-reader smoke
  scope as current-scope complete.

This accepted scope is synthetic/local only. It uses already-loaded in-memory
project-authored mappings and existing synthetic/local fixtures only where
tests explicitly read them. It does not approve real data, ingestion, broad
parser / reader work, actual feature extraction, actual label generation,
dataset construction, training, evaluation or P8-P12.

## Current Non-Approved Scope

The following remain unapproved:

- Source approval for training or ingestion.
- Real Tenhou data, real haifu, external logs, platform data, online accounts
  or third-party artifacts.
- Source ingestion and broad parser / reader / ingestion implementation.
- Actual feature extraction.
- Actual label generation.
- Supervised dataset construction.
- Split creation and leakage-test implementation.
- Training-data approval.
- Training-run approval.
- Training, tuning, checkpoints, weights or model artifacts.
- Model architecture / trainer implementation.
- Evaluation implementation, metric implementation, evaluation runner or
  benchmark harness.
- Model-output integration.
- Model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison and candidate promotion.
- Self-play, league and P8-P12 entry.

## What This Plan Is Not

This plan is not:

- implementation approval.
- source approval.
- source ingestion approval.
- parser / reader / ingestion approval.
- feature extraction approval.
- label generation approval.
- dataset approval.
- training-data approval.
- training-run approval.
- model architecture or trainer approval.
- evaluation approval.
- strength evidence.
- full P7 closure.
- P8-P12 transition approval.

## Full P7 Expansion Purpose

Full P7 is meant to prepare a supervised policy route that can eventually
produce a high-quality base model for later evaluation and possible downstream
training stages. That long-term purpose supports the north-star goal of
exceeding LuckyJ `10.68` stable dan, but this plan itself is not evidence that
any model can do so.

The expansion plan exists to:

- inventory remaining full-P7 work.
- sequence required approvals before implementation.
- keep source, ingestion, feature, label, dataset, training and evaluation
  work separated.
- prevent synthetic/local smoke evidence from being overclaimed.
- define the next docs-only review gate before any new implementation task.

## Workstream Inventory

| Workstream | Current status | Next possible task type | Required upstream artifacts | Forbidden current scope | Risks | Evidence required | Likely next gate | Notes |
|---|---|---|---|---|---|---|---|---|
| Source approval / data rights | Not approved | Docs-only source-specific approval process or decision | Source inventory, rights notes, allowed-use status, storage policy, privacy/compliance review | real data use, account/session data, platform automation, external logs | rights ambiguity, platform-policy drift, accidental real-data use | source approval record, risk entry, allowed-use evidence | source approval review | No source is approved for training or ingestion now. |
| Parser / reader / ingestion | Boundary defined; exact synthetic smoke accepted only | proposal or approval-decision task after source decision | approved source, parser schema, ingestion boundary, exact files | broad ingestion, arbitrary paths, CLI, real Tenhou, real haifu | smoke path mistaken for ingestion, source leakage | approval record, exact file list, validation commands | implementation proposal review | Current parser-reader smoke is not broad ingestion. |
| Actual feature extraction | Boundary defined only | docs-only proposal after parser/source gates | approved source, parser output schema, feature vocabulary, leakage controls | feature tensors, examples, model inputs | hidden information leakage, feature drift | feature approval record, leakage guardrails | feature proposal review | Current smoke validates schema/guardrails only. |
| Actual label generation | Boundary defined only | docs-only proposal after parser/source gates | approved source, public-information policy, label taxonomy, leakage controls | generated labels, targets, supervised examples | hidden/future info leakage, target ambiguity | label approval record, label provenance | label proposal review | Current labels are smoke placeholders, not training labels. |
| Supervised dataset construction | Boundary defined only | docs-only dataset proposal after feature/label approval | approved feature/label outputs, dataset record schema, manifest plan | dataset files, manifests, examples, records | synthetic smoke mistaken for dataset, invalid provenance | dataset approval record, manifest schema | dataset proposal review | No dataset is approved now. |
| Split / leakage controls | Boundary defined only | docs-only split/leakage proposal after dataset boundary | dataset schema, split unit, grouping policy, duplicate policy, seeds | split files, leakage-test code | cross-split leakage, duplicate leakage, seat/round leakage | split/leakage approval record, validation plan | split proposal review | Leakage checks must precede training approval. |
| Training-data approval | Boundary defined only | docs-only training-data approval after dataset/split review | dataset manifest, source approvals, leakage results, evidence grade | training-data use, training examples | bad source promoted to training, smoke data misuse | training-data approval record | training-data review | Approval must be separate from dataset creation. |
| Training-run approval | Boundary defined only | docs-only training-run approval after training-data approval | training data approval, model/trainer plan, run config, compute/artifact policy | training, tuning, checkpoints, weights | accidental training, artifact leakage | run approval record, command plan, artifact policy | run approval review | Approval is needed before any training command. |
| Model architecture / trainer implementation | Boundary defined only | docs-only proposal after training-data/run prerequisites | architecture plan, trainer plan, loss/objective plan, dataloader plan | trainer code, optimizer, loss, dataloader, checkpoints | optimizing wrong metric, premature model artifact | implementation proposal, tests plan, risk controls | proposal review / approval decision | No trainer implementation now. |
| Evaluation dependency / evidence | Boundary defined only | docs-only evaluation dependency review after model-output boundary | approved evaluation protocol, metrics, sample-size rules, model-output approval | evaluation implementation, runner, benchmark harness | strength overclaim, insufficient sample size | evaluation approval record, uncertainty plan | evidence boundary review | No model-strength evidence is produced in P7 planning. |
| Model-output integration | Not approved | docs-only boundary/proposal after model/trainer and evaluation prerequisites | model artifact policy, output schema, evaluation dependencies | reading model outputs, inference integration | output mistaken for strength evidence | model-output approval record | model-output review | Blocked until model/trainer/evaluation boundaries mature. |
| Real data / Tenhou / haifu / platform data | Blocked | source-specific legal/provenance review only | explicit lawful source, allowed-use decision, storage policy, privacy review | real Tenhou access, real haifu ingestion, external logs, platform data | compliance, secrets, account/tooling drift | external-source evidence and decision record | source review | No real data is approved. |
| Governance / evidence / risk / decision records | Active | update with every gate | current docs, validation output, risk decisions | unlogged approvals, silent scope drift | evidence inflation, stale next task | changelog, evidence log, risk register, decision record | every review gate | Governance is the control surface for P7. |
| Full P7 closure criteria | Not complete | docs-only closure criteria definition after expansion review | accepted current scopes, remaining-scope inventory, evidence index | closing P7 without required reviews | premature closure, skipped risks | closure checklist, evidence index | closure criteria review | Full P7 remains open. |
| P8-P12 transition boundary | Not approved | post-full-P7 transition review only | final full P7 closure decision, risk review, next-stage scope | self-play, league, RL, Tenhou validation | stage jump, training before data/eval readiness | transition review, entry criteria | P8/P9/etc. scope definition | No P8-P12 entry is approved. |

## Expansion Sequence

The conservative expansion sequence is:

1. Review P7 full scope expansion plan after current-scope acceptance.
2. Define full P7 closure criteria after expansion plan review.
3. Define source-specific approval decision process if real or approved-source
   work is desired.
4. Define the next exact minimal implementation proposal only if upstream
   gates permit it.
5. Prepare an approval decision after proposal review.
6. Implement only the exact approved scope.
7. Review that implementation.
8. Accept the current scope only if warranted.
9. Repeat narrow proposal / approval / implementation / review / acceptance
   loops until full P7 closure criteria are reviewed.
10. Only after full P7 closure and a separate transition review may any P8-P12
    task be considered.

There is no immediate implementation next task.

## Near-Term Docs-Only Candidate Tasks

Recommended next task:

```text
Review P7 full scope expansion plan after current-scope acceptance.
```

Other possible docs-only tasks, not selected now:

- Define full P7 closure criteria after expansion plan review.
- Define a source-specific approval decision process.
- Review data-rights and source-readiness vocabulary against current P7 docs.
- Review P7 risk register consistency before any new implementation proposal.

## Later Implementation Candidate Classes

These classes are candidates only. None is approved now.

| Candidate | Current status | Approved now | Upstream required | Risk | Notes |
|---|---|---|---|---|---|
| Synthetic/local record validator extension | Possible future exact proposal | No | proposal review and approval decision | smoke evidence overclaim | Must remain synthetic/local if proposed. |
| Synthetic/local parser-reader follow-up | Current exact scope accepted | No | new proposal if more files are needed | drifting into ingestion | Existing helper is complete for its exact scope. |
| Approved-source reader | Blocked | No | source approval, ingestion boundary, exact proposal | real-data leakage | Cannot use real sources without approval. |
| Approved-source feature extractor | Blocked | No | source + parser approval, feature approval | hidden information leakage | Must not emit tensors before approval. |
| Approved-source label generator | Blocked | No | source + parser approval, label approval | target leakage | Must separate labels from smoke placeholders. |
| Dataset manifest builder | Blocked | No | feature/label and dataset approvals | dataset misuse | No dataset construction now. |
| Split/leakage validator | Blocked | No | dataset schema and split policy approval | leakage false negatives | Future exact checks must be approved. |
| Training-data manifest validator | Blocked | No | dataset/split/leakage evidence | bad training-data promotion | Training data approval remains separate. |
| Model/trainer config validator | Blocked | No | model/trainer planning approval | premature trainer implementation | Must not add trainer code without approval. |
| Evaluation evidence envelope validator | Blocked | No | evaluation boundary and model-output approval | strength overclaim | P5 envelope patterns may inform future docs only. |

## Deferred / Blocked / Later-Stage Inventory

Deferred inside P7:

- source approval.
- broad parser / reader / ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- training-data approval.
- model / trainer implementation.
- evaluation dependency integration.

Blocked until separate approval:

- real Tenhou.
- real haifu and external logs.
- platform data and account/session data.
- model-output integration.
- third-party binaries and unknown checkpoints.

Later-stage only:

- self-play.
- league.
- reinforcement learning.
- P8-P12.
- Tenhou ranked validation.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

## Risk Controls

- Every future implementation must name exact files before approval.
- Any need for real data stops the task and requires source-specific approval.
- Any need for source ingestion stops the task and requires ingestion approval.
- Any emission of feature tensors, labels, examples, datasets, splits, model
  inputs or model outputs stops the task unless explicitly approved.
- Any training command, training run, checkpoint, weights, optimizer, loss,
  dataloader or trainer implementation stops the task unless explicitly
  approved.
- Any evaluation runner, metric implementation, benchmark harness or
  model-strength claim stops the task unless explicitly approved.
- Any P8-P12 drift stops the task.
- Each gate must update `10_NEXT`, handoff, changelog, evidence log and risk
  register as needed.

## Evidence Requirements

Future P7 evidence records should include:

- `evidence_id`
- `workstream`
- `current_status`
- `upstream_artifacts`
- `approval_status`
- `implementation_status`
- `validation_commands`
- `evidence_grade`
- `risk_register_reference`
- `decision_record_reference`
- `known_exclusions`
- `explicit_non_evidence_warning`

## Full P7 Closure Preparation

Full P7 closure requires at minimum:

- expansion plan review.
- full P7 closure criteria definition.
- full P7 closure criteria review.
- handoff / evidence index synchronization.
- risk register and source-rights consistency review.
- final full P7 closure review.
- post-full-P7 transition review before any later-stage task.

This document does not close full P7.

## Planning Decision

Decision:

```text
P7 full scope expansion plan is defined for review.
```

The plan is conservative and docs-only. It records remaining workstreams,
dependencies, risks, evidence requirements and next gates after accepting the
exact synthetic/local parser-reader smoke scope.

## Evidence Grade

```text
P7 full scope expansion plan definition evidence only.
```

## Explicit Non-Evidence

This document is not:

- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
- training evidence.
- evaluation evidence.
- real-data evidence.
- full P7 closure evidence.
- P8-P12 evidence.

## First Task Candidate

The next task should be:

```text
Review P7 full scope expansion plan after current-scope acceptance.
```

That task must be docs-only. It must not approve or implement source approval,
source ingestion, broad parser / reader / ingestion, actual feature
extraction, actual label generation, dataset construction, split creation,
leakage-test implementation, training-data approval, training-run approval,
training, model architecture / trainer implementation, evaluation
implementation, metric implementation, evaluation runner, benchmark harness,
model-output integration, real data, self-play, league, P8-P12 or strength
claims.
