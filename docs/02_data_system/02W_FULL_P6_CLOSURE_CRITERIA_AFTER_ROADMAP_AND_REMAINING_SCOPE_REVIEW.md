# 02W_FULL_P6_CLOSURE_CRITERIA_AFTER_ROADMAP_AND_REMAINING_SCOPE_REVIEW

## Scope

This document defines full P6 closure criteria after the full P6 roadmap and
remaining scope inventory were reviewed in
`docs/02_data_system/02V_FULL_P6_CLOSURE_ROADMAP_AND_REMAINING_SCOPE_INVENTORY_REVIEW.md`.

This task is docs-only. It does not close full P6, approve P7-P12 entry,
approve implementation, add code, add tests, add fixtures, add data files or
modify implementation artifacts.

Current status:

- P5 is closed only for the current synthetic/local evaluation groundwork
  scope.
- Accepted current-scope P6 is closed only for the synthetic/local minimal
  replay schema and project-authored synthetic fixture scope.
- Full P6 remains open.
- P7-P12 remain unapproved.
- Parser, dataset reader, ingestion, feature extraction, label generation,
  real data, model-output integration, CLI, training, self-play and league
  remain unapproved.

## Full P6 Closure Scope

Full P6 closure scope is limited to the data-system documentation,
governance and accepted synthetic/local minimal data-system groundwork needed
before any later supervised-learning or broader data work can be considered.

Included scope:

- P6 scope, entry criteria and first-task definition.
- Source inventory and source-rights guardrails.
- Replay schema documentation boundary.
- Synthetic/local replay fixture boundary.
- Readiness checklist.
- Implementation proposal boundary.
- Minimal accepted replay schema and project-authored synthetic fixture smoke
  implementation.
- Implementation review and current-scope acceptance.
- Current-scope closure criteria, review and final current-scope closure gate.
- Post-current-scope transition review.
- Full P6 roadmap / remaining inventory and review.
- Full P6 closure criteria and review.
- Full P6 handoff / evidence / risk / source-rights finalization.
- Final full P6 closure review gate.
- Deferred, blocked, later-stage and explicitly out-of-scope inventory.
- P7-P12 non-entry boundaries.

Excluded scope:

- Parser.
- Dataset reader.
- Data ingestion.
- Feature extraction.
- Label generation.
- Real Tenhou.
- Real haifu.
- External logs.
- Platform data.
- Account / session / cookie / token usage.
- CLI.
- Broad file ingestion.
- Model-output integration.
- Training.
- Tuning.
- Self-play.
- League / runner.
- Model-strength evidence.
- Tenhou ranked evidence.
- Stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- Candidate promotion.
- P7-P12 entry.

## Full P6 Closure Criteria

