# 02B_REPLAY_SCHEMA

## Scope

This document defines the P6 replay schema documentation boundary after the
P6 data-source provenance and rights inventory review.

It is a planning artifact only. It does not implement:

- replay schema code.
- dataset readers.
- data ingestion.
- feature extraction.
- label generation.
- CLI or broad file ingestion.
- model-output integration.
- real Tenhou, real haifu, external-log or platform-data access.
- training, tuning, self-play, league, runner behavior or P7-P12 work.

North-star relationship:

```text
Future replay data must be lawful, reproducible and auditable before it can
support supervised learning, reinforcement learning, search or Tenhou-target
validation toward stable dan > 10.68.
```

This document is not model-strength evidence and is not LuckyJ `10.68`
comparison evidence.

## Post-Source-Inventory Context

Current preconditions:

- P5 evaluation groundwork is closed for the current synthetic/local scope.
- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md` allows docs-only
  P6 planning after final P5 closure.
- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
  defines P6 data-system scope, entry criteria and first task before
  implementation.
- `docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 data-source
  provenance and rights inventory.
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
  reviews the inventory with no blocker.

Current closed items:

- P6 implementation is still not approved.
- Replay schema implementation is still not approved.
- Source ingestion is still not approved.
- Feature extraction and label generation are still not approved.
- P7-P12 remain closed.

## Replay Schema Purpose

The future replay schema should provide a normalized, auditable representation
of mahjong replay records for later P6 data-system work. Its intended use is to
make every future training or evaluation example traceable back to:

- a replay identity.
- an approved data source.
- a versioned transform.
- a ruleset / room context.
- a deterministic event index.
- an observation or decision-state boundary.
- a terminal result boundary.
- validation and provenance metadata.

This document defines field families and guardrails only. It does not define a
Python dataclass, JSON schema, parser, reader, writer or storage layout.

## Allowed Documentation Scope

| scope_item | allowed_definition | implementation_allowed_now | source_inventory_dependency | notes |
|---|---|---:|---|---|
| replay record identity | Define future identity fields such as `replay_id`, `source_id`, `source_record_id`, `schema_version`, `transform_version` and hash references. | no | Requires an approved source inventory record before real replay use. | IDs are planning names, not storage implementation. |
| source provenance reference | Define links to `02A`, evidence log entries and risk-register entries. | no | Requires source id, origin, rightsholder and allowed-use status. | Provenance reference is mandatory before ingestion. |
| source approval reference | Define future `approval_status`, reviewer and review-date fields. | no | Requires source-specific approval. | Inventory review is not approval. |
| ruleset / room / game context | Define field families for `ruleset`, `room_context`, table context and source time status. | no | Depends on source terms and source format. | Do not infer real Tenhou semantics without approved source review. |
| table / player / seat metadata | Define anonymized seat and player metadata boundaries. | no | Requires privacy review and account-identifier policy. | Player identity must not enter Git without approval. |
| event sequence | Define future `event_index`, `event_type` and `event_payload_boundary`. | no | Depends on approved replay source format. | No event parser is implemented here. |
| event type vocabulary planning | List future vocabulary families such as start, draw, discard, call, reach, win, abort and terminal events. | no | Requires schema review and source-specific examples. | Vocabulary planning is not parser support. |
| action vocabulary planning | Define future action vocabulary families and dependency on canonical action review. | no | Depends on `05L` and future P6 schema review. | No legal-action checker or canonicalizer is added. |
| observation / decision-state boundary | Define where visible-state, hidden-information policy, legal-action context and labels may live later. | no | Requires leakage controls and approved source. | Feature extraction is not implemented. |
| terminal result / placement / score boundary | Define field families for final placement, score and rank-point result. | no | Requires source-specific result semantics. | Not stable-dan evidence by itself. |
| round / hand / honba / kyotaku / dealer / dora context planning | Define future field families for hand context. | no | Requires source format and ruleset review. | No tile parser or dora normalization is implemented. |
| anonymization / privacy hooks | Define future privacy review, anonymization status and account-identifier policy. | no | Requires source-specific privacy review. | Private/account data remains blocked. |
| raw-vs-derived distinction | Define future raw replay reference versus normalized derived record boundary. | no | Requires raw/derived storage policy in source inventory. | Raw real data must not enter Git by default. |
| schema versioning | Define `schema_version` as a mandatory future field family. | no | Requires implementation review before use. | Documentation name only. |
| transform versioning | Define `transform_version` and transform provenance family. | no | Requires transform implementation approval. | No transform code is approved. |
| validation status field planning | Define future `validation_status`, parse status and quality flags. | no | Requires validation command and tests in a later implementation task. | No validation code is added. |
| known exclusions | Define excluded source and event categories. | no | Depends on source inventory and risk review. | Exclusions prevent silent scope expansion. |
| non-evidence warnings | Define warnings that replay schema planning is not strength or LuckyJ evidence. | no | Applies to every future source and schema artifact. | Required in evidence log / docs. |
| future implementation entry criteria | Define required approvals before schema code may start. | no | Requires 02A/02D plus future review gate. | Current status: not satisfied. |
| future review requirements | Define review gates before implementation, ingestion and training. | no | Requires governance synchronization. | Next task is review boundary, not implementation. |

