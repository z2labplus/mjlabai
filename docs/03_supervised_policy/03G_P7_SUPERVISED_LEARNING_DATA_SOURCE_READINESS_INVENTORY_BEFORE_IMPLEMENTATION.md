# 03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION

## Scope

This document defines the P7 supervised-learning data/source readiness
inventory before implementation.

This is P7 docs-only readiness groundwork. It only inventories future
supervised-learning data/source requirements, current readiness gaps, blockers,
deferred categories and approval requirements.

This document does not approve:

- P7 implementation.
- P7 first-task execution.
- training data source selection.
- source ingestion.
- parser, dataset reader or ingestion.
- feature extraction or label generation.
- real Tenhou, real haifu, external logs or platform data.
- model-output integration.
- CLI or broad file ingestion.
- self-play, league or runner behavior.
- P8-P12 entry.

## Post-P7-Scoping Context

`docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
defines P7 scope, entry criteria and the first task candidate before
implementation.

`docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`
reviews that definition and records:

```text
Review can close.
```

P5 is closed only for the current synthetic/local evaluation groundwork scope.
Full P6 is closed only for the documented P6 data-system scope:
docs/governance/source-rights planning, accepted synthetic/local minimal
replay schema, project-authored synthetic fixture smoke implementation, and
deferred / blocked / later-stage inventory.

Full P6 closure does not approve P7 training data, source ingestion, parser,
dataset reader, feature extraction, label generation, real data,
model-output integration or P8-P12 entry.

## Candidate Data / Source Categories

| candidate_category | current_status | allowed_for_docs_planning | approved_for_training | approved_for_ingestion | approved_for_feature_label | source_rights_status | privacy_platform_risk | required_before_use | blocker | notes |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| project-authored synthetic/local fixture from P6 | docs_context_only | yes | no | no | no | project_authored for smoke context only | none expected, synthetic/local | explicit future synthetic-only P7 task if ever used; must not be treated as training data | no training approval | `tests/fixtures/data/synthetic_replay_smoke.json` validates schema shape only and says not training data. |
| repository documentation | docs_context_only | yes | no | no | no | project docs | none expected | none for planning; cannot become dataset | not data | Docs are governance/context only. |
| future project-authored synthetic supervised-learning fixture | not_ready_for_training | yes as future planning | no | no | no | not created / not reviewed | none expected if project-authored synthetic | fixture boundary, schema smoke test, source note, review gate and explicit `10_NEXT` approval | missing fixture boundary and review | Could support future smoke tests only, not strength claims. |
| future approved real replay source | blocked_by_source_rights | restricted planning only | no | no | no | source-specific rights unknown | privacy/platform review required | source id, owner, license/terms, allowed use, storage policy, privacy review, parser/reader/ingestion boundary, feature/label boundary, split policy, evidence/risk entries, human/Web approval and explicit `10_NEXT` task | no approved source | Candidate category only; no source is selected. |
| real Tenhou / ranked logs | blocked_by_privacy_or_platform_terms | no except risk discussion | no | no | no | platform terms / source rights unapproved | high | lawful source-specific review, platform terms review, privacy review and no account/session/cookie/token risk | real Tenhou unapproved | No Tenhou access, scraping, automation or account tooling. |
| real haifu / external logs | blocked_by_source_rights | restricted risk planning only | no | no | no | rights/provenance unknown | privacy review required | source-specific allowed-use evidence, storage policy, parser/reader/ingestion boundary and approval | external source unapproved | Do not read or ingest real haifu or external logs. |
| platform data / online account data | blocked_by_privacy_or_platform_terms | no except risk boundary | no | no | no | platform/account rights unapproved | high | separate lawful compliance review; account/session/cookie/token use remains forbidden now | platform/account data blocked | No platform automation, scraping, evasion or account tooling. |
| model outputs / self-play / league outputs | deferred_later_stage | planning only as later-stage category | no | no | no | not applicable until later stages | depends on future source | P8/P10/P11 scope, provenance, generation config, evidence/risk review and explicit approval | later-stage unapproved | Not current P7 input and not current label source. |
| third-party open-source references | docs_context_only | yes as methodology/reference | no | no | no | external license review required | depends on source | license review and explicit scope before any use beyond reference | reference only | Mortal/Akochan/Kanachan/Suphx may inform design but are not training data. |
| third-party binaries / weights / params / checkpoints | prohibited_artifact | no except risk note | no | no | no | external/unknown or restricted | artifact/provenance risk | explicit lawful artifact review; do not download/vendor/use now | prohibited | Includes `system.exe`, `libai.so`, `params/`, `*.pth`, `*.pt`, checkpoints and snapshots. |
| human-authored labels or annotations | not_ready_for_training | planning only | no | no | no | author/rights not defined | privacy/leakage review required | annotation source rights, labeling protocol, hidden-information policy, split policy, evidence/risk review and explicit approval | no label policy | No supervised labels are approved. |
| generated labels from future approved pipeline | blocked_by_missing_label_boundary | planning only | no | no | no | depends on source and generator | leakage/provenance risk | approved source, parser/reader/ingestion, feature boundary, label boundary, generator version, leakage policy and validation | no pipeline | No generated labels are approved. |

## Currently Approved For P7 Training

```text
None.
```

No current source is approved for P7 training.

The P6 project-authored synthetic/local fixture can be used as documentation
and schema context only. It is not training dataset approval.

Repository documentation can be used for planning and governance context only.
It is not training data.

Real Tenhou, real haifu, external logs and platform data are not approved.
Model outputs, self-play outputs and league outputs are not approved.
Third-party binaries, weights, params and checkpoints are not approved and must
not be downloaded, vendored, committed or used.

Human-authored labels and generated labels are not approved.

## Readiness Status Vocabulary

Use the following statuses for P7 data/source readiness:

| status | meaning |
|---|---|
| `docs_context_only` | May be referenced in documentation and planning only. Not data approval. |
| `not_ready_for_training` | Potential future category, but not approved for training. |
| `blocked_by_source_rights` | Rights, ownership, license or allowed use is unresolved. |
| `blocked_by_privacy_or_platform_terms` | Privacy, platform terms, account or compliance risk blocks use. |
| `blocked_by_missing_parser_reader_ingestion` | Parser, dataset reader or ingestion boundary is missing or unapproved. |
| `blocked_by_missing_feature_boundary` | Feature extraction boundary and hidden-information policy are missing. |
| `blocked_by_missing_label_boundary` | Label generation or annotation boundary is missing. |
| `deferred_later_stage` | Belongs to P8-P12 or a later approved task, not current P7 readiness. |
| `prohibited_artifact` | Must not be downloaded, vendored, committed or used in the repository now. |
| `requires_human_web_chatgpt_approval` | Requires explicit human/Web ChatGPT approval before any implementation. |
| `implementation_allowed_only_after_explicit_10_NEXT_task` | Cannot proceed unless it becomes the first task in `docs/10_next/10_NEXT.md`. |

No readiness status means current training approval.

## Training-Data Readiness Requirements

Before any future training data source can be approved, the project must record:

| requirement | required_status_before_training_use |
|---|---|
| `source_id` | stable source id assigned |
| source owner / rightsholder | documented |
| license / terms summary | documented and reviewed |
| allowed use | explicit and compatible with training |
| forbidden use | explicit |
| raw / derived storage policy | documented |
| `may_enter_git` | explicit; raw real data should not enter Git |
| privacy / platform terms review | complete when applicable |
| automation / scraping risk review | complete and safe |
| source-specific approval | recorded |
| parser / reader / ingestion boundary | defined, reviewed and approved or explicitly scoped out |
| feature extraction boundary | defined and reviewed |
| label generation boundary | defined and reviewed |
| train / validation split policy | defined |
| leakage prevention policy | defined |
| hidden-information policy | defined |
| evidence log reference | created |
| risk register reference | created |
| validation commands | defined |
| human / Web ChatGPT approval | recorded |
| explicit implementation task in `10_NEXT` | first unchecked item before any implementation |

If any requirement is missing, the source is not approved for training,
ingestion, feature extraction or label generation.

## Source-Rights Consistency With P6

P7 inherits the P6 source-rights guardrails:

- `docs/02_data_system/02A_DATA_SOURCES.md` remains the source-rights baseline.
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
  confirms the P6 inventory guardrails.
- `docs/02_data_system/02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE.md`
  found no risk/source-rights blocker for P6 closure but did not approve real
  data, source ingestion, parser, dataset reader, feature extraction or label
  generation.
- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md` closes full P6
  only for the documented P6 data-system scope.
