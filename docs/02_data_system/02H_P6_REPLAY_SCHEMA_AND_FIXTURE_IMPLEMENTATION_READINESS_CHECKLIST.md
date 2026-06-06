# 02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST

## Scope

This document defines the P6 replay schema and fixture implementation readiness
checklist before code.

It is a docs-only readiness checklist definition. It does not:

- approve P6 implementation.
- approve replay schema implementation.
- approve replay fixture implementation.
- create fixture files.
- add tests.
- add production code.
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
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

North-star relationship:

```text
Readiness checklists support the long-term stable-dan > 10.68 target only by
preventing unsafe or premature data-system implementation before replay,
fixture, source, storage, privacy and evidence boundaries are ready. This
checklist is not strength evidence and does not approve implementation.
```

## Prior Boundary Context

Current context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md` allows docs-only
  P6 planning after final P5 closure.
- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
  defines P6 data-system scope before implementation.
- `docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 data-source
  provenance and rights inventory.
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
  reviews that inventory with no blocker.
- `docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the replay schema
  documentation boundary.
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
  reviews that boundary with no blocker.
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
  defines the synthetic/local replay fixture boundary.
- `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
  reviews that boundary with no blocker.

Current closed items:

- P6 implementation is not approved.
- Replay schema implementation is not approved.
- Replay fixture implementation is not approved.
- Data ingestion is not approved.
- Parser and dataset reader implementation is not approved.
- Feature extraction and label generation are not approved.
- Tests and fixtures for P6 replay data are not approved.
- P7-P12 remain closed.

## Readiness Checklist Purpose

The purpose of this checklist is to define how future implementation tasks
should be judged before any code, fixture, test or ingestion path is created.

The checklist is positioned after:

- source inventory definition and review.
- replay schema documentation boundary definition and review.
- synthetic/local replay fixture boundary definition and review.

The checklist is positioned before:

- replay schema code.
- fixture implementation.
- parser or dataset reader implementation.
- data ingestion.
- feature extraction.
- label generation.
- tests or fixtures.

It can be used by a future docs-only review gate to decide whether a specific
implementation task is ready to be proposed. It does not approve any
implementation by itself.

## Candidate Implementation Classes

| candidate | current_status | implementation_allowed_now | earliest_possible_condition | notes |
|---|---|---:|---|---|
| A. replay schema code implementation | not_ready | no | readiness checklist review plus explicit `10_NEXT` implementation approval | No dataclass, pydantic model or JSON schema now. |
| B. synthetic/local replay fixture file creation | not_ready | no | fixture source id, storage policy, validation scope and explicit `10_NEXT` approval | No fixture file now. |
| C. schema validation test implementation | not_ready | no | schema code scope approved first | No tests now. |
| D. fixture validation test implementation | not_ready | no | fixture file scope approved first | No tests now. |
| E. parser / dataset reader implementation | deferred | no | source-specific approval, parser scope and storage policy review | Parser / reader remains later P6 implementation work. |
| F. feature extraction implementation | deferred | no | schema implementation, fixture validation and hidden-information policy review | Feature extraction remains later P6/P7-boundary work. |
| G. label generation implementation | deferred | no | label source policy and leakage review plus later approval | Label generation remains later P6/P7-boundary work. |
| H. data ingestion implementation | deferred | no | source-specific rights, license, terms, privacy, storage and approval review | No ingestion now. |
| I. real / external / platform source integration | blocked | no | separate source-specific legal / terms / privacy / platform review | Real Tenhou, real haifu, external logs and platform data remain closed. |
| J. CLI / broad file ingestion | blocked | no | separate implementation boundary and risk review | No CLI or broad file ingestion now. |
| K. model-output integration | blocked | no | separate model-output boundary after P6 readiness and later-stage review | No model outputs now. |
| L. training / self-play / league / P7-P12 work | deferred_later_stage | no | independent stage scope, entry criteria, risk review and first-task approval | Not part of P6 checklist implementation. |

Current planning decision:

```text
No candidate implementation class is approved by this checklist definition.
```

## Replay Schema Code Readiness Checklist

