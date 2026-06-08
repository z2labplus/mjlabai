# 03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK

## Scope

This document defines P7 supervised-learning scope, entry criteria and the
first task candidate before implementation.

This is a docs-only P7 scoping task. It does not implement P7, execute the
first P7 task, approve training, approve data ingestion, approve parser /
dataset-reader work, approve feature extraction, approve label generation,
approve model-output integration, approve real Tenhou / real haifu /
external-log / platform-data use, approve CLI / broad ingestion, approve
self-play, approve league behavior or approve P8-P12 entry.

## Post-Full-P6 Context

| context_item | status | notes |
|---|---|---|
| P5 evaluation groundwork | closed for current synthetic/local scope | `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md` closes only the current synthetic/local evaluation groundwork scope. |
| full P6 data-system scope | closed for documented scope only | `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md` closes docs/governance/source-rights planning, accepted synthetic/local minimal replay schema and project-authored fixture smoke implementation, and deferred/blocked/later-stage inventory. |
| post-full-P6 transition review | complete | `docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md` allows only docs-only P7 scope / entry criteria / first-task definition. |
| P7 implementation | not approved | Full P6 closure does not approve supervised-learning code, training, model architecture, parser, reader, ingestion, feature extraction or label generation. |
| P8-P12 entry | not approved | Later stages need separate transition review, scope, entry criteria, risk review and first-task approval. |

## P7 Purpose

P7 is the supervised-learning stage. Its future role is to build a base
strategy policy from approved data, approved features and approved labels, then
make that policy eligible for later evaluation and improvement gates.

Relationship to the north-star target:

- The north-star target remains long-term Tenhou performance above LuckyJ,
  with stable dan greater than `10.68`.
- P7 supports that target indirectly by preparing a supervised base policy.
- P7 scoping is not model-strength evidence.
- P7 scoping does not produce a model.
- P7 scoping does not train or evaluate model strength.
- Future P7 implementation must still pass data/source, risk, feature/label
  and evaluation gates before any claim or downstream stage transition.

## P7 Allowed Docs-Only Scope

| scope_item | allowed_definition | implementation_allowed_now | evidence_required_later | notes |
|---|---|---:|---|---|
| P7 purpose | define supervised-learning purpose and north-star relationship | no | reviewed P7 scope doc | Purpose must stay tied to Tenhou-like long-term performance. |
| P7 entry criteria | define requirements before any implementation | no | reviewed entry-criteria checklist | Defining criteria does not satisfy them. |
| P7 exit criteria draft | draft future completion conditions | no | future P7 closure review | Draft only; not satisfied now. |
| upstream artifacts | list required P5/P6 artifacts and current status | no | docs index / evidence log | Full P6 closure is prerequisite context, not implementation approval. |
| forbidden scope | list disallowed work | no | stage contract / risk register | Must prevent premature training and ingestion. |
| data readiness | define required future data approvals | no | source-rights review and data policy | No real source is approved by this document. |
| source rights | define license/permission prerequisites | no | source-specific rights evidence | Synthetic/local P6 fixture remains the only accepted current data artifact. |
| parser / reader / ingestion dependency | define future dependency requirements | no | explicit later task approval | Parser, reader and ingestion remain unapproved. |
| feature extraction readiness | define future feature-boundary requirements | no | feature schema/review task | No features are created here. |
| label generation readiness | define future label-boundary requirements | no | label schema/review task | No labels are created here. |
| model architecture planning | define planning boundary only | no | reviewed architecture proposal | No model code or config is added. |
| training-loop planning | define planning boundary only | no | reviewed training proposal | No optimizer, loss, trainer or dataloader is added. |
| validation / evaluation dependency | define dependency on P5-style evidence | no | future validation commands and offline reports | Supervised loss alone must not be enough. |
| risk review | define P7 risk review requirements | no | updated risk register | Risks must be reviewed before implementation. |
| evidence requirements | define future evidence fields | no | evidence log updates | Evidence grade remains planning-only now. |
| first task candidate | name next docs-only review gate | no | `10_NEXT` review item | Next task must not be implementation. |
| P8-P12 boundary | define non-entry guardrail | no | later transition review | P7 scoping does not approve later stages. |

