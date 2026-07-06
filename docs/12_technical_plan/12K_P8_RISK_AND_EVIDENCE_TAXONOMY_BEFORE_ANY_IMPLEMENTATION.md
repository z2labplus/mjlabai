# 12K_P8_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_ANY_IMPLEMENTATION

## Scope

This document defines the P8 risk and evidence taxonomy before any
implementation.

This is a docs-only taxonomy definition. It is not:

- P8 entry approval.
- P8 implementation approval.
- a P8 implementation prompt.
- a P8 first executable task.
- P9-P12 entry approval.
- training, tuning, evaluation, self-play, league or reinforcement-learning
  execution.
- source approval or source ingestion.
- real data, real Tenhou, real haifu, external logs or platform data.
- broad file ingestion or CLI.
- feature extraction, label generation or supervised dataset construction.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

North-star relationship: this taxonomy supports the long-term Tenhou
stable-dan `> 10.68` target only by defining risk and evidence vocabulary
before any later P8 work can request approval. It is not evidence that any
model can beat LuckyJ.

## Full P7 / P8 Scope Recap

- Full P7 closed only for the documented P7 supervised-learning scope.
- `12F`, `12G` and `12H` established P8-P12 docs-only transition planning.
- `12I` defined P8 scope, entry criteria and the first planning task.
- `12J` reviewed `12I` and recorded `A. Review can close`.
- P8 remains docs-only planning.
- P8 entry remains unapproved.
- P8 implementation remains unapproved.
- P9-P12 remain unapproved.

## P8 Non-Approval Baseline

Current baseline:

- P8 entry remains unapproved.
- P8 implementation remains unapproved.
- P8 first executable task remains unapproved.
- P8 implementation prompt remains unapproved.
- P9-P12 remain unapproved.
- No self-play evidence exists.
- No RL evidence exists.
- No league evidence exists.
- No training evidence exists.
- No evaluation evidence exists.
- No model-output evidence exists.
- No model-strength evidence exists.
- No real-data permission exists.
- No source-ingestion permission exists.

## Risk Taxonomy

