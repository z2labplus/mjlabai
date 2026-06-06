# 02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY

## Scope

This document defines the P6 synthetic/local replay fixture boundary before any
replay schema implementation.

It is a docs-only planning artifact. It does not:

- approve P6 implementation.
- approve replay fixture implementation.
- create a replay fixture file.
- add tests.
- add production code.
- implement replay schema code.
- implement dataclasses, pydantic models or JSON schema.
- implement parsers or dataset readers.
- implement data ingestion.
- implement feature extraction or label generation.
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
Future replay fixtures can help the data system become lawful, reproducible
and auditable before training data exists. This boundary itself is not strength
evidence and is not LuckyJ comparison evidence.
```

## Replay Boundary Review Context

Current context:

- P5 is closed for the current synthetic/local evaluation groundwork scope.
- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md` allows docs-only
  P6 planning after final P5 closure.
- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
  defines P6 data-system scope before implementation.
- `docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 data-source
  provenance and rights inventory.
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
  reviews the inventory with no blocker.
- `docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the replay schema
  documentation boundary.
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
  reviews that boundary with no blocker.

Current closed items:

- P6 implementation is still not approved.
- Replay schema implementation is still not approved.
- Replay fixture implementation is still not approved.
- Data ingestion is still not approved.
- Dataset readers, feature extraction and label generation are still not
  approved.
- P7-P12 remain closed.

## Fixture Boundary Purpose

The purpose of this boundary is to define how a future synthetic/local replay
fixture may be planned before fixture implementation.

A future fixture may be useful as a small, project-authored, repo-local smoke
artifact for checking replay-shape documentation and future validation logic.
It must not be mistaken for real gameplay data, a parser contract, a training
dataset, model-output evidence, Tenhou evidence or LuckyJ comparison evidence.

This document defines:

- project-authored and repo-local requirements.
- allowed fixture shape families.
- forbidden content and forbidden interpretations.
- source / provenance dependencies.
- privacy and storage guardrails.
- non-evidence warnings.
- future fixture implementation entry criteria.
- future review and validation expectations.

This document does not create a fixture and does not approve fixture creation.

## Allowed Fixture Boundary

| boundary_item | allowed_definition | implementation_allowed_now | dependency | notes |
|---|---|---:|---|---|
| project-authored only | Future fixture content must be authored by the project. | no | `02A` project-authored synthetic fixture source category. | No third-party, real platform or model output content. |
| repo-local only | Future fixture, if later approved, must be a small repo-local artifact. | no | storage / Git policy review. | Raw real data must not enter Git. |
| small / smoke-only | Future fixture may be small enough for schema-shape smoke checks. | no | later explicit fixture task. | Not a dataset. |
| no real gameplay log | Fixture must not copy real gameplay sequences. | no | source review. | Synthetic event ordering only. |
| no real player/account identifiers | Participants must be synthetic seats or synthetic ids. | no | privacy review. | No accounts, sessions, cookies or tokens. |
| no platform data | Fixture must not include platform-derived content. | no | platform terms review if ever considered. | Current boundary forbids platform data. |
| no external log lines | Fixture must not include external replay/log text. | no | source-specific approval. | External logs remain unapproved. |
| no Tenhou / real haifu content | Fixture must not include real Tenhou or real haifu content. | no | source-specific legal / terms review. | Real data remains closed. |
| no model output | Fixture must not include policy/tool/model actions. | no | later model-output boundary if ever approved. | Prevents premature evaluator coupling. |
| no labels derived from real data | Fixture must not include supervised labels from real games. | no | future label policy. | P7 remains closed. |
| no training use | Fixture may not be used for model training. | no | stage gate. | It is only future smoke context. |
| no evaluation strength use | Fixture may not be used for model-strength or promotion claims. | no | evidence taxonomy. | Synthetic shape checks are non-strength evidence. |
| schema-aligned shape only | Future fixture shape should align with `02B` field families. | no | `02B` / `02E`. | Alignment is not schema implementation. |
| replay field-family coverage only | Future fixture may touch replay identity, provenance, context, events and terminal result families. | no | later review. | It must not become parser or feature code. |
| source id | Future fixture must use a project-authored synthetic source id. | no | `02A` source inventory. | No unapproved source id. |
| evidence reference | Future fixture planning must include an evidence-log reference. | no | evidence log. | Reference is not strength evidence. |
| risk reference | Future fixture planning must include a risk-register reference. | no | risk register. | Keeps overclaiming and real-data risks visible. |
| non-evidence warning | Future fixture must state that it is not Tenhou, real haifu, training or strength evidence. | no | evidence taxonomy. | Required on every fixture artifact. |
| deterministic planning | Future fixture should be deterministic and inspectable. | no | later implementation task. | No random generation hidden from review. |
| validation planning | Future fixture should have planned validation checks. | no | later test/validation task. | No tests are created here. |
| review before creation | Future fixture creation requires a separate review gate. | no | `10_NEXT`. | This task does not approve creation. |

