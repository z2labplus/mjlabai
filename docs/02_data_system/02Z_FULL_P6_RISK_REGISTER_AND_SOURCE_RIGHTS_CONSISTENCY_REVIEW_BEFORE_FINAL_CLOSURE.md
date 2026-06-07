# 02Z_FULL_P6_RISK_REGISTER_AND_SOURCE_RIGHTS_CONSISTENCY_REVIEW_BEFORE_FINAL_CLOSURE

## Scope

This document reviews full P6 risk-register and source-rights inventory
consistency before the final full P6 closure review gate.

This is a docs-only consistency review. It does not close full P6, approve
P7-P12 entry, approve implementation, add code, add tests, add fixtures, add
data files or modify implementation artifacts.

Current status:

- P5 is closed only for the current synthetic/local evaluation groundwork
  scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored synthetic fixture scope.
- Full P6 remains open until a later final full P6 closure review gate passes.
- P7-P12 entry remains unapproved.
- Parser, dataset reader, ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.

This review checks whether the risk register, source-rights inventory,
evidence index, closure criteria and governance docs are consistent enough to
proceed to the final full P6 closure review gate.

## Reviewed Artifacts

Primary source-rights and risk artifacts:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`

Full-P6 closure context:

- `docs/02_data_system/02U_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY.md`
- `docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`
- `docs/02_data_system/02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/02_data_system/02X_FULL_P6_CLOSURE_CRITERIA_REVIEW_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW.md`
- `docs/02_data_system/02Y_FULL_P6_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION_AFTER_CLOSURE_CRITERIA_REVIEW.md`
- `docs/12_technical_plan/12C_POST_CURRENT_SCOPE_P6_TRANSITION_REVIEW.md`

Read-only implementation context:

- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

Governance and tracking context:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

## Source-Rights Inventory Consistency Review

`02A` and `02D` remain consistent with the full-P6 closure path.

Findings:

- Project-authored synthetic/local fixtures remain the only source family
  allowed in current repository smoke contexts.
- Repository documentation remains allowed as project documentation only.
- Third-party code references remain methodology/interface references only.
- Real Tenhou, real haifu, external logs, platform data and account/session /
  cookie / token data remain unapproved or blocked.
- Model outputs, self-play outputs and league outputs remain later-stage and
  unapproved as P6 sources.
- Third-party binaries, `system.exe`, `libai.so`, `params/`, model weights,
  checkpoints and snapshots remain blocked from repository storage and use.
- No source category is newly approved for ingestion, training, model
  evaluation, parser / reader consumption or P7-P12 work.

No source-rights inventory blocker was found.

## Risk Register Coverage Review

`09_RISK_REGISTER.md` covers the main risks required before final full P6
closure review.

The register explicitly tracks:

- stage-control risks where current-scope P6 or full-P6 review artifacts could
  be mistaken for full P6 closure or P7-P12 approval.
- implementation drift risks where docs-only review gates could be misused to
  add parser, reader, ingestion, feature extraction, label generation, CLI or
  model-output paths.
- source-rights risks for real Tenhou, real haifu, external logs, platform
  data, account/session/cookie/token data and source-specific real-data
  approval.
- artifact risks for third-party binaries, `params/`, unknown model weights,
  checkpoints and snapshots.
- overclaim risks where P6 governance, schema, fixture or review evidence
  could be misread as model strength, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison or candidate-promotion
  evidence.

No risk-register coverage blocker was found.

## Risk / Source-Rights Consistency Matrix

| risk_or_source_item | source_inventory_status | risk_register_status | evidence_index_status | full_p6_closure_relevance | current_status | closure_blocker | required_before_final_closure | deferred_or_blocked_reason | guardrail | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Project-authored synthetic/local fixture | Allowed only for current docs/smoke/review context; small project-authored fixture may remain in Git. | Synthetic overclaim and no-real-data guardrails tracked. | Accepted current-scope P6 smoke evidence only. | Required accepted current-scope evidence. | consistent | no | Keep synthetic-only warning active. | n/a | No real data, no training use, no strength claim. | `tests/fixtures/data/synthetic_replay_smoke.json` remains read-only in this review. |
| Repository documentation | Project-owned docs in Git. | Governance overclaim/stage drift risks tracked. | Planning/review/finalization evidence only. | Required for closure audit. | consistent | no | Keep docs as source of truth. | n/a | Docs do not approve implementation by themselves. | Git + docs remain source of truth. |
| Third-party code references | Methodology/interface reference only; no vendoring or data use. | Third-party artifact and license/hygiene risks tracked. | External reference evidence only where logged. | Not required for full P6 closure beyond risk awareness. | consistent | no | Preserve reference-only status. | External license and artifact policy. | No third-party source, binaries or params in repo. | Akochan/Mortal references are not P6 data sources. |
| Real Tenhou / ranked logs | Unapproved / blocked. | Platform/legal/privacy/account risk tracked. | No approved source evidence. | Not required for full P6 closure. | blocked | no | Keep blocked. | Requires separate lawful source, terms, privacy and storage review. | No Tenhou access, scraping, automation or account tooling. | Not stable-dan evidence in P6. |
| Real haifu / external logs | Unapproved / blocked. | Rights/provenance/privacy risk tracked. | No approved source evidence. | Not required for full P6 closure. | blocked | no | Keep blocked. | Requires source-specific allowed-use and storage approval. | No real haifu or external-log ingestion. | No parser/reader approval. |
| Platform/account data | Blocked. | Account/session/cookie/token security and platform risks tracked. | No approved evidence. | Not required for full P6 closure. | blocked | no | Keep blocked. | Privacy/security/platform terms risk. | No account/session/cookie/token handling. | No online account data path. |
| Model outputs / self-play / league outputs | Later-stage / unapproved as P6 source. | Stage-drift and provenance risks tracked. | No source approval. | Not required for full P6 closure. | deferred / later-stage | no | Keep deferred. | Requires later model-output, self-play or league stage approval. | No model-output integration. | Not current P6 source data. |
| Third-party binaries / weights / params / checkpoints | Blocked. | Artifact provenance/license/hygiene risks tracked. | No repository artifact evidence. | Not required for full P6 closure. | blocked | no | Keep blocked. | Unknown provenance or redistribution constraints. | No `system.exe`, `libai.so`, `params/`, `*.pth`, `*.pt`, checkpoints or snapshots. | Fixed-sample Akochan workflow evidence remains interface evidence only. |
| Parser / dataset reader / ingestion | Source-consuming implementation not approved. | Implementation-drift and real-data ambiguity risks tracked. | Explicitly non-evidence / unapproved. | Not required for full P6 closure. | deferred / blocked | no | Keep unapproved. | Needs source approval plus parser/reader/ingestion proposal. | No parser, reader, ingestion or broad file interface. | Current schema validates in-memory mappings only. |
| Feature extraction / label generation | Unapproved training-facing data work. | Hidden-information, leakage and stage-drift risks tracked. | No feature/label evidence. | Not required for full P6 closure. | deferred | no | Keep deferred. | Requires parser/reader/source readiness and later P7-adjacent review. | No derived feature or label pipeline. | No supervised labels in accepted fixture. |
| CLI / broad file ingestion | Explicitly out of scope. | Scope expansion risk tracked. | No evidence. | Not required for full P6 closure. | out of scope | no | Keep out of scope. | Expands ingestion and misuse surface. | No CLI, directory reader, glob reader or generic path ingestion. | Future task required if ever needed. |
| Data-quality/storage/versioning expansion | Docs only beyond current smoke scope. | Data hygiene/storage risks tracked. | Deferred beyond accepted current scope. | Not required for full P6 closure. | deferred | no | Keep deferred. | No approved broad dataset or real/derived corpus. | No raw real data in Git. | Future source-specific policy needed. |
| Evidence/model-strength/Tenhou/LuckyJ/candidate promotion overclaims | All source docs mark current evidence as non-strength. | Overclaim risks tracked as high severity. | Evidence index forbids these interpretations. | Required guardrail for closure. | consistent | no | Keep warnings active. | No model evaluation or ranked-game evidence exists. | Do not claim strength, Tenhou, stable-dan ranked-game, LuckyJ or candidate promotion. | P6 evidence is governance/schema/smoke only. |
| P7-P12 premature entry | P6 docs do not approve later stages. | Stage-control risks tracked. | Evidence index marks P7-P12 entry as no. | Required guardrail for closure. | unapproved | no | Keep unapproved. | Requires post-full-P6 transition review plus stage-specific scope/risk/first-task approval. | Do not define or execute P7 tasks from this review. | Final closure, if it passes later, is still not P7 implementation. |

## Blocked / Deferred / Later-Stage / Out-of-Scope Consistency

The blocked, deferred, later-stage and out-of-scope classifications are
consistent across `02A`, `02D`, `02U`, `02V`, `02W`, `02X`, `02Y`, the risk
register and the evidence log.

Blocked items remain:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token usage.
- source-specific real-data approval.
- parser / reader paths that consume external or platform data.
- ingestion pipeline using unapproved sources.
- third-party binaries, `params/`, model weights, checkpoints and snapshots.

Deferred items remain:

- additional replay schema expansion.
- additional synthetic fixtures.
- parser.
- dataset reader.
- data ingestion.
- feature extraction.
- label generation.
- broader data-quality checks.
- storage/versioning expansion.
- CLI / broad file ingestion.
- model-output integration.

Later-stage or out-of-scope items remain:

- training.
- tuning.
- self-play.
- league / runner.
- P7-P12 execution.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

No classification mismatch was found.

## Final Full P6 Closure Blocker Status

No risk/source-rights blocker was found for the final full P6 closure review
gate.

This does not close full P6. It only means the risk register and source-rights
inventory are consistent enough for the next docs-only closure review gate to
decide whether full P6 can close for the documented synthetic/local
data-system groundwork scope.

## Governance Synchronization Review

| document | review_finding | blocker |
|---|---|---|
| `docs/00_HANDOFF.md` | Current P6 state, accepted current-scope closure, full P6 open status and next final closure review gate are recorded. | no |
| `docs/00_DOCS_INDEX.md` | P6 docs index includes the closure path through `02Y`; this task adds `02Z`. | no |
| `docs/10_next/10_NEXT.md` | Current first item is this review gate; this task sets final full P6 closure review as the next first item. | no |
| `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` | Current stage and forbidden scope match this review. | no |
| `docs/09_governance/09_EVIDENCE_LOG.md` | Evidence grades remain conservative and non-strength. | no |
| `docs/09_governance/09_RISK_REGISTER.md` | Risk categories cover overclaim, stage drift, implementation drift, source rights and artifact hazards. | no |
| `docs/09_governance/09_CHANGELOG.md` | This task is recorded as docs-only consistency review. | no |
| `docs/09_governance/09_DECISION_RECORD.md` | Decision records next docs-only final closure review gate. | no |
| `docs/09_governance/09_STAGE_TASK_CONTRACT.md` | Stage contract points to this review and then final full P6 closure review. | no |
| `docs/07_development_execution/07B_TASK_BACKLOG.md` | Current task moves from planned/current to done and next gate is planned. | no |
| `docs/07_development_execution/07A_MILESTONES.md` | Current position is updated to final full P6 closure review pending. | no |

No governance mismatch was found.

## Validation Results

Validation commands for this task:

```text
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Results:

```text
git diff --check: passed
python3 -m unittest tests/data/test_replay_schema.py: passed, 7 tests
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py: passed, 1 test
```

## Review Decision

```text
Review can close; no risk/source-rights blocker for final full P6 closure review.
```

Rationale:

- Source-rights inventory status remains consistent with the P6 closure path.
- Risk register coverage is sufficient for final full P6 closure review.
- Blocked real-data, platform, external-log, account and third-party artifact
  categories remain explicitly blocked.
- Deferred parser, reader, ingestion, feature, label, CLI and model-output
  categories remain unapproved.
- Evidence grades remain conservative and do not imply strength, Tenhou,
  stable-dan ranked-game, LuckyJ comparison or candidate promotion.
- P7-P12 non-entry boundaries remain explicit.
- Governance docs are synchronized.
- No blocker was found.

This decision does not close full P6 and does not approve P7-P12.

## Next Task Recommendation

Recommended next task:

```text
Run final full P6 closure review gate.
```

The next task must be docs-only. It may decide whether full P6 can close for
the documented synthetic/local data-system groundwork scope. It must not be
implementation, P7 execution, P7 entry approval, production code, tests,
fixtures, parser, dataset reader, ingestion, feature extraction, label
generation, real Tenhou, real haifu, external logs, platform data, account /
session / cookie / token handling, model-output integration, CLI, broad file
ingestion, training, tuning, self-play, league or model-strength claims.

If the final full P6 closure review passes, the next step must still be a
separate post-full-P6 transition review before defining any P7 scope or task.

## Evidence Grade

```text
P6 risk-register and source-rights consistency review before final closure evidence only.
```

## Explicit Non-Evidence

This review is not:

- full P6 closure.
- P7-P12 entry approval.
- P7 scope approval.
- new implementation approval.
- source approval.
- data ingestion.
- parser.
- dataset reader.
- feature extraction.
- label generation.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- account/session/cookie/token handling.
- model-output integration.
- CLI or broad file ingestion.
- third-party artifact approval.
- metric implementation or registry code change.
- promotion criteria change.
- training.
- tuning.
- self-play.
- league.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