| risk_id | risk_name | description | current_status | severity | blocked_by | required_controls | evidence_required | forbidden_current_action | notes |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Scope / entry approval confusion | Planning docs are mistaken for P8 entry approval. | open | high | `12K` review and later approval chain | explicit non-approval text in every gate | scope definition and review evidence | P8 entry approval | Current docs-only scope is not entry. |
| R2 | Implementation creep | Taxonomy or planning drifts into code, tests, fixtures or data. | open | high | exact approval decision | `10_NEXT` single-task control | approval-decision evidence | implementation | No code/test/data changes now. |
| R3 | Self-play / RL execution creep | P8 label is mistaken for self-play or RL execution permission. | open | high | self-play / RL dependency map and approval | separate protocol, risk review and approval | self-play protocol evidence | self-play or RL execution | P8 label is a roadmap label only. |
| R4 | Training / tuning creep | P8 planning is used to start training or tuning. | open | high | training-data and training-run approvals | training-data gate, run gate, artifact policy | training-run evidence | training or tuning | No training data is approved. |
| R5 | Evaluation / benchmark creep | Diagnostics or planning become evaluation claims. | open | high | evaluation protocol approval | sample-size, leakage and uncertainty controls | evaluation protocol evidence | evaluation runner or benchmark | No strength evaluation exists. |
| R6 | Model-output integration creep | Model outputs are read or integrated before approval. | open | high | model-output boundary approval | adapter/output schema and evidence warnings | model-output integration evidence | model-output path | Current artifacts have no model outputs. |
| R7 | Model-strength overclaim | Planning or smoke tests are described as model strength. | open | high | approved evaluation protocol | evidence-grade vocabulary and warnings | model-strength evidence | strength claim | No current artifact supports this. |
| R8 | Source approval / source ingestion gap | Source work proceeds without rights/provenance approval. | open | high | source-rights review | source inventory, allowed-use and privacy review | source-rights evidence | source approval or ingestion | No real source is approved. |
| R9 | Real-data / platform / account risk | Real Tenhou, haifu, platform or account data appears early. | open | high | platform/privacy review | no account/session/cookie/token handling | source and compliance evidence | real data or platform access | Forbidden in current scope. |
| R10 | Feature / label / dataset dependency ambiguity | P7 smoke helpers are mistaken for real feature/label/dataset readiness. | open | high | feature/label/dataset approvals | dependency map and leakage guardrails | dependency-map evidence | feature tensors, labels, dataset | Current helpers are guardrail summaries only. |
| R11 | Reward hacking / objective mismatch risk | Future RL optimizes proxy reward instead of Tenhou EV/rank outcomes. | not started | high | reward/eval boundary | reward design review, evaluation alignment | RL dependency evidence | reward implementation | Must align with Tenhou pt EV, rank and stable dan. |
| R12 | Self-play collapse / overfitting risk | Future self-play overfits to narrow policies or collapses. | not started | high | opponent-pool protocol | diversity, checkpoints, regression monitoring | self-play protocol/result evidence | self-play run | No opponent pool is approved. |
| R13 | Opponent-pool / league bias risk | Future league/opponent setup creates biased promotion evidence. | not started | high | league boundary | opponent pool, uncertainty and promotion controls | league protocol evidence | league runner | P10 later-stage work. |
| R14 | Reproducibility / stochasticity risk | Future P8 runs cannot be reproduced. | not started | medium | run protocol | seeds, configs, versions, commands, env logs | validation and run evidence | stochastic run without record | Needed before any run. |
| R15 | Compute / resource escalation risk | Future training/self-play consumes resources before gates justify it. | not started | high | training-run approval | budget, stop conditions, artifact policy | approval-decision evidence | large compute run | No compute escalation now. |
| R16 | Safety / governance / auditability mismatch | Governance docs disagree or miss a decision. | open | high | governance sync | update handoff, index, evidence, risk, decisions, backlog | governance evidence | silent scope changes | `10_NEXT` remains control surface. |
| R17 | P9-P12 scope creep | P8 planning leaks into search, league, large-scale training or Tenhou validation. | open | high | separate stage scopes | explicit P9-P12 non-entry warnings | stage-boundary evidence | P9-P12 work | P9-P12 are unapproved. |
| R18 | Tenhou / stable-dan / LuckyJ / promotion overclaim | P8 evidence is overclaimed as final target evidence. | open | high | approved evaluation and promotion protocol | evidence-grade gate and review | ranked / stable-dan / comparison evidence | Tenhou / LuckyJ / promotion claim | No current evidence supports these claims. |
| R19 | Third-party artifact / binary / model-weight risk | Unknown weights or binaries enter the workflow. | open | high | artifact policy | checksum, license, provenance and approval | artifact evidence | use unknown weights/binaries | Forbidden now. |
| R20 | `10_NEXT` / governance drift | The first unchecked task drifts into implementation without approval. | open | high | `10_NEXT` hygiene | one first task, explicit limits, validation | governance sync evidence | implementation task without approval | Stop if `10_NEXT` drifts. |

## Evidence Taxonomy