## P7 Forbidden Scope

| forbidden_item | reason | earliest_possible_condition | guardrail |
|---|---|---|---|
| training implementation | requires approved data, features, labels, model design and risk review | after P7 implementation task approval | `10_NEXT` must explicitly approve exact training scope. |
| model architecture implementation | architecture is not yet reviewed for P7 | after architecture proposal/review | No model code or config now. |
| loss / optimizer / trainer implementation | training loop is not approved | after training-loop boundary review | No optimizer, loss, trainer or dataloader now. |
| data loader implementation | would imply dataset construction / ingestion | after data-source and split approvals | No dataloader now. |
| dataset construction | data source and rights are not approved for training | after source-rights and storage policy approval | No data files now. |
| parser | full P6 closure excluded parser approval | after separate parser scope approval | No parser code now. |
| dataset reader | full P6 closure excluded reader approval | after separate reader scope approval | No reader code now. |
| ingestion | real/source ingestion remains unapproved | after source-specific lawful approval | No ingestion code or commands now. |
| feature extraction | feature boundary not approved | after feature schema task | No feature extractor now. |
| label generation | label boundary not approved | after label schema task | No label generator now. |
| real Tenhou | platform/legal/privacy risks unresolved | after separate compliance/source review | No Tenhou data or accounts. |
| real haifu | source rights and privacy unresolved | after source-specific approval | No real logs. |
| external logs | provenance and rights unresolved | after source-specific approval | No external log ingestion. |
| platform data | platform terms/privacy unresolved | after compliance review | No platform data. |
| account/session/cookie/token | privacy/security risk | never without explicit lawful task | Forbidden now. |
| platform automation / scraping / evasion | compliance risk | only after explicit lawful clearance | Forbidden now. |
| model-output integration | would connect P5/P7 outputs prematurely | after separate integration boundary | Not allowed now. |
| CLI / broad ingestion | would become a data path | after explicit ingestion design | Not allowed now. |
| self-play / reinforcement learning | belongs to P8, not P7 scoping | after P8 transition and approval | Not allowed now. |
| league / runner | belongs to later evaluation/league stages | after P10 transition and approval | Not allowed now. |
| P8-P12 | later stages need separate gates | after separate transition reviews | Not approved by P7 scoping. |
| model-strength claims | no trained/evaluated model exists here | after valid P5/P10/P12 evidence | Forbidden now. |
| Tenhou ranked claims | no ranked evidence exists | after lawful P12 validation | Forbidden now. |
| LuckyJ comparison | no stable-dan ranked evidence exists | after P12 evidence and review | Forbidden now. |
| candidate promotion | no promotion evidence exists | after funnel gate evidence | Forbidden now. |

## P7 Entry Criteria Before Implementation

| criterion | required_before_implementation | current_status | evidence_needed | blocker | notes |
|---|---:|---|---|---|---|
| full P6 closed for documented scope | yes | satisfied for documented P6 scope | `02AA` | none for docs-only scoping | Does not approve P7 implementation. |
| post-full-P6 transition review complete | yes | satisfied | `12D` | none for docs-only scoping | Allows only this scope-definition task. |
| P7 scope / entry criteria / first task defined | yes | defined by this document | this document | pending review | Must be reviewed next. |
| P7 scope reviewed | yes | not yet | future `Review P7 scope...` task | open | Required before implementation prompt. |
| source-rights status reviewed | yes | not satisfied for training data | source-specific review | open | Current synthetic fixture is not a training dataset. |
| selected data source approved | yes | not selected / not approved | source inventory update | open | No real Tenhou or external source approved. |
| parser / reader / ingestion readiness reviewed or scoped out | yes | not satisfied | parser/reader/ingestion boundary review | open | Can be scoped out only for an explicitly synthetic-only task. |
| feature extraction boundary approved | yes | not satisfied | feature-boundary doc/review | open | No feature extractor now. |
| label generation boundary approved | yes | not satisfied | label-boundary doc/review | open | No label generator now. |
| training data policy approved | yes | not satisfied | data policy + split policy | open | Must cover leakage and hidden information. |
| storage / Git policy approved | yes | partially established | artifact/checkpoint policy | open | No weights/checkpoints in Git. |
| privacy / platform terms risk reviewed | yes | not satisfied for real data | compliance/risk review | open | Required for real or platform-derived data. |
| evidence log and risk register updated | yes | updated for this scoping task | evidence/risk docs | none for docs-only | Must continue for future tasks. |
| validation commands defined | yes | defined for this task | `10_NEXT` | none for docs-only | Future implementation needs task-specific validation. |
| first P7 implementation task explicitly approved in `10_NEXT` | yes | not approved | later `10_NEXT` item | open | This document recommends review, not implementation. |
| human / Web ChatGPT approval recorded | yes | not recorded for implementation | Web review prompt/decision | open | Required before implementation. |
| implementation prompt lists exact allowed files and forbidden expansions | yes | not present | later implementation prompt | open | No implementation prompt now. |
| P8-P12 non-entry reaffirmed | yes | satisfied by this document | this document / stage contract | none | Later stages remain closed. |

