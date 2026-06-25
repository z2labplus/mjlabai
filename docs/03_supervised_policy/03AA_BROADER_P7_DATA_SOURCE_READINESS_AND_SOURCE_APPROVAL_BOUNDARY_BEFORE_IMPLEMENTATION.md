# 03AA Broader P7 Data Source Readiness And Source Approval Boundary Before Implementation

## Scope

This document defines broader P7 data/source readiness and source approval
boundary before implementation.

This is a docs-only boundary definition. It is not source approval,
training-data approval, source-ingestion approval, parser / reader / ingestion,
actual feature extraction, actual label generation, supervised dataset
construction, training, real-data use, broader P7 implementation approval or
P8-P12 entry.

## Purpose

This document exists to make broader P7 data/source work auditable before any
implementation starts.

It defines:

- data/source readiness vocabulary.
- source-specific approval boundary.
- training-use approval boundary.
- source-ingestion dependency.
- parser / reader / ingestion dependency.
- feature / label dependency.
- rights / provenance / storage / privacy / platform-terms requirements.
- future approval-record required fields.
- evidence and risk requirements for later source-specific decisions.

The main guardrail is simple:

```text
Readiness, inventory and docs context are not approved sources.
```

This supports the north-star target indirectly. A future supervised policy may
need approved, lawful and reproducible training sources before it can support
later RL, search, league and Tenhou validation stages. This document does not
train or evaluate a policy and is not model-strength evidence.

## Current Source Status

Current broader P7 source status:

- no source is approved for P7 training.
- no source is approved for source ingestion.
- no source is approved for actual feature extraction.
- no source is approved for actual label generation.
- the current synthetic/local supervised smoke fixture is not training data.
- repository docs are not training data.
- the P6 synthetic/local replay fixture is not a P7 training source.
- real Tenhou, real haifu, external logs and platform data remain blocked.
- model-output, self-play and league outputs remain unapproved.
- human-authored labels and generated labels remain unapproved.
- third-party binaries, weights, params, checkpoints and snapshots remain
  prohibited artifacts unless a later explicit review says otherwise.

## Source Category Inventory