| evidence_family_id | name | allowed_current_status | future_use | required_prerequisites | cannot_support | risk_controls | notes |
|---|---|---|---|---|---|---|---|
| E1 | Scope definition evidence | allowed | Defines scope boundaries. | docs-only task | implementation or strength claims | non-approval warnings | `12I` is this class. |
| E2 | Scope review evidence | allowed | Reviews scope sufficiency. | scope doc | implementation or entry approval | review decision language | `12J` is this class. |
| E3 | Risk/evidence taxonomy evidence | allowed now | Defines risk and evidence vocabulary. | reviewed P8 scope | implementation or strength claims | taxonomy review next | This document is E3. |
| E4 | Risk/evidence taxonomy review evidence | not yet | Reviews this taxonomy. | this document | implementation or entry approval | review gate | Next safe task. |
| E5 | Dependency-map evidence | future only | Maps self-play/RL/training/eval dependencies. | taxonomy reviewed | execution permission | dependency review | Not available now. |
| E6 | Dependency-map review evidence | future only | Reviews dependency map. | dependency map | implementation approval | review gate | Not available now. |
| E7 | Approval-decision evidence | future only | Approves or rejects exact next task. | proposal/review | work outside exact scope | exact file/task limits | None for P8 now. |
| E8 | Exact implementation evidence | future only | Shows exact approved implementation occurred. | approval decision | broader implementation | exact-file review | None for P8 now. |
| E9 | Implementation review evidence | future only | Reviews exact implementation. | implementation artifact | acceptance by itself | review checklist | None for P8 now. |
| E10 | Test / validation evidence | existing limited | Supports exact code-path validation. | test command | strength, Tenhou, LuckyJ | evidence-grade warnings | Current tests are smoke/guardrail evidence only. |
| E11 | Source-rights evidence | future only | Supports source eligibility. | source inventory/review | training/eval by itself | rights/privacy review | No source approved now. |
| E12 | Source-ingestion evidence | future only | Supports exact ingestion behavior. | source approval | arbitrary broad ingestion | parser/ingestion boundary | Not available now. |
| E13 | Training-data approval evidence | future only | Supports using data for training. | source, ingestion, feature/label, leakage approvals | training run by itself | separate approval | Not available now. |
| E14 | Training-run evidence | future only | Records approved training run. | run approval | model strength by itself | config/artifact logging | Not available now. |
| E15 | Self-play protocol evidence | future only | Defines self-play setup. | dependency map, approval | self-play result by itself | reproducibility / stop conditions | Not available now. |
| E16 | Self-play result evidence | future only | Records approved self-play outputs. | protocol and run approval | Tenhou or LuckyJ claim by itself | sample/report guardrails | Not available now. |
| E17 | League protocol evidence | future only | Defines league / opponent pool. | evaluation and promotion protocols | promotion by itself | uncertainty and anti-bias controls | P10 later-stage. |
| E18 | Evaluation protocol evidence | future only | Defines evaluation metrics/sample rules. | model-output/source boundaries | result claim by itself | sample-size / uncertainty | Not available now. |
| E19 | Model-output integration evidence | future only | Shows model outputs are integrated. | adapter/output approval | strength by itself | output schema and warnings | Not available now. |
| E20 | Model-strength evidence | future only | Supports strength claims under approved protocol. | evaluation protocol, model output, sample size | Tenhou/LuckyJ by itself | uncertainty and leakage review | None now. |
| E21 | Tenhou ranked evidence | future only | Supports real ranked Tenhou claims. | compliance, source, protocol | LuckyJ comparison by itself | platform and safety review | None now. |
| E22 | Stable-dan evidence | future only | Supports stable-dan estimates. | approved evidence source and uncertainty | LuckyJ proof by itself | CI/sample rules | None now. |
| E23 | LuckyJ comparison evidence | future only | Supports target comparison. | stable-dan evidence and protocol | broad superiority by itself | final validation review | None now. |
| E24 | Candidate-promotion evidence | future only | Supports funnel promotion. | racing-funnel criteria and eval evidence | final target proof | decision record | None now. |
| E25 | Governance synchronization evidence | allowed | Shows docs stayed aligned. | any gate completion | technical merit or strength | changelog/evidence/risk sync | Required every gate. |

## Evidence Grade Vocabulary

Allowed now:

- P8 scope definition evidence only.
- P8 scope review evidence only.
- P8 risk/evidence taxonomy definition evidence only.
- governance synchronization evidence only.
- existing synthetic/local guardrail validation evidence only.

Future-only grades:

- P8 risk/evidence taxonomy review evidence only.
- P8 dependency-map evidence only.
- P8 approval-decision evidence only.
- P8 exact implementation evidence only.
- P8 implementation review evidence only.
- P8 validation evidence only.
- P8 self-play protocol evidence only.
- P8 self-play result evidence only.
- P8 evaluation protocol evidence only.
- P8 model-output integration evidence only.
- P8 model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison evidence.
- candidate-promotion evidence.

Current task evidence grade:

```text
P8 risk/evidence taxonomy definition evidence only.
```

No model-strength evidence exists now.

## Current Evidence Classification

