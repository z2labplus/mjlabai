# 12I_P8_SCOPE_ENTRY_CRITERIA_AND_FIRST_PLANNING_TASK_AFTER_P8_P12_TRANSITION_SCOPE_REVIEW

## Scope

This document defines P8 scope, P8 entry criteria and the first P8 planning
task after the reviewed P8-P12 transition-scope document in `12H`.

This is a docs-only P8 scope definition. It is not:

- P8 entry approval.
- P8 implementation approval.
- a P8 implementation prompt.
- a P8-P12 implementation task.
- production code, tests, fixtures or data files.
- source approval or source ingestion.
- parser / reader / ingestion implementation.
- feature extraction or label generation.
- supervised dataset construction.
- training, tuning or training-run approval.
- evaluation implementation, metric implementation or evaluation runner.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- real Tenhou, real haifu, external logs or platform data.
- broad file ingestion or CLI.
- self-play, league or reinforcement-learning execution.
- P9-P12 entry approval.

## Full P7 / P8-P12 Transition Recap

The transition chain before this document is:

- `03BL` ran the final full P7 closure review and recorded
  `A. Full P7 can close`.
- Full P7 is closed only for the documented P7 supervised-learning scope.
- `12F` found no blocker for defining P8-P12 docs-only transition scope,
  entry criteria and first planning task.
- `12G` defined P8-P12 transition scope, entry criteria and first planning
  task.
- `12H` reviewed `12G` and recorded `A. Review can close`.
- `12H` selected this task as the next first planning task:
  `Define P8 scope, entry criteria and first planning task after P8-P12
  transition-scope review.`

None of `03BL`, `12F`, `12G`, `12H` or this document approves P8 entry, P8
implementation, P8 implementation prompts, P9-P12 entry, source approval,
source ingestion, real data, training, evaluation, model-output integration,
self-play, league or model-strength evidence.

## P8 Stage Interpretation

P8 is the roadmap label for:

```text
self-play reinforcement learning
```

That stage label is not approval to execute self-play, reinforcement learning,
training, tuning, league, evaluation, model-output integration or any
model-strength claim.

In the current task, P8 means only:

- define the P8 planning boundary.
- define conservative P8 entry criteria.
- define non-entry conditions.
- define risk and evidence controls.
- select the next docs-only review gate.

## P8 Non-Approval Baseline

The baseline after this document remains:

- P8 entry is unapproved.
- P8 implementation is unapproved.
- the first executable P8 task is unapproved.
- any P8 implementation prompt is unapproved.
- P9-P12 entry remains unapproved.
- no self-play, reinforcement-learning, league, training, evaluation,
  model-output or model-strength evidence exists.
- no real-data, source-approval or source-ingestion permission exists.

Any future movement from P8 planning toward implementation must pass a
separate review and approval chain and must be explicitly named in
`docs/10_next/10_NEXT.md`.

## P8 Scope Boundary

Current P8 scope is docs-only planning. It may describe later-stage candidate
purpose and dependencies:

- self-play / reinforcement-learning planning.
- training, model-output and evaluation dependency review.
- risk / evidence taxonomy for P8.
- future first-task selection.
- transition safeguards from P7 into P8.
- governance synchronization for later approval decisions.

Current P8 scope must not execute or approve later-stage work. It must not
create production code, tests, fixtures, data files, source ingestion,
training runs, evaluation results, self-play games, league runs, model-output
paths or model-strength evidence.

## P8 Entry Criteria

P8 implementation may not begin until all applicable criteria are met,
reviewed and explicitly approved:

- P8-E1. Full P7 closure is recorded and bounded.
- P8-E2. Post-full-P7 transition review is completed.
- P8-E3. P8-P12 transition scope is defined and reviewed.
- P8-E4. P8 scope, entry criteria and first planning task are defined and
  reviewed.
- P8-E5. P8 risk / evidence taxonomy is defined and reviewed.
- P8-E6. Self-play / reinforcement-learning dependency map is defined and
  reviewed.
- P8-E7. Training, model-output and evaluation dependencies are explicitly
  classified.
- P8-E8. Source, real-data and platform dependencies are explicitly
  classified.
- P8-E9. No self-play or league work begins without a separate approval
  decision.
- P8-E10. No training or tuning begins without explicit training-data and
  training-run approval.
- P8-E11. No model-strength claim is made without an approved evaluation
  protocol and approved evidence.
- P8-E12. No real or platform data work begins without source-rights,
  privacy and platform-policy review.
- P8-E13. P9-P12 remain unapproved unless separately scoped and reviewed.
- P8-E14. `docs/10_next/10_NEXT.md` explicitly authorizes any future task.
- P8-E15. Human / Web ChatGPT review approves any planning-to-implementation
  transition.