- Full P6 closure does not approve P7 training data.
- Real, external and platform sources remain blocked until source-specific
  rights, privacy, platform terms, storage and evidence reviews approve them.
- The P6 synthetic/local replay fixture must not be used as P7 training
  approval.

## Parser / Reader / Ingestion Dependency Status

Current status:

- no parser is approved.
- no dataset reader is approved.
- no ingestion path is approved.
- no broad file ingestion is approved.
- no CLI data path is approved.

P7 cannot consume real, external or platform data without future approvals for:

- source-specific rights and allowed use.
- parser boundary.
- dataset reader boundary.
- ingestion boundary.
- storage policy.
- evidence and risk records.

If a future P7 task is explicitly synthetic-only, it must state whether parser,
reader and ingestion are not required. That synthetic-only scoping still needs
review and must not become real-data ingestion.

## Feature / Label Readiness Status

Current status:

- no feature extraction boundary is approved.
- no label generation boundary is approved.
- no supervised labels are approved.
- no labels from real data are approved.
- no hidden-information leakage policy is approved for training.
- no train/test leakage policy is approved.
- no split policy is approved.

P7 cannot train until feature and label readiness are defined and reviewed.

Future feature/label work must address:

- visible-state boundary.
- hidden-information exclusion.
- action and decision target definitions.
- train/validation split policy.
- temporal/source leakage prevention.
- label provenance.
- label-generation versioning if generated labels are used.
- evaluation mapping to P5 guardrails.

