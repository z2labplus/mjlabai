# 02P_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_CURRENT_SCOPE_ACCEPTANCE_DECISION

## Scope

This document decides whether the exact minimal P6 replay schema and
project-authored synthetic fixture implementation can be accepted as
current-scope complete.

This is a docs-only acceptance decision gate. It does not:

- add production code.
- add tests.
- add fixtures or data files.
- modify `src/mjlabai/data/replay_schema.py`.
- modify `tests/fixtures/data/synthetic_replay_smoke.json`.
- modify `tests/data/test_replay_schema.py`.
- modify `tests/data/test_synthetic_replay_fixture_schema.py`.
- expand replay schema implementation.
- implement parser, dataset reader, data ingestion, feature extraction or label
  generation.
- read real Tenhou, real haifu, external logs or platform data.
- use account, session, cookie, token or private-log data.
- add model-output integration, CLI, broad file ingestion, latency measurement,
  fixed-position exact-match, metric implementation, registry code changes,
  promotion-criteria changes or evidence-taxonomy changes.
- call OpenAI, LLM, model, Akochan `system.exe`, `libai.so` or third-party
  binary paths.
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- close full P6.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

North-star relationship:

```text
This decision supports the long-term stable-dan > 10.68 target only by
confirming that the first minimal P6 data-system smoke implementation has a
bounded current-scope completion status before any broader data-system work.
It is not strength evidence.
```

## Reviewed Artifacts

Implementation artifacts:

- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

Implementation and review commits:

- `232a0c51460a0168f3f5415d26bff1268b713d35`
  `Implement minimal P6 replay schema and synthetic fixture`
- `d10f2c45ba2f38c836d2b23befc4b721296f5dbc`
  `Review minimal P6 replay schema implementation`

Primary P6 planning / approval context:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
- `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`
- `docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`
- `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`
- `docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md`

Governance / tracking context:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

## Acceptance Decision Purpose

The purpose of this decision is to record whether the exact minimal replay
schema module, project-authored synthetic/local replay fixture and two minimal
local tests created by the approved `02N` task and reviewed by `02O` can be
marked complete for the current narrow P6 scope.

This decision is deliberately smaller than P6 closure. It does not approve the
next P6 implementation step, source ingestion, parser, dataset reader, feature
extraction, label generation, model-output integration or P7-P12 entry.

## Acceptance Options

A. Accepted as current-scope complete.

- The exact minimal implementation and review evidence are sufficient.
- The current narrow implementation can be treated as complete for its approved
  scope.
- Any next task must be separately defined and bounded.

B. Not accepted because blockers exist.

- A blocker in the implementation, validation, governance synchronization or
  evidence boundary prevents current-scope completion.
- The next task must fix or review that blocker before proceeding.

C. Deferred pending additional review.

- The evidence is not blocked, but the project needs another docs-only review
  before deciding.

## Current Evidence Review