| artifact_or_class | classification | cannot_support |
|---|---|---|
| P7 closure evidence | historical prerequisite evidence only | P8 performance or strength claims |
| `12G` / `12H` | P8-P12 transition planning / review evidence only | P8-P12 entry approval |
| `12I` / `12J` | P8 scope definition / review evidence only | P8 implementation approval |
| This `12K` document | P8 risk/evidence taxonomy definition evidence only | P8 entry or implementation |
| Accepted synthetic/local P7 smoke helpers | local guardrail validation evidence only | training data, real data, model strength |
| Existing unit tests | validation evidence for exact synthetic/local code paths only | policy quality or Tenhou evidence |
| Current repository state | no self-play, RL, model-strength, Tenhou ranked, stable-dan, LuckyJ comparison or candidate-promotion evidence | any strength claim |

## P8 Workstream Risk / Evidence Matrix

| workstream | risk families | evidence required | current evidence | current status | approved_now | blocked_by | forbidden_current_scope | next safe gate |
|---|---|---|---|---|---:|---|---|---|
| P8 scope / entry planning | R1, R16, R20 | E1, E2, E25 | `12I`, `12J` | reviewed | yes, docs-only | none | implementation | taxonomy definition |
| P8 risk/evidence taxonomy | R1-R20 | E3, later E4, E25 | this document | definition in progress | yes, docs-only | review | implementation | taxonomy review |
| Self-play/RL dependency mapping | R3, R11, R12, R14, R15 | E5, E6, E15 | none | not started | no | taxonomy review | self-play/RL execution | dependency-map definition |
| Training dependency mapping | R4, R10, R14, R15 | E5, E6, E13, E14 | none | not started | no | source/data/model boundaries | training/tuning | dependency-map definition |
| Model-output dependency mapping | R6, R7 | E5, E6, E19 | none | not started | no | model artifact/output boundary | model-output integration | dependency-map definition |
| Evaluation dependency mapping | R5, R7, R18 | E5, E6, E18 | none | not started | no | evaluation protocol boundary | evaluation runner | dependency-map definition |
| Real-data / source-rights dependency mapping | R8, R9, R19 | E11, E12 | none | not started | no | source/privacy/platform review | real data / ingestion | source dependency definition |
| League dependency boundary | R13, R18 | E17, E24 | none | later-stage | no | evaluation and promotion protocols | league runner | later P10 scope |
| Model-strength evidence boundary | R5, R7, R18 | E18, E19, E20 | none | not started | no | evaluation/source/model-output approvals | strength claims | evidence boundary definition |
| P9-P12 non-entry boundary | R17, R18 | stage-boundary evidence | `12G`, `12H`, `12I`, `12J` | unapproved | no | separate stage reviews | P9-P12 work | later stage scope review |
| Governance / risk / evidence synchronization | R16, R20 | E25 | governance docs | active | yes, docs-only | continuous sync | silent approvals | every gate |

## Model-Strength Evidence Boundary

No current artifact is model-strength evidence.

Future model-strength evidence requires:

- approved evaluation protocol.
- approved model-output path.
- approved sample definition.
- sufficient sample-size / uncertainty method.
- leakage controls.
- governance review.
- separate approval decision.

Synthetic/local smoke evidence and unit tests cannot be used as
model-strength evidence.

## Tenhou / Stable-Dan / LuckyJ / Promotion Boundary

No current artifact is:

- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison evidence.
- candidate-promotion evidence.

Future such evidence requires separate protocol, source approval, sample
definition, uncertainty method, leakage review and governance approval.

## Source / Real-Data / Platform Boundary

No current source is approved for P8 self-play, RL, training, evaluation,
real-data use or platform-data use.

Future source work requires:

- source-rights review.
- platform / privacy / account-policy review.
- source approval decision.
- ingestion boundary.
- validation protocol.
- evidence logging.

## Self-Play / RL Boundary

No self-play is approved now. No RL execution is approved now. No opponent
pool is approved now. No league is approved now. No training loop is approved
now.

Future self-play/RL work requires:

- dependency map.
- risk/evidence review.
- source/model-output/evaluation boundary.
- approval decision.
- exact implementation scope.
- validation and review.

## Stop Conditions

Stop if any task:

- implies P8 entry approval.
- implies P8 implementation approval.
- generates an implementation prompt.
- runs training or tuning.
- runs self-play.
- runs league.
- uses real data.
- uses Tenhou / haifu / platform data.
- approves source ingestion.
- emits model-output integration.
- claims model strength.
- claims Tenhou / stable-dan / LuckyJ / promotion evidence.
- enters P9-P12.
- creates production code.
- creates tests, fixtures or data.
- downloads or uses unknown model artifacts.
- vendors third-party binaries.
- calls Akochan `system.exe`, `libai.so` or another third-party binary.
- changes `10_NEXT` to an implementation task without approval.

## Candidate Next Directions

| candidate | status | benefits | risks | blocked_by | docs_only | implementation_approval | P8_entry_risk | P9_P12_risk | decision |
|---|---|---|---|---|---:|---:|---|---|---|
| Review P8 risk and evidence taxonomy before any implementation. | selected | Checks this taxonomy before dependency mapping. | low if docs-only | none | yes | no | low | low | selected |
| Define P8 self-play / RL dependency map before any implementation. | deferred | Useful next dependency step. | may imply self-play approval if taxonomy is unreviewed | taxonomy review | yes | no | medium | low | defer |
| Define P8 training / model-output / evaluation dependency map. | deferred | Clarifies downstream gates. | may bundle too many workstreams | taxonomy review | yes | no | medium | low | defer |
| Prepare P8 entry approval decision. | rejected now | Could accelerate entry. | too early; no reviewed taxonomy or dependency map | multiple entry criteria | yes | no | high | medium | reject |
| Draft P8 implementation proposal. | rejected now | Could define exact files later. | premature implementation path | entry/dependency approvals | yes | no | high | medium | reject |
| Start P8 implementation. | forbidden | none now | stage jump | all P8 gates | no | no | high | high | forbidden |
| Start training / tuning. | forbidden | none now | unapproved data/run | training approvals | no | no | high | high | forbidden |
| Start self-play / league. | forbidden | none now | unapproved protocol/result | self-play/league approvals | no | no | high | high | forbidden |
| Start real-data / Tenhou work. | forbidden | none now | compliance and source risk | source/platform review | no | no | high | high | forbidden |
| Start model-output integration / model-strength evidence work. | forbidden | none now | overclaim | model-output/eval approval | no | no | high | high | forbidden |
| Define P9-P12 scope. | rejected now | Later useful. | jumps beyond P8 | P8 planning and review | yes | no | medium | high | reject |

## Recommended First Planning Task

The next first task should be:

```text
Review P8 risk and evidence taxonomy before any implementation.
```

That next task must be a docs-only review gate. It must not approve P8 entry,
approve P8 implementation, generate a P8 implementation prompt, train,
evaluate, run self-play, run league, approve source work, use real data,
integrate model output, claim strength or enter P9-P12.

## Planning Decision

```text
P8 risk and evidence taxonomy is defined before any implementation.
```

This task does not approve P8 entry, P8 implementation, any P8 implementation
prompt, training, tuning, evaluation, self-play, league, source approval,
source ingestion, real data, model-output integration, model-strength
evidence, Tenhou ranked evidence, stable-dan evidence, LuckyJ `10.68`
comparison, candidate promotion or P9-P12 entry. The next safe task is a
docs-only review of this risk/evidence taxonomy.

## Evidence Grade

```text
P8 risk/evidence taxonomy definition evidence only.
```

## Explicit Non-Evidence

This document is not:

- P8 entry approval.
- P8 implementation approval.
- P8 implementation prompt.
- P9-P12 entry approval.
- training.
- tuning.
- evaluation.
- self-play.
- league.
- source approval.
- source ingestion.
- real data.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- model-output integration.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

## Validation

Validation for this task must include:

```text
git diff --check
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Results:

```text
git diff --check: passed.
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py: passed, 15 tests.
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py: passed, 11 tests.
python3 -m unittest tests/supervised/test_feature_label_schema.py: passed, 11 tests.
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py: passed, 1 test.
python3 -m unittest tests/data/test_replay_schema.py: passed, 7 tests.
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py: passed, 1 test.
```
