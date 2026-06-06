# 02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW

## Scope

This document reviews:

```text
docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md
```

It is a docs-only P6 implementation proposal boundary review gate. It does not:

- approve P6 implementation.
- approve replay schema implementation.
- approve replay fixture implementation.
- approve tests.
- create fixture files.
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
- add latency measurement, fixed-position exact-match computation, metric
  implementation, registry code changes or promotion criteria changes.
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

North-star relationship:

```text
This review supports the long-term stable-dan > 10.68 goal only by checking
that future P6 implementation proposals cannot bypass source, schema, fixture,
readiness, evidence, risk and stage boundaries. It is not strength evidence
and does not approve implementation.
```

## Reviewed Artifacts

Primary review target:

- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`

P6 planning context:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md`
- `docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md`
- `docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md`
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
- `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`

P5 closure / transition context:

- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md`
- `docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md`
- `docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md`

Evaluation / evidence context:

- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md`
- `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`

Governance context:

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

These source, test and fixture files were context only. This review did not
modify code, tests or fixtures.

## Proposal Boundary Scope Review

`02J` correctly limits itself to the P6 replay schema and synthetic fixture
implementation proposal boundary before code.

| scope question | finding | blocker | notes |
|---|---:|---:|---|
| Is `02J` docs-only? | yes | no | It is proposal-boundary definition evidence only. |
| Does `02J` avoid approving P6 implementation? | yes | no | Scope, planning decision and non-evidence list keep implementation closed. |
| Does `02J` avoid approving replay schema implementation? | yes | no | It allows only candidate concepts, not schema code. |
| Does `02J` avoid approving fixture implementation? | yes | no | It defines fixture candidate boundary only. |
| Does `02J` avoid approving tests? | yes | no | It defines validation/test proposal candidates only. |
| Does `02J` avoid approving data ingestion? | yes | no | Ingestion remains deferred / blocked. |
| Does `02J` avoid approving parser / dataset reader work? | yes | no | Parser and reader are deferred. |
| Does `02J` avoid approving feature extraction / label generation? | yes | no | Feature and label work remain deferred. |
| Does `02J` avoid real Tenhou / real haifu / external logs / platform data? | yes | no | These are explicitly forbidden. |
| Does `02J` avoid model-output integration, CLI, broad ingestion, training, self-play, league, runner or P7-P12? | yes | no | These remain forbidden or later-stage only. |

Review finding:

```text
02J scope is correct.
```

## Candidate Proposal Classes Review

| candidate | covered_in_02J | current_status | implementation_allowed_now | review_finding |
|---|---:|---|---:|---|
| minimal replay schema code | yes | proposal_defined_for_review | no | covered as candidate only; no dataclass / pydantic / JSON schema is approved. |
| project-authored synthetic/local replay fixture | yes | proposal_defined_for_review | no | covered as candidate only; no fixture file is approved. |
| schema validation tests | yes | proposal_defined_for_review | no | covered as candidate only; no tests are approved. |
| fixture validation tests | yes | proposal_defined_for_review | no | covered as candidate only; no tests are approved. |
| no-op / static documentation-only validation plan | yes | proposal_defined_for_review | no | covered as a non-code review concept. |
| future parser / dataset reader | yes | deferred_later_stage | no | sufficiently deferred. |
| future feature extraction / label generation | yes | deferred_later_stage | no | sufficiently deferred; P7 remains closed. |
| future data ingestion | yes | deferred_later_stage | no | sufficiently deferred; source-specific approval required later. |
| real / external / platform source integration | yes | blocked_by_source_policy | no | sufficiently blocked. |
| CLI / broad file ingestion | yes | blocked_by_source_policy | no | sufficiently blocked. |
| model-output integration | yes | blocked_by_source_policy | no | sufficiently blocked. |
| training / self-play / league / P7-P12 | yes | deferred_later_stage | no | sufficiently deferred to later independent stage gates. |

Review finding:

```text
Candidate proposal classes are sufficient and conservative.
No candidate is approved for implementation.
```