| criterion | status | evidence | blocker | required_before_implementation | notes |
|---|---|---|---|---|---|
| `02A` source inventory defined | ready_for_review_only | `02A` exists | no for review; yes for implementation | yes | Inventory definition is not source approval. |
| `02D` source inventory review can close | ready_for_review_only | `02D` no-blocker review | no for review; yes for implementation | yes | Review is not ingestion approval. |
| `02B` replay schema documentation boundary defined | ready_for_review_only | `02B` exists | no for review; yes for implementation | yes | Boundary is not schema code. |
| `02E` replay schema boundary review can close | ready_for_review_only | `02E` no-blocker review | no for review; yes for implementation | yes | Review is not implementation approval. |
| `02F` synthetic/local replay fixture boundary defined | ready_for_review_only | `02F` exists | no for review; yes for implementation | yes | Fixture boundary is not fixture creation. |
| `02G` fixture boundary review can close | ready_for_review_only | `02G` no-blocker review | no for review; yes for implementation | yes | Review is not fixture implementation approval. |
| source category selected and approved | not_ready | not selected for implementation | yes | yes | A specific source category must be approved later. |
| no real/external/platform data unless source-specific approval exists | not_ready | policy exists, approval absent | yes | yes | Real/external/platform sources remain closed. |
| schema field families reviewed | ready_for_review_only | `02B` / `02E` | no for review; yes for implementation | yes | Field families are planning only. |
| schema version policy defined | not_ready | planned only | yes | yes | Needs concrete implementation-scope review. |
| raw-vs-derived storage policy reviewed | not_ready | source policy planned | yes | yes | Required before schema code consumes data. |
| privacy / platform terms risk reviewed | not_ready | general risks recorded | yes | yes | Needs implementation-scope review. |
| hidden-information leakage policy reviewed | not_ready | field-family boundary only | yes | yes | Required before decision-state fields become code. |
| evidence log reference ready | ready_for_review_only | current evidence log updated | yes for implementation | yes | Implementation requires new evidence entry. |
| risk register reference ready | ready_for_review_only | current risk register updated | yes for implementation | yes | Implementation requires updated risk entry. |
| implementation task first in `10_NEXT` | not_ready | current task is review next | yes | yes | No implementation task is first now. |
| human / Web ChatGPT approval recorded | not_ready | not approved | yes | yes | Future approval must be explicit. |
| implementation prompt explicitly allows replay schema code and limits scope | not_ready | absent | yes | yes | Current prompt forbids code. |
| no P7-P12 entry | ready | stage contract active | yes for later stages | yes | Later stages remain closed. |

Replay schema code readiness decision:

```text
not_ready_for_implementation
```

## Synthetic/Local Replay Fixture Readiness Checklist

| criterion | status | evidence | blocker | required_before_implementation | notes |
|---|---|---|---|---|---|
| fixture boundary defined | ready_for_review_only | `02F` exists | no for review; yes for implementation | yes | Boundary definition is complete. |
| fixture boundary reviewed | ready_for_review_only | `02G` no-blocker review | no for review; yes for implementation | yes | Review is not fixture approval. |
| project-authored source id assigned | not_ready | not assigned | yes | yes | Required before file creation. |
| fixture content confirmed project-authored | not_ready | no content exists | yes | yes | Future content must be authored by project. |
| no real gameplay logs | not_ready | planned only | yes | yes | Future fixture must assert no real logs. |
| no real player/account identifiers | not_ready | planned only | yes | yes | Requires synthetic seats / ids. |
| no platform data | not_ready | planned only | yes | yes | Platform data remains closed. |
| no external logs | not_ready | planned only | yes | yes | External logs remain closed. |
| no model output | not_ready | planned only | yes | yes | Model-output integration remains closed. |
| no labels from real data | not_ready | planned only | yes | yes | Label generation remains closed. |
| small / deterministic / repo-local | not_ready | planned only | yes | yes | No fixture file exists now. |
| Git storage policy reviewed | not_ready | planned only | yes | yes | Needed before a file enters Git. |
| evidence log reference ready | ready_for_review_only | current evidence log updated | yes for implementation | yes | Future fixture needs new evidence entry. |
| risk register reference ready | ready_for_review_only | current risk register updated | yes for implementation | yes | Future fixture needs new risk entry. |
| validation expectations reviewed | ready_for_review_only | `02F` / `02G` | yes for implementation | yes | Validation scope still needs fixture-specific task. |
| future fixture file path approved | not_ready | absent | yes | yes | No fixture path is approved now. |
| future test scope approved | not_ready | absent | yes | yes | No test scope is approved now. |
| explicit `10_NEXT` implementation task | not_ready | absent | yes | yes | Current next is review of this checklist. |
| human / Web ChatGPT approval | not_ready | absent | yes | yes | Must be explicit later. |
| no P7-P12 entry | ready | stage contract active | yes for later stages | yes | Later stages remain closed. |