## P8 Non-Entry Conditions

The project must not enter P8 implementation while any of the following is
true:

- P8 scope has not been reviewed.
- P8 risk / evidence taxonomy is missing.
- self-play / reinforcement-learning scope is missing.
- model-output dependency status is missing.
- evaluation protocol is missing.
- source approval is missing.
- source ingestion approval is missing.
- real data permission is missing.
- training-data approval is missing.
- training-run approval is missing.
- self-play approval is missing.
- league approval is missing.
- model-strength evidence boundary is missing.
- governance docs disagree.
- `docs/10_next/10_NEXT.md` does not explicitly authorize the exact task.
- validation fails.

## Forbidden Current Scope

This document and the next review gate must not:

- approve P8 entry.
- approve P8 implementation.
- generate a P8 implementation prompt.
- implement any P8-P12 task.
- train, tune, evaluate, run self-play or run league.
- approve source approval, source ingestion or real data.
- read or use real Tenhou, real haifu, external logs or platform data.
- add production code, tests, fixtures or data files.
- add broad file ingestion or CLI.
- implement feature extraction, label generation or dataset construction.
- integrate model outputs.
- produce model-strength, Tenhou ranked, stable-dan, LuckyJ `10.68` or
  candidate-promotion evidence.
- approve P9-P12 entry.

## P8 Workstream Inventory

| workstream | current_status | approved_now | entry_prerequisites | evidence_required | main_risks | forbidden_current_scope | notes |
|---|---|---:|---|---|---|---|---|
| P8 scope / entry criteria planning | current docs-only definition | yes, docs-only | reviewed P8-P12 transition scope | `12I`, later review gate, governance sync | mistaken for P8 entry approval | implementation, self-play, training, evaluation | This document selects a review gate next. |
| P8 risk / evidence taxonomy | not started | no | review of `12I` | taxonomy doc, review, risk/evidence sync | evidence overclaim | model-strength claims, training, self-play | Candidate later docs-only task. |
| self-play / RL dependency mapping | not approved | no | P8 scope review and risk taxonomy | dependency map, review, approval decision | self-play creep, invalid objectives | self-play execution, RL implementation | P8 label only until separately approved. |
| training dependency mapping | not approved | no | source/training-data boundary and P8 review | training dependency record | premature training | training, tuning, checkpoints | Must not start from smoke evidence alone. |
| model-output dependency mapping | not approved | no | model artifact and adapter boundaries | model-output boundary doc and review | treating outputs as strength | model-output integration | Later approval required. |
| evaluation dependency mapping | not approved | no | approved protocol / evidence taxonomy | evaluation dependency record | LuckyJ / stable-dan overclaim | evaluation implementation or runner | Diagnostics are not strength evidence. |
| real-data / source-rights dependency mapping | not approved | no | source-rights / privacy / platform-policy review | source approval record | data rights and platform risk | real data, Tenhou, haifu, external logs | No current real source approval. |
| league dependency boundary | not approved | no | evaluation protocol, candidate promotion rules | league boundary and review | league/ranking overclaim | league runner or match harness | P10 roadmap item, not P8 approval. |
| model-strength evidence boundary | not approved | no | approved evaluation protocol and data source | evidence schema, uncertainty, warnings | false strength claims | strength claims | No current model-strength evidence. |
| P9-P12 non-entry boundary | not approved | no | P8 reviewed scope and separate later stage reviews | stage boundary records | stage jump | search, league, large-scale training, Tenhou validation | P9-P12 remain unapproved. |
| governance / risk / evidence synchronization | current docs-only planning | yes, docs-only | current task completion | handoff, index, risk, evidence, decisions | governance mismatch | approvals beyond docs | Required for every step. |

## P8 Risk Controls

