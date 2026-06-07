# 02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE

## Scope

This document defines P6 current-scope data-system closure criteria after the
minimal replay schema and project-authored synthetic/local fixture were
accepted as current-scope complete in `02P`.

This is a docs-only closure criteria definition. It does not:

- close full P6.
- close current-scope P6.
- approve P7-P12 entry.
- approve new implementation.
- add production code, tests, fixtures or data files.
- modify `src/mjlabai/data/replay_schema.py`.
- modify `tests/fixtures/data/synthetic_replay_smoke.json`.
- modify `tests/data/test_replay_schema.py`.
- modify `tests/data/test_synthetic_replay_fixture_schema.py`.
- implement parser, dataset reader, data ingestion, feature extraction or label
  generation.
- read real Tenhou, real haifu, external logs or platform data.
- use account, session, cookie, token or private-log data.
- add model-output integration, CLI or broad file ingestion.
- train, tune, self-play, run league or runner behavior.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

This document only defines the conditions under which the current
synthetic/local P6 data-system scope may enter a later docs-only closure review.

## Current Accepted Scope

Accepted current scope from `02P`:

- minimal replay schema module current-scope complete.
- project-authored synthetic/local replay fixture current-scope complete.
- two minimal local tests current-scope complete.
- directly related governance synchronization current-scope complete.

Task-selection context from `02Q`:

- the next-task definition reviewed candidate P6 docs-only follow-ups.
- `02Q` selected closure criteria definition as the safest next step.
- the reason was to prevent P6 from continuing indefinitely through more schema
  or fixture planning before deciding whether the current synthetic/local scope
  is closeable.

Not accepted:

- full P6 closure.
- additional replay schema expansion.
- additional fixtures.
- additional tests.
- parser.
- dataset reader.
- data ingestion.
- feature extraction.
- label generation.
- real data.
- CLI.
- model-output integration.
- training, self-play or league.
- P7-P12.
- model-strength evidence.

## P6 Current-Scope Closure Criteria

Current-scope P6 may enter a final closure review only if all required criteria
below remain true.

| id | criterion | required_before_closure | current_status | evidence |
|---|---|---|---|---|
| C1 | P6 scope, entry criteria and first task are documented. | yes | satisfied | `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` |
| C2 | Data-source provenance and rights inventory is defined and reviewed. | yes | satisfied | `docs/02_data_system/02A_DATA_SOURCES.md`; `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md` |
| C3 | Replay schema documentation boundary is defined and reviewed. | yes | satisfied | `docs/02_data_system/02B_REPLAY_SCHEMA.md`; `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md` |
| C4 | Synthetic/local replay fixture boundary is defined and reviewed. | yes | satisfied | `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`; `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md` |
| C5 | Replay schema and fixture readiness checklist is defined and reviewed. | yes | satisfied | `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`; `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md` |
| C6 | Implementation proposal boundary is defined and reviewed. | yes | satisfied | `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`; `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md` |
| C7 | Minimal implementation proposal is prepared and reviewed. | yes | satisfied | `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`; `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md` |
| C8 | Approval decision for exact minimal implementation is complete. | yes | satisfied | `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md` |
| C9 | Exact minimal implementation is complete only in approved files. | yes | satisfied | `src/mjlabai/data/replay_schema.py`; `tests/fixtures/data/synthetic_replay_smoke.json`; `tests/data/test_replay_schema.py`; `tests/data/test_synthetic_replay_fixture_schema.py` |
| C10 | Exact minimal implementation is reviewed. | yes | satisfied | `docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md` |
| C11 | Exact minimal implementation is accepted as current-scope complete. | yes | satisfied | `docs/02_data_system/02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION.md` |
| C12 | Next-task definition is complete and selects closure criteria as next step. | yes | satisfied | `docs/02_data_system/02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md` |
| C13 | Closure criteria are defined. | yes | satisfied by this document | `docs/02_data_system/02R_P6_CURRENT_SCOPE_DATA_SYSTEM_CLOSURE_CRITERIA_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE.md` |
| C14 | Docs index is synchronized. | yes | must be reviewed | `docs/00_DOCS_INDEX.md` |
| C15 | Handoff is synchronized. | yes | must be reviewed | `docs/00_HANDOFF.md` |
| C16 | Technical plan is synchronized. | yes | must be reviewed | `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` |
| C17 | Evidence log remains conservative. | yes | must be reviewed | `docs/09_governance/09_EVIDENCE_LOG.md` |
| C18 | Risk register covers overclaim, stage creep, real-data and implementation-expansion risks. | yes | must be reviewed | `docs/09_governance/09_RISK_REGISTER.md` |
| C19 | `10_NEXT` hygiene is correct. | yes | must be reviewed | `docs/10_next/10_NEXT.md` |
| C20 | Required validation commands pass. | yes | must be rerun in review | `git diff --check`; data unittest commands |
| C21 | No unresolved blocker remains. | yes | must be reviewed | closure review gate |
| C22 | No unclassified required P6 current-scope item remains. | yes | must be reviewed | closure review gate |
| C23 | Deferred items are explicitly marked not required for current-scope closure. | yes | defined below | this document |
| C24 | P7-P12 non-entry boundary is clear. | yes | defined below | this document |
| C25 | No model-strength overclaim exists. | yes | must be reviewed | evidence log, handoff and `10_NEXT` |