Synthetic/local replay fixture readiness decision:

```text
not_ready_for_implementation
```

## Parser / Dataset Reader Readiness Checklist

Parser and dataset reader work is defined here only as a deferred future class.
It is not approved.

| criterion | status | evidence | blocker | required_before_implementation | notes |
|---|---|---|---|---|---|
| source approval required | blocked_by_source_approval | no source-specific approval | yes | yes | Real/external/platform sources remain closed. |
| parser scope required | not_ready | no parser boundary | yes | yes | No parser contract exists. |
| source format rights reviewed | blocked_by_source_approval | rights inventory only | yes | yes | Needs source-specific review. |
| storage policy approved | blocked_by_storage_policy | planned only | yes | yes | No storage policy for implementation. |
| no real/external/platform data unless source-specific approval | blocked_by_source_approval | policy exists, approval absent | yes | yes | Real data remains closed. |
| privacy / platform terms review | blocked_by_privacy_review | planned only | yes | yes | Required before source handling. |
| validation commands planned | not_ready | no commands | yes | yes | No validation command now. |
| tests planned | not_ready | no test task | yes | yes | No tests now. |
| risk register updated | ready_for_review_only | current risks updated | yes for implementation | yes | Future parser risk entry required. |
| explicit implementation task | not_ready | absent | yes | yes | Current `10_NEXT` forbids implementation. |
| human / Web ChatGPT approval | requires_human_approval | absent | yes | yes | Must be explicit later. |

Parser / dataset reader readiness decision:

```text
deferred_later_stage
```

## Feature Extraction / Label Generation Readiness Checklist

Feature extraction and label generation are defined here only as deferred
future classes. They are not approved.

| criterion | status | evidence | blocker | required_before_implementation | notes |
|---|---|---|---|---|---|
| replay schema implementation reviewed | not_ready | no schema implementation exists | yes | yes | Schema code must exist and be reviewed first. |
| fixture validation reviewed | not_ready | no fixture exists | yes | yes | Fixture validation must exist first. |
| decision-state boundary approved | not_ready | documentation boundary only | yes | yes | Needs implementation-scope leakage review. |
| hidden-information policy reviewed | not_ready | planned only | yes | yes | Must precede feature extraction. |
| label source policy reviewed | not_ready | absent | yes | yes | Required before label generation. |
| no labels from unapproved real data | blocked_by_source_approval | no approved real data | yes | yes | Real labels remain blocked. |
| P7 supervised-learning scope not entered | ready | stage contract active | yes for P7 | yes | P7 remains closed. |
| explicit later approval required | requires_human_approval | absent | yes | yes | Must be separate task. |
| evidence / risk records updated | ready_for_review_only | current governance updated | yes for implementation | yes | Future implementation needs new entries. |

Feature extraction / label generation readiness decision:

```text
deferred_later_stage
```

## Data Ingestion Readiness Checklist

Data ingestion is defined here only as a deferred future class. It is not
approved.