| criterion | required_before_full_p6_closure | current_status | evidence | blocker | notes |
|---|---|---|---|---|---|
| C1. P6 scope / entry criteria / first task definition complete. | yes | ready | `02C` | none | Docs-only P6 entry was defined after post-P5 review. |
| C2. Source inventory defined and reviewed. | yes | ready | `02A`, `02D` | none | Inventory is not source approval. |
| C3. Replay schema documentation boundary defined and reviewed. | yes | ready | `02B`, `02E` | none | Boundary is documentation-only; implementation remains limited to later approved files. |
| C4. Synthetic/local replay fixture boundary defined and reviewed. | yes | ready | `02F`, `02G` | none | Fixture scope is project-authored synthetic/local only. |
| C5. Readiness checklist defined and reviewed. | yes | ready | `02H`, `02I` | none | Checklist did not approve implementation. |
| C6. Implementation proposal boundary defined and reviewed. | yes | ready | `02J`, `02K` | none | Proposal boundary kept parser / reader / ingestion closed. |
| C7. Minimal implementation proposal prepared and reviewed. | yes | ready | `02L`, `02M` | none | Proposal was conservative and limited to exact future files. |
| C8. Approval decision completed. | yes | ready | `02N` | none | Approval was only for the exact minimal implementation task. |
| C9. Exact minimal implementation completed in approved files only. | yes | ready | `src/mjlabai/data/replay_schema.py`, `tests/fixtures/data/synthetic_replay_smoke.json`, `tests/data/test_replay_schema.py`, `tests/data/test_synthetic_replay_fixture_schema.py` | none | This is in-memory synthetic/local schema smoke implementation only. |
| C10. Minimal implementation reviewed. | yes | ready | `02O` | none | Review found no blocker. |
| C11. Minimal implementation accepted as current-scope complete. | yes | ready | `02P` | none | Accepted only for current-scope minimal schema / fixture. |
| C12. Current-scope closure criteria defined and reviewed. | yes | ready | `02R`, `02S` | none | Criteria review can close. |
| C13. Final current-scope closure review completed. | yes | ready | `02T` | none | Current-scope P6 closed only for accepted synthetic/local minimal scope. |
| C14. Post-current-scope transition review completed. | yes | ready | `12C` | none | Full P6 remained open. |
| C15. Full P6 roadmap / remaining inventory defined and reviewed. | yes | ready | `02U`, `02V` | none | Review can close with no blocker. |
| C16. Full P6 closure criteria defined and reviewed. | yes | partially_ready | this document defines criteria; review is not done | review gate pending | This task defines criteria only; the next task must review them. |
| C17. Full P6 handoff and evidence index finalized. | yes | not_ready | n/a | criteria review pending | Must happen after criteria review. |
| C18. Full P6 risk register and source-rights consistency reviewed. | yes | not_ready | n/a | criteria review pending | Must confirm blocked/deferred real-data items remain explicit. |
| C19. Final full P6 closure review gate completed. | yes | not_ready | n/a | handoff/evidence/risk finalization pending | Only this later gate may close full P6. |
| C20. Validation commands pass. | yes | ready_for_this_task | local validation required each gate | none for this definition | Required commands remain `git diff --check` and the two data unittests. |
| C21. No unresolved blocker. | yes | ready_for_this_task | this document classifies blockers | later review must confirm | Any blocker found later stops closure. |
| C22. No unclassified required full-P6 item. | yes | ready_for_this_task | `02U`, `02V`, this document | later review must confirm | Parser / reader / ingestion / feature / label are not required closure items. |
| C23. Deferred / blocked / later-stage items clearly classified. | yes | ready_for_this_task | `02U`, this document | later review must confirm | Classification prevents implicit approval. |
| C24. P7-P12 non-entry boundary clear. | yes | ready_for_this_task | this document, `10_NEXT` | later review must confirm | P7-P12 require separate transition, scope, risk and first-task approval. |
| C25. No model-strength / Tenhou / LuckyJ / candidate-promotion overclaim. | yes | ready_for_this_task | this document, evidence log | later review must confirm | P6 artifacts are data-system governance/smoke evidence only. |
| C26. Governance synchronized. | yes | ready_for_this_task | handoff, index, changelog, evidence, risk, decision, stage contract, backlog, milestones, technical plan, `10_NEXT` | sync must be checked | This task updates governance docs. |
| C27. `10_NEXT` hygiene maintained. | yes | ready_for_this_task | `docs/10_next/10_NEXT.md` | none if updated | The next task must be a docs-only criteria review gate. |

## Full P6 Exit Readiness Checklist