## P7 Data / Source Risks

| risk | mitigation | current_status | owner_doc_or_followup | notes |
|---|---|---|---|---|
| synthetic fixture mistaken for training data | repeat non-training warning in P7 readiness docs and next task | open | `03G`, `10_NEXT` | P6 fixture is schema context only. |
| docs context mistaken for dataset | classify repository docs as `docs_context_only` | open | `03G`, docs index | Docs are not training data. |
| source inventory mistaken for source approval | distinguish inventory from approval in `10_NEXT` | open | `03G`, risk register | No source approval here. |
| real data used without rights | require source owner, license/terms, allowed use and approval | open | future source-specific review | Blocks training and ingestion. |
| platform/account data leakage | forbid account/session/cookie/token data and automation | open | risk register / compliance follow-up | No platform data now. |
| parser/reader/ingestion creep | require separate explicit task and review | open | future parser/reader/ingestion boundary | No parser or reader now. |
| feature/label leakage | require feature/label boundary and leakage tests before training | open | future feature/label readiness task | Hidden-information risk remains high. |
| hidden-information leakage | define visible-state boundary before features | open | future feature boundary | Must match player-observable information. |
| train/test leakage | require split policy before training data construction | open | future data policy | No split policy now. |
| model outputs used as labels too early | defer model-output integration and generated labels | open | future model-output / label task | Not current P7 source. |
| third-party weights/binaries introduced | forbid unknown weights, binaries, params and artifacts | open | risk register / stage contract | No `*.pth`, `*.pt`, `system.exe`, `libai.so`, `params/`. |
| P7 training starts before data readiness | require data/source readiness review and explicit implementation task | open | `10_NEXT`, future review | No training now. |
| model-strength overclaim | keep evidence grade as readiness definition only | open | evidence log / ranking protocol | No strength evidence. |
| P8/P10 stage creep | require separate transition reviews for later stages | open | stage contract / future transition docs | P8-P12 remain closed. |

## P7 Data / Source Evidence Requirements

Future evidence entries for P7 data/source readiness must record:

- `source_id`.
- `source_category`.
- rights status.
- approval status.
- privacy / platform review status.
- parser / reader / ingestion status.
- feature boundary status.
- label boundary status.
- training use allowed.
- validation commands.
- evidence log reference.
- risk register reference.
- known exclusions.
- explicit non-evidence warning.

Evidence must also state whether the source is:

- planning context only.
- synthetic/local smoke context only.
- approved for training.
- approved for ingestion.
- approved for feature extraction.
- approved for label generation.

Unless explicitly approved by a later task, all sources remain not approved for
training.

## Planning Decision

```text
P7 supervised-learning data/source readiness inventory is defined before
implementation. It does not approve P7 implementation, P7 first-task execution,
training, source ingestion, parser, dataset reader, feature extraction, label
generation, real data, model-output integration, self-play, league or P8-P12
entry.
```

## Next Task Recommendation

Recommended next task:

```text
Review P7 supervised-learning data/source readiness inventory before implementation.
```

The next task should be docs-only. It must not approve P7 implementation,
P7 first-task execution, training data, source ingestion, parser, dataset
reader, feature extraction, label generation, real data, model-output
integration, CLI, self-play, league or P8-P12 entry.

## Evidence Grade

```text
P7 supervised-learning data/source readiness inventory definition evidence only.
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
- source approval.
- training-data approval.
- model-output integration.
- CLI.
- broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
