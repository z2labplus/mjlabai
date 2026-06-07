# 02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION

## Scope

This document prepares the approval decision for the minimal P6 replay schema
and project-authored synthetic fixture implementation task.

This is a docs-only P6 implementation approval decision / approval review. It
does not:

- execute P6 implementation.
- create replay schema code.
- create fixture files.
- create tests.
- implement dataclasses, pydantic models or JSON schema.
- implement parsers or dataset readers.
- implement data ingestion.
- implement feature extraction or label generation.
- read real Tenhou, real haifu, external logs or platform data.
- use online accounts, sessions, cookies, tokens or private logs.
- create platform automation, scraping, evasion or account tooling.
- connect model outputs.
- add CLI or broad file ingestion.
- add latency measurement, fixed-position exact-match computation, metric
  implementation, registry code changes or promotion criteria changes.
- call OpenAI, LLM or model APIs.
- call Akochan `system.exe`, `libai.so` or any third-party binary.
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

North-star relationship:

```text
Approving a tiny P6 replay schema / synthetic fixture implementation task can
serve the long-term stable-dan > 10.68 target only by allowing the smallest
auditable data-system smoke artifact before training, self-play or real-data
work. This approval decision is not implementation execution and is not
strength evidence.
```

## Reviewed Artifacts

Primary approval inputs:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
- `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
- `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`

Transition and evaluation context:

- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`

Governance / tracking context:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

Read-only source / test / fixture context:

- `src/mjlabai/eval/offline_result.py`
- `src/mjlabai/eval/stable_dan.py`
- `src/mjlabai/eval/legal_action_metric.py`
- `src/mjlabai/eval/tiny_benchmark_harness.py`
- `tests/fixtures/eval/stable_dan_placements_smoke.json`
- `tests/fixtures/eval/legal_action_metric_smoke.json`
- `tests/fixtures/eval/tiny_benchmark_harness_smoke.json`

The source, test and fixture files were context only. This approval decision
does not modify code, tests or fixtures.

## Approval Decision Purpose

This approval decision exists to decide whether a later first `10_NEXT` task
may implement the minimal P6 replay schema and project-authored synthetic
fixture described in `02L` and reviewed in `02M`.

This document may:

- decide whether the next task can be a minimal implementation task.
- define the exact files allowed in that future task.
- define exact forbidden expansions.
- define future validation commands.
- define rollback and stop conditions.
- require docs, evidence and risk synchronization.

This document must not:

- execute the implementation.
- create implementation files.
- approve real Tenhou, real haifu, external logs or platform data.
- approve P7-P12 entry.
- produce model-strength evidence.

## Approval Options

| option | decision | conditions | action |
|---|---|---|---|
| A | Approve next minimal implementation task. | `02M` found no blocker; exact minimal files are listed; no real / external / platform data is allowed; parser / reader / ingestion / feature / label work remains forbidden; rollback, stop conditions and validation commands are defined; docs / evidence / risk sync is defined. | Set `10_NEXT` to the exact minimal implementation task and do not execute it in this approval decision. |
| B | Do not approve; require blocker resolution. | A blocker exists, boundaries are unclear, source risk is unresolved, governance is mismatched or `10_NEXT` is inconsistent. | Keep implementation closed and set `10_NEXT` to the smallest docs-only blocker-resolution task. |
| C | Defer decision. | Human / Web ChatGPT needs more review, risk is not agreed or the project needs a more conservative approval review. | Keep implementation closed and set `10_NEXT` to a continued docs-only approval-review task. |

## Approval Criteria Review

| criterion | status | evidence | blocker | notes |
|---|---|---|---:|---|
| `02A` source inventory defined and reviewed. | pass | `02A`, `02D` | no | Source categories and rights/provenance vocabulary are defined and reviewed. |
| `02D` source inventory review found no blocker. | pass | `02D` | no | Review keeps source approval and ingestion approval separate. |
| `02B` replay schema documentation boundary defined. | pass | `02B` | no | Field families and forbidden scope are defined before code. |
| `02E` replay schema boundary review found no blocker. | pass | `02E` | no | Review keeps replay schema implementation closed. |
| `02F` synthetic/local fixture boundary defined. | pass | `02F` | no | Fixture boundary remains project-authored synthetic/local only. |
| `02G` fixture boundary review found no blocker. | pass | `02G` | no | Review keeps fixture implementation closed. |
| `02H` readiness checklist defined. | pass | `02H` | no | Readiness classes, dependencies and non-entry conditions are documented. |
| `02I` readiness checklist review found no blocker. | pass | `02I` | no | Review keeps all implementation classes closed. |
| `02J` proposal boundary defined. | pass | `02J` | no | Future proposal structure and approval conditions are defined. |
| `02K` proposal boundary review found no blocker. | pass | `02K` | no | Review allows only a later proposal draft. |
| `02L` minimal proposal prepared. | pass | `02L` | no | Exact candidate files, scope, validation, rollback and stop conditions are listed. |
| `02M` minimal proposal review found no blocker. | pass | `02M` | no | Review says the proposal is narrow enough for this approval decision. |
| Proposed file candidates are exact and narrow. | pass | `02L`, `02M` | no | Four exact future files are named. |
| No real / external / platform data. | pass | `02A`, `02F`, `02L`, `02M` | no | Future work remains synthetic/local only. |
| No parser / reader / ingestion / feature / label work. | pass | `02L`, `02M` | no | These classes remain forbidden. |
| Validation commands are future-safe. | pass | `02L`, `02M` | no | Commands are limited to `git diff --check` and two future unit tests. |
| Rollback plan exists. | pass | `02L`, `02M` | no | Rollback removes artifacts if they expand scope or overclaim evidence. |
| Stop conditions exist. | pass | `02L`, `02M` | no | Stop conditions cover forbidden data, tooling, overclaims and stage drift. |
| Evidence / risk / docs update plan exists. | pass | `02L`, `02M` | no | Governance synchronization is defined. |
| P7-P12 non-entry is clear. | pass | `02L`, `02M`, stage contract | no | Later stages remain closed. |
| Human / Web ChatGPT approval requirement is documented. | pass | `02L`, `02M` | no | Implementation requires explicit first `10_NEXT` implementation task. |
| No current code, tests or fixtures were created. | pass | current diff scope | no | This approval decision remains docs-only. |