| checklist_item | status | evidence | blocker | required_before_closure | notes |
|---|---|---|---|---|---|
| Source inventory / rights consistency. | ready | `02A`, `02D`, `02U`, `02V` | none for docs closure | yes | Inventory remains a guardrail, not source approval. |
| Replay schema boundary consistency. | ready | `02B`, `02E`, minimal implementation artifacts | none | yes | Existing implementation is accepted only for minimal synthetic/local scope. |
| Synthetic/local fixture boundary consistency. | ready | `02F`, `02G`, `tests/fixtures/data/synthetic_replay_smoke.json` | none | yes | Fixture is project-authored synthetic/local only. |
| Minimal implementation review / acceptance consistency. | ready | `02O`, `02P` | none | yes | Exact approved files only. |
| Full P6 roadmap / inventory consistency. | ready | `02U`, `02V` | none | yes | Classification review can close. |
| Full P6 closure criteria review requirement. | not_ready | this document | criteria review pending | yes | Next task must review this document. |
| Full P6 handoff / evidence finalization. | not_ready | n/a | criteria review pending | yes | Must finalize after criteria review. |
| Risk register / source-rights consistency review. | not_ready | n/a | criteria review pending | yes | Must verify blocked real-data categories remain blocked. |
| Validation status. | ready_for_this_task | required commands | none if commands pass | yes | Must be rerun for each closure gate. |
| No unresolved blocker. | ready_for_this_task | this document | later review pending | yes | If a blocker appears, stop before closure. |
| No implementation expansion. | ready | git diff / docs-only scope | none | yes | This task adds documentation only. |
| No real data. | ready | docs and fixture guardrails | none | yes | Real Tenhou, haifu, logs and platform data remain absent. |
| No parser / reader / ingestion. | ready | source boundaries | none | yes | Current schema validates in-memory mappings only. |
| No feature / label generation. | ready | source boundaries | none | yes | Training-facing data remains later-stage. |
| No P7-P12 entry. | ready | this document and `10_NEXT` | none | yes | Later stages require independent approval. |
| Final full P6 closure review. | not_ready | n/a | prerequisites incomplete | yes | This task does not close full P6. |

## Required Remaining Full-P6 Items

Required before full P6 closure:

- Review full P6 closure criteria after roadmap and remaining scope review.
- Finalize full P6 handoff and evidence index.
- Review full P6 risk register and source-rights inventory consistency.
- Run final full P6 closure review gate.
- If final full P6 closure passes, run a separate post-full-P6 transition
  review before defining any P7 task.

Parser, dataset reader, ingestion, feature extraction, label generation, real
data, CLI, training, tuning, self-play, league and P7-P12 are not required
full-P6 closure items for this roadmap. They remain deferred, blocked,
later-stage or out of scope unless a later approved task changes that status.

## Deferred Items

| deferred_item | defer_reason | earliest_possible_condition | why_not_required_for_full_p6_closure | guardrail | owner_doc_or_future_review |
|---|---|---|---|---|---|
| Additional replay schema expansion. | Minimal accepted schema is enough for current closure path. | Later explicit schema expansion proposal and review. | Full P6 can close with minimal accepted schema plus deferred inventory. | No `replay_schema.py` change without `10_NEXT`. | Future replay schema expansion proposal. |
| Additional synthetic fixtures. | Current fixture covers accepted smoke scope. | Later fixture-boundary update / proposal / approval. | Not needed for current synthetic/local closure path. | No new fixture without explicit task. | Future synthetic fixture proposal. |
| Parser. | Raw-log semantics and source approval are absent. | Parser boundary, source approval and implementation approval. | Current schema validates in-memory mappings only. | No parser from closure wording. | Future parser boundary review. |
| Dataset reader. | Reader creates file-ingestion surface. | Reader boundary, storage policy and approval. | Current tests use a known project-authored fixture only. | No broad file ingestion. | Future dataset-reader proposal. |
| Data ingestion. | Source rights, privacy and storage approval are absent. | Source-specific approval plus ingestion proposal. | Closure can record ingestion as blocked/deferred. | No real/external/platform data ingestion. | Future ingestion boundary review. |
| Feature extraction. | Requires parser/reader/source and hidden-information policy. | Feature policy and source readiness. | P6 can close current docs/smoke path without training-ready features. | No derived feature pipeline. | Future feature policy review. |
| Label generation. | Requires approved data and leakage policy. | Label policy, leakage review and P7 readiness. | Current P6 artifacts are not supervised labels. | No labels or label fields. | Future label policy review. |
| Data-quality expansion beyond current smoke. | No broad approved dataset exists. | Approved dataset/source and quality policy. | Current tests cover smoke schema only. | No broad checker now. | Future data-quality boundary. |
| Storage/versioning expansion beyond current docs. | No approved real or derived corpus exists. | Source-specific storage/versioning review. | Full P6 can close with this item recorded as deferred. | No raw real data in git. | Future storage/versioning policy. |
| CLI / broad file ingestion. | Creates broad ingestion and misuse surface. | Separate CLI/file-ingestion proposal if ever needed. | Not needed for closure or current fixture validation. | No CLI or directory/glob reader. | Future CLI/file-ingestion boundary. |
| Model-output integration. | Model-output provenance and stage boundary are absent. | Separate model-output boundary. | Not a data-system closure requirement. | No model code integration. | Future model-output review. |

