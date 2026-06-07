# 02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY

## Scope

This document defines the full P6 closure roadmap and remaining scope inventory
after accepted current-scope closure.

Current-scope P6 is closed only for the accepted synthetic/local minimal replay
schema and project-authored synthetic fixture scope. Full P6 remains open.
P7-P12 remain unapproved.

This task is docs-only. It does not add code, tests, fixtures or data files. It
does not modify implementation artifacts. It does not approve implementation,
close full P6, approve real data, approve parser / reader / ingestion, approve
feature extraction / label generation or approve P7-P12. It only inventories,
classifies and roadmaps the remaining P6 closure work.

## Current-Scope Closed Artifacts

The accepted current-scope P6 chain is closed for:

- P6 scope / entry criteria / first task definition.
- source inventory and review.
- replay schema documentation boundary and review.
- synthetic/local replay fixture boundary and review.
- readiness checklist and review.
- proposal boundary and review.
- minimal proposal and review.
- approval decision.
- exact minimal implementation in:
  - `src/mjlabai/data/replay_schema.py`
  - `tests/fixtures/data/synthetic_replay_smoke.json`
  - `tests/data/test_replay_schema.py`
  - `tests/data/test_synthetic_replay_fixture_schema.py`
- implementation review.
- current-scope acceptance decision.
- next-task definition.
- closure criteria definition and review.
- final current-scope closure review.
- post-current-scope transition review.
- governance synchronization.

This closed chain is current-scope evidence only. It is not full P6 closure and
not P7-P12 entry approval.

## Full P6 Remaining Scope Inventory