## Forbidden Fixture Boundary

| forbidden_item | reason | earliest_possible_condition | guardrail |
|---|---|---|---|
| Real Tenhou sample | Platform, account and rights risk. | Separate source-specific legal / terms review. | Forbidden now. |
| Real haifu sample | Rights, privacy and provenance risk. | Separate source-specific approval. | Forbidden now. |
| External log sample | Unknown provenance and allowed-use risk. | Source inventory, approval and storage policy. | Forbidden now. |
| Platform-data sample | Platform terms and privacy risk. | Separate compliance approval. | Forbidden now. |
| Account/session/cookie/token sample | Security and privacy risk. | Not approved by current stage. | Forbidden now. |
| Scraped sample | Compliance and anti-abuse risk. | Not approved by current stage. | Forbidden now. |
| Model-output sample | Would couple P6 fixture planning to models/evaluators. | Later model-output boundary, if approved. | Forbidden now. |
| Self-play sample | Belongs to later stages and needs provenance. | Later stage approval. | Forbidden now. |
| League sample | Belongs to later league stages. | Later stage approval. | Forbidden now. |
| Training dataset | Would enter P7 readiness. | P6 implementation and P7 entry approval. | Forbidden now. |
| Supervised-learning label source | Would imply label generation. | Approved label policy and source. | Forbidden now. |
| Benchmark strength evidence | Synthetic fixtures cannot prove strength. | Real evaluation protocol later. | Forbidden now. |
| Legal-action broad evaluator evidence | Fixture shape is not a broad legal-action evaluator. | Later evaluator review. | Forbidden now. |
| Stable-dan evidence | Fixture is not ranked-game result evidence. | Later approved evaluation evidence. | Forbidden now. |
| LuckyJ comparison evidence | Fixture cannot support LuckyJ `10.68` claims. | Later ranked/evaluation protocol. | Forbidden now. |
| Candidate promotion evidence | Fixture shape cannot promote candidates. | Later funnel gates. | Forbidden now. |
| P7-P12 entry evidence | Fixture boundary is P6 planning only. | Separate stage transition. | Forbidden now. |
| Fixture file creation | This task defines boundary only. | Separate explicit `10_NEXT` task. | Forbidden now. |

## Source Inventory Dependency

Future synthetic/local replay fixture planning depends on `02A` and `02D`.

The only currently relevant source category is:

```text
project-authored synthetic/local fixture
```

Future fixture implementation still requires:

- explicit fixture `source_id`.
- project-authored confirmation.
- license / rights status equal to project-owned or project-authored.
- raw / derived storage policy.
- `may_enter_git = yes_small_project_authored_only` or equivalent reviewed
  value.
- no real, external or platform content.
- no account, session, cookie, token or private log content.
- evidence-log reference.
- risk-register reference.
- explicit `docs/10_next/10_NEXT.md` implementation approval.
- review before fixture creation.

`02D` reviews the source inventory, but it does not approve fixture
implementation, source ingestion, replay schema implementation or training use.

## Replay Schema Boundary Dependency

Future synthetic/local replay fixtures should align with the field-family draft
in `02B` and the no-blocker review in `02E`.

This boundary may reference field families, but it must not define:

- concrete JSON schema.
- Python dataclasses.
- pydantic models.
- parser contracts.
- dataset-reader contracts.
- event/action implementation semantics.
- decision-state implementation semantics.
- ingestion paths.
- feature extraction paths.
- label generation paths.

Field-family alignment is only a planning boundary. It is not fixture
implementation and not schema implementation.

## Future Fixture Shape Families

The following shape families are documentation boundaries only. They are not
fixture JSON, schema implementation, parser contracts or test fixtures.

