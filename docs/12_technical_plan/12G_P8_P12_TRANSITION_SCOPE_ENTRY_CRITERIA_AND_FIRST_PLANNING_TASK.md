# 12G_P8_P12_TRANSITION_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK

## Scope

This document defines the P8-P12 transition scope, entry criteria and first
planning task after the post-full-P7 transition review in `12F`.

This is a docs-only transition-scope definition. It is not:

- P8-P12 entry approval.
- P8 implementation approval.
- P8-P12 implementation task definition.
- a P8-P12 implementation prompt.
- production code, tests, fixtures or data files.
- source approval or source ingestion.
- parser / reader / ingestion implementation.
- feature extraction or label generation.
- supervised dataset construction.
- training, tuning or training-run approval.
- model architecture, trainer, dataloader, optimizer or loss implementation.
- checkpoint, weights or snapshot creation.
- evaluation implementation, metric implementation or evaluation runner.
- benchmark harness implementation.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- real Tenhou, real haifu, external logs or platform data.
- self-play or league.

## Full P7 Closure Recap

`docs/03_supervised_policy/03BL_FINAL_FULL_P7_CLOSURE_REVIEW.md` records:

```text
A. Full P7 can close.
```

Full P7 is closed only for the documented P7 supervised-learning scope:

- accepted current-scope synthetic/local supervised feature-label smoke.
- accepted current-scope synthetic/local parser-reader smoke.
- accepted current-scope synthetic/local parser-reader smoke extension.
- exact test-only blocker fix.
- docs-only readiness / boundary / proposal / review / approval / acceptance
  chain.
- full-scope expansion plan and review.
- closure criteria definition and review.
- handoff / evidence index finalization and review.
- risk/source-rights/evidence consistency review.
- governance synchronization and validation evidence.

`docs/12_technical_plan/12F_POST_FULL_P7_TRANSITION_REVIEW.md` records:

```text
A. No post-full-P7 transition blocker found for defining P8-P12 docs-only scope / entry criteria / first planning task.
```

That decision allows this docs-only transition-scope definition. It does not
approve P8-P12 entry, P8 implementation, training, evaluation, self-play,
league, real data, source ingestion, model-output integration or
model-strength evidence.

## P8-P12 Non-Approval Baseline

The baseline after full P7 closure is conservative:

- P8-P12 remain unapproved.
- No P8-P12 task is approved for execution.
- No P8-P12 implementation prompt is approved.
- No P8-P12 implementation evidence exists.
- No training, evaluation, self-play or league evidence is created by this
  task.
- No source approval, source ingestion or real-data permission exists.
- No model-output integration is approved.
- No model-strength evidence exists.

Any future movement from planning to execution must pass a separate approval
chain, update `docs/10_next/10_NEXT.md`, record risk/evidence boundaries and
stay within the exact approved task.

## P8-P12 Transition Scope

The P8-P12 transition scope is a docs-only framework for later-stage planning
after full P7 closure. It may describe:

- candidate stage purposes.
- entry criteria.
- dependency ordering.
- risk controls.
- evidence requirements.
- forbidden scope.
- first planning task.

It must not execute or approve later-stage work.

The existing roadmap names P8-P12 as:

- P8: self-play reinforcement learning.
- P9: search and risk model.
- P10: model league and mainline selection.
- P11: large-scale training and stability validation.
- P12: Tenhou target validation.

Those stage names remain roadmap labels only. This document does not approve
any implementation, training, self-play, search, league, large-scale training
or Tenhou validation work.

## Candidate P8-P12 Workstream Inventory