## Exit Readiness Checklist

| checklist_item | status | evidence | blocker | required_before_closure | notes |
|---|---|---|---|---|---|
| P6 docs consistency | ready | `02A` through `02Q` | no | yes | Needs review after this `02R` sync. |
| Source inventory consistency | ready | `02A`, `02D` | no | yes | Project-authored synthetic/local fixture remains the only accepted source. |
| Replay schema boundary consistency | ready | `02B`, `02E`, `02N`, `02O`, `02P` | no | yes | No further schema expansion is approved. |
| Synthetic fixture boundary consistency | ready | `02F`, `02G`, `02O`, `02P` | no | yes | No additional fixture is approved. |
| Minimal implementation review consistency | ready | `02O` | no | yes | Exact implementation was reviewed with no blocker. |
| Current-scope acceptance consistency | ready | `02P` | no | yes | Accepted only the exact minimal scope. |
| Governance tracking consistency | ready | handoff, index, changelog, evidence, risk, stage contract, backlog, milestones, technical plan | no | yes | Must be reviewed in next gate after this update. |
| Validation status | ready | existing data unittest commands | no | yes | Must be rerun in the closure-criteria review gate. |
| No implementation expansion | ready | git diff and file list | no | yes | This task must remain docs-only. |
| No real data | ready | fixture source note and P6 source inventory | no | yes | Real/external/platform sources remain unapproved. |
| No parser / reader / ingestion | ready | `02P`, `02Q`, this document | no | yes | These are deferred, not required for current-scope closure. |
| No feature / label | ready | `02P`, `02Q`, this document | no | yes | These remain deferred. |
| No P7-P12 | ready | stage contract and `10_NEXT` | no | yes | Later-stage entry requires separate transition review. |
| Final closure review required | not_ready | this document | no | yes | Current-scope P6 is not closed by this criteria definition. |

## Required Remaining Current-Scope P6 Items

Before current-scope P6 can be closed, the remaining required items are:

1. Review P6 current-scope data-system closure criteria after minimal replay
   schema acceptance.
2. If that review finds no blocker, run a final P6 current-scope data-system
   closure review gate.
3. If the closure review requires final synchronization, perform final handoff /
   evidence index sync before recording closure.

No implementation blocker is currently identified. Parser, dataset reader,
ingestion, feature extraction, label generation, real data, CLI, training,
self-play, league and P7-P12 work are not required current-scope items.

## Deferred Items