| evidence_item | status | source | blocker | notes |
|---|---|---|---|---|
| `02N` approval decision exists | pass | `docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md` | no | It approved only the exact next minimal implementation task. |
| Exact implementation files match approval | pass | `docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md` | no | The implementation created only `src/mjlabai/data/replay_schema.py`, `tests/fixtures/data/synthetic_replay_smoke.json`, `tests/data/test_replay_schema.py` and `tests/data/test_synthetic_replay_fixture_schema.py`, plus allowed docs/governance synchronization. |
| Implementation commit used exact files | pass | `232a0c51460a0168f3f5415d26bff1268b713d35` | no | The implementation stayed within the `02N` file boundary. |
| `02O` implementation review can close | pass | `docs/02_data_system/02O_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_REVIEW.md` | no | Review found no blocker. |
| Replay schema module remains minimal | pass | `src/mjlabai/data/replay_schema.py`; `02O` | no | Standard-library-only, in-memory mapping validation; no file reader, parser, ingestion, feature or label behavior. |
| Synthetic fixture remains project-authored synthetic/local | pass | `tests/fixtures/data/synthetic_replay_smoke.json`; `02O` | no | Not Tenhou data, not real haifu, not external log, not platform data, not model output, not training data. |
| Minimal local tests exist | pass | `tests/data/test_replay_schema.py`; `tests/data/test_synthetic_replay_fixture_schema.py`; `02O` | no | Tests cover schema/fixture smoke behavior only. |
| Validation passed | pass | `02O` validation record; current validation rerun | no | `git diff --check`, `python3 -m unittest tests/data/test_replay_schema.py` and `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py` passed. |
| No parser / reader / ingestion behavior | pass | `02O`; implementation files | no | Explicitly absent and still unapproved. |
| No feature extraction or label generation | pass | `02O`; implementation files | no | Explicitly absent and still unapproved. |
| No real data or source approval | pass | `02A`, `02D`, `02O` | no | Real Tenhou, real haifu, external logs, platform data and source ingestion remain unapproved. |
| No model-output path | pass | `02O`; implementation files | no | Synthetic fixture forbids model-output use. |
| No CLI or broad ingestion | pass | `02O`; implementation files | no | No CLI, glob, directory scan or generic file-ingestion interface. |
| No P7-P12 entry | pass | `02O`; stage contract; `10_NEXT` | no | Training, self-play, league, runner behavior and later stages remain closed. |
| Governance synchronized | pass | `02O`; handoff/index/changelog/evidence/risk/stage/backlog/milestones/technical plan | no | Current acceptance decision updates the next status. |
| Evidence grade remains conservative | pass | `02O`; evidence log | no | The evidence is P6 synthetic/local schema smoke and current-scope acceptance evidence only. |

## Acceptance Scope

Accepted as current-scope complete:

- minimal replay schema module current-scope complete.
- project-authored synthetic/local replay fixture current-scope complete.
- two minimal local tests current-scope complete.
- directly related governance synchronization current-scope complete.

Not accepted or approved by this decision:

- full P6 closure.
- additional replay schema expansion.
- additional fixtures or tests.
- parser.
- dataset reader.
- data ingestion.
- feature extraction.
- label generation.
- real Tenhou data.
- real haifu data.
- external-log ingestion.
- platform-data ingestion.
- account, session, cookie, token or private-log handling.
- CLI or broad file ingestion.
- model-output integration.
- training, tuning, self-play, league or runner behavior.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
- P7-P12 entry approval.

## Decision

```text
Accepted as current-scope complete.
```

Reason:

- `02N` approved the exact minimal implementation task.
- The implementation commit created the exact allowed files only.
- `02O` reviewed the exact implementation and found no blocker.
- Required validation passed.
- The implementation remains synthetic/local, minimal and non-ingestive.
- The evidence grade is conservative and does not imply full P6 closure or
  later-stage approval.

## Next Task Recommendation

Recommended next first task:

```text
Define next P6 current-scope data-system task after minimal replay schema acceptance.
```

Required boundary for that next task:

- docs-only.
- no code.
- no tests.
- no fixtures.
- no replay schema expansion.
- no parser.
- no dataset reader.
- no data ingestion.
- no feature extraction.
- no label generation.
- no real Tenhou, real haifu, external logs or platform data.
- no account, session, cookie, token or private-log data.
- no model-output integration.
- no CLI or broad file ingestion.
- no training, tuning, self-play, league or runner behavior.
- no P7-P12.
- no model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claim.

## Evidence Grade

```text
P6 minimal replay schema and project-authored synthetic fixture current-scope
acceptance decision evidence only.
```

## Explicit Non-Evidence

This decision is not evidence of:

- full P6 closure.
- new implementation.
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
- CLI or broad file ingestion.
- training.
- tuning.
- self-play.
- league.
- runner behavior.
- model strength.
- Tenhou ranked performance.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- P7-P12 entry approval.
