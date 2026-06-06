# 02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW

## Scope

This document reviews `docs/02_data_system/02B_REPLAY_SCHEMA.md` before any
replay schema implementation.

This is a P6 data-system docs-only review gate. It reviews the documentation
boundary only. It does not:

- approve P6 implementation.
- implement replay schema code.
- implement dataclasses, pydantic models or JSON schema.
- implement parsers, dataset readers, feature extraction or label generation.
- approve data ingestion.
- read real Tenhou, real haifu, external logs or platform data.
- use online accounts, sessions, cookies, tokens or private logs.
- create platform automation, scraping, evasion or account tooling.
- connect model outputs.
- add CLI or broad file ingestion.
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

North-star relationship:

```text
Replay schema planning supports the long-term stable-dan > 10.68 target only
by keeping future data lawful, reproducible and auditable before training or
evaluation data can exist. This review is not strength evidence.
```

## Reviewed Artifacts

- `AGENTS.md`
- `README.md`
- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md`
- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md`
- `docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md`
- `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `src/mjlabai/eval/offline_result.py` as read-only context.
- `src/mjlabai/eval/stable_dan.py` as read-only context.
- `src/mjlabai/eval/legal_action_metric.py` as read-only context.
- `src/mjlabai/eval/tiny_benchmark_harness.py` as read-only context.
- current project-authored synthetic evaluation fixtures as read-only context.

## Replay Schema Scope Review

`02B` correctly limits itself to the P6 replay schema documentation boundary
after source-inventory review and before replay schema implementation.

Review finding:

| item | finding | blocker | notes |
|---|---|---|---|
| stage | correct | no | It is P6 data-system docs-only planning. |
| artifact type | correct | no | It is a planning / boundary document, not implementation. |
| implementation approval | closed | no | It explicitly keeps P6 and replay schema implementation unapproved. |
| ingestion approval | closed | no | It keeps source ingestion, real data and platform data closed. |
| data pipeline approval | closed | no | It keeps dataset readers, feature extraction and label generation closed. |
| later-stage entry | closed | no | It keeps training, self-play, league, runner behavior and P7-P12 closed. |
| evidence claim | conservative | no | It states that schema planning is not model-strength or LuckyJ evidence. |

Decision:

```text
No scope blocker found.
```

## Allowed Documentation Scope Review

`02B` covers the required documentation-only field and governance areas:

| required_area | coverage_status | review_finding | blocker | notes |
|---|---|---|---|---|
| replay record identity | covered | sufficient | no | `replay_id`, `source_id`, schema and transform version concepts are planning names only. |
| source provenance reference | covered | sufficient | no | Links future records to source inventory, evidence and risks. |
| source approval reference | covered | sufficient | no | Makes inventory review distinct from source approval. |
| ruleset / room / game context | covered | sufficient | no | Requires source/ruleset review before implementation. |
| table / player / seat metadata boundary | covered | sufficient | no | Includes privacy and account-identifier policy boundaries. |
| event sequence boundary | covered | sufficient | no | Defines event order planning without parser support. |
| event type vocabulary planning | covered | sufficient | no | Lists vocabulary families but does not implement them. |
| action vocabulary planning | covered | sufficient | no | References future canonical-action review without expanding action support. |
| observation / decision-state boundary | covered | sufficient | no | Keeps hidden-information leakage controls explicit. |
| terminal result / placement / score boundary | covered | sufficient | no | Does not overclaim stable-dan evidence. |
| round / hand / honba / kyotaku / dealer / dora context planning | covered | sufficient | no | Plans context fields without tile/dora parser work. |
| anonymization / privacy hooks | covered | sufficient | no | Requires privacy review before account/player data. |
| raw-vs-derived field distinction | covered | sufficient | no | Keeps raw real data out of Git by default. |
| schema versioning | covered | sufficient | no | Version names are documentation only. |
| transform versioning | covered | sufficient | no | No transform code is approved. |
| validation status field planning | covered | sufficient | no | Validation fields are planned only. |
| known exclusions | covered | sufficient | no | Exclusions prevent silent scope expansion. |
| non-evidence warnings | covered | sufficient | no | Repeated across scope, decision and evidence-grade sections. |
| future implementation entry criteria | covered | sufficient | no | Current status is clearly not satisfied. |
| future review requirements | covered | sufficient | no | Next step remains a review / docs-only follow-up. |

Review decision:

```text
The allowed documentation scope is sufficient. No missing area, unsafe
ambiguity, overbroad interpretation or implementation-like wording was found.
```

## Forbidden Scope Review

`02B` is strict enough for the current review gate. It forbids:

- replay schema code.
- dataclass / pydantic / JSON schema implementation.
- parser implementation.
- dataset reader.
- data ingestion.
- feature extraction.
- label generation.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- online account / session / cookie / token handling.
- platform automation, scraping, evasion or anti-detection tooling.
- model-output integration.
- CLI or broad file ingestion.
- Akochan `system.exe`, `libai.so` and third-party binaries.
- third-party source, `params/`, build artifacts and unknown weights.
- training, tuning, self-play, league or runner behavior.
- metric implementation or registry changes.
- promotion criteria changes.
- source approval, model-strength claims, Tenhou ranked claims, LuckyJ
  comparison, candidate promotion and P7-P12 entry.

Review decision:

```text
No forbidden-scope blocker found.
```

## Source Inventory Dependency Review

`02B` correctly depends on `02A` and `02D`:

- `02A` defines source inventory fields, source categories, rights status,
  storage policy, privacy/platform review, evidence references and risk
  references.
- `02D` reviews that inventory with no blocker for the current review gate.
- Neither `02A` nor `02D` is source approval, ingestion approval or replay
  schema implementation approval.

`02B` requires future implementation to have:

- `source_id`.
- source category and source owner / rightsholder.
- license / terms summary.
- allowed use and forbidden use.
- raw and derived storage policy.
- `may_enter_git` decision.
- privacy / personal-data review.
- platform-terms review when applicable.
- evidence-log reference.
- risk-register reference.
- reviewer / approval owner.
- explicit ingestion approval.
- explicit replay schema implementation task in `docs/10_next/10_NEXT.md`.

Review decision:

```text
The source inventory dependency is clear. No source dependency blocker found.
```

## Field-Family Draft Review

The field-family draft is sufficient and safe for documentation-boundary use.

| field_family | coverage_status | implementation_boundary | source_dependency | review_finding | blocker | notes |
|---|---|---|---|---|---|---|
| A. replay_identity | covered | documentation boundary only | approved source inventory record | safe | no | Does not create concrete schema fields. |
| B. provenance | covered | documentation boundary only | source rights review | safe | no | Keeps approval and evidence references visible. |
| C. game_context | covered | documentation boundary only | source format and terms | safe | no | Does not infer real Tenhou semantics. |
| D. participants | covered | documentation boundary only | privacy review | safe | no | Protects identities and account data. |
| E. hand_round_context | covered | documentation boundary only | source and ruleset review | safe | no | No tile, dora or hand parser is implied. |
| F. event_sequence | covered | documentation boundary only | source event format | safe | no | Event planning is not event parsing. |
| G. action_context | covered | documentation boundary only | `05L` plus future schema review | safe | no | No legal-action checker, model-output path or canonicalizer is approved. |
| H. decision_state_boundary | covered | documentation boundary only | source and leakage policy | safe | no | Hidden-information policy is required before features or labels. |
| I. terminal_result | covered | documentation boundary only | source result semantics | safe | no | Terminal results are not stable-dan evidence by themselves. |
| J. validation_metadata | covered | documentation boundary only | later tests and validation command | safe | no | No validation code is approved here. |
| K. storage_and_privacy | covered | documentation boundary only | source inventory and privacy review | safe | no | Raw real data remains out of Git by default. |

Review decision:

```text
No field-family blocker found. The draft does not read as JSON schema,
dataclass, parser contract, ingestion approval, feature extraction, label
generation, model-output integration or model-strength evidence.
```

## Validation Expectations Review

`02B` requires future implementation to confirm:

- source inventory has been reviewed.
- source-specific approval exists for the selected source category.
- `schema_version` is assigned and reviewed.
- an example source category is selected.
- synthetic/local starter fixtures are allowed only after explicit approval.
- no real data is used unless approved through source-specific review.
- validation command is planned.
- failure modes are documented.
- evidence log is updated.
- risk register is updated.
- tests are planned, but not created in this task.
- code implementation is explicitly approved by a later `10_NEXT` task.

Review decision:

```text
The validation expectations are sufficient for preventing premature
implementation and unapproved source consumption at this stage.
```

## Future Implementation Entry Criteria Review

`02B` lists future implementation criteria and marks current blockers clearly.

| criterion | current_status_review | blocker | notes |
|---|---|---|---|
| source-specific approval | not satisfied for implementation | yes | `02A` / `02D` are preconditions only. |
| schema version approval | defined here only | yes | No JSON/Python schema exists. |
| raw-vs-derived storage policy | planned only | yes | Requires source-specific storage decision. |
| privacy / anonymization policy | planned only | yes | Account/session/token data remains blocked. |
| event vocabulary approval | planned only | yes | Requires source examples and review. |
| action vocabulary approval | planned only | yes | No action-space expansion now. |
| hidden-information leakage policy | planned only | yes | Required before feature/label generation. |
| validation command plan | planned only | yes | No validation command exists now. |
| evidence / risk synchronization | satisfied for docs boundary only | yes for implementation | Must repeat at implementation review. |
| implementation task approval | not satisfied | yes | `10_NEXT` does not authorize code yet. |

Review decision:

```text
The future implementation entry criteria are sufficient and clearly show that
implementation conditions are not currently satisfied.
```

## Replay Schema Risk Review

| risk | mitigation_present | blocker | owner_doc_or_followup | notes |
|---|---|---|---|---|
| Boundary documentation mistaken for implementation approval. | yes | no for review; yes for implementation | `02B`, `10_NEXT`, evidence log | The docs repeat that implementation remains closed. |
| Source inventory review mistaken for source approval. | yes | no for review; yes for ingestion | `02A`, `02D`, `02B` | Source-specific approval is still required. |
| Real Tenhou or real haifu enters before compliance review. | yes | no for review; yes for real data | `02A`, risk register | Real/platform sources remain blocked. |
| Hidden-information leakage baked into schema. | yes | no for review; yes for features/labels | `02B`, future P6 review | Decision-state boundary is explicitly planned. |
| Raw real data or private data committed to Git. | yes | no for review; yes for storage | source inventory | `may_enter_git` and privacy review are required. |
| Event/action vocabulary expands without review. | yes | no for review; yes for parser/canonicalizer | `02B`, `05L`, future review | Vocabulary is planning only. |
| Schema planning overclaimed as strength or LuckyJ evidence. | yes | no | evidence log / ranking protocol | Evidence grade is conservative. |
| P6 docs planning drifts into P7-P12. | yes | no | stage contract / `10_NEXT` | Later stages remain closed. |
| CLI or broad file ingestion appears under schema work. | yes | no for review; yes for implementation | future implementation review | CLI and broad ingestion remain forbidden. |
| Third-party binaries or artifacts enter repo. | yes | no | risk register / `10_NEXT` | `system.exe`, `libai.so`, `params/` and weights remain forbidden. |

Review decision:

```text
Replay schema risks are adequately recorded for this docs-only review gate.
No review blocker found.
```

## Governance Synchronization Review

The governance and tracking docs are synchronized with the replay schema
boundary:

| doc | synchronization_status | blocker | notes |
|---|---|---|---|
| `docs/00_HANDOFF.md` | updated by this review | no | Records review closure and next docs-only task. |
| `docs/00_DOCS_INDEX.md` | updated by this review | no | Indexes this `02E` review document. |
| `docs/10_next/10_NEXT.md` | updated by this review | no | Moves the first item to a docs-only synthetic/local replay fixture boundary task. |
| `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` | updated by this review | no | Records review completion and current non-implementation status. |
| `docs/09_governance/09_EVIDENCE_LOG.md` | updated by this review | no | Classifies the review as P6 documentation-boundary review evidence only. |
| `docs/09_governance/09_RISK_REGISTER.md` | updated by this review | no | Adds review-gate risk synchronization. |
| `docs/09_governance/09_STAGE_TASK_CONTRACT.md` | updated by this review | no | Keeps P6 implementation, replay schema implementation and ingestion closed. |
| `docs/07_development_execution/07B_TASK_BACKLOG.md` | updated by this review | no | Marks the review task done and adds the next docs-only task. |
| `docs/07_development_execution/07A_MILESTONES.md` | updated by this review | no | Records current P6 docs-only review status. |
| `docs/09_governance/09_CHANGELOG.md` | updated by this review | no | Adds this review entry. |
| `docs/09_governance/09_DECISION_RECORD.md` | updated by this review | no | Records the no-blocker review decision. |

Review decision:

```text
No governance synchronization blocker found.
```

## Review Decision

```text
Review can close, but replay schema implementation remains closed.
```

No blocker was found in:

- `02B` scope.
- allowed documentation scope.
- forbidden scope.
- source inventory dependency.
- field-family draft.
- validation expectations.
- future implementation entry criteria.
- replay schema risks / mitigations.
- governance synchronization.

This decision does not approve implementation. P6 implementation, replay schema
implementation, data ingestion, dataset readers, feature extraction, label
generation and P7-P12 remain closed.

## Next Task Recommendation

Recommended next first task:

```text
Define P6 synthetic/local replay fixture boundary before schema implementation.
```

Rationale:

- The replay schema documentation boundary is now reviewed.
- Before implementation, the project should define a synthetic/local fixture
  boundary that keeps future examples project-authored, repo-local and safe.
- This keeps the next step docs-only and prevents a direct jump into schema
  code, ingestion, real-data access, dataset readers, CLI, feature extraction,
  label generation or P7-P12.

The next task must remain docs-only unless a later review explicitly approves
implementation.

## Evidence Grade

```text
P6 replay schema documentation boundary review evidence only.
```

## Explicit Non-Evidence

This review is not evidence of:

- P6 implementation approval.
- replay schema implementation.
- data ingestion.
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
- runner behavior.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
- P7-P12 entry approval.
