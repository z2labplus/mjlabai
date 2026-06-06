# 02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW

## Scope

This document reviews
`docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
before any synthetic/local replay fixture implementation.

This is a P6 data-system docs-only review gate. It reviews the fixture
boundary only. It does not:

- approve P6 implementation.
- approve replay fixture implementation.
- approve replay schema implementation.
- create a replay fixture file.
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
Synthetic/local replay fixture boundary review supports the long-term
stable-dan > 10.68 target only by keeping future data-system work lawful,
reproducible and auditable before any replay fixture, schema implementation,
ingestion, training or evaluation data can exist. This review is not strength
evidence.
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
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
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

## Fixture Boundary Scope Review

`02F` correctly limits itself to the P6 synthetic/local replay fixture
boundary after replay schema documentation boundary review and before any
fixture implementation, replay schema implementation or ingestion.

Review finding:

| item | finding | blocker | notes |
|---|---|---|---|
| stage | correct | no | It is P6 data-system docs-only planning. |
| artifact type | correct | no | It is a boundary definition, not a fixture or schema implementation. |
| timing | correct | no | It follows `02E` and precedes any fixture, schema or ingestion task. |
| P6 implementation approval | closed | no | `02F` explicitly keeps P6 implementation unapproved. |
| fixture implementation approval | closed | no | It creates no fixture and says fixture creation remains unapproved. |
| replay schema implementation approval | closed | no | It references `02B` field families only as planning boundaries. |
| ingestion / reader / parser approval | closed | no | It keeps ingestion, parsers and dataset readers closed. |
| feature / label approval | closed | no | It keeps feature extraction and label generation closed. |
| real / external data approval | closed | no | It keeps real Tenhou, real haifu, external logs and platform data closed. |
| later-stage entry | closed | no | It keeps training, self-play, league, runner behavior and P7-P12 closed. |
| evidence claim | conservative | no | It states the boundary is not strength or LuckyJ evidence. |

Decision:

```text
No scope blocker found.
```

## Allowed Fixture Boundary Review

`02F` covers the required allowed fixture boundary areas without approving
implementation.

| boundary_area | coverage_status | implementation_boundary | review_finding | blocker | notes |
|---|---|---|---|---|---|
| project-authored only | covered | no implementation now | sufficient | no | Future content must be project-authored. |
| repo-local only | covered | no implementation now | sufficient | no | Future small fixtures may be repo-local only after approval. |
| small / smoke-only | covered | no implementation now | sufficient | no | Future fixture is not a dataset. |
| no real gameplay log | covered | no implementation now | sufficient | no | Synthetic event ordering only. |
| no real player/account identifiers | covered | no implementation now | sufficient | no | Requires synthetic seats / ids. |
| no platform data | covered | no implementation now | sufficient | no | Platform-derived content remains forbidden. |
| no external log lines | covered | no implementation now | sufficient | no | External logs remain unapproved. |
| no Tenhou / real haifu content | covered | no implementation now | sufficient | no | Real data remains closed. |
| no model output | covered | no implementation now | sufficient | no | Prevents premature model/evaluator coupling. |
| no labels derived from real data | covered | no implementation now | sufficient | no | P7 remains closed. |
| no training use | covered | no implementation now | sufficient | no | Fixture planning cannot become training data. |
| no evaluation strength use | covered | no implementation now | sufficient | no | Synthetic shape checks remain non-strength evidence. |
| schema-aligned shape only | covered | no implementation now | sufficient | no | Alignment to `02B` is not schema implementation. |
| replay field-family coverage only | covered | no implementation now | sufficient | no | Prevents parser/feature creep. |
| source id | covered | no implementation now | sufficient | no | Future fixture needs project-authored source id. |
| evidence log reference | covered | no implementation now | sufficient | no | Evidence reference is not strength evidence. |
| risk register reference | covered | no implementation now | sufficient | no | Keeps future risks visible. |
| explicit non-evidence warning | covered | no implementation now | sufficient | no | Required on future artifact. |
| deterministic fixture planning | covered | no implementation now | sufficient | no | No hidden random generation. |
| future validation command planning | covered | no implementation now | sufficient | no | Validation is planned only. |
| future review before fixture creation | covered | no implementation now | sufficient | no | Current task does not approve creation. |

Review decision:

```text
The allowed fixture boundary is sufficient. No missing area, unsafe ambiguity,
overbroad interpretation or implementation-like wording was found.
```

## Forbidden Fixture Boundary Review

`02F` is strict enough for the current review gate. It explicitly forbids:

- real Tenhou samples.
- real haifu samples.
- external log samples.
- platform-data samples.
- account / session / cookie / token samples.
- scraped samples.
- model-output samples.
- self-play samples.
- league samples.
- training datasets.
- supervised-learning label sources.
- benchmark strength evidence.
- legal-action broad evaluator evidence.
- stable-dan evidence.
- LuckyJ comparison evidence.
- candidate promotion evidence.
- P7-P12 entry evidence.
- fixture file creation in the boundary task.

Review decision:

```text
No forbidden-scope blocker found.
```

## Source Inventory Dependency Review

`02F` correctly depends on `02A` and `02D`.

The only currently relevant source category for a future fixture remains:

```text
project-authored synthetic/local fixture
```

`02F` correctly states that `02D` reviewed the source inventory but does not
approve fixture implementation, source ingestion, replay schema implementation
or training use.

Future fixture implementation still needs:

- explicit fixture `source_id`.
- project-authored confirmation.
- project-owned or project-authored rights.
- raw / derived storage policy.
- `may_enter_git = yes_small_project_authored_only` or equivalent reviewed
  value.
- no real, external or platform content.
- no account, session, cookie, token or private log content.
- evidence-log reference.
- risk-register reference.
- explicit `docs/10_next/10_NEXT.md` implementation approval.
- review before creation.

Review decision:

```text
The source inventory dependency is clear. No source dependency blocker found.
```

## Replay Schema Boundary Dependency Review

`02F` correctly depends on `02B` and `02E`.

The review confirms that:

- future fixture shape should align with the `02B` field-family draft.
- `02E` reviewed the replay schema documentation boundary with no blocker.
- `02E` did not approve replay schema code or fixture creation.
- `02F` may reference field families, but it must not define concrete JSON
  schema, Python dataclasses, pydantic models, parser contracts, dataset-reader
  contracts, event/action implementation semantics, decision-state
  implementation semantics, ingestion paths, feature extraction paths or label
  generation paths.
- field-family alignment remains planning only, not fixture implementation and
  not schema implementation.

Review decision:

```text
The replay schema boundary dependency is clear. No schema dependency blocker
found.
```

## Future Fixture Shape Families Review

The future fixture shape families in `02F` are sufficient and safe for
documentation-boundary use.

| shape_family | coverage_status | implementation_boundary | source_dependency | replay_schema_dependency | review_finding | blocker | notes |
|---|---|---|---|---|---|---|---|
| A. fixture_identity | covered | documentation boundary only | project-authored synthetic source id | replay identity family | safe | no | Does not create a fixture id now. |
| B. replay_identity_shape | covered | documentation boundary only | source inventory | replay identity family | safe | no | Replay-like ids do not imply real replays. |
| C. provenance_shape | covered | documentation boundary only | `02A` / `02D` | provenance family | safe | no | Provenance planning is not ingestion approval. |
| D. game_context_shape | covered | documentation boundary only | project synthetic source | game context family | safe | no | Does not claim Tenhou semantics. |
| E. participant_shape | covered | documentation boundary only | privacy / storage policy | participants family | safe | no | Synthetic seats are not real players. |
| F. hand_round_context_shape | covered | documentation boundary only | later fixture review | hand / round context family | safe | no | No tile, dora or rules parser implied. |
| G. event_sequence_shape | covered | documentation boundary only | future fixture approval | event sequence family | safe | no | Event planning is not parsing. |
| H. action_context_shape | covered | documentation boundary only | future action review if needed | action context family / `05L` | safe | no | No legal-action checker, canonicalizer or model output. |
| I. decision_state_shape | covered | documentation boundary only | leakage policy | decision-state family | safe | no | No features or labels generated. |
| J. terminal_result_shape | covered | documentation boundary only | source / result semantics review | terminal result family | safe | no | Synthetic results are not stable-dan evidence. |
| K. validation_metadata_shape | covered | documentation boundary only | future validation task | validation metadata family | safe | no | No validation command implemented now. |
| L. storage_privacy_shape | covered | documentation boundary only | source inventory / privacy review | storage / privacy family | safe | no | Storage approval limited to future small synthetic content. |

Review decision:

```text
No shape-family blocker found. The families are not written as fixture JSON,
schema implementation, parser contract, test fixture, data ingestion, feature
extraction, label generation, model-output integration, training or
model-strength evidence.
```

## Future Implementation Entry Criteria Review

`02F` lists future fixture implementation entry criteria and marks current
implementation blockers clearly.

| criterion | current_status_review | blocker | notes |
|---|---|---|---|
| fixture boundary reviewed | satisfied by this review for boundary closure only | yes for implementation | Review closure is not implementation approval. |
| source inventory reviewed | satisfied for planning only | yes for implementation | `02A` / `02D` do not approve fixture creation. |
| replay schema boundary reviewed | satisfied for planning only | yes for implementation | `02B` / `02E` do not approve schema code. |
| project-authored source id | not assigned | yes | No fixture id or source id is created here. |
| small deterministic repo-local fixture | planned only | yes | No fixture file exists now. |
| no real/external/platform data | planned only | yes | Needs future fixture-specific review. |
| no account/session/cookie/token | planned only | yes | Needs future privacy/security check. |
| no model output | planned only | yes | Model-output integration remains closed. |
| no labels from real data | planned only | yes | P7 remains closed. |
| field-family alignment reviewed | planned only | yes | Future fixture must be checked against `02B`. |
| storage / Git policy reviewed | planned only | yes | Requires future `may_enter_git` decision. |
| evidence / risk references ready | planned only | yes | Must be updated at implementation time. |
| human / Web ChatGPT approval | not approved for implementation | yes | This review does not approve implementation. |
| `10_NEXT` implementation approval | not approved | yes | Current and next tasks remain docs-only. |
| P7-P12 non-entry | active | yes for later stages | Fixture work cannot open training stages. |

Review decision:

```text
The future implementation entry criteria are sufficient and clearly express
that current implementation conditions are not satisfied.
```

## Future Validation Expectations Review

`02F` plans future validation expectations without creating tests or commands.
It covers:

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
- storage / privacy field validation planned.
- tests planned but not created in this task.
- validation command planned but not run in this task.

Review decision:

```text
The validation expectations are sufficient to prevent premature fixture
creation or unapproved implementation at this stage.
```

## Synthetic/Local Fixture Risk Review

`02F` covers the expected synthetic/local fixture risks and the risk register is
consistent with the boundary.

| risk | mitigation_present | blocker | owner_doc_or_followup | notes |
|---|---|---|---|---|
| Synthetic fixture mistaken for real data. | yes | no for review; yes for future fixture implementation | `02F`, future review | Requires synthetic/local warnings and project-authored source id. |
| Fixture boundary mistaken for fixture implementation approval. | yes | no for review; yes for implementation | `02F`, `10_NEXT` | Boundary and review both keep fixture creation closed. |
| Fixture shape mistaken for schema implementation. | yes | no for review; yes for schema implementation | `02B`, `02E`, `02F` | Shape families are documentation boundary only. |
| Real log accidentally copied into fixture. | yes | no for review; yes for future fixture | future validation task | Requires no-real-data assertion. |
| Player/account identifiers accidentally included. | yes | no for review; yes for future fixture | source inventory / privacy review | Requires synthetic seats and privacy review. |
| Model outputs included too early. | yes | no for review; yes for future fixture | future review | Model-output content remains forbidden. |
| Labels or features creep into fixture. | yes | no for review; yes for future fixture | P6/P7 stage gates | No features or labels now. |
| Fixture used for training. | yes | no for review; yes for training | stage contract | Synthetic fixture is not a dataset. |
| Fixture overclaimed as strength / Tenhou / LuckyJ evidence. | yes | no for review; governance blocker if violated | evidence log / ranking protocol | Evidence grade is conservative. |
| Fixture used to bypass source approval. | yes | no for review; yes for ingestion | source inventory | Source approval remains separate. |
| Fixture expands into broad ingestion or CLI. | yes | no for review; yes for implementation | future review | CLI and broad ingestion remain forbidden. |
| Fixture implementation jumps into parser / dataset reader. | yes | no for review; yes for parser/reader | future `10_NEXT` | No parser or reader now. |
| P6 fixture planning drifts into P7-P12. | yes | no for review; yes for later stages | stage contract | P7-P12 require separate entry approval. |

Review decision:

```text
The risk coverage and mitigation wording are sufficient for this docs-only
review gate. No risk blocker found.
```

## Governance Synchronization Review

The governance and tracking documents are consistent with `02F`.

| document | review_status | finding | blocker |
|---|---|---|---|
| `docs/00_HANDOFF.md` | synchronized after this review | P6 fixture boundary is defined and reviewed; implementation remains closed. | no |
| `docs/00_DOCS_INDEX.md` | synchronized after this review | `02G` is indexed as review evidence. | no |
| `docs/10_next/10_NEXT.md` | synchronized after this review | Current task is completed and next task remains docs-only. | no |
| `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` | synchronized after this review | P6 status records boundary review closure and no implementation approval. | no |
| `docs/09_governance/09_EVIDENCE_LOG.md` | synchronized after this review | Evidence grade is review-only, not implementation or strength evidence. | no |
| `docs/09_governance/09_RISK_REGISTER.md` | synchronized after this review | Boundary-review risks are recorded. | no |
| `docs/09_governance/09_STAGE_TASK_CONTRACT.md` | synchronized after this review | Current next task remains docs-only and P6 implementation closed. | no |
| `docs/07_development_execution/07B_TASK_BACKLOG.md` | synchronized after this review | Review is done and next checklist task is planned. | no |
| `docs/07_development_execution/07A_MILESTONES.md` | synchronized after this review | P6 remains docs-only planning with implementation closed. | no |
| `docs/09_governance/09_CHANGELOG.md` | synchronized after this review | Review closure is recorded. | no |
| `docs/09_governance/09_DECISION_RECORD.md` | synchronized after this review | Decision to close review while keeping implementation closed is recorded. | no |

Review decision:

```text
No governance synchronization blocker found.
```

## Review Decision

```text
Review can close, but fixture implementation remains closed.
```

No blocker was found.

This review confirms:

- `02F` scope is correct.
- allowed fixture boundary is sufficient.
- forbidden fixture boundary is strict enough.
- source inventory dependency is clear.
- replay schema boundary dependency is clear.
- future fixture shape families are sufficient and safe.
- future implementation entry criteria are sufficient.
- future validation expectations are sufficient.
- risks / mitigations are sufficient.
- governance docs are synchronized.

This review does not approve:

- P6 implementation.
- fixture implementation.
- replay schema implementation.
- data ingestion.
- dataset readers.
- parsers.
- feature extraction.
- label generation.
- real Tenhou, real haifu, external-log or platform-data access.
- model-output integration.
- CLI or broad file ingestion.
- training, tuning, self-play, league or runner behavior.
- P7-P12 entry.

## Next Task Recommendation

```text
Define P6 replay schema and fixture implementation readiness checklist before code.
```

The next task should remain docs-only. It must not implement replay fixture
files, replay schema code, dataclasses, pydantic models, JSON schema, parsers,
dataset readers, ingestion, feature extraction, label generation, CLI,
model-output integration, real data access, training, self-play, league,
runner behavior, metric implementation, registry changes, promotion criteria
changes or P7-P12 work.

## Evidence Grade

```text
P6 synthetic/local replay fixture boundary review evidence only.
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