## Required Proposal Sections Review

`02J` requires future implementation proposals to include the following
sections:

- proposal title.
- target stage.
- implementation candidate class.
- scope.
- non-goals.
- source inventory dependency.
- replay schema boundary dependency.
- synthetic/local fixture boundary dependency.
- readiness checklist status.
- allowed files.
- forbidden files.
- allowed code changes.
- forbidden code changes.
- fixture policy.
- test policy.
- validation commands.
- evidence log update plan.
- risk register update plan.
- docs index / handoff / `10_NEXT` update plan.
- rollback plan.
- blocker list.
- human / Web ChatGPT approval requirement.
- P7-P12 non-entry boundary.
- explicit non-evidence warnings.

Review finding:

```text
Required proposal sections are sufficient. No missing, ambiguous, unsafe or
implementation-like required section was found.
```

## Allowed Proposal Boundary Review

`02J` allows a future proposal to describe only candidate artifacts and review
plans:

- candidate minimal schema names and module paths.
- candidate fixture file path and small JSON shape.
- candidate test file names.
- candidate validation commands.
- candidate evidence-log updates.
- candidate risk-register updates.
- candidate rollback criteria.
- candidate implementation stop conditions.
- candidate later review gate.
- source inventory dependencies.
- replay schema boundary dependencies.
- synthetic/local fixture boundary dependencies.
- readiness checklist dependencies.

Review finding:

```text
Allowed proposal boundary is safe and proposal-only. It does not approve code,
tests, fixtures, ingestion paths or stage transitions.
```

## Forbidden Proposal Boundary Review

`02J` explicitly forbids a proposal from treating the following as currently
approved:

- real Tenhou data.
- real haifu data.
- external logs.
- platform data.
- online accounts, sessions, cookies or tokens.
- platform automation, scraping, evasion or anti-detection tooling.
- source ingestion pipeline.
- broad dataset reader.
- CLI or broad file ingestion.
- parser for real logs.
- feature extraction.
- label generation.
- model-output integration.
- training, tuning, self-play, league or runner behavior.
- P7-P12 work.
- strength evidence, Tenhou ranked evidence, stable-dan ranked-game evidence,
  LuckyJ `10.68` comparison or candidate-promotion evidence.
- third-party binaries, `system.exe`, `libai.so`, `params/`, model weights,
  checkpoints or build artifacts.

Review finding:

```text
Forbidden proposal boundary is sufficiently strict.
```

## Source And Fixture Constraints Review

`02J` limits future proposals to:

- project-authored synthetic/local source category.
- small deterministic repo-local fixture candidates only if later approved.
- no real gameplay logs.
- no real player/account identifiers.
- no platform data.
- no external logs.
- no model output.
- no labels from real data.
- no training use.
- no strength/evaluation-claim use.
- `may_enter_git` only for small project-authored synthetic content after
  explicit future approval.
- required `source_id`, evidence-log reference and risk-register reference.
- source inventory as prerequisite, not approval.

Review finding:

```text
Source and fixture constraints are sufficient and conservative.
```

## Minimal Replay Schema Code Candidate Boundary Review

`02J` defines, but does not implement, a minimal replay schema code candidate.
It limits that candidate to:

- module path candidate.
- schema object concept.
- `schema_version` concept.
- field-family alignment with `02B`.
- source / provenance hook concept.
- validation metadata hook concept.
- storage / privacy hook concept.
- explicit synthetic/local starter scope.
- explicit no-real-data assertion.

It explicitly forbids:

- replay schema code.
- Python dataclasses.
- pydantic model.
- JSON schema.
- parser.
- data ingestion.
- dataset reader.
- feature extraction.
- label generation.
- real data.
- P7-P12 entry.

Review finding:

```text
Minimal replay schema code candidate boundary is safe. No implementation,
schema, dataclass, pydantic model, JSON schema, parser contract or
implementation semantics are approved.
```

## Minimal Synthetic/Local Fixture Candidate Boundary Review