| source_category | current_status | allowed_for_docs_planning | approved_for_training | approved_for_source_ingestion | approved_for_feature_extraction | approved_for_label_generation | rights_provenance_status | privacy_platform_risk | storage_policy_status | required_before_use | blocker | notes |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|---|---|
| current P7 synthetic/local feature-label smoke fixture | synthetic_local_smoke_only | yes | no | no | no | no | project-authored synthetic/local smoke | low | small fixture already in Git | separate later task if reused beyond current smoke context | not training data | Accepted current-scope smoke artifact only; not a training source. |
| P6 synthetic/local replay fixture | synthetic_local_smoke_only | yes | no | no | no | no | project-authored synthetic/local smoke | low | small fixture already in Git | explicit P7 task and review before any P7 use | P6 fixture is not P7 training source | Schema/context smoke only. |
| repository docs / planning docs | docs_context_only | yes | no | no | no | no | project documentation | low | docs in Git | none for planning; cannot become dataset without separate task | docs are not data | Governance context only. |
| future project-authored synthetic supervised fixture | not_approved_for_training | yes | no | no | no | no | not yet created or reviewed | low if synthetic/local | not defined | fixture boundary, schema, review and explicit `10_NEXT` approval | missing future fixture approval | Could support future smoke tests only. |
| future approved real replay source | blocked_by_missing_source_specific_approval | restricted | no | no | no | no | unknown until source-specific review | requires privacy/platform review | not defined | source-specific approval record, rights, storage, parser / reader / ingestion, feature / label and leakage boundaries | no source approved | Candidate category only. |
| real Tenhou / ranked logs | blocked_by_privacy_or_platform_terms | risk discussion only | no | no | no | no | platform/source rights unapproved | high | forbidden now | lawful source-specific, platform, privacy and account-risk review | real Tenhou unapproved | No Tenhou access, scraping, automation or account tooling. |
| real haifu / external logs | blocked_by_source_rights | restricted | no | no | no | no | rights/provenance unknown | requires review | forbidden now | source-specific rights, storage and parser / reader / ingestion approval | external source unapproved | Do not read or ingest real haifu or external logs. |
| platform data / online account data | blocked_by_privacy_or_platform_terms | risk boundary only | no | no | no | no | platform/account rights unapproved | high | forbidden now | separate lawful compliance review | platform/account data blocked | No account/session/cookie/token handling. |
| human-authored labels / annotations | not_approved_for_training | planning only | no | no | no | no | author/rights not defined | requires privacy/leakage review | not defined | annotation rights, labeling protocol, leakage policy and approval | no label policy | No human labels are approved. |
| generated labels from future approved pipeline | blocked_by_missing_feature_label_boundary | planning only | no | no | no | no | depends on approved source and generator | leakage/provenance risk | not defined | approved source, generator version, label boundary, leakage policy and validation | no approved pipeline | No generated labels are approved. |
| model outputs | deferred_later_stage | later-stage planning only | no | no | no | no | depends on future model provenance | leakage/quality risk | not defined | model-output integration scope, evidence and approval | model-output integration unapproved | Not a current P7 source. |
| self-play / league outputs | later_stage_only | later-stage planning only | no | no | no | no | depends on P8/P10/P11 scope | stage/provenance risk | not defined | separate later-stage transition and approval | P8/P10/P11 unapproved | Not current P7 input. |
| third-party open-source references | docs_context_only | yes as reference | no | no | no | no | external license review required for any use beyond reference | depends on source | do not vendor by default | license review and explicit scope before any use beyond reference | reference only | Mortal/Akochan/Kanachan/Suphx may inform design but are not training data. |
| third-party binaries / weights / params / checkpoints | prohibited_artifact | risk note only | no | no | no | no | external/unknown or restricted | artifact/provenance risk | forbidden in repo | explicit lawful artifact review; do not download/vendor/use now | prohibited | Includes `system.exe`, `libai.so`, `params/`, `*.pth`, `*.pt`, checkpoints and snapshots. |

## Readiness And Approval Vocabulary

Use the following status vocabulary:

| status | meaning |
|---|---|
| `docs_context_only` | May be referenced in documentation and planning only. Not source approval. |
| `synthetic_local_smoke_only` | Project-authored synthetic/local smoke artifact. Not training source approval. |
| `not_approved_for_training` | Not approved for supervised training. |
| `not_approved_for_ingestion` | Not approved for parser / reader / ingestion or file loading. |
| `blocked_by_source_rights` | Rights, owner, license or allowed use is unresolved. |
| `blocked_by_privacy_or_platform_terms` | Privacy, account, platform terms or compliance risk blocks use. |
| `blocked_by_missing_source_specific_approval` | Needs a source-specific approval record. |
| `blocked_by_missing_parser_reader_ingestion_boundary` | Parser / reader / ingestion boundary is missing or unapproved. |
| `blocked_by_missing_feature_label_boundary` | Feature extraction or label generation boundary is missing or unapproved. |
| `blocked_by_missing_split_leakage_policy` | Split and leakage policy is missing or unapproved. |
| `prohibited_artifact` | Must not be downloaded, vendored, committed or used now. |
| `later_stage_only` | Belongs to later stages such as P8-P12. |
| `requires_human_web_chatgpt_approval` | Requires explicit human / Web ChatGPT approval before any implementation. |
| `implementation_allowed_only_after_explicit_10_NEXT_task` | Cannot proceed unless it becomes the first unchecked `10_NEXT` task. |

No status above means current source approval, training approval, ingestion
approval, feature extraction approval or label generation approval.

## Source-Specific Approval Record Requirements

Any future source-specific approval record must contain:

- `source_id`.
- `source_name`.
- `source_category`.
- owner / rightsholder.
- license / terms summary.
- allowed use.
- forbidden use.
- training-use allowed.
- evaluation-use allowed.
- raw-storage allowed.
- derived-storage allowed.
- whether source content may enter Git.
- privacy review.
- platform-terms review.
- automation / scraping risk review.
- account / session / cookie / token policy.
- data-retention / deletion policy.
- provenance evidence.
- parser / reader / ingestion dependency.
- feature extraction dependency.
- label generation dependency.
- split / leakage dependency.
- evidence log reference.
- risk register reference.
- decision record reference.
- human / Web ChatGPT approval reference.
- `10_NEXT` implementation gate requirement.

## Conditions Before Future Source-Specific Approval

Before any future source-specific approval, the project must have:

1. a stable `source_id`.
2. source owner / rightsholder documented.
3. license or terms summarized.
4. allowed use and forbidden use documented.
5. training-use and evaluation-use decisions separated.
6. raw and derived storage policies defined.
7. Git inclusion policy defined.
8. privacy and platform-terms review completed when applicable.
9. automation / scraping / account-risk review completed when applicable.
10. parser / reader / ingestion dependency identified.
11. feature extraction dependency identified.
12. label generation dependency identified.
13. split / leakage dependency identified.
14. evidence log entry planned or created.
15. risk register entry planned or created.
16. decision record path planned.
17. human / Web ChatGPT approval path recorded.
18. explicit first `10_NEXT` implementation gate required before use.

If any applicable condition is missing, the source is not approved.

## Source Approval Vs Ingestion Vs Training Approval

These concepts are intentionally separate:

| concept | meaning | can it substitute for another approval |
|---|---|---|
| source readiness | A source category has enough documented context to discuss future use. | no |
| source-specific approval | A specific source has been reviewed for rights, allowed use, storage, privacy and platform terms. | no |
| source ingestion approval | Parser / reader / ingestion behavior for a source is separately approved. | no |
| parser / reader / ingestion approval | Code and boundaries for reading or normalizing a source are approved. | no |
| feature extraction approval | Actual feature extraction behavior is separately approved. | no |
| label generation approval | Actual label generation or annotation behavior is separately approved. | no |
| training data approval | A source, derived dataset and split/leakage policy are approved for training use. | no |
| training run approval | A specific training run, config, artifact policy and validation plan are approved. | no |
| model-strength evidence | Empirical evidence from approved evaluation protocols. | no |

Source readiness does not approve source use. Source approval does not approve
ingestion. Ingestion approval does not approve feature extraction, label
generation or training. Training approval does not create model-strength
evidence.

## Parser Reader Ingestion Dependency Boundary

Source approval does not automatically approve parser / reader / ingestion.

Parser / reader / ingestion must have a separate boundary, review and approval
before any source can be read by code. Broad file ingestion remains unapproved.
CLI data paths remain unapproved. Real-data ingestion remains blocked until
source-specific approval and parser / reader / ingestion approval both exist.

This task does not approve parser, dataset reader, ingestion, broad file
ingestion or CLI data paths.

## Feature Label Dependency Boundary

Source readiness does not approve actual feature extraction. Source readiness
does not approve actual label generation.

Feature extraction requires separate boundary, proposal, review and approval.
Label generation requires separate boundary, proposal, review and approval.

Future feature / label work must address:

- decision-time public-information boundary.
- hidden-information exclusion.
- future-information exclusion.
- split leakage controls.
- source leakage controls.
- label provenance.
- generated-label versioning if generated labels are later approved.

This task does not approve actual feature extraction or actual label
generation.

## Current Smoke Fixture Is Not A Training Source

The accepted P7 synthetic/local supervised feature-label smoke fixture is
accepted only as current-scope smoke evidence. It validates JSON-safe
synthetic/local mappings and guardrails. It is not a supervised training
source, not source approval, not training-data approval, not model-strength
evidence and not LuckyJ `10.68` comparison evidence.