## Blocked Items

| blocked_item | blocker_reason | release_condition | guardrail |
|---|---|---|---|
| Real Tenhou. | Platform/legal/privacy/account risk. | Separate lawful compliance, source-rights, privacy and storage review. | No Tenhou access, scraping, automation or account tooling. |
| Real haifu. | Provenance, rights, privacy and storage approval absent. | Source-specific allowed-use and storage approval. | No real haifu ingestion. |
| External logs. | Source rights, provenance and privacy absent. | Source-specific evidence and approval. | No external-log ingestion. |
| Platform data. | Platform terms, privacy and account/session risk. | Platform-data legal/privacy review. | No platform data or automation. |
| Account / session / cookie / token usage. | Security, privacy and platform risk. | Not part of current roadmap. | Do not handle or store account credentials. |
| Source-specific real-data approval. | No source-specific rights/terms/storage evidence. | Future source-specific review with evidence and risk updates. | Inventory is not approval. |
| Parser / reader consuming external or platform data. | Source format and source rights are not approved. | Source approval plus parser/reader boundary and implementation approval. | No parser/reader implementation now. |
| Ingestion pipeline using unapproved sources. | Rights, privacy, storage and evidence absent. | Source-specific approval and ingestion proposal. | No ingestion pipeline. |
| Third-party binaries / params / model weights. | Provenance, license, redistribution and artifact policy unresolved. | Verified lawful artifact review, if ever relevant. | No `*.pth`, `*.pt`, checkpoints, snapshots, `system.exe`, `libai.so`, `params/` or third-party artifacts. |

## Later-Stage And Out-of-Scope Items

Later-stage items:

- Training.
- Tuning.
- Self-play.
- League / runner.
- P7 supervised learning.
- P8 reinforcement learning.
- P9 search / risk model.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou validation.

Explicitly out of scope for full P6 closure:

- Model-strength evidence.
- Tenhou ranked evidence.
- Stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- Candidate promotion.
- Production evaluator claims.

## P7-P12 Non-Entry Conditions

Do not enter P7-P12 if any of the following are true:

- Full P6 closure criteria have not been reviewed.
- Full P6 handoff / evidence finalization is incomplete.
- Risk register / source-rights consistency review is incomplete.
- Final full P6 closure review has not passed.
- Any unresolved blocker remains.
- Required validation fails.
- Governance docs disagree on current stage or next task.
- Evidence is overclaimed as model strength, Tenhou ranked evidence, stable-dan
  ranked-game evidence, LuckyJ comparison or candidate promotion.
- Real-data or source approval remains ambiguous.
- Parser, reader, ingestion, feature extraction or label generation is
  misclassified as approved.
- P7-P12 lacks independent scope, entry criteria, risk review, first task and
  human/Web ChatGPT approval.
- `docs/10_next/10_NEXT.md` does not explicitly permit a post-P6 transition
  review.

## Planning Decision

```text
Full P6 closure criteria are defined after roadmap and remaining scope review.
Full P6 remains open, and P7-P12 remain unapproved. This task does not approve
implementation, real data, parser, reader, ingestion, feature extraction,
label generation, training, self-play, league or model-strength claims.
```

## Next Task Recommendation

Recommended next task:

```text
Review full P6 closure criteria after roadmap and remaining scope review.
```

The next task must be a docs-only review gate. It must not be implementation,
P7 execution, P7 entry approval, full P6 closure, production code, tests,
fixtures, parser, dataset reader, ingestion, feature extraction, label
generation, real Tenhou, real haifu, external logs, platform data, account /
session / cookie / token handling, model-output integration, CLI, broad file
ingestion, training, tuning, self-play, league or model-strength claims.

## Evidence Grade

```text
P6 full-closure criteria definition evidence only.
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
