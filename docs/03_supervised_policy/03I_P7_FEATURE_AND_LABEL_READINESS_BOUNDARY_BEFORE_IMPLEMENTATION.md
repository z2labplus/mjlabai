# 03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION

## Purpose

This document defines the P7 supervised-learning feature and label readiness
boundary before implementation.

This is a docs-only P7 boundary definition. It exists to prevent feature
extraction, label generation, parser work, dataset-reader work, ingestion,
training and model-output integration from starting before the project has a
reviewed leakage policy and a reviewed source / provenance boundary.

This document does not approve:

- P7 implementation.
- P7 first-task execution.
- feature extraction.
- label generation.
- parser, dataset reader or ingestion.
- source approval or training-data approval.
- supervised dataset construction.
- model architecture, dataloader, optimizer, loss, trainer or checkpoint work.
- real Tenhou, real haifu, external-log or platform-data use.
- model-output integration.
- CLI or broad file ingestion.
- training, tuning, self-play, league or runner behavior.
- P8-P12 entry.
- model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claims.

## Context

P5 is closed only for the current synthetic/local evaluation groundwork scope.
Full P6 is closed only for the documented P6 data-system scope: docs /
governance / source-rights planning, accepted synthetic/local minimal replay
schema and project-authored synthetic fixture smoke implementation, and
deferred / blocked / later-stage inventory.

P6 closure does not approve P7 training data, source ingestion, parser,
dataset reader, feature extraction, label generation, real data,
model-output integration or P8-P12 entry.

`docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
records that no source is currently approved for P7 training, source
ingestion, parser / reader / ingestion, feature extraction or label
generation.

`docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`
reviews that inventory and records:

```text
Review can close.
```

The next safe step is to define feature and label readiness boundaries before
any P7 implementation task.

## Feature Readiness Boundary

Before any future feature extraction implementation can be approved, a later
task must record and review all of the following:

| requirement | required boundary before implementation |
|---|---|
| `source_id` | Stable source id assigned and linked to source inventory. |
| source category | Category must be approved for the requested use, not merely listed. |
| source rights | Rights, license / terms, allowed use, forbidden use and storage policy reviewed. |
| privacy / platform terms | Privacy, platform terms, account/session/cookie/token and automation risks reviewed. |
| parser / reader / ingestion status | Parser, dataset reader and ingestion boundaries must be explicit, approved or explicitly not required for a synthetic-only task. |
| schema version | Replay / decision schema version recorded. |
| feature version | Feature schema version recorded before any extraction output is produced. |
| feature family list | Exact candidate feature families listed and reviewed. |
| public-information-only policy | Feature inputs must be limited to information available to the acting player at the decision time. |
| hidden-info exclusion | Opponent concealed hands, wall order, future draws and any unavailable private state must be excluded. |
| future-info leakage policy | Future draws, future discards, future calls, final score and final placement must not appear as decision-time features. |
| turn / action timing boundary | The observation timestamp and action target timestamp must be explicit. |
| seat / round / score visibility | Dealer, round, honba, riichi sticks, scores, placement and turn index may be considered only as visible context. |
| hand visibility | Acting player's visible hand representation must not include opponent concealed tiles. |
| discard / call / riichi visibility | Discard ponds, open melds, riichi declarations and similar public events must be timestamped and decision-time visible. |
| dora visibility | Dora indicators may be included only when publicly visible at the decision time. |
| derived feature policy | Derived features must declare raw inputs and leakage checks. |
| raw vs derived storage | Raw decision records and derived features must have separate versions and provenance. |
| train / validation split leakage | Split policy must prevent same-game, same-source, temporal or near-duplicate leakage. |
| validation command plan | Future implementation must name validation commands before code starts. |
| evidence / risk update plan | Evidence log and risk register updates must be planned. |
| human / Web ChatGPT approval | Required before any feature extraction implementation. |
| explicit `10_NEXT` implementation task | Implementation is allowed only if it becomes the first unchecked task. |

Current task approval:

```text
No feature extraction implementation is approved by this document.
```

## Label Readiness Boundary

Before any future label generation implementation can be approved, a later
task must record and review all of the following:

| requirement | required boundary before implementation |
|---|---|
| label source policy | Every label source must be named, versioned and linked to an approved source category. |
| allowed candidate label types | Candidate label types may be defined now, but none are approved for generation now. |
| forbidden label types | Labels from unapproved real data, hidden information, future information, model outputs, self-play or league outputs remain forbidden unless a later task approves them. |
| human-authored label boundary | Human labels need author/source rights, protocol, annotation version and leakage review. |
| generated label boundary | Generated labels need source approval, generator version, deterministic settings, provenance and validation. |
| model-output label boundary | Model outputs are not approved as labels before a later policy explicitly permits them. |
| action imitation label boundary | Action imitation labels require approved action source, legal action mapping and decision-time observation boundary. |
| value / reward target boundary | Value or reward targets require future-outcome leakage policy and stage approval. |
| future outcome leakage policy | Future score, placement, draw sequence or post-decision events must not leak into decision-time labels unless explicitly framed as a future target with separated use. |
| hidden-info leakage policy | Labels must not require hidden opponent hands or unavailable private state unless a later oracle-style task explicitly approves a separated diagnostic use. |
| train / test leakage policy | Label grouping and splits must avoid same-game and near-duplicate leakage. |
| label provenance | Label source, version, generator / annotator, schema version and timestamp must be recorded. |
| label validation | Future implementation must include validation commands and failure behavior. |
| evidence / risk review | Evidence and risk entries must be updated before implementation is accepted. |
| human / Web ChatGPT approval | Required before any label generation implementation. |
| explicit `10_NEXT` implementation task | Implementation is allowed only if it becomes the first unchecked task. |

Current task approval:

```text
No label generation implementation is approved by this document.
```

## Candidate Feature Families

All candidate feature families in this table are allowed to be defined for
planning only. None are approved for implementation now.

| candidate_feature_family | allowed_to_define_now | implementation_allowed_now | source_dependency | hidden_information_risk | leakage_risk | required_before_implementation | notes |
|---|---:|---:|---|---|---|---|---|
| round / honba / riichi-stick context | yes | no | approved decision source | low if public | medium if timestamp wrong | source approval, timing policy, schema version | Public table context only. |
| seat / dealer / turn index | yes | no | approved decision source | low if public | medium if turn order leaks future | source approval, timing policy | Must be decision-time state. |
| visible hand tile counts | yes | no | approved source with acting player's hand | medium | high if opponent hidden tiles included | hidden-info exclusion, public-info validation | Acting player's hand only. |
| visible discard pond | yes | no | approved decision source | low if timestamped | high if future discards included | event timestamp policy, validation | Public discards up to decision only. |
| visible calls / melds | yes | no | approved decision source | low if public | medium if future calls included | call timestamp policy, schema version | Open melds only. |
| visible dora indicators | yes | no | approved decision source | low if visible | medium if unrevealed indicators included | visibility policy, validation | Publicly visible indicators only. |
| score / placement context | yes | no | approved decision source | low if public | high if final result included | decision-time score policy | No final score as decision feature. |
| legal action mask candidate | yes | no | approved legal-action source or synthetic fixture | medium | high if generated from future state | legal-action boundary, rule-source review | Not current legal-action checker approval. |
| previous action context | yes | no | approved event source | low if public | medium if future events included | timestamp and event-order validation | Only events before decision. |
| synthetic-only provenance indicators | yes | no | project-authored synthetic context | low | medium if used as training shortcut | provenance policy, train split policy | Planning only; not training approval. |

## Candidate Label Families

All candidate label families in this table are allowed to be defined for
planning only. None are approved for generation now.

| candidate_label_family | allowed_to_define_now | implementation_allowed_now | source_dependency | leakage_risk | required_before_implementation | notes |
|---|---:|---:|---|---|---|---|
| action imitation label | yes | no | approved decision/action source | high if source or timing unapproved | source approval, observation boundary, label version | Not approved now. |
| discard choice label | yes | no | approved dahai decision source | high if legal-action context leaks | action schema, feature boundary, split policy | Candidate only. |
| call / no-call label | yes | no | approved call decision source | high if non-decision events mixed | call decision schema, source approval | Not current action scope. |
| riichi / no-riichi label | yes | no | approved riichi decision source | high if future outcomes used | riichi timing schema, leakage policy | Candidate only. |
| legal action target label | yes | no | approved legal-action source | medium | legal-action source policy, validator boundary | Diagnostic only until approved. |
| synthetic smoke label | yes | no | project-authored synthetic fixture | medium if mistaken for training data | fixture boundary, review gate | Smoke labels are not training labels. |
| future value / reward target | yes | no | approved outcome source | very high | future-outcome target policy, stage approval | Not current P7 implementation. |
| future ranking / placement target | yes | no | approved outcome source | very high | outcome source approval, split policy | Not decision-time feature. |
| generated pseudo-label | yes | no | approved generator and source | high | generator version, provenance, validation | Model-output policy required. |
| human-authored annotation label | yes | no | approved annotation protocol | medium-high | annotator rights, protocol, quality checks | Not approved now. |

## Forbidden Feature / Label Scope

The following are forbidden unless a later explicit task changes the boundary
after review:

- Hidden opponent hands.
- Wall order or unrevealed future draws.
- Future discards, future calls or future riichi declarations.
- Final score or final placement as a decision-time feature.
- Any information unavailable to the acting player at the decision time.
- Labels from unapproved real data.
- Labels from model outputs before a model-output label policy exists.
- Labels from self-play or league outputs before P8 / P10 approval.
- Labels requiring parser, reader or ingestion before those are approved.
- Labels that imply training data approval without source approval.
- Any feature or label from real Tenhou, real haifu, external logs or platform
  data before source-specific approval.
- Account, session, cookie, token or online-platform private data.
- Third-party binaries, weights, params, checkpoints or snapshots as feature
  or label sources without a later lawful artifact review.

## Dependency Map

Future feature / label implementation must follow this dependency order:

```text
data/source readiness inventory
-> source approval
-> parser / reader / ingestion boundary
-> replay schema
-> feature boundary
-> label boundary
-> train / validation split policy
-> leakage policy
-> evidence / risk update plan
-> future implementation proposal
-> approval decision
-> exact implementation task in docs/10_next/10_NEXT.md
```

If any dependency is missing, implementation remains blocked.

## Risks

| risk | mitigation | current_status | owner_doc_or_followup | notes |
|---|---|---|---|---|
| hidden-information leakage | Define public-information-only feature policy and hidden-info exclusion before code. | open | `03I`, future feature review | Highest P7 feature risk. |
| future-information leakage | Require action timestamp, decision timestamp and future-event exclusion. | open | `03I`, future leakage policy | Future outcomes cannot become decision-time features. |
| train/test leakage | Require split policy before dataset construction. | open | future split policy | Same-game leakage must be blocked. |
| labels from unapproved source | Keep all label families not approved for implementation now. | open | `03I`, future source approval | Source approval must precede labels. |
| synthetic fixture mistaken as training source | Repeat synthetic smoke / docs context warnings. | open | `03G`, `03I`, risk register | Synthetic fixtures are not training data. |
| docs context mistaken as data | Classify docs as planning context only. | open | `03G`, `03I` | Docs are not datasets. |
| generated labels mistaken as ground truth | Require generator version, provenance and validation. | open | future label policy | Pseudo-labels need separate approval. |
| model outputs used too early | Keep model-output labels forbidden until a later policy. | open | future model-output label boundary | No model-output integration now. |
| feature extraction creeps into parser / ingestion | Require separate parser / reader / ingestion approval. | open | future parser / ingestion boundary | No ingestion in this task. |
| label generation creeps into training | Require separate implementation task and training policy. | open | future label review | Label generation is not training approval. |
| P7 feature/label boundary mistaken for implementation approval | Explicitly classify `03I` as boundary definition only. | open | `03I`, `10_NEXT` | Next task is review, not implementation. |
| model-strength overclaim | Evidence grade remains boundary definition evidence only. | open | evidence log, ranking protocol | No strength evidence here. |
| P8/P10 stage creep | Keep self-play / league / runner outputs forbidden. | open | stage contract | P8-P12 require separate transition reviews. |

## Evidence Requirements

Future P7 feature / label evidence must record:

- `source_id`.
- schema version.
- feature version.
- label version.
- feature family.
- label family.
- public-information-only validation.
- hidden-information exclusion validation.
- future-information exclusion validation.
- train / validation split validation.
- provenance.
- validation commands.
- evidence log reference.
- risk register reference.
- known exclusions.
- explicit non-evidence warning.

Evidence entries must state whether the artifact is planning context, synthetic
smoke context, implementation evidence, source approval evidence, training-data
approval evidence, feature extraction evidence or label generation evidence.

This document is only:

```text
P7 feature and label readiness boundary definition evidence only.
```

## Readiness Vocabulary

Use the following vocabulary for future P7 feature and label readiness:

| status | meaning |
|---|---|
| `docs_boundary_defined` | Boundary is defined in docs only. |
| `not_approved_for_implementation` | Implementation is not allowed now. |
| `blocked_by_missing_source_approval` | Source rights or allowed-use approval is missing. |
| `blocked_by_missing_parser_reader_ingestion` | Parser, reader or ingestion boundary is missing or unapproved. |
| `blocked_by_missing_feature_boundary_review` | Feature boundary has not passed review. |
| `blocked_by_missing_label_boundary_review` | Label boundary has not passed review. |
| `blocked_by_leakage_policy` | Hidden-info, future-info or split-leakage policy is missing or insufficient. |
| `requires_human_web_chatgpt_approval` | Human / Web ChatGPT approval is required before implementation. |
| `implementation_allowed_only_after_explicit_10_NEXT_task` | Implementation is allowed only when the exact task is first unchecked in `docs/10_next/10_NEXT.md`. |

None of these statuses means current feature extraction approval or current
label generation approval.

## Next Task Recommendation

If this document lands without blocker, the next P7 task should be:

```text
Review P7 feature and label readiness boundary before implementation.
```

That next task must be a docs-only review gate. It must not implement feature
extraction, label generation, parser, dataset reader, ingestion, training,
model-output integration, CLI, broad file ingestion or P8-P12 work.

## Review Status

`docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`
reviews this boundary and records:

```text
Review can close.
```

That review confirms this boundary is sufficient for the current docs-only P7
review gate. It does not approve P7 implementation, P7 first-task execution,
training data source, source ingestion, parser, dataset reader, ingestion,
feature extraction, label generation, real Tenhou, real haifu, external logs,
platform data, model-output integration, CLI, self-play, league or P8-P12
entry.

`docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`
now defines the follow-up P7 risk and evidence taxonomy. That taxonomy is also
docs-only and does not approve feature extraction, label generation, source
approval, training or P8-P12 entry.

## Planning Decision

```text
P7 feature and label readiness boundary is defined before implementation. This does not approve P7 implementation, feature extraction, label generation, parser, dataset reader, ingestion, training, real data, model-output integration, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
P7 feature and label readiness boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

- P7 implementation.
- P7 first-task execution.
- P8-P12 entry.
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
- feature extraction implementation.
- label generation implementation.
- source approval.
- training-data approval.
- model-output integration.
- CLI.
- broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