## Forbidden Scope

| forbidden_item | reason | earliest_possible_condition | guardrail |
|---|---|---|---|
| Replay schema code | Current task is documentation boundary only. | Separate P6 implementation task after review. | `10_NEXT` must explicitly approve code. |
| Dataset reader | Reader would imply ingestion path. | Source approval plus schema implementation approval. | No broad file ingestion. |
| Data ingestion | Ingestion can introduce rights, privacy and leakage risks. | Source-specific approval and implementation task. | Real/external sources remain blocked. |
| Feature extraction | Feature code can leak hidden information or create training data prematurely. | Approved schema, leakage policy and tests. | No feature extraction in this task. |
| Label generation | Labels can imply supervised learning readiness. | Approved source, schema and label policy. | P7 remains closed. |
| Real Tenhou data | Platform, privacy and compliance risks. | Separate legal/terms/source approval. | No Tenhou access or account tooling. |
| Real haifu ingestion | Rights/provenance and privacy risks. | Source-specific approval and storage policy. | No parser/ingestion code. |
| External logs | Unknown provenance and rights. | Source-specific inventory and approval. | No external-log reader. |
| Platform data | Platform terms and account risks. | Compliance review and explicit approval. | No platform automation. |
| Online accounts / sessions / cookies / tokens / private logs | Security, privacy and compliance risks. | Separate compliance clearance. | Forbidden now. |
| Platform automation / scraping / evasion / anti-detection | Compliance and safety risk. | Not approved by this stage. | Forbidden now. |
| Model-output integration | Would couple P6 planning to evaluators/models. | Later scoped adapter task, if approved. | No model code. |
| CLI or broad file ingestion | Can become unbounded data ingestion. | Separate implementation boundary. | No CLI. |
| Akochan `system.exe`, `libai.so` or third-party binaries | Third-party artifact and license risk. | Separate audited integration task. | Do not call or store binaries. |
| Third-party source, `params/`, build artifacts or unknown weights | License/provenance risk. | Explicit artifact approval. | Do not vendor or save artifacts. |
| Training, tuning, self-play, league or runner behavior | Wrong stage; P7-P12 remain closed. | Later stage entry approval. | Forbidden now. |
| Strength, Tenhou, stable-dan or LuckyJ claims | Schema planning is not performance evidence. | Requires later ranked/evaluation evidence. | Non-evidence warnings required. |

## Source Inventory Dependency

No replay schema implementation may consume a source until the source has an
approved inventory record with at least:

- `source_id`.
- source category and source owner / rightsholder.
- license / terms summary.
- allowed use and forbidden use.
- raw storage policy and derived storage policy.
- `may_enter_git` decision.
- privacy / personal-data review.
- platform-terms review, when applicable.
- evidence-log reference.
- risk-register reference.
- reviewer / approval owner.
- explicit ingestion approval.
- explicit replay schema implementation task in `docs/10_next/10_NEXT.md`.

The `02A` inventory and `02D` review are necessary prerequisites, but they are
not source approval, ingestion approval or replay schema implementation
approval.

## Replay Schema Field-Family Draft

The following field families define documentation boundaries only. They are not
implemented schema fields and must not be treated as a JSON schema, dataclass or
parser contract.

