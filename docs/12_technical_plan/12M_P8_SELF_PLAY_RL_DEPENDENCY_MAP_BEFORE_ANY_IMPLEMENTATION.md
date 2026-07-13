# 12M_P8_SELF_PLAY_RL_DEPENDENCY_MAP_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 self-play / reinforcement-learning dependency
map before any implementation.

This is docs-only dependency-map definition evidence. It is not:

- P8 entry approval, P8 implementation approval, a P8 implementation prompt
  or a P8 first executable task.
- P9-P12 entry or implementation approval.
- production code, tests, fixtures or data files.
- self-play, reinforcement-learning execution, training, tuning, evaluation
  or league execution.
- source approval, source ingestion, real data, real Tenhou, real haifu,
  external logs or platform data.
- broad file ingestion, CLI, account/session/cookie/token handling, feature
  extraction, label generation or dataset construction.
- model-output integration, model-strength evidence, Tenhou ranked evidence,
  stable-dan evidence, LuckyJ `10.68` comparison or candidate promotion.

North-star relationship: this map supports the long-term Tenhou stable-dan
`> 10.68` target only by preventing future self-play / RL work from bypassing
required technical, evidence and governance gates. It is not evidence that a
model can beat LuckyJ.

## Full P7 / P8 Risk-Taxonomy Recap

- Full P7 closed only for the documented P7 supervised-learning scope.
- `12F`, `12G` and `12H` established and reviewed P8-P12 docs-only transition
  planning.
- `12I` defined P8 scope, entry criteria and the first planning task.
- `12J` reviewed `12I` and recorded `A. Review can close`.
- `12K` defined P8 risk families R1-R20 and evidence families E1-E25.
- `12L` reviewed `12K` and recorded `A. Review can close`.
- P8 remains docs-only planning. P8 entry and implementation remain
  unapproved. P9-P12 remain unapproved.

## P8 Self-Play / RL Non-Approval Baseline

- P8 entry, implementation, first executable task and implementation prompt
  remain unapproved.
- Self-play, RL execution, training, tuning, evaluation, league and
  model-output integration remain unapproved.
- P9-P12 remain unapproved.
- No self-play, RL, training, evaluation, league, model-output or
  model-strength evidence exists.
- No real-data permission or source-ingestion permission exists.

## Dependency Map Overview

Vocabulary:

- `required`: must be satisfied before the named future action; it does not
  mean approved now.
- `blocked`: cannot proceed until a separate review and approval resolves the
  blocker.
- `deferred`: intentionally postponed; it does not mean approved.
- `later-stage`: belongs to a later roadmap stage or gate.
- `out-of-scope`: forbidden in the current task.
- `not approved now`: no execution permission exists.
- `planning-only`: documentation may define the boundary without authorizing
  implementation.

Dependency definition does not approve a dependency. A required dependency is
still unapproved until its own review and approval record exists.

## P8 Self-Play / RL Dependency Families