| workstream | current_status | approved_now | entry_prerequisites | evidence_required | main_risks | forbidden_current_scope | notes |
|---|---|---:|---|---|---|---|---|
| P8-P12 scope / entry criteria planning | current docs-only definition | yes, docs-only | full P7 closure and `12F` transition review | this document, review gate, governance sync | mistaken for entry approval | implementation, training, evaluation, self-play, league | Selected current workstream. |
| P8 scope definition | not started | no | review of this transition scope | P8 scope doc, risk/evidence review | P8 entry creep | P8 implementation prompt or task execution | Possible later docs-only task after review. |
| training / tuning planning | not approved | no | source/data/model/evaluation prerequisites | training approval record, data approval, validation plan | premature training and weak evidence | training, tuning, checkpoint creation | Must not start from smoke evidence. |
| RL planning | not approved | no | P8 scope, reward/eval boundaries, safety review | RL scope, self-play risk record, evaluation dependency record | self-play and objective drift | RL implementation, self-play, league | P8 roadmap item only. |
| self-play planning | not approved | no | P8 scope and self-play environment boundary | self-play scope, risk controls, reproducibility plan | runaway compute or invalid evidence | self-play execution | Later-stage only. |
| league planning | not approved | no | evaluation protocol, candidate promotion rules | league scope, uncertainty/reporting policy | ranking overclaim | league runner or match harness | P10 roadmap item only. |
| evaluation / benchmark planning | not approved | no | P5 evidence boundaries and future real-eval approvals | evaluation protocol, sample-size policy, uncertainty rules | LuckyJ/stable-dan overclaim | evaluation implementation or runner | Must separate diagnostics from strength. |
| model-output integration planning | not approved | no | model artifact, adapter, evaluation scope | adapter boundary, evidence refs, safety flags | treating model output as strength evidence | model-output path implementation | Later approval required. |
| model-strength evidence planning | not approved | no | approved evaluation protocol and data source | evidence record schema, uncertainty, non-evidence warnings | false strength claims | strength claims | No current evidence exists. |
| candidate promotion planning | not approved | no | racing-funnel alignment and evaluation evidence | promotion criteria, decision record | premature promotion | promotion claims | Must follow F0-F7 funnel. |
| Tenhou ranked evidence planning | not approved | no | compliance, platform, account and risk review | lawful protocol, safety review, evidence log | platform compliance and overclaim | real Tenhou access | P12 later-stage only. |
| stable-dan evidence planning | not approved | no | approved ranked/evaluation evidence source | sample size, CI, stable-dan report | unstable estimates | stable-dan claims | P5 calculator exists; evidence source does not. |
| LuckyJ `10.68` comparison planning | not approved | no | approved stable-dan evidence with uncertainty | comparison protocol and decision record | target overclaim | LuckyJ comparison claim | Final validation only. |
| real-data / source-rights planning | not approved | no | source-rights, privacy and platform review | source approval record, allowed-use terms | data rights and privacy | ingestion, scraping, external logs | No current source approval. |
| governance / risk / evidence controls | current docs-only planning | yes, docs-only | full P7 closure and `12F` | risk register, evidence log, decision record | governance drift | approvals beyond docs | Required for all later stages. |

## P8-P12 Entry Criteria

P8-P12 implementation may not begin until all applicable criteria are met and
reviewed:

- E1. Full P7 closure is recorded and bounded.
- E2. Post-full-P7 transition review is completed.
- E3. P8-P12 transition scope is defined and reviewed.
- E4. P8-P12 entry criteria are reviewed.
- E5. P8-P12 risk/evidence taxonomy is defined and reviewed.
- E6. Source / real-data / platform dependencies are explicitly classified.
- E7. Training, evaluation and model-output dependencies are explicitly
  classified.
- E8. No model-strength claim is made without approved evaluation evidence.
- E9. No real-data work begins without source-rights / platform / privacy
  review.
- E10. No self-play or league work begins without separate scope and approval.
- E11. The first task must be docs-only unless later approval explicitly
  authorizes exact implementation.
- E12. Human / Web ChatGPT review must approve any transition from planning to
  implementation.

## P8-P12 Non-Entry Conditions

The project must not enter P8-P12 implementation while any of the following is
true:

- source approval is missing.
- source ingestion approval is missing.
- real data source is not approved.
- training data is missing or unapproved.
- model / trainer is missing or unapproved.
- evaluation protocol is missing or unapproved.
- model-output integration is missing or unapproved.
- model-strength evidence is overclaimed.
- self-play / league scope is missing.
- P8-P12 risk/evidence taxonomy is missing.
- first task has not been reviewed.
- `docs/10_next/10_NEXT.md` does not explicitly authorize the task.
- governance docs disagree.
- validation fails.

## Forbidden Current Scope

This task and the next planning review must not do any of the following:

- approve P8-P12 entry.
- implement P8.
- define a P8-P12 implementation prompt.
- train or tune.
- run self-play or league.
- use real Tenhou, real haifu, external logs or platform data.
- approve source approval or source ingestion.
- add broad file ingestion or CLI.
- implement feature extraction or label generation.
- construct datasets.
- implement evaluation.
- integrate model outputs.
- produce model-strength evidence.
- produce Tenhou ranked evidence.
- produce stable-dan evidence.
- produce LuckyJ `10.68` comparison.
- make candidate-promotion claims.

## Risk Controls