Approval criteria finding:

```text
All approval criteria pass. No blocker was found.
```

## Exact Allowed Files If Approved

The next minimal implementation task, and only that task, may create or modify
these implementation files:

- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

The next minimal implementation task may also synchronize these docs:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`
- `docs/07_development_execution/07A_MILESTONES.md`

No other code, test, fixture or data file is approved by this decision unless
a later task explicitly updates the approval with the same narrow scope
discipline.

## Exact Allowed Future Scope If Approved

The approved next implementation task may include only:

- one minimal replay schema module.
- one project-authored synthetic/local replay fixture.
- one minimal replay schema unit test.
- one minimal synthetic fixture schema unit test.
- no-real-data / no-account-id / no-model-output / no-training-use assertions.
- JSON-safe serialization / validation helper if needed.
- evidence, risk, docs, handoff and `10_NEXT` synchronization.
- `git diff --check`.
- the newly created tests only.

The future implementation must use only the Python standard library.

## Forbidden Future Expansion

The approved next implementation task must not include:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account, session, cookie or token data.
- private logs.
- scraping, platform automation, evasion or anti-detection tooling.
- parser for real logs.
- dataset reader.
- ingestion pipeline.
- feature extraction.
- label generation.
- model-output integration.
- CLI.
- broad file ingestion.
- training, tuning, self-play, league or runner behavior.
- P7-P12.
- metric implementation.
- registry code changes.
- promotion criteria changes.
- model-strength claims.
- LuckyJ comparison.
- candidate promotion.
- third-party binaries, weights, params, checkpoints or snapshots.
- any file outside the exact allowed list unless a later approval decision
  explicitly documents and approves the change before modification.

## Future Validation Commands If Approved

The next implementation task should run:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

It may add only lightweight repository-local checks if needed. It must not
require real data, Tenhou, self-play, league, training, model-output,
Akochan `system.exe`, `libai.so` or any third-party binary.

## Stop Conditions

The next implementation task must stop before committing if any of these
appear:

- a required file outside the exact allowed implementation file list.
- real Tenhou, real haifu, external-log or platform-data content.
- account, session, cookie, token or private-log content.
- parser, dataset reader, ingestion pipeline, feature extraction or label
  generation behavior.
- model-output integration.
- CLI or broad file ingestion.
- third-party source, binary, params, weights, checkpoint or snapshot.
- OpenAI / LLM / model API call.
- tests or docs implying model strength, Tenhou evidence, stable-dan
  ranked-game evidence, LuckyJ `10.68` comparison or candidate promotion.
- validation failure.
- `git status` containing unapproved files.
- P7-P12 treated as current execution.

## Does This Task Generate Or Run Implementation Code?

No.

```text
This approval decision task may decide whether the next task can be a minimal
implementation task, but it does not execute implementation and does not
itself generate or run implementation code.
```

## Decision

```text
Approved for next minimal implementation task.
```

This approval is limited to the exact minimal task described in this decision.
It does not extend to P7-P12, real data, ingestion, parser, dataset reader,
feature extraction, label generation, CLI, model-output integration, training,
self-play or league.

Approved only for the next task:

```text
Implement minimal P6 replay schema and project-authored synthetic fixture only.
```

## Next Task Recommendation

Set the next first unchecked `docs/10_next/10_NEXT.md` task to:

```text
Implement minimal P6 replay schema and project-authored synthetic fixture only.
```

That next task must repeat the exact allowed files, exact allowed future
scope, forbidden future expansion, validation commands and stop conditions
listed above.

## Evidence Grade

```text
P6 minimal replay schema and synthetic fixture implementation approval-decision evidence only.
```

## Explicit Non-Evidence

This approval decision is not evidence of:

- P6 implementation execution.
- replay schema implementation.
- fixture implementation.
- test implementation.
- data ingestion.
- dataset reader.
- parser.
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
- P7-P12 entry approval.