| dependency_id | name | description | current_status | required_for | approved_now | blocked_by | evidence_required | risk_families | stop_condition | notes |
|---|---|---|---|---|---:|---|---|---|---|---|
| D1 | P8 scope / entry criteria | Defines what P8 could contain and when entry may be considered. | reviewed docs-only | any later P8 gate | no | separate entry decision | E1, E2, E25 | R1, R2, R16, R20 | stop if treated as entry | `12I` / `12J` are prerequisites, not approval. |
| D2 | P8 risk / evidence taxonomy | Defines risk and evidence vocabulary. | reviewed docs-only | all P8 planning | no | dependency-map review | E3, E4, E25 | R1-R20 | stop on evidence overclaim | `12K` / `12L` are prerequisites. |
| D3 | Self-play protocol | Future opponent, episode, seed, termination and logging rules. | blocked | self-play | no | protocol boundary and approval | E15 | R3, R12, R14, R15 | stop before any episode | No protocol exists now. |
| D4 | RL objective / reward specification | Future reward, objective and anti-reward-hacking rules. | blocked | RL and training | no | reward boundary and review | E5, future objective evidence | R3, R11, R14 | stop before reward implementation | Must align with Tenhou EV/rank metrics later. |
| D5 | Environment / simulator | Future deterministic legal environment interface and reproducibility boundary. | blocked | self-play and RL | no | environment boundary and validation | E5, E10 | R3, R12, R14 | stop before simulator execution | Existing P4/P5 context is not execution approval. |
| D6 | Model output | Future policy/value output schema and adapter boundary. | blocked | self-play, RL, evaluation | no | interface, schema, review and approval | E19 | R6, R7, R19 | stop before loading/calling a model | No model output path is approved. |
| D7 | Training / tuning | Future run config, optimizer, budget, stop and artifact rules. | blocked | RL updates | no | training-data and run approval | E13, E14 | R4, R14, R15, R19 | stop before any run | No training data or run is approved. |
| D8 | Evaluation protocol | Future metrics, samples, leakage, uncertainty and regression rules. | blocked | acceptance and strength claims | no | protocol boundary and approval | E18, later E20 | R5, R7, R18 | stop before evaluation runner | Existing diagnostics are not strength evidence. |
| D9 | Source / real data | Future provenance, rights, privacy and platform boundary. | blocked | any real-data use | no | source-rights and platform review | E11, E12 | R8, R9, R19 | stop on any real source access | No real source is approved. |
| D10 | Feature / label / dataset | Future training representation and leakage-safe dataset boundary. | blocked | training | no | exact approvals beyond P7 smoke scope | E5, E13 | R4, R10 | stop before tensor/label/dataset creation | P7 smoke helpers are not training data. |
| D11 | Opponent pool | Future diversity, checkpoint sampling and anti-collapse rules. | blocked | self-play | no | self-play protocol and artifact policy | E15 | R12, R13, R14 | stop before opponent selection | No opponent pool is approved. |
| D12 | League / candidate promotion | Future fair league, uncertainty and promotion rules. | later-stage | P10 promotion | no | evaluation and P10 scope | E17, E24 | R13, R17, R18 | stop before league/promotion | P10 work, not current P8. |
| D13 | Compute / reproducibility | Future seeds, versions, commands, environment and budget controls. | blocked | any executable run | no | exact run protocol and budget | E10, E14, E25 | R14, R15, R16 | stop if reproducibility/budget missing | No compute escalation is approved. |
| D14 | Checkpoint / artifact | Future provenance, checksum, license, retention and rollback rules. | blocked | model loading and training | no | artifact policy and approval | E14, E19 | R15, R19 | stop on unknown artifact | Unknown weights/binaries are forbidden. |
| D15 | Governance / `10_NEXT` / decisions | Exact task, review, approval and audit trail. | active docs-only | every gate | yes, docs-only only | continuous synchronization | E25, later E7 | R1, R2, R16, R20 | stop on silent scope change | Only the first unchecked task may run. |
| D16 | P9-P12 boundary | Keeps search, league, scale and Tenhou validation separate. | unapproved | later stages | no | separate stage scopes/reviews | stage-boundary evidence | R17, R18 | stop on stage jump | P9-P12 remain unapproved. |
| D17 | Safety / overclaim / evidence grade | Binds claims to reviewed evidence grades. | active docs-only | all P8 reporting | yes, docs-only only | future protocol evidence | E3-E6, E25 | R7, R16, R18 | stop on strength claim | Current grade is dependency-map evidence only. |
| D18 | Third-party artifact / binary / weight | Future external artifact provenance and permitted-use boundary. | blocked | any external integration | no | license, provenance, checksum and approval | artifact evidence | R9, R19 | stop before download/load/call | No `system.exe`, `libai.so` or unknown weight use. |

## Dependency Matrix

| dependency | current_status | self_play | RL | training | evaluation | approved_now | blocker | required_evidence | next_safe_gate | forbidden_current_action |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| P8 scope / taxonomy | reviewed docs-only | yes | yes | yes | yes | no | no entry decision | E1-E4, E25 | dependency-map review | infer P8 entry |
| self-play protocol | blocked | yes | yes | indirect | indirect | no | no protocol/review | E15 | protocol boundary after review | run self-play |
| RL objective / reward | blocked | indirect | yes | yes | indirect | no | no specification/review | dependency-map/objective evidence | objective boundary after review | implement reward/RL |
| environment / simulator | blocked | yes | yes | indirect | yes | no | no approved boundary | E5, E10 | environment boundary | run simulator |
| model output | blocked | yes | yes | yes | yes | no | no interface/schema approval | E19 | model-output boundary | call/load model |
| feature / label / dataset | blocked | indirect | yes | yes | indirect | no | P7 smoke is not training data | E13 | separate data approval chain | build tensors/dataset |
| training / tuning | blocked | indirect | yes | yes | indirect | no | no data/run approval | E13, E14 | training dependency boundary | train/tune |
| evaluation protocol | blocked | indirect | indirect | indirect | yes | no | no approved protocol | E18 | evaluation boundary | evaluate/benchmark |
| source / real data | blocked | no for synthetic planning | no for synthetic planning | possible future | possible future | no | rights/privacy/platform review | E11, E12 | source dependency review | access real data |
| opponent pool | blocked | yes | yes | indirect | indirect | no | no protocol/artifact approval | E15 | self-play protocol boundary | select/run opponents |
| league / promotion | later-stage | no | no | no | later | no | P10 scope/evaluation | E17, E24 | later P10 review | run league/promote |
| compute / reproducibility | blocked | yes | yes | yes | yes | no | no exact run/budget | E10, E14 | run-protocol boundary | consume run budget |
| checkpoint / third-party artifacts | blocked | yes | yes | yes | yes | no | no artifact approval | E14, E19 | artifact boundary | load/download artifacts |
| governance / evidence grade | active docs-only | yes | yes | yes | yes | docs-only | continuous sync | E25, later E7 | dependency-map review | silent approval/overclaim |
| P9-P12 boundary | later-stage | no | no | no | no | no | separate stage review | stage-boundary evidence | later transition review | enter P9-P12 |