| item | category | current_status | required_for_full_p6_closure | blocker | defer_reason | earliest_possible_condition | guardrail | notes |
|---|---|---|---|---|---|---|---|---|
| Full P6 closure criteria definition. | required for full P6 closure | not done | yes | none | n/a | current roadmap accepted for review | docs-only criteria task | Defines what full P6 closure means after current-scope closure. |
| Full P6 closure criteria review. | required for full P6 closure | not done | yes | criteria not yet defined | n/a | criteria definition complete | docs-only review gate | Reviews criteria before finalization. |
| Full P6 evidence index / handoff finalization. | required for full P6 closure | not done | yes | closure criteria not reviewed | n/a | criteria review passes | docs-only finalization | Keeps source of truth coherent. |
| Full P6 risk / source-rights consistency review. | required for full P6 closure | not done | yes | closure criteria not reviewed | n/a | criteria review passes | docs-only consistency review | Confirms blocked/deferred real-data risks remain explicit. |
| Final full P6 closure review gate. | required for full P6 closure | not done | yes | prerequisite reviews incomplete | n/a | evidence/handoff/risk finalization complete | docs-only closure gate | May close full P6 only if all criteria pass. |
| Additional replay schema expansion. | deferred beyond full P6 current roadmap | unapproved | no for this roadmap | none if synthetic-only, otherwise scope approval needed | accepted minimal schema is enough for current closure path | later explicit proposal and review | no `replay_schema.py` changes without `10_NEXT` approval | Could be revisited after closure roadmap review. |
| Additional synthetic fixtures. | deferred beyond full P6 current roadmap | unapproved | no for this roadmap | fixture scope approval needed | current fixture is enough for accepted current scope | later fixture-boundary / proposal / approval | no new fixtures in roadmap or review gates | Not required to close current documentation-level P6 track. |
| Source-specific real data approval. | blocked until source / legal / platform / privacy approval | absent | no | rights, terms, privacy, storage and evidence not approved | real sources are outside current closure path | separate lawful source-specific review | no source approval by implication | Needed only for future real-data ingestion tasks. |
| Parser. | deferred / blocked until source and parser approval | unapproved | no | source format, rights, storage and parser scope absent | parser is broader implementation | separate parser boundary and approval | no parser implementation from roadmap wording | Current schema validates in-memory mappings only. |
| Dataset reader. | deferred / blocked until source and reader approval | unapproved | no | source/storage policy and file interface absent | reader creates ingestion surface | separate reader boundary and approval | no broad file ingestion | Not required for current P6 closure roadmap. |
| Data ingestion. | blocked until source / legal / storage approval | unapproved | no | source rights, privacy, terms, storage and evidence absent | ingestion is unsafe without source approvals | source-specific approval plus ingestion proposal | no real/external/platform data | Not required for current closure. |
| Feature extraction. | deferred beyond full P6 current roadmap | unapproved | no | parser/reader/source/hidden-information policy absent | derived features belong to later approved P6/P7 boundary | feature policy and approval after data readiness | no derived feature pipeline | Must not be inferred from replay schema. |
| Label generation. | deferred beyond full P6 current roadmap | unapproved | no | label source policy and approved data absent | labels are training-facing and need P7 readiness | label policy and leakage review | no labels in P6 fixture path | Not required before current P6 closure roadmap can proceed. |
| Data quality checks beyond current smoke scope. | deferred beyond full P6 current roadmap | minimal smoke checks only | no | broader data scope absent | no broad datasets exist | later data-quality boundary after source approval | no broad checker now | Current tests validate synthetic schema/fixture only. |
| Storage / versioning policies beyond current docs. | deferred / blocked until source scope exists | docs only | no | real/derived storage scope absent | no approved real data or derived corpus | source-specific storage/versioning review | no raw real data in git | Can be required later before ingestion. |
| CLI / broad file ingestion. | explicitly out of scope for full P6 closure | unapproved | no | expands attack/scope surface | not needed for docs closure or current fixture | separate CLI/file-ingestion proposal if ever needed | no CLI, no glob/directory reader | Keep closed. |
| Model-output integration. | explicitly out of scope for full P6 closure | unapproved | no | model-output provenance and stage boundary absent | belongs to later adapter/evaluation/model stages | separate model-output boundary | no model code integration | Not a P6 closure requirement. |
| Real Tenhou. | blocked until legal/platform/privacy approval | unapproved | no | platform/account/legal/privacy risk | outside current closure path | separate compliance and source approval | no Tenhou access | Not evidence here. |
| Real haifu. | blocked until source-rights/privacy approval | unapproved | no | provenance, rights and storage absent | outside current closure path | source-specific review | no real haifu ingestion | Not required for current closure. |
| External logs. | blocked until source-rights/privacy approval | unapproved | no | provenance, allowed use and privacy absent | outside current closure path | source-specific review | no external-log ingestion | Not required for current closure. |
| Platform data. | blocked until platform/legal/privacy approval | unapproved | no | terms, account, privacy and storage risk | outside current closure path | platform-data review | no platform automation/data | Not required for current closure. |
| Account / session / cookie / token usage. | explicitly out of scope for full P6 closure | blocked | no | privacy/security/platform risk | not needed for offline docs/data groundwork | none in current roadmap | never infer account access from P6 docs | Keep absent. |
| Training / tuning. | later-stage P7-P12 | unapproved | no | P7/P8/P11 not approved | training is not P6 closure work | independent stage transition | no training commands | Not a P6 closure item. |
| Self-play. | later-stage P8/P10 | unapproved | no | P8/P10 not approved | later RL/league work | independent stage transition | no self-play commands | Not a P6 closure item. |
| League / runner. | later-stage P10 | unapproved | no | P10 not approved | later evaluation/model selection work | independent stage transition | no league/runner | Not a P6 closure item. |
| P7-P12 execution. | later-stage P7-P12 | unapproved | no | no independent scope/entry/risk/first-task approval | later stages require separate transition | later stage-specific review | do not jump stages | P6 closure does not grant entry. |
| Model-strength evidence. | explicitly out of scope for full P6 closure | absent | no | no model evaluation evidence | P6 docs/schema smoke cannot prove strength | later evaluation protocol | no strength claims | Not a data-system closure artifact. |
| LuckyJ `10.68` comparison. | explicitly out of scope for full P6 closure | absent | no | no ranked stable-dan evidence | P6 data docs are not evaluation results | P12 validation only | no LuckyJ claims | Not a P6 closure item. |
| Candidate promotion. | explicitly out of scope for full P6 closure | absent | no | no model-candidate evidence | belongs to racing funnel later gates | later F-stage evidence | no promotion language | Not a P6 closure item. |