## P7 Exit Criteria Draft

| exit_criterion | future_evidence_needed | current_status | notes |
|---|---|---|---|
| supervised-learning scope implemented only after approval | approved implementation tasks and validation | not started | No implementation now. |
| data/source rights satisfied | source license/permission records | not satisfied | Real/external sources remain unapproved. |
| parser/reader/ingestion/feature/label dependencies resolved or scoped out | reviewed dependency docs | not satisfied | Synthetic-only exceptions must be explicit. |
| minimal synthetic/local SL fixture or approved dataset boundary validated | fixture/schema/test evidence | not satisfied | No P7 fixture added now. |
| training pipeline implemented after approval | code review and tests | not started | No trainer now. |
| artifact provenance and checksum policy defined before artifact use | artifact policy and checksums | not satisfied | No weights/checkpoints now. |
| offline evaluation dependency established | P5/P7 compatible report evidence | partially available from P5 | Future P7 must map to existing evaluation guardrails. |
| evidence/risk/handoff/10_NEXT synchronized | governance docs | ongoing | This task updates planning docs only. |
| no model-strength claims without P5/P10/P12 evidence | evidence review | ongoing | Supervised loss is not enough. |
| P7 final closure review completed before P8 | final P7 review | not started | P8 remains unapproved. |

## P7 Required Inputs And Current Status

| input | required_for_future_implementation | current_status | blocker | notes |
|---|---:|---|---|---|
| data source | yes | not selected for P7 training | source approval | P6 synthetic fixture is not training data. |
| source rights / license / permission | yes | not approved for training data | rights review | Must be source-specific. |
| replay schema | yes | minimal synthetic/local schema accepted | parser/real-data scope absent | Current schema validates in-memory synthetic mappings only. |
| parser / dataset reader | usually yes | not implemented / not approved | separate approval required | May be scoped out only for explicit synthetic-only task. |
| ingestion pipeline | usually yes | not implemented / not approved | source/data policy | No broad ingestion. |
| feature extraction | yes | not defined / not approved | feature-boundary review | Hidden-information guardrails needed. |
| label generation | yes | not defined / not approved | label-boundary review | Must avoid leakage and overfitting to unsupported targets. |
| train/validation split policy | yes | not defined | data policy | Must prevent train/test and temporal/source leakage. |
| model architecture boundary | yes | only early placeholder docs exist | architecture proposal/review | Existing `03A_MODEL_ARCHITECTURE.md` is not implementation approval. |
| training configuration boundary | yes | not defined | training proposal/review | Must cover loss, optimizer, seeds and resources. |
| evaluation metrics / offline envelope | yes | P5 groundwork exists | P7 mapping not defined | Must include legality and Tenhou-oriented metrics. |
| risk register | yes | active | P7-specific risks added by this task | Must be reviewed before implementation. |
| evidence log | yes | active | future evidence fields needed | This task adds planning evidence only. |
| storage / checkpoint policy | yes | partially covered by no-large-artifact rule | artifact policy | No weights or checkpoints may be committed. |
| validation commands | yes | current docs-only commands defined | future task commands needed | Implementation commands must be task-specific. |

## P7 Risk Review Requirements