`02J` defines, but does not create, a minimal synthetic/local replay fixture
candidate. It limits that candidate to:

- fixture path candidate.
- top-level shape concept.
- project-authored `source_id`.
- field-family coverage aligned with `02B`.
- deterministic smoke-only purpose.
- source / provenance metadata.
- evidence-log and risk-register references.
- explicit non-evidence warnings.

It explicitly forbids:

- fixture file creation.
- real Tenhou, real haifu, external logs or platform data.
- player/account identifiers.
- model output.
- real labels.
- training use.
- evaluation-strength use.
- broad ingestion path.

Review finding:

```text
Minimal synthetic/local fixture candidate boundary is safe. No fixture creation
is approved.
```

## Test And Validation Proposal Boundary Review

`02J` defines, but does not create, a test and validation plan. It allows only
candidate descriptions for:

- schema validation test.
- fixture validation test.
- no-real-data assertion.
- no-account / session / cookie / token assertion.
- no-model-output assertion.
- required top-level field assertion.
- source / provenance reference assertion.
- evidence-log reference assertion.
- risk-register reference assertion.
- candidate validation command.

It explicitly forbids:

- tests.
- fixtures.
- test execution beyond `git diff --check` for the docs-only task.
- real data commands.
- Tenhou commands.
- `system.exe`, `libai.so` or third-party binary commands.
- training, self-play, league or runner commands.

Review finding:

```text
Test and validation proposal boundary is safe. No test creation or validation
execution is approved.
```

## Future Implementation Approval Conditions Review

`02J` requires all of the following before future implementation may be
considered:

- proposal boundary reviewed in a separate docs-only review gate.
- explicit implementation task becomes first unchecked item in `10_NEXT`.
- human / Web ChatGPT approval is recorded.
- Codex prompt explicitly allows limited code, fixture or test changes.
- source inventory remains clean and source category remains approved for the
  exact implementation scope.
- no real / external / platform source is introduced.
- rollback plan is documented.
- evidence-log and risk-register update plans are documented.
- validation commands are listed.
- stop conditions are documented.
- P7-P12 non-entry remains explicit.

Review finding:

```text
Future implementation approval conditions are sufficient. 02J does not mark
these conditions as currently satisfied and does not approve implementation.
```

## Proposal Decision Vocabulary Review

`02J` defines the following proposal decision vocabulary:

- `proposal_defined_for_review`.
- `not_implementation_approval`.
- `implementation_not_ready`.
- `implementation_candidate_requires_review`.
- `blocked_by_source_policy`.
- `blocked_by_real_data`.
- `deferred_later_stage`.
- `requires_human_approval`.
- `implementation_allowed_only_after_explicit_10_NEXT_task`.

Every term has `implementation_approved = no`.

Review finding:

```text
Proposal decision vocabulary is safe. No term can be read as current
implementation approval.
```

## P7-P12 Non-Entry Boundary Review

`02J` explicitly does not approve:

- P7 supervised learning.
- P8 reinforcement learning.
- P9 search / risk model implementation.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou target validation.
- training, tuning, self-play, league or runner behavior.
- model-output integration.
- real Tenhou, real haifu, external logs or platform-data ingestion.
- model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claims.

Review finding:

```text
P7-P12 non-entry boundary is sufficient.
```

## Proposal Boundary Risk Review