## Full P6 Closure Roadmap

| roadmap_step | purpose | current_status | required_evidence | blocker | implementation_required | docs_only_possible | depends_on | next_review_gate | notes |
|---|---|---|---|---|---|---|---|---|---|
| Review this roadmap / inventory. | Confirm remaining full-P6 classification. | current next after this task | `02U` review evidence and validation | none if docs consistent | no | yes | `02U` complete | Review full P6 closure roadmap and remaining scope inventory after current-scope closure. | Prevents roadmap from becoming closure by assertion. |
| Define full P6 closure criteria. | Convert inventory into auditable closure criteria. | not started | criteria doc, required/deferred/blocked taxonomy, validation plan | roadmap review not complete | no | yes | roadmap review | closure-criteria review | Does not close full P6. |
| Review full P6 closure criteria. | Check criteria are sufficient and conservative. | not started | review doc, no-blocker/blocked decision, validation | criteria absent | no | yes | criteria definition | handoff/evidence finalization | Keeps implementation closed. |
| Finalize full P6 handoff / evidence index. | Prepare closure evidence packet. | not started | handoff, docs index, evidence log, risk register, backlog, milestones consistency | criteria review not complete | no | yes | criteria review | finalization review or final closure gate | Similar to P5 finalization pattern. |
| Review source-rights / risk consistency for closure. | Ensure blocked/deferred source categories remain clear. | not started | risk/source consistency review | criteria review not complete | no | yes | criteria review | final closure gate | Prevents accidental real-data approval. |
| Run final full P6 closure review gate. | Decide whether full P6 can close for the documented scope. | not started | closure criteria pass, evidence/handoff complete, validation pass | prerequisite gates incomplete | no | yes | finalization and risk consistency | post-P6 transition review if closed | May close full P6 only if criteria pass. |
| Post-P6 transition review. | Decide whether a later-stage scope definition may start. | not started | final full P6 closure decision | full P6 not closed | no | yes | final full P6 closure | P7 scope/entry definition if approved | Must not be P7 implementation. |

## Required Before Full P6 Closure

Required before full P6 closure:

- Review this full P6 closure roadmap and remaining scope inventory.
- Define full P6 closure criteria.
- Review full P6 closure criteria.
- Finalize full P6 handoff and evidence index.
- Review full P6 risk register and source-rights inventory consistency.
- Run a final full P6 closure review gate.
- Explicitly preserve deferred/blocked status for real data, parser, dataset
  reader, ingestion, feature extraction, label generation, model-output
  integration, CLI, training, self-play, league and P7-P12 unless a separate
  future approval changes that status.

Not required before this full-P6 closure roadmap can proceed:

- training.
- tuning.
- self-play.
- league / runner.
- model-strength evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

## Deferred Items

| deferred_item | defer_reason | earliest_possible_condition | why_not_required_for_full_p6_closure_roadmap | guardrail | owner_doc_or_future_review |
|---|---|---|---|---|---|
| Additional replay schema expansion. | Minimal accepted schema is enough for current closure path. | Later proposal / approval after roadmap review. | Full-P6 closure can record minimal scope and defer expansion. | No schema code changes without `10_NEXT`. | Future replay schema expansion proposal. |
| Additional synthetic fixtures. | Current project-authored fixture covers accepted smoke scope. | Later fixture-boundary update / approval. | Not needed to close current P6 documentation/data-smoke scope. | No new fixture without explicit task. | Future synthetic fixture proposal. |
| Parser. | Broad implementation and source-specific semantics are absent. | Parser boundary, source approval and implementation approval. | Current schema validates mappings, not raw logs. | No parser from docs wording. | Future parser boundary review. |
| Dataset reader. | Reader creates file-ingestion surface. | Reader boundary, storage policy and approval. | Current tests use a known project-authored fixture only. | No broad file ingestion. | Future dataset-reader proposal. |
| Feature extraction. | Requires parser/reader/source and hidden-information policy. | Feature policy and source readiness. | P6 can close current scope without training-ready features. | No derived feature pipeline. | Future feature policy review. |
| Label generation. | Requires label source policy and approved data. | Label policy, leakage review and P7 readiness. | Current P6 artifacts are not supervised labels. | No labels or label fields. | Future label policy review. |
| Data quality checks beyond smoke scope. | No broad dataset exists. | Approved dataset/source and quality policy. | Current tests cover smoke schema only. | No broad checker now. | Future data quality boundary. |
| Storage / versioning beyond current docs. | No approved real/derived corpus exists. | Source-specific storage/versioning review. | Closure can record that real/derived storage is unapproved. | No raw real data in git. | Future storage/versioning policy. |