| risk | control |
|---|---|
| P8-P12 transition scope is mistaken for P8-P12 entry approval. | State non-approval in `12G`, `10_NEXT`, handoff, evidence log, risk register and decision record. |
| P8-P12 entry criteria are mistaken for implementation approval. | Require a separate review gate and later approval decision before exact implementation. |
| Full P7 closure is mistaken for training readiness. | Keep full P7 closure scoped to documented supervised-learning groundwork and smoke artifacts only. |
| Full P7 closure is mistaken for model-strength evidence. | Evidence log records closure and transition documents as governance evidence only. |
| Synthetic/local smoke evidence is overclaimed. | Preserve explicit non-evidence warnings for smoke artifacts. |
| Source approval gap is ignored. | Keep all source/real-data work unapproved until source-rights review. |
| Real-data / platform / account risk is normalized too early. | Keep Tenhou, haifu, platform and account material forbidden in current scope. |
| Training/evaluation creep. | Keep `10_NEXT` docs-only and run only existing smoke/schema unittests. |
| Model-output integration creep. | Require a separate adapter/integration boundary before any model-output path. |
| Self-play / league creep. | Keep self-play and league as later-stage, separately approved workstreams. |
| Tenhou / stable-dan / LuckyJ overclaim. | Require approved evidence source, sample size, uncertainty and review before claims. |
| Candidate-promotion overclaim. | Require racing-funnel alignment and explicit promotion decision record. |
| Governance mismatch. | Synchronize handoff, index, technical plan, evidence, risk, changelog, decision record, stage contract, milestones, backlog and `10_NEXT`. |
| `10_NEXT` drift. | Keep only one unchecked first task and make it a docs-only review gate. |

## Evidence Requirements

Future P8-P12 evidence records must include:

- `evidence_id`.
- `stage_or_workstream`.
- `scope_status`.
- `entry_status`.
- `approval_status`.
- `source_status`.
- `data_status`.
- `training_status`.
- `evaluation_status`.
- `model_output_status`.
- `self_play_status`.
- `league_status`.
- `model_strength_status`.
- `validation_commands`.
- `risk_reference`.
- `decision_reference`.
- `evidence_grade`.
- `explicit_non_evidence_warning`.

The current task evidence grade is:

```text
P8-P12 transition scope, entry criteria and first planning task definition evidence only.
```

## Candidate Next Directions

| candidate | status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_P12_entry_risk | decision |
|---|---|---|---|---|---:|---:|---|---|
| Review P8-P12 transition scope, entry criteria and first planning task. | available | Adds a review gate before later planning or approval. | Review may be mistaken for entry approval. | none | yes | no | low if wording stays strict | selected |
| Define P8-specific scope, entry criteria and first task. | premature | Narrows toward the next stage. | Skips review of the whole transition framework. | 12G review | yes | no | medium | not selected |
| Define P8-P12 risk and evidence taxonomy before any implementation. | possible later | Useful governance artifact. | Could duplicate review findings before `12G` is reviewed. | 12G review | yes | no | low | not selected |
| Prepare P8 entry approval decision. | premature | Would move toward execution readiness. | Too close to entry approval before transition review. | 12G review and risk taxonomy | yes | no | high | rejected now |
| Start P8 implementation. | forbidden | none in current scope | Stage jump. | entry approval missing | no | no | severe | rejected |
| Start training / tuning. | forbidden | none in current scope | Training without approved data/eval. | source/data/model/eval approvals missing | no | no | severe | rejected |
| Start self-play / league. | forbidden | none in current scope | Later-stage execution without scope. | P8/P10 scopes missing | no | no | severe | rejected |
| Start real-data / Tenhou work. | forbidden | none in current scope | Compliance, privacy and platform risk. | source/platform approval missing | no | no | severe | rejected |
| Start model-output integration / model-strength evidence work. | forbidden | none in current scope | Overclaim and unsupported integration. | model/eval approvals missing | no | no | severe | rejected |

## Recommended First Planning Task

The next first task should be:

```text
Review P8-P12 transition scope, entry criteria and first planning task after post-full-P7 transition review.
```

This next task must be a docs-only review gate. It must not approve P8-P12
entry, P8 implementation, P8-P12 implementation prompts, training, evaluation,
self-play, league, source approval, source ingestion, real data,
model-output integration, model-strength evidence or model-strength claims.

## Planning Decision

P8-P12 transition scope, entry criteria and first planning task are defined
after post-full-P7 transition review. This task does not approve P8-P12 entry,
P8 implementation, any P8-P12 implementation prompt, training, tuning,
evaluation, self-play, league, source approval, source ingestion, real data,
model-output integration, model-strength evidence, Tenhou ranked evidence,
stable-dan evidence, LuckyJ `10.68` comparison or candidate promotion.

The next safe task is a docs-only review of this transition scope / entry
criteria / first planning task.

## Explicit Non-Evidence

This document is not:

- P8-P12 entry approval.
- P8 implementation approval.
- a P8-P12 implementation prompt.
- training or tuning.
- evaluation.
- self-play or league.
- source approval or source ingestion.
- real data, real Tenhou, real haifu, external logs or platform data.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