| shape_family | example_fields_or_concepts | purpose | implementation_status | source_dependency | replay_schema_dependency | non_evidence_warning |
|---|---|---|---|---|---|---|
| A. fixture_identity | `fixture_id`, `fixture_version`, `source_id`, `synthetic_authoring_note`, `evidence_ref` | Make future fixture identity explicit and auditable. | documentation boundary only | project-authored synthetic source id | replay identity family | Fixture identity is not strength evidence. |
| B. replay_identity_shape | replay id policy, `schema_version` placeholder, `transform_version` placeholder, checksum/hash placeholder | Plan traceable replay-like identity for a future synthetic fixture. | documentation boundary only | source inventory | replay identity family | Replay-like ids do not imply real replays. |
| C. provenance_shape | `source_inventory_ref`, rights status, approval status, non-evidence warning | Keep source/provenance visible in future fixture shape. | documentation boundary only | `02A` / `02D` | provenance family | Provenance does not approve ingestion. |
| D. game_context_shape | ruleset placeholder, room context placeholder, table context placeholder | Plan context fields without claiming real Tenhou semantics. | documentation boundary only | project synthetic source | game context family | Context placeholders are not Tenhou evidence. |
| E. participant_shape | synthetic seat ids, no account ids, anonymization status | Keep participants synthetic and privacy-safe. | documentation boundary only | privacy / storage policy | participants family | Synthetic seats are not real players. |
| F. hand_round_context_shape | round / honba / kyotaku / dealer / dora placeholders, no parser semantics | Plan round context shape without tile/dora parsing. | documentation boundary only | later fixture review | hand / round context family | No parser or rules engine is implied. |
| G. event_sequence_shape | small deterministic event list planning, event index policy, event type vocabulary placeholder, payload boundary placeholder | Plan deterministic event order for future smoke fixture. | documentation boundary only | future fixture approval | event sequence family | Event planning is not event parsing. |
| H. action_context_shape | synthetic action vocabulary placeholder, no legal-action checker, no model output, no canonicalizer implementation | Keep action shape scoped and non-executable. | documentation boundary only | future action review if needed | action context family / `05L` | Action placeholders are not legal-action evaluator evidence. |
| I. decision_state_shape | observation boundary placeholder, hidden-information warning, no feature extraction, no labels | Prevent leakage and training-readiness overclaims. | documentation boundary only | leakage policy | decision-state boundary family | No features or labels are generated. |
| J. terminal_result_shape | placement / score placeholder, no stable-dan evidence, no strength interpretation | Plan terminal result shape without evaluation claims. | documentation boundary only | source / result semantics review | terminal result family | Synthetic results are not stable-dan evidence. |
| K. validation_metadata_shape | future validation status placeholder, future validation command placeholder, known exclusions | Plan validation metadata before tests exist. | documentation boundary only | future validation task | validation metadata family | No validation command is implemented now. |
| L. storage_privacy_shape | `may_enter_git` policy, raw/derived distinction, privacy review status | Keep Git/storage/privacy status explicit. | documentation boundary only | source inventory and privacy review | storage/privacy family | Storage approval is limited to small project-authored synthetic content. |

## Future Fixture Implementation Entry Criteria

Before any future synthetic/local replay fixture implementation task starts,
the project must satisfy:

| criterion | required_before_implementation | current_status | evidence_needed | blocker | notes |
|---|---|---|---|---|---|
| fixture boundary reviewed | A later review confirms this boundary. | not satisfied | review document and decision record | yes | Next task is review, not implementation. |
| source inventory reviewed | `02A` / `02D` remain available and current. | satisfied for planning only | source inventory references | yes for implementation | Does not approve fixture creation. |
| replay schema boundary reviewed | `02B` / `02E` remain available and current. | satisfied for planning only | replay boundary references | yes for implementation | Does not approve schema code. |
| project-authored source id | Fixture source id assigned. | not assigned | source record / inventory update | yes | No fixture id is created here. |
| small deterministic repo-local fixture | Fixture is small, deterministic and repo-local. | planned only | future fixture task | yes | No fixture file now. |
| no real/external/platform data | Explicit no-real-data review. | planned only | future review checklist | yes | Real sources remain closed. |
| no account/session/cookie/token | Privacy / security review. | planned only | future privacy check | yes | No account content now. |
| no model output | Confirm fixture does not include model/tool output. | planned only | future review checklist | yes | Model-output integration remains closed. |
| no labels from real data | Confirm no labels or features from real logs. | planned only | future label policy | yes | P7 remains closed. |
| field-family alignment reviewed | Fixture shape reviewed against `02B`. | planned only | future schema-shape review | yes | Alignment is not schema implementation. |
| storage / Git policy reviewed | `may_enter_git` and raw/derived status documented. | planned only | source inventory update | yes | Only small synthetic content may enter Git. |
| evidence / risk references ready | Evidence and risk references prepared. | planned only | evidence log / risk register | yes | Future implementation must update both. |
| human / Web ChatGPT approval | Explicit implementation boundary approved. | not approved | review output | yes | No implementation approval now. |
| `10_NEXT` implementation approval | First task explicitly allows fixture implementation. | not approved | later `10_NEXT` item | yes | Current task is boundary definition. |
| P7-P12 non-entry | Later stages remain closed. | active | stage contract | yes for later stages | Fixture work cannot open training stages. |