| risk | control |
|---|---|
| P8 scope is mistaken for P8 entry approval. | State in `12I`, `10_NEXT`, handoff, evidence log, risk register and decision record that this is scope-definition evidence only. |
| P8 entry criteria are mistaken for implementation approval. | Require a separate review gate and later explicit approval decision before any executable task. |
| P8 stage label is mistaken for self-play approval. | State that `self-play reinforcement learning` is a roadmap label, not execution permission. |
| Full P7 closure is mistaken for training readiness. | Preserve `03BL` closure boundary: documented P7 supervised-learning scope only. |
| Synthetic/local smoke evidence is overclaimed. | Classify smoke artifacts as guardrail/schema evidence only, not training or model-strength evidence. |
| Source approval gap is skipped. | Require source-rights, provenance, privacy and platform-policy review before real-data work. |
| Real-data / platform / account risk appears too early. | Keep Tenhou, haifu, platform data, external logs and account/session material forbidden. |
| Training or tuning creep. | Keep training-data approval and training-run approval as separate future gates. |
| Self-play creep. | Require self-play / RL dependency map, risk review and approval before execution. |
| League creep. | Keep league as a later separately approved workstream. |
| Evaluation creep. | Require approved evaluation protocol and evidence taxonomy before evaluation work. |
| Model-output integration creep. | Require adapter / model-output boundary and approval before integration. |
| Model-strength overclaim. | Require approved protocol, sample-size / uncertainty treatment and evidence log before claims. |
| Tenhou / stable-dan / LuckyJ overclaim. | Keep ranked evidence and LuckyJ comparison as later-stage, separately approved evidence only. |
| Candidate promotion overclaim. | Require racing-funnel alignment and explicit promotion decision record. |
| P9-P12 creep. | Keep P9-P12 out of current P8 planning unless separately scoped and reviewed. |
| Governance mismatch. | Synchronize `10_NEXT`, handoff, index, technical plan, evidence, risk, changelog, decisions, milestones and backlog. |
| `10_NEXT` drift. | Keep exactly one first unchecked task and make it a docs-only review gate. |

## P8 Evidence Requirements

Future P8 evidence records must include:

- `evidence_id`.
- `p8_workstream`.
- `scope_status`.
- `entry_status`.
- `approval_status`.
- `self_play_status`.
- `rl_status`.
- `training_status`.
- `evaluation_status`.
- `model_output_status`.
- `source_status`.
- `real_data_status`.
- `league_status`.
- `model_strength_status`.
- `validation_commands`.
- `risk_reference`.
- `decision_reference`.
- `evidence_grade`.
- `explicit_non_evidence_warning`.

Current evidence grade:

```text
P8 scope, entry criteria and first planning task definition evidence only.
```

It is not model-strength evidence, Tenhou ranked evidence, stable-dan
ranked-game evidence, LuckyJ `10.68` comparison evidence, candidate-promotion
evidence, source approval, training approval, evaluation approval, self-play
approval or league approval.

## Candidate Next Directions

| candidate | status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| Review P8 scope, entry criteria and first planning task after P8-P12 transition-scope review. | selected | checks this document before any later P8 planning | low if docs-only | none | yes | no | low | low | selected |
| Define P8 risk and evidence taxonomy before any implementation. | not selected now | useful next planning artifact | should follow review of `12I` | review of `12I` | yes | no | medium | low | defer |
| Define P8 self-play / RL dependency map before any implementation. | not selected now | clarifies self-play prerequisites | may be mistaken for self-play approval | risk/evidence taxonomy | yes | no | medium | low | defer |
| Prepare P8 entry approval decision. | rejected now | could accelerate entry | too early; criteria not reviewed | `12I` review and taxonomy/dependency work | yes | no | high | medium | reject now |
| Start P8 implementation. | forbidden | none now | stage jump | multiple entry criteria | no | no | high | high | forbidden |
| Start training / tuning. | forbidden | none now | training without approval | source/training/eval approvals | no | no | high | high | forbidden |
| Start self-play / league. | forbidden | none now | invalid evidence / compute drift | self-play/league scopes | no | no | high | high | forbidden |
| Start real-data / Tenhou work. | forbidden | none now | source-rights / platform risk | source/privacy/platform review | no | no | high | high | forbidden |
| Start model-output integration / model-strength evidence work. | forbidden | none now | overclaim | adapter/eval/evidence approvals | no | no | high | high | forbidden |
| Define P9-P12 scope. | rejected now | later useful | jumps beyond P8 | P8 planning and review | yes | no | medium | high | reject now |

## Recommended First Planning Task

The recommended next first task is:

```text
Review P8 scope, entry criteria and first planning task after P8-P12 transition-scope review.
```

That next task must be a docs-only review gate. It must not approve P8 entry,
approve implementation, generate a prompt, train, evaluate, run self-play,
run league, approve source work, use real data, integrate model output,
claim strength or enter P9-P12.

## Planning Decision

```text
P8 scope, entry criteria and first planning task are defined after P8-P12 transition-scope review.
```

This decision defines the P8 planning boundary and conservative entry
criteria. It does not approve P8 entry, P8 implementation, a P8
implementation prompt, training, tuning, evaluation, self-play, league,
source approval, source ingestion, real data, model-output integration,
model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison, candidate promotion or P9-P12 entry.

## Validation

Validation for this task must include:

- `git diff --check`
- `python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py`
- `python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py`
- `python3 -m unittest tests/supervised/test_feature_label_schema.py`
- `python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `python3 -m unittest tests/data/test_replay_schema.py`
- `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`

Results are recorded in `docs/09_governance/09_EVIDENCE_LOG.md`.