| risk | mitigation_present | blocker | owner_doc_or_followup | notes |
|---|---:|---:|---|---|
| proposal mistaken for implementation approval | yes | no for review; yes for implementation | `02J`, this review, `10_NEXT` | Repeated non-approval language is present. |
| proposal includes too broad file scope | yes | no for review; yes for implementation | future proposal | Allowed/forbidden file sections are required. |
| proposal silently expands to parser / ingestion | yes | no for review; yes for implementation | `02J`, future proposal review | Parser, reader and ingestion are forbidden / deferred. |
| proposal introduces real data assumptions | yes | no for review; yes for implementation | `02A`, `02J` | Project-authored synthetic/local source category only. |
| proposal creates fixture without approval | yes | no for review; yes for implementation | `02F`, `02J` | Fixture creation remains forbidden. |
| proposal creates tests without approval | yes | no for review; yes for implementation | `02J`, `10_NEXT` | Tests remain forbidden. |
| proposal bypasses source inventory | yes | no for review; yes for implementation | `02A`, future proposal | `02A` / `02D` dependency is required. |
| proposal treats synthetic fixture as model evidence | yes | no for review; governance blocker if claimed | evidence log / ranking protocol | Evidence grade and warnings are required. |
| proposal leaks into feature extraction / label generation | yes | no for review; yes for implementation | future feature/label review | Feature and label work are deferred. |
| proposal creates CLI or broad file ingestion | yes | no for review; yes for implementation | future boundary | CLI and broad ingestion are forbidden. |
| proposal enters P7-P12 | yes | no for review; yes for later stages | stage contract | Non-entry boundary is explicit. |
| proposal lacks rollback plan | yes | no for review; yes for implementation | future proposal | Rollback plan is required. |
| proposal lacks validation commands | yes | no for review; yes for implementation | future proposal | Candidate validation commands are required. |
| proposal lacks evidence / risk updates | yes | no for review; yes for implementation | evidence log / risk register | Evidence/risk update plans are required. |

Review finding:

```text
Proposal boundary risks and mitigations are sufficient. No blocker was found.
```

## Governance Synchronization Review

| document | synchronized_by_this_review | finding | blocker |
|---|---:|---|---:|
| `docs/00_HANDOFF.md` | yes | records `02K`, current status and next docs-only proposal task. | no |
| `docs/00_DOCS_INDEX.md` | yes | indexes `02K` and evidence meaning. | no |
| `docs/10_next/10_NEXT.md` | yes | marks this review complete and sets the next docs-only proposal drafting task. | no |
| `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` | yes | records proposal boundary review completion and next task. | no |
| `docs/09_governance/09_EVIDENCE_LOG.md` | yes | records review evidence and non-evidence. | no |
| `docs/09_governance/09_RISK_REGISTER.md` | yes | records review-specific risks. | no |
| `docs/09_governance/09_STAGE_TASK_CONTRACT.md` | yes | records current focus and next-only boundary. | no |
| `docs/07_development_execution/07B_TASK_BACKLOG.md` | yes | marks review done and adds next task. | no |
| `docs/07_development_execution/07A_MILESTONES.md` | yes | updates P6 status and next proposal-drafting boundary. | no |
| `docs/09_governance/09_CHANGELOG.md` | yes | records review completion. | no |
| `docs/09_governance/09_DECISION_RECORD.md` | yes | records the review closure decision. | no |

Review finding:

```text
Governance and tracking docs are synchronized.
```

## Review Decision

```text
Review can close, but P6 implementation remains closed.
```

Consequences:

- `02J` is sufficient as a proposal boundary before code.
- no blocker was found.
- P6 implementation remains closed.
- replay schema implementation remains closed.
- replay fixture implementation remains closed.
- tests remain closed.
- data ingestion remains closed.
- parser / dataset reader implementation remains closed.
- feature extraction / label generation remain closed.
- P7-P12 remain closed.

## Next Task Recommendation

```text
Review P6 minimal replay schema and synthetic fixture implementation proposal before code.
```

`02L` now prepares the docs-only proposal. The next task must remain a
docs-only proposal review gate. It must not implement P6, replay schema code,
dataclasses, pydantic models, JSON schema, parsers, dataset readers, fixture
files, tests, ingestion, feature extraction, label generation, CLI, broad file
ingestion, model-output integration, latency measurement, fixed-position
exact-match, metric implementation, registry code changes, promotion criteria
changes, training, tuning, self-play, league, runner behavior, real Tenhou,
real haifu, external logs, platform data or P7-P12.

## Evidence Grade

```text
P6 replay schema and synthetic fixture implementation proposal boundary review evidence only.
```

## Explicit Non-Evidence

This review is not evidence of:

- P6 implementation approval.
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