| risk | mitigation | current_status | owner_doc_or_followup | notes |
|---|---|---|---|---|
| P7 scoping mistaken for implementation approval | require review gate before implementation | open | `10_NEXT`, this document | This task defines only. |
| supervised-learning training before data/source approval | require source-rights and training-data policy | open | future source/data task | No training now. |
| real data used without rights review | require source-specific approval | open | source inventory / risk register | No real data now. |
| platform data / account data leakage | forbid accounts, sessions, cookies, tokens | open | compliance/risk docs | No platform data now. |
| parser / reader / ingestion scope creep | separate each as explicit task | open | future boundary docs | Not approved now. |
| feature / label leakage | require feature/label review and leakage tests | open | future P7 feature/label tasks | Hidden information risk is high. |
| hidden-information leakage | define observation boundary before features | open | future feature schema | Must match player-visible information. |
| train/test leakage | require split policy before training | open | future data policy | No split policy now. |
| model artifact provenance ambiguity | require artifact source, checksum and storage policy | open | future artifact policy | No checkpoints now. |
| checkpoint / weights committed accidentally | enforce no-large-artifact rule and checksums outside Git | open | storage policy / AGENTS | Existing rule already forbids weights in repo. |
| training results overclaimed as model strength | require P5/P10/P12 evidence before strength claims | open | evaluation docs | Loss/accuracy are proxies only. |
| skipping P5/P6 evidence boundaries | keep evidence grades explicit | open | evidence log / stage contract | P5/P6 closures are bounded. |
| stage creep into P8 RL or P10 league | require separate transition reviews | open | `10_NEXT`, stage contract | P8-P12 not approved. |
| LuckyJ comparison overclaim | require ranked evidence and stable-dan protocol | open | P5/P12 docs | P7 cannot compare to LuckyJ. |
| candidate promotion overclaim | require racing-funnel gate evidence | open | funnel docs / evidence log | No candidate promotion now. |

## P7 Evidence Requirements

Future P7 evidence must record, when applicable:

- data source id.
- source rights / license / permission.
- schema version.
- parser / reader version if later approved.
- feature version.
- label version.
- split policy.
- model architecture version.
- training config.
- random seeds.
- dependency versions.
- validation commands.
- metric outputs.
- artifact checksums.
- known exclusions.
- failure modes.
- evidence grade.
- explicit non-evidence warning.

Current evidence grade:

```text
P7 scope / entry criteria / first-task definition evidence only.
```

## P8-P12 Non-Entry Boundary

P7 scoping does not approve:

- P8 reinforcement learning.
- P9 search / risk model implementation.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou validation.

Future P7 closure also must not automatically approve P8-P12. Each later stage
needs a separate transition review, scope, entry criteria, risk review and
first-task approval.

## First Task Candidate

Recommended next task:

```text
Review P7 scope, entry criteria and first task before implementation.
```

The next task should be docs-only. It must not implement training code, model
architecture, dataset reader, parser, feature extraction, label generation,
real Tenhou dataset use, self-play, league behavior, model-output integration
or P8-P12 entry.

## Review Status

`docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`
reviews this scope, entry criteria and first-task definition. The review
decision is:

```text
Review can close.
```

The review does not approve P7 implementation, P7 first-task execution,
training, parser, dataset reader, ingestion, feature extraction, label
generation, real Tenhou, real haifu, external logs, platform data,
model-output integration, CLI, self-play, league or P8-P12 entry. The next
task remains docs-only and moves to P7 supervised-learning data/source
readiness inventory before implementation.

`docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
defines that inventory. It records that no source is currently approved for P7
training, source ingestion, parser / reader / ingestion, feature extraction or
label generation. It is inventory-definition evidence only, not source
approval, training-data approval or implementation approval.

## Planning Decision

```text
P7 scope, entry criteria and first task are defined for review before
implementation. This does not approve P7 implementation, training, data
ingestion, parser, dataset reader, feature extraction, label generation,
model-output integration, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
P7 scope / entry criteria / first-task definition evidence only.
```

## Explicit Non-Evidence

This document is not:

- P7 implementation.
- P7 first-task execution.
- P8-P12 entry approval.
- training.
- tuning.
- self-play.
- league.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- parser.
- dataset reader.
- data ingestion.
- feature extraction.
- label generation.
- model-output integration.
- CLI.
- broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