This task defines these criteria only. It does not satisfy or execute them.

## Future Fixture Validation Expectations

Future validation expectations, if a later task approves fixture creation:

- fixture file path proposed only after approval.
- JSON syntax validation planned.
- required top-level field validation planned.
- `source_id` / provenance validation planned.
- no-real-data assertion planned.
- no-account-identifier assertion planned.
- no-model-output assertion planned.
- no-training-use warning planned.
- schema-family coverage validation planned.
- evidence / risk references validation planned.
- deterministic ordering validation planned.
- storage / privacy fields validation planned.
- tests planned but not created in this task.
- validation command planned but not run in this task.

No test, fixture file or validation command is created by this task.

## Synthetic/Local Fixture Risks

| risk | mitigation | blocker_status | owner_doc_or_followup | notes |
|---|---|---|---|---|
| Synthetic fixture mistaken for real data. | Require explicit synthetic/local warnings and project-authored source id. | blocker for future fixture implementation | this document, future review | Fixture must say it is not real Tenhou or real haifu. |
| Fixture boundary mistaken for fixture implementation approval. | Keep implementation disallowed in this document and `10_NEXT`. | blocker for implementation | `10_NEXT` | No fixture file is created now. |
| Fixture shape mistaken for schema implementation. | Label shape families as documentation boundary only. | blocker for schema implementation | `02B`, `02E`, this document | No JSON schema/dataclass/parser contract. |
| Real log accidentally copied into fixture. | Require no-real-data assertion and source review before creation. | blocker for future fixture | future validation task | Real/external logs remain forbidden. |
| Player/account identifiers accidentally included. | Require synthetic seat ids and privacy review. | blocker for future fixture | source inventory / privacy review | No account/session/cookie/token data. |
| Model outputs included too early. | Forbid model-output content in fixture boundary. | blocker for future fixture | future review | Model-output integration remains closed. |
| Labels or features creep into fixture. | Require no feature extraction and no label generation. | blocker for future fixture | P6/P7 stage gates | P7 remains closed. |
| Fixture used for training. | Require non-training warnings and stage boundaries. | blocker for training | stage contract | Synthetic smoke fixture is not a dataset. |
| Fixture overclaimed as strength / Tenhou / LuckyJ evidence. | Evidence grade and explicit non-evidence warnings. | governance blocker | evidence log / ranking protocol | Cannot support LuckyJ `10.68` claims. |
| Fixture used to bypass source approval. | Require `02A` source id and future approval. | blocker for ingestion | source inventory | Source approval remains separate. |
| Fixture expands into broad ingestion or CLI. | Keep fixture boundary repo-local and docs-only. | blocker for implementation | future review | No broad file ingestion or CLI. |
| Fixture implementation jumps into parser / dataset reader. | Require separate implementation task and review. | blocker for parser/reader | future `10_NEXT` | No parser or reader now. |
| P6 fixture planning drifts into P7-P12. | Keep training, self-play, league and runner behavior forbidden. | blocker for later stages | stage contract | P7-P12 require separate entry approval. |

## Planning Decision

```text
P6 synthetic/local replay fixture boundary is defined for review before schema
implementation. Fixture implementation is still not approved.
```

## Review Status

`docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
reviews this boundary and records:

```text
Review can close, but fixture implementation remains closed.
```

The review does not approve fixture implementation, replay schema
implementation, data ingestion, dataset readers, parsers, feature extraction,
label generation, real data access, model-output integration, CLI, training,
self-play, league, runner behavior or P7-P12 work.

`docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
defines readiness criteria before future fixture implementation or replay
schema code can be considered. It does not approve fixture implementation.

`docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
reviews that checklist with no blocker. It keeps fixture implementation closed
and does not approve fixture files, validation tests, schema code, ingestion,
parser, dataset reader, feature extraction or label generation.

`docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
defines the proposal boundary for any future replay schema and synthetic
fixture implementation proposal. It keeps fixture implementation closed and
does not approve fixture files, validation tests, schema code, ingestion,
parser, dataset reader, feature extraction or label generation.

## Next Task Recommendation

```text
Review P6 replay schema and synthetic fixture implementation proposal boundary before code.
```

The proposal boundary is now defined in `02J`; the next task should review it
and remain docs-only. It must not implement fixture files, replay schema code,
tests, parsers, dataset readers, ingestion, feature extraction, label
generation, CLI, model-output integration, real data access, training,
self-play, league, runner behavior or P7-P12 work.

## Evidence Grade

```text
P6 synthetic/local replay fixture boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

- P6 implementation approval.
- fixture implementation.
- replay schema implementation.
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