## Required Dependencies Before Any Future P8 Implementation

- RD1. P8 scope is reviewed and closed.
- RD2. P8 risk/evidence taxonomy is reviewed and closed.
- RD3. This self-play / RL dependency map is defined and reviewed.
- RD4. A self-play protocol boundary is defined and reviewed.
- RD5. An RL objective / reward specification boundary is defined and
  reviewed.
- RD6. An environment / simulator boundary is defined and reviewed.
- RD7. A model-output dependency is defined and reviewed.
- RD8. Training / tuning dependencies are defined and reviewed.
- RD9. An evaluation protocol dependency is defined and reviewed.
- RD10. Source / real-data dependencies are classified and reviewed.
- RD11. Governance and `10_NEXT` explicitly authorize the exact future task.
- RD12. A separate approval decision exists before any implementation.

None of these dependencies are approved by this document.

## Blocked Dependencies

The following remain blocked: source approval; source ingestion; real Tenhou;
real haifu; external logs; platform data; account/session/cookie/token use;
training data; training runs; model-output integration; evaluation
implementation; self-play execution; RL execution; league; model-strength
evidence; P9-P12 work; third-party binaries and unknown model artifacts.

## Deferred Dependencies

Deferred, not approved:

- exact self-play protocol proposal.
- exact RL objective / reward proposal.
- environment / simulator boundary proposal.
- training / model-output / evaluation dependency follow-up.
- source-rights review.
- exact approval-decision path.

## Later-Stage / Out-of-Scope Dependencies

- P9 search / risk model.
- P10 model league and mainline selection.
- P11 large-scale training / stability validation.
- P12 Tenhou target validation.
- candidate promotion, Tenhou ranked evidence, stable-dan evidence and LuckyJ
  `10.68` comparison.

## Self-Play / RL Risk Linkage

| dependency area | linked 12K risks | required control |
|---|---|---|
| reward / objective | R3, R11 | objective review and alignment with later approved evaluation metrics |
| collapse / overfitting | R12 | opponent diversity, regressions and stop rules before execution |
| opponent pool / league bias | R13 | separate protocol, uncertainty and anti-bias review |
| reproducibility / stochasticity | R14 | seeds, configs, versions, commands and environment records |
| compute escalation | R15 | explicit budget and run approval |
| model-strength overclaim | R5, R7, R18 | evidence-grade enforcement and approved evaluation protocol |
| source / real data | R8, R9 | rights, privacy, platform and source approval |
| P9-P12 creep | R17 | separate stage scope and review |
| third-party artifacts | R19 | provenance, license, checksum and approval |
| governance drift | R1, R2, R16, R20 | one `10_NEXT` task, review and explicit decision records |

## Evidence Linkage

| dependency evidence | linked 12K evidence families | current status |
|---|---|---|
| scope / taxonomy prerequisites | E1-E4, E25 | reviewed docs-only |
| this dependency map | E5, E25 | defined by this document |
| dependency-map review | E6, E25 | not yet available |
| exact approval / implementation | E7-E9 | not available |
| source / training data / training run | E11-E14 | not available |
| self-play protocol / results | E15-E16 | not available |
| league / evaluation / model output | E17-E19 | not available |
| model strength / Tenhou / stable dan / LuckyJ / promotion | E20-E24 | not available |

This document is dependency-map evidence only. It is not approval,
implementation, self-play, RL, training, evaluation, model-output,
model-strength, Tenhou, stable-dan, LuckyJ or promotion evidence.