## Blocked Items

| blocked_item | blocker_reason | release_condition | guardrail |
|---|---|---|---|
| Real Tenhou. | Platform/legal/privacy/account risk. | Separate lawful compliance, source-rights, privacy and storage review. | No Tenhou access, scraping, automation or account tooling. |
| Real haifu. | Provenance, rights, privacy and storage absent. | Source-specific allowed-use and storage approval. | No real haifu ingestion. |
| External logs. | Source rights, provenance and privacy absent. | Source-specific evidence and approval. | No external-log ingestion. |
| Platform data. | Platform terms, privacy and account/session risk. | Platform-data legal/privacy review. | No platform data or automation. |
| Account / session / cookie / token. | Security, privacy and platform risk. | Not part of current roadmap. | Do not handle or store account credentials. |
| Source-specific real-data approval. | No source-specific rights/terms/storage evidence. | A future source-specific review with evidence and risk updates. | Inventory is not approval. |
| Parser / reader consuming external data. | Source format and source rights not approved. | Source approval plus parser/reader boundary and implementation approval. | No parser/reader implementation now. |
| Ingestion pipeline using unapproved sources. | Rights, privacy, storage and evidence absent. | Source-specific approval and ingestion proposal. | No ingestion pipeline. |
| Model weights / third-party artifacts. | Unknown provenance / repository artifact policy. | Verified lawful artifact review, if ever relevant. | No `*.pth`, `*.pt`, checkpoints, snapshots, `system.exe`, `libai.so`, `params/` or third-party artifacts. |

## P7-P12 Non-Entry Boundary

The full P6 closure roadmap does not approve P7. P7 requires independent
scope, entry criteria, source/data readiness, risk review, first task and
human/Web ChatGPT approval.

P8-P12 likewise require separate transition review, scope, entry criteria,
risk review and first-task approval. Current P6 synthetic/local artifacts are
not a training data pipeline, not source approval, not model-strength evidence
and not LuckyJ `10.68` comparison.

## Planning Decision

```text
Full P6 closure roadmap and remaining scope inventory are defined after
accepted current-scope closure. Full P6 remains open, and P7-P12 remain
unapproved. This task does not approve implementation, real data, parser,
reader, ingestion, feature extraction, label generation, training, self-play,
league or model-strength claims.
```

## Next Task Recommendation

Recommended next task:

```text
Review full P6 closure roadmap and remaining scope inventory after current-scope closure.
```

The next task must be a docs-only review gate. It must not be implementation,
P7 execution, P7 entry approval, full P6 closure, production code, tests,
fixtures, parser, dataset reader, ingestion, feature extraction, label
generation, real Tenhou, real haifu, external logs, platform data, account /
session / cookie / token handling, model-output integration, CLI, broad file
ingestion, training, tuning, self-play, league or model-strength claims.

## Evidence Grade

```text
P6 full-closure roadmap and remaining-scope inventory evidence only.
```

## Explicit Non-Evidence

This task is not:

- full P6 closure.
- P7-P12 entry approval.
- new implementation approval.
- data ingestion.
- parser.
- dataset reader.
- feature extraction.
- label generation.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- source approval.
- model-output integration.
- CLI.
- broad file ingestion.
- training.
- tuning.
- self-play.
- league.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