| criterion | status | evidence | blocker | required_before_implementation | notes |
|---|---|---|---|---|---|
| source-specific rights approval | blocked_by_source_approval | absent | yes | yes | No source-specific ingestion approval. |
| license / terms approval | blocked_by_source_approval | inventory only | yes | yes | Needs review for each source. |
| rightsholder documented | not_ready | inventory fields only | yes | yes | Required for selected source. |
| raw / derived storage policy | blocked_by_storage_policy | planned only | yes | yes | Required before ingestion. |
| `may_enter_git` policy | blocked_by_storage_policy | planned only | yes | yes | Raw real data must not enter Git by default. |
| privacy / personal data review | blocked_by_privacy_review | planned only | yes | yes | Required before any personal/platform data. |
| platform terms risk review | blocked_by_privacy_review | planned only | yes | yes | Required for platform-derived data. |
| automation / scraping risk review | blocked_by_source_approval | current policy forbids automation | yes | yes | No automation/scraping/evasion now. |
| checksum / version policy | not_ready | planned only | yes | yes | Required before source versioning. |
| schema mapping | not_ready | field-family planning only | yes | yes | No schema code exists. |
| validation command | not_ready | absent | yes | yes | No command now. |
| evidence log entry | ready_for_review_only | current evidence log updated | yes for implementation | yes | Future ingestion requires new evidence entry. |
| risk register entry | ready_for_review_only | current risk register updated | yes for implementation | yes | Future ingestion requires new risk entry. |
| human approval | requires_human_approval | absent | yes | yes | Required later. |
| explicit implementation task | not_ready | absent | yes | yes | Current `10_NEXT` forbids ingestion. |

Data ingestion readiness decision:

```text
deferred_later_stage
```

## Readiness Decision Vocabulary

| decision_status | meaning | implementation_approved |
|---|---|---:|
| `ready_for_review_only` | Documentation prerequisite exists and may be reviewed, but implementation is not approved. | no |
| `not_ready_for_implementation` | Required implementation prerequisites are missing. | no |
| `blocked_by_source_approval` | Source-specific rights, license, terms or source-category approval is missing. | no |
| `blocked_by_storage_policy` | Raw / derived storage, Git inclusion or retention policy is missing. | no |
| `blocked_by_privacy_review` | Privacy, personal-data or platform-terms review is missing. | no |
| `blocked_by_missing_schema_boundary` | Replay schema boundary or review is missing. | no |
| `blocked_by_missing_fixture_boundary` | Fixture boundary or review is missing. | no |
| `blocked_by_missing_evidence_log` | Evidence-log entry is missing for the proposed implementation. | no |
| `blocked_by_missing_risk_register` | Risk-register entry is missing for the proposed implementation. | no |
| `deferred_later_stage` | Work belongs to a later stage or later implementation gate. | no |
| `requires_human_approval` | Human / Web ChatGPT approval is required before implementation can be proposed. | no |
| `implementation_allowed_only_after_explicit_10_NEXT_task` | Implementation can be considered only if it is the first unchecked `10_NEXT` task and explicitly permits code. | no |
| `ready` | A non-implementation prerequisite is present. | no by itself |

Rule:

```text
This checklist cannot mark any candidate as implementation approved.
```

## Cross-Artifact Dependency Map

| dependency | required_for | current_status | implementation_allowed | blocker | notes |
|---|---|---|---:|---|---|
| `02A` source inventory | all future P6 implementation candidates | defined | no | yes for implementation | Inventory is not source approval. |
| `02D` source inventory review | replay schema / fixture planning | review can close | no | yes for implementation | Review is not ingestion approval. |
| `02B` replay schema boundary | replay schema code and fixture shape | defined | no | yes for implementation | Field-family planning only. |
| `02E` replay schema boundary review | readiness checklist and later implementation review | review can close | no | yes for implementation | Does not approve schema code. |
| `02F` fixture boundary | synthetic/local fixture planning | defined | no | yes for implementation | Does not create a fixture. |
| `02G` fixture boundary review | readiness checklist | review can close | no | yes for implementation | Does not approve fixture implementation. |
| `02H` readiness checklist | future readiness review | defined here | no | yes for implementation | Checklist definition only. |
| future `02H` readiness checklist review | future implementation proposal | not created | no | yes | Next task should review this checklist. |
| future implementation approval task | schema / fixture / parser / ingestion work | absent | no | yes | Must be first unchecked `10_NEXT` item and explicit. |
| future implementation PR / code task | actual code, tests or fixtures | absent | no | yes | Requires separate approval and evidence/risk updates. |