## Model-Output Dependency Boundary

No model-output integration is approved. Future work requires a model
interface boundary, output schema boundary, environment boundary, evaluation
boundary, risk/evidence review and exact approval decision.

## Evaluation Dependency Boundary

No evaluation implementation is approved. Future work requires an evaluation
protocol, metric and sample definitions, leakage and uncertainty controls,
governance review and exact approval decision.

## Source / Real-Data Dependency Boundary

No real data or source ingestion is approved. Future work requires a
source-rights review, platform/privacy/account-policy review, source approval
decision, ingestion boundary, validation protocol and evidence logging.

## Stop Conditions

Stop if a future task:

- implies P8 entry or implementation approval or generates an implementation
  prompt.
- runs self-play, RL, training, tuning, evaluation or league.
- uses real data, Tenhou, haifu, external logs, platform data or account
  material.
- approves source ingestion or emits model-output integration.
- claims model strength, Tenhou rank, stable dan, LuckyJ comparison or
  candidate promotion.
- enters P9-P12 or creates production code, tests, fixtures or data.
- downloads/uses unknown model artifacts, vendors third-party binaries or
  calls Akochan `system.exe` / `libai.so`.
- changes `10_NEXT` to an implementation task without a separate approval.

## Candidate Next Directions

| candidate | status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| A. Review this dependency map. | selected | validates completeness and non-approval boundaries | low if review-only | none | yes | no | low | low | selected |
| B. Define self-play protocol boundary. | deferred | clarifies future protocol | may imply execution | map review | yes | no | medium | low | defer |
| C. Define RL objective / reward boundary. | deferred | controls reward hacking | may imply RL approval | map review | yes | no | medium | low | defer |
| D. Define training/model-output/evaluation dependencies. | deferred | clarifies downstream gates | bundles broad workstreams | map review | yes | no | medium | low | defer |
| E. Prepare P8 entry approval decision. | rejected now | could advance stage | dependencies are unreviewed/unapproved | multiple entry criteria | yes | no | high | medium | reject |
| F. Draft P8 implementation proposal. | forbidden | none now | premature implementation | entry and exact approval | no | no | high | high | forbid |
| G. Start P8 implementation. | forbidden | none now | stage jump | all implementation gates | no | no | high | high | forbid |
| H. Start training / tuning. | forbidden | none now | no data/run approval | training gates | no | no | high | high | forbid |
| I. Start self-play / league. | forbidden | none now | no protocol/approval | self-play/league gates | no | no | high | high | forbid |
| J. Start real-data / Tenhou work. | forbidden | none now | rights/platform risk | source review | no | no | high | high | forbid |
| K. Integrate model output / claim strength. | forbidden | none now | evidence overclaim | model/evaluation approvals | no | no | high | high | forbid |
| L. Define P9-P12 scope. | rejected now | later useful | stage jump | P8 completion/review | yes | no | medium | high | reject |

Recommended next direction: A. Review P8 self-play / reinforcement-learning
dependency map before any implementation.

## Recommended First Planning Task

If no blocker is found, the next first task is:

```text
Review P8 self-play / reinforcement-learning dependency map before any implementation.
```

It must remain a docs-only review gate. It must not approve P8 entry,
implementation or an implementation prompt; run self-play, RL, training,
evaluation or league; approve source/ingestion/real data/model output; claim
model strength; or enter P9-P12.

## Planning Decision

```text
P8 self-play / reinforcement-learning dependency map is defined before any implementation.
```

This task does not approve P8 entry, P8 implementation, a P8 implementation
prompt, self-play execution, RL execution, training, tuning, evaluation,
league, source approval, source ingestion, real data, model-output integration,
model-strength evidence, Tenhou ranked evidence, stable-dan evidence, LuckyJ
`10.68` comparison, candidate promotion or P9-P12 entry. The next safe task is
a docs-only review of this dependency map.

## Evidence Grade

```text
P8 self-play / reinforcement-learning dependency map definition evidence only.
```

## Explicit Non-Evidence

This task is not P8 entry or implementation approval, an implementation
prompt, P9-P12 approval, training, tuning, evaluation, self-play, league, RL
execution, source approval/ingestion, real data, Tenhou/haifu/external/platform
data, model-output integration, model-strength evidence, Tenhou ranked
evidence, stable-dan evidence, LuckyJ `10.68` comparison or candidate
promotion.

## Validation

Validation for this docs-only task:

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```