| field_family | example_fields_or_concepts | purpose | implementation_status | source_dependency | non_evidence_warning |
|---|---|---|---|---|---|
| A. replay_identity | `replay_id`, `source_id`, `source_record_id`, `schema_version`, `transform_version`, `checksum_or_hash_reference` | Make each future replay record traceable and versioned. | documentation boundary only | approved source inventory record | Identity fields are not strength evidence. |
| B. provenance | `source_inventory_ref`, `evidence_log_ref`, `risk_register_ref`, `approval_status`, `rights_status`, `allowed_use_summary`, `non_evidence_warning` | Keep rights/provenance visible in every future replay record. | documentation boundary only | source rights review | Provenance links do not approve ingestion. |
| C. game_context | `ruleset`, `room_context`, `table_context`, `game_start_time_status`, `source_time_status` | Record future context needed for rule-consistent interpretation. | documentation boundary only | source format and terms | Context metadata is not Tenhou evidence. |
| D. participants | `player_count`, `seat_index_policy`, `anonymized_player_id_policy`, `account_identifier_policy` | Preserve seat semantics while protecting identities. | documentation boundary only | privacy review | Participant metadata is not approved account data. |
| E. hand_round_context | `round_index_policy`, `honba_policy`, `kyotaku_policy`, `dealer_policy`, `dora_indicator_policy` | Define future round/hand context families. | documentation boundary only | source and ruleset review | No tile or dora parser is implemented. |
| F. event_sequence | `event_index`, `event_type`, `event_payload_boundary`, `actor_seat`, `visibility_boundary`, `known_exclusions` | Give every future replay event deterministic order and visibility boundary. | documentation boundary only | source event format | Event planning is not event parsing. |
| G. action_context | `action_type_vocabulary`, `legal_action_context_boundary`, `model_output_absent_boundary`, `canonicalization_dependency` | Tie future actions to canonicalization and legal-action boundaries. | documentation boundary only | `05L` plus future schema review | No model-output or legal-action checker is approved. |
| H. decision_state_boundary | `observation_scope`, `hidden_information_policy`, `available_action_policy`, `label_availability_policy`, `feature_extraction_not_implemented_warning` | Prevent hidden-information leakage in future examples. | documentation boundary only | source + leakage policy | No features or labels are generated. |
| I. terminal_result | `placement_policy`, `score_policy`, `rank_point_policy`, `outcome_source_policy` | Define future final outcome representation. | documentation boundary only | source result semantics | Results are not stable-dan evidence without later evaluation. |
| J. validation_metadata | `validation_status`, `validation_command_future`, `parse_status_future`, `quality_flags_future`, `known_failure_modes` | Plan future validation and quality reporting. | documentation boundary only | later tests and validation command | No validation code exists here. |
| K. storage_and_privacy | `raw_storage_policy`, `derived_storage_policy`, `may_enter_git`, `anonymization_status`, `privacy_review_status` | Keep storage, Git and privacy status explicit. | documentation boundary only | source inventory and privacy review | Raw real data must not enter Git by default. |

## Validation Expectations Before Future Implementation

Before any future replay schema implementation starts, the project must confirm:

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
- tests are planned, but no tests are created by this task.
- code implementation is explicitly approved by a later `10_NEXT` task.

## Future Implementation Entry Criteria

| criterion | required_before_implementation | current_status | evidence_needed | blocker | notes |
|---|---|---|---|---|---|
| Source-specific approval | Approved source inventory record. | not satisfied for implementation | Source id, terms, allowed-use and reviewer approval. | yes | `02A`/`02D` are preconditions, not approvals. |
| Schema version approval | Reviewed schema version and compatibility plan. | defined here only | Review document and decision record. | yes | No JSON/Python schema yet. |
| Raw-vs-derived storage policy | Storage and Git policy for selected source. | planned only | `may_enter_git`, raw/derived policy and privacy review. | yes | Raw real data must not enter Git by default. |
| Privacy / anonymization policy | Participant/account fields handled safely. | planned only | Privacy review and anonymization status. | yes | Account/session/token data remains forbidden. |
| Event vocabulary approval | Event type vocabulary reviewed against source format. | planned only | Source examples and review. | yes | No parser support yet. |
| Action vocabulary approval | Action context reviewed against canonical action scope. | planned only | Cross-reference to `05L` and future P6 review. | yes | No action-space expansion now. |
| Hidden-information leakage policy | Observation and label visibility rules documented. | planned only | Leakage risk review and tests plan. | yes | Training examples are not generated now. |
| Validation command plan | Future command/test plan documented. | planned only | Validation task in `10_NEXT`. | yes | No validation command now. |
| Evidence / risk synchronization | Evidence log and risk register updated. | satisfied for this docs task only | Current docs update. | no for docs boundary; yes for implementation | Must repeat at implementation review. |
| Implementation task approval | `10_NEXT` explicitly authorizes code. | not satisfied | Later review gate. | yes | Next task is review, not implementation. |