Repository docs and P6 synthetic/local fixtures are also not training sources.

## Why This Task Cannot Approve Sources

This task cannot approve sources because it does not perform source-specific
rights review, privacy review, platform-terms review, storage review,
provenance evidence review, parser / reader / ingestion review, feature /
label review, split / leakage review or human / Web ChatGPT source-specific
approval.

It only defines the boundary that a later source-specific approval task must
satisfy.

## Why This Task Cannot Read Real Data

This task cannot read real data because no source-specific approval exists and
no parser / reader / ingestion path is approved. Real Tenhou, real haifu,
external logs, platform data, account/session/cookie/token data and any
external source file remain blocked.

## Why This Task Cannot Train

Training cannot start because there is no approved training source, no
approved source ingestion, no parser / reader / ingestion, no actual feature
extraction, no actual label generation, no supervised dataset construction,
no split / leakage policy, no model architecture / trainer approval, no
checkpoint policy and no first `10_NEXT` training task.

## Why This Task Cannot Enter P8-P12

P8-P12 cannot start because full P7 is not closed, broader P7 implementation
is not approved, no P7 training has occurred, no supervised model candidate
exists and no model-strength evidence exists. Later stages require separate
transition review, scope, entry criteria, risk / evidence review and first-task
approval.

## Risk Controls

| risk | mitigation | current_status |
|---|---|---|
| readiness mistaken for approval | repeat that readiness / inventory / docs context are not approval | open |
| source inventory mistaken for dataset | keep `approved_for_training = no` for every current category | open |
| smoke fixture mistaken for training data | classify as `synthetic_local_smoke_only` and not training data | open |
| repository docs mistaken for training data | classify as `docs_context_only` | open |
| real data used without rights | require source-specific rights / provenance / storage / privacy / platform review | open |
| platform/account data leakage | forbid account/session/cookie/token handling and platform automation | open |
| parser / reader / ingestion creep | require separate boundary, review and explicit `10_NEXT` approval | open |
| feature / label creep | require separate feature / label boundary and leakage controls | open |
| training creep | require training-data approval and training-run approval later | open |
| model-output labels used too early | keep model-output integration unapproved | open |
| self-play / league data used too early | classify as later-stage only | open |
| third-party weights / binaries introduced | classify as prohibited artifacts | open |
| model-strength overclaim | evidence grade remains boundary definition only | open |
| P8-P12 stage creep | require separate transition reviews and approvals | open |

## Evidence Requirements

Future source readiness / approval evidence must record:

- `source_id`.
- `source_category`.
- readiness status.
- approval status.
- rights status.
- privacy status.
- platform-terms status.
- storage status.
- parser / reader / ingestion status.
- feature extraction status.
- label generation status.
- training-use status.
- validation commands.
- evidence log reference.
- risk register reference.
- decision record reference.
- known exclusions.
- explicit non-evidence warning.

## First Task Candidate

Recommended next task:

```text
Review broader P7 data/source readiness and source approval boundary before implementation.
```

The next task must be a docs-only review gate. It must not approve sources,
approve source ingestion, implement parser / reader / ingestion, read data,
implement feature extraction, implement label generation, construct datasets,
train, implement model architecture / trainer code or enter P8-P12.

## Planning Decision

```text
Broader P7 data/source readiness and source approval boundary is defined before
implementation. This does not approve any source, source ingestion, parser,
dataset reader, actual feature extraction, actual label generation, supervised
dataset construction, training, model architecture, real data, model-output
integration, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
Broader P7 data/source readiness and source-approval boundary definition
evidence only.
```

## Explicit Non-Evidence

This boundary definition is not:

- source approval.
- training-data approval.
- source ingestion.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- training.
- model architecture.
- trainer.
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
- candidate promotion evidence.