## P7-P12 Non-Entry Boundary

This readiness checklist does not approve:

- P7 supervised learning.
- P8 reinforcement learning.
- P9 search / risk model implementation.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou target validation.
- training, tuning, self-play, league or runner behavior.
- model-output integration.
- real Tenhou, real haifu, external logs or platform-data ingestion.

Each later stage requires independent scope, entry criteria, risk review and
first-task approval before any work can begin.

## Readiness Risks

| risk | mitigation | blocker_status | owner_doc_or_followup | notes |
|---|---|---|---|---|
| Readiness checklist mistaken for implementation approval. | Repeatedly state checklist is definition evidence only and implementation remains closed. | blocker for implementation | this document, `10_NEXT` | No code, test or fixture is approved here. |
| Partial readiness mistaken for full approval. | Candidate tables separate `ready_for_review_only`, `not_ready` and blockers. | blocker for implementation | future readiness review | Every candidate still needs explicit approval. |
| Fixture readiness used to bypass source approval. | Require project-authored source id, source inventory and future approval. | blocker for fixture implementation | `02A`, `02F`, future review | Source approval remains separate. |
| Schema readiness used to bypass ingestion guardrails. | Keep schema code separate from ingestion and storage policy. | blocker for ingestion | `02B`, this document | Schema code cannot ingest data by itself. |
| Parser / reader deferred status ignored. | Mark parser and reader as deferred / not approved. | blocker for parser/reader | future parser boundary | No parser contract now. |
| Feature / label generation creeps into P7. | Keep feature/label work deferred and require hidden-information review. | blocker for P7 | future feature/label review | P7 remains closed. |
| Data ingestion begins before source-specific approval. | Require rights, license, terms, storage, privacy and approval checklist. | blocker for ingestion | `02A`, future ingestion review | No ingestion now. |
| Real data enters via synthetic fixture. | Require no-real-data assertions, project-authored source id and fixture review. | blocker for fixture implementation | `02F`, future fixture validation | Synthetic fixture must not copy real logs. |
| Tests / fixtures created before approval. | Next task is review-only and current checklist forbids tests/fixtures. | blocker for implementation | `10_NEXT` | Tests and fixtures need explicit future task. |
| Model-output integration added too early. | Keep model outputs blocked until separate model-output boundary. | blocker for model-output work | future model-output boundary | No model path now. |
| P6 planning drifts into P7-P12. | Non-entry boundary and stage contract keep later stages closed. | blocker for later stages | stage contract | Separate stage approvals required. |
| Model-strength evidence overclaiming. | Evidence grade and explicit non-evidence warnings. | governance blocker | evidence log / ranking protocol | Checklist is not Tenhou or LuckyJ evidence. |

## Planning Decision

```text
P6 replay schema and fixture implementation readiness checklist is defined for
review before code. It does not approve replay schema implementation, fixture
implementation, data ingestion, parser, dataset reader, feature extraction or
label generation.
```

## Next Task Recommendation

```text
Review P6 replay schema and fixture implementation readiness checklist before code.
```

That follow-up has now been completed in
`docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`.
The review found no blocker and can close, while P6 implementation, replay
schema implementation, fixture implementation, data ingestion, parser /
dataset-reader work, feature extraction, label generation and P7-P12 remain
closed.

The docs-only replay schema and synthetic fixture implementation proposal
boundary is now defined in
`docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`.
The current next task is to review that proposal boundary before code. It must
not implement replay schema code, fixture files, dataclasses, pydantic models,
JSON schema, parsers, dataset readers, ingestion, feature extraction, label
generation, CLI, model-output integration, real data access, training,
self-play, league, runner behavior, metric implementation, registry changes,
promotion criteria changes or P7-P12 work.

## Evidence Grade

```text
P6 replay schema and fixture implementation readiness checklist definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

- P6 implementation approval.
- replay schema implementation.
- fixture implementation.
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
- runner behavior.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
- P7-P12 entry approval.