## Replay Schema Risks

| risk | mitigation | blocker_status | owner_doc_or_followup | notes |
|---|---|---|---|---|
| Boundary documentation is mistaken for replay schema implementation approval. | Repeat non-approval in `02B`, `10_NEXT`, stage contract and evidence log. | blocker for implementation | `02B`, `10_NEXT` | Current task is docs-only. |
| Source inventory review is mistaken for source approval. | Require source-specific approval before implementation. | blocker for ingestion | `02A`, `02D` | No source is over-approved here. |
| Real Tenhou or real haifu data enters before compliance review. | Keep real/platform sources blocked until source-specific review. | blocker for real data | `02A`, risk register | No real data path now. |
| Hidden-information leakage is baked into future schema. | Require observation/decision-state boundary and leakage tests before implementation. | blocker for features/labels | future P6 schema review | No feature extraction now. |
| Raw real data or private data is committed to Git. | Require `may_enter_git`, storage policy and privacy review. | blocker for storage | source inventory | Raw real data should default to out-of-Git. |
| Event/action vocabulary expands without review. | Keep event/action vocabulary as planning only. | blocker for parser/canonicalizer | `05L`, future P6 review | No reach/call/kan/hora expansion now. |
| Replay schema planning is overclaimed as model strength or LuckyJ evidence. | Evidence grade and non-evidence warnings remain explicit. | open governance risk | evidence log / ranking protocol | Schema planning is not evaluation evidence. |
| P6 docs planning drifts into P7-P12. | Keep training, self-play, league and model-output paths forbidden. | blocker for later stages | stage contract / `10_NEXT` | Later stages require separate approval. |
| CLI or broad file ingestion appears under schema work. | Require separate implementation boundary. | blocker for implementation | future task review | No CLI now. |
| Third-party binaries or artifacts enter the repo. | Keep artifact storage forbidden. | blocker for artifacts | risk register | No system.exe/libai.so/weights. |

## Planning Decision

```text
P6 replay schema documentation boundary is defined for review after source
inventory review. Replay schema implementation is still not approved.
```

## Review Status

`docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
reviews this replay schema documentation boundary before implementation.

Review decision:

```text
Review can close, but replay schema implementation remains closed.
```

This review reference does not widen the boundary. P6 implementation, replay
schema implementation, data ingestion, dataset readers, feature extraction,
label generation, real Tenhou / real haifu / external-log / platform-data
access, model-output integration, CLI, training, self-play, league and P7-P12
remain closed.

Synthetic/local replay fixture boundary:

```text
docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md
defines future project-authored synthetic/local replay fixture shape families
as documentation boundaries only. It does not create a fixture, implement this
schema, approve ingestion, approve dataset readers or approve feature/label
generation.

docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md
reviews that boundary with no blocker and keeps fixture implementation, replay
schema implementation, ingestion, dataset readers, parsers, feature extraction
and label generation closed.

docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md
defines readiness criteria before replay schema code or fixture implementation
can be considered. It does not approve replay schema implementation.
```

## Next Task Recommendation

```text
Review P6 replay schema and fixture implementation readiness checklist before code.
```

The next task should remain docs-only unless a later review explicitly approves
implementation. It must not implement replay schema code, fixtures, ingestion,
validation commands, dataset readers, parsers, feature extraction, label
generation, CLI, model-output integration, real data access, training,
self-play, league, runner behavior or P7-P12 work.

## Evidence Grade

```text
P6 replay schema documentation boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

- P6 implementation approval.
- replay schema implementation.
- data ingestion.
- source approval.
- feature extraction.
- label generation.
- dataset generation.
- supervised-learning readiness.
- real Tenhou access.
- real haifu ingestion.
- external-log ingestion.
- platform-data access.
- model-output integration.
- training, tuning, self-play, league or runner behavior.
- model strength.
- Tenhou ranked performance.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.
- P7-P12 entry.