| deferred_item | defer_reason | earliest_possible_condition | why_not_required_for_current_scope_closure | guardrail |
|---|---|---|---|---|
| Additional replay schema expansion | Current minimal schema is accepted for smoke scope. | Later explicit proposal and approval decision. | Current-scope closure concerns only accepted minimal schema. | Do not modify `replay_schema.py` without `10_NEXT` approval. |
| Additional fixtures | Current fixture is accepted for smoke scope. | Later fixture-boundary update and approval. | Current-scope closure does not require broader fixture coverage. | No new fixture without explicit task. |
| Additional tests | Two minimal tests are accepted for current scope. | Later test proposal and approval. | Current-scope closure can rely on accepted minimal tests. | No test edits in closure tasks. |
| Parser | Parser work is broader data-system implementation. | Separate parser scope, source approval and implementation approval. | Current synthetic/local smoke scope validates mappings only. | Parser remains closed. |
| Dataset reader | Reader work implies ingestion/file interfaces. | Separate reader boundary and approval. | Current scope has no dataset reading requirement. | No reader or broad file ingestion. |
| Data ingestion | Ingestion requires source rights and storage approvals. | Source-specific approval and ingestion plan. | Current accepted source is project-authored synthetic/local only. | No real/external/platform ingestion. |
| Feature extraction | Feature generation depends on parser/reader and label plans. | Later P6/P7 transition scope and approval. | Current closure is schema/fixture smoke only. | No derived feature pipeline. |
| Label generation | Labels require approved data and training objective boundary. | Later supervised-policy scope and approval. | Current closure does not create training labels. | No label fields or label generation. |
| Real Tenhou | Platform access/compliance is unapproved. | Separate lawful/compliance review. | Current source inventory accepts only project-authored synthetic/local fixture. | No Tenhou account/session/platform access. |
| Real haifu | Real log rights/provenance are unapproved. | Source-specific rights and storage approval. | Current closure does not need real logs. | No real haifu ingestion. |
| External logs | External provenance and allowed use are unapproved. | Source-specific rights and evidence review. | Current scope uses no external logs. | No external-log ingestion. |
| Platform data | Platform terms, privacy and storage are unapproved. | Separate platform-data review. | Current closure does not require platform data. | No platform data. |
| Source approval beyond project-authored synthetic fixture | Only project-authored synthetic/local source is accepted. | Future source inventory update and approval. | Current closure can close without broader sources. | Keep source approvals explicit. |
| CLI | CLI creates broader use and ingestion surface. | Separate CLI scope and approval. | Current tasks are local docs/schema smoke only. | No CLI. |
| Broad file ingestion | Broad ingestion expands risk and scope. | Separate ingestion proposal and approval. | Current fixture path is known and minimal. | No glob/directory readers. |
| Model-output integration | Model outputs are not part of current P6 scope. | Later model/evaluation integration approval. | Current closure has no model output. | No model-output fields or paths. |
| Training | Training is P7/P8/P11 work. | Later stage entry after independent scope review. | Current P6 closure is data groundwork only. | No training. |
| Self-play | Self-play is later RL/evaluation work. | Later P8/P10 scope approval. | Current closure has no simulator or league. | No self-play. |
| League / runner | League/runner belongs later evaluation/training stages. | Later P10 scope approval. | Current closure does not need match execution. | No runner or league. |
| P7-P12 | Later stages need independent transition review. | Current-scope P6 closure plus separate scope / entry criteria / risk review / first task approval. | Current closure is not later-stage entry. | Do not jump stages. |
| Model-strength evidence | No model is evaluated. | Later validated model evaluation with samples and guardrails. | Current schema/fixture work is not strength evidence. | No strength claims. |
| LuckyJ `10.68` comparison | Requires real evaluation evidence, not schema smoke. | Later compliant stable-dan validation. | Current closure has no ranked-game evidence. | No LuckyJ claim. |
| Candidate promotion | Promotion requires racing-funnel evidence. | Later funnel gate evidence and review. | Current P6 closure does not evaluate candidates. | No promotion claims. |

## P7-P12 Non-Entry Conditions

Do not enter P7-P12 if any of the following is true:

- P6 current-scope closure criteria have not been reviewed.
- final P6 current-scope closure review has not passed.
- any unresolved P6 blocker remains.
- validation fails.
- governance documents disagree about current stage or next task.
- evidence is overclaimed.
- real-data or source approval is ambiguous.
- parser, reader, ingestion, feature or label work is treated as already
  approved.
- P7-P12 lacks independent scope, entry criteria, risk review and first task.
- human / Web ChatGPT approval is absent.
- `docs/10_next/10_NEXT.md` does not explicitly allow transition.

## Closure Criteria Decision

```text
P6 current-scope data-system closure criteria are defined for review after
minimal replay schema acceptance.
```

This does not close full P6, does not close current-scope P6 and does not
approve P7-P12 entry.

Current-scope closure decision now:

```text
No.
```

A later docs-only closure-criteria review gate must review these criteria
before any final current-scope closure decision.

## Next Task Recommendation

Recommended next first task:

```text
Review P6 current-scope data-system closure criteria after minimal replay schema acceptance.
```

Required boundary for that next task:

- docs-only review gate.
- no code.
- no tests.
- no fixtures.
- no replay schema expansion.
- no parser.
- no dataset reader.
- no ingestion.
- no feature extraction.
- no label generation.
- no real Tenhou, real haifu, external logs or platform data.
- no model-output integration.
- no CLI or broad file ingestion.
- no training, tuning, self-play, league or runner behavior.
- no P7-P12.
- no model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claim.

## Evidence Grade

```text
P6 current-scope data-system closure criteria definition after minimal replay
schema acceptance evidence only.
```

## Explicit Non-Evidence

This closure criteria definition is not evidence of:

- full P6 closure.
- current-scope P6 closure.
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
- model strength.
- Tenhou ranked performance.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- P7-P12 entry approval.
