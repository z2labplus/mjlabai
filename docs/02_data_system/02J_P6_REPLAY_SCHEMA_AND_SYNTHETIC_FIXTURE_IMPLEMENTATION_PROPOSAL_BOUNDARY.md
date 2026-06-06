# 02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY

## Scope

This document defines the P6 replay schema and synthetic fixture
implementation proposal boundary before code.

It is a docs-only proposal-boundary definition. It does not:

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
Replay schema and synthetic fixture implementation proposals can support the
long-term stable-dan > 10.68 target only by preventing unsafe or premature P6
data-system implementation. This proposal boundary is not implementation
approval and is not strength evidence.
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
- `docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md`
  defines readiness criteria before code.
- `docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md`
  reviews that checklist with no blocker.

Current closed items:

- P6 implementation is not approved.
- Replay schema implementation is not approved.
- Replay fixture implementation is not approved.
- Data ingestion is not approved.
- Parser and dataset reader implementation is not approved.
- Feature extraction and label generation are not approved.
- Tests and fixtures for P6 replay data are not approved.
- P7-P12 remain closed.

## Proposal Boundary Purpose

The purpose of this boundary is to define how a future implementation proposal
must be written and reviewed before any replay schema code, synthetic replay
fixture, validation test, parser, reader, ingestion path, feature extraction or
label generation can be considered.

This boundary is positioned after:

- source inventory definition and review.
- replay schema documentation boundary definition and review.
- synthetic/local replay fixture boundary definition and review.
- replay schema and fixture implementation readiness checklist definition and
  review.

It is positioned before:

- minimal replay schema code.
- synthetic/local replay fixture creation.
- schema validation tests.
- fixture validation tests.
- parser or dataset reader implementation.
- data ingestion.
- feature extraction.
- label generation.

It defines proposal content, proposal risks, proposal vocabulary, required
review gates and stop conditions. It does not approve the future proposal and
does not approve implementation.

## Candidate Proposal Classes

All classes below are proposal candidates only. None is approved for
implementation by this document.

| candidate | current_status | implementation_allowed_now | proposal_boundary | notes |
|---|---|---:|---|---|
| A. minimal replay schema code | proposal_defined_for_review | no | may be described as a future candidate only | No dataclass, pydantic model or JSON schema now. |
| B. project-authored synthetic/local replay fixture | proposal_defined_for_review | no | may be described as a future candidate only | No fixture file now. |
| C. schema validation tests | proposal_defined_for_review | no | may be described as a future candidate only | No tests now. |
| D. fixture validation tests | proposal_defined_for_review | no | may be described as a future candidate only | No tests now. |
| E. no-op / static documentation-only validation plan | proposal_defined_for_review | no | may be described for review | Static validation is not code. |
| F. future parser / dataset reader | deferred_later_stage | no | deferred out of proposal implementation scope | Parser / reader work needs a later boundary. |
| G. future feature extraction / label generation | deferred_later_stage | no | deferred out of proposal implementation scope | P7 remains closed. |
| H. future data ingestion | deferred_later_stage | no | deferred out of proposal implementation scope | Needs source-specific approval. |
| I. real / external / platform source integration | blocked_by_source_policy | no | must be explicitly forbidden | Real Tenhou, real haifu, external logs and platform data remain closed. |
| J. CLI / broad file ingestion | blocked_by_source_policy | no | must be explicitly forbidden | No CLI or broad ingestion now. |
| K. model-output integration | blocked_by_source_policy | no | must be explicitly forbidden | No model-output path now. |
| L. training / self-play / league / P7-P12 work | deferred_later_stage | no | must be explicitly forbidden | Later stages require independent approval. |

## Required Sections For Future Implementation Proposal

Any future implementation proposal for P6 replay schema and synthetic fixture
work must include all sections below before it can be reviewed:

| required_section | purpose | implementation_approval_effect |
|---|---|---:|
| proposal title | Stable proposal identity. | none |
| target stage | Must state `P6 data system`. | none |
| implementation candidate class | Must identify the candidate class, such as minimal schema code or synthetic fixture. | none |
| scope | Narrow allowed changes. | none |
| non-goals | Explicitly forbid real data, ingestion, parser, labels, training and P7-P12. | none |
| source inventory dependency | Reference `02A` and `02D`; record source category and approval status. | none |
| replay schema boundary dependency | Reference `02B` and `02E`. | none |
| synthetic/local fixture boundary dependency | Reference `02F` and `02G`. | none |
| readiness checklist status | Reference `02H` and `02I`; state readiness remains not implementation approval. | none |
| allowed files | List exact candidate file paths if a later task approves implementation. | none |
| forbidden files | List code, test, fixture, data and artifact paths that must not be touched. | none |
| allowed code changes | Candidate-only description of minimal future code changes. | none |
| forbidden code changes | Forbid parser, reader, ingestion, feature, label, CLI and model-output paths. | none |
| fixture policy | State project-authored synthetic/local only, no real/external/platform data. | none |
| test policy | State candidate test scope and no broad data reads. | none |
| validation commands | List candidate commands for future review. | none |
| evidence log update plan | Describe required future evidence entries. | none |
| risk register update plan | Describe required future risk entries. | none |
| docs index / handoff / 10_NEXT update plan | Describe synchronization plan. | none |
| rollback plan | Define revert criteria and files. | none |
| blocker list | Record unresolved source, storage, privacy, fixture and validation blockers. | none |
| human / Web ChatGPT approval requirement | State that implementation needs explicit approval. | none |
| P7-P12 non-entry boundary | Forbid later-stage work. | none |
| explicit non-evidence warnings | State proposal and future synthetic artifacts are not strength evidence. | none |

Rule:

```text
A complete implementation proposal is still not implementation approval.
```

## Allowed Proposal Boundary

A future proposal may describe, for review only:

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

These are proposal candidates only. They are not approved code, tests,
fixtures, ingestion paths or stage transitions.

## Forbidden Proposal Boundary

A future proposal must not propose, imply or treat as currently approved:

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

If a proposal relies on any item above, it is blocked before review.

## Source And Fixture Constraints

Future implementation proposals may reference only this current source class:

```text
project-authored synthetic/local source category
```

Constraints:

- fixture content must be authored by the project.
- fixture content must be small, deterministic and repo-local only if later
  approved.
- fixture content must not contain real gameplay logs.
- fixture content must not contain real player identifiers, account IDs,
  sessions, cookies, tokens or private logs.
- fixture content must not contain platform data or external logs.
- fixture content must not contain model outputs.
- fixture content must not contain real labels or training targets.
- fixture content must not be used for training.
- fixture content must not be used as model-strength, Tenhou, stable-dan,
  LuckyJ or candidate-promotion evidence.
- `may_enter_git` can be considered only for small project-authored synthetic
  fixture content after explicit future approval.
- a future fixture proposal must include `source_id`, evidence-log reference
  and risk-register reference.

The source inventory remains a prerequisite. This proposal boundary does not
grant source approval.

## Minimal Replay Schema Code Candidate Boundary

A future proposal may define, but not implement, a minimal replay schema code
candidate.

Candidate-only concepts:

- module path candidate, such as a small P6 replay-schema module.
- schema object concept.
- `schema_version` concept.
- field-family alignment with `02B`.
- source / provenance hook concept.
- validation metadata hook concept.
- storage / privacy hook concept.
- explicit synthetic/local starter scope.
- explicit no-real-data assertion.

Forbidden in this boundary:

- no replay schema code.
- no Python dataclasses.
- no pydantic model.
- no JSON schema.
- no parser.
- no data ingestion.
- no dataset reader.
- no feature extraction.
- no label generation.
- no real data.
- no P7-P12 entry.

## Minimal Synthetic/Local Fixture Candidate Boundary

A future proposal may define, but not create, a minimal synthetic/local replay
fixture candidate.

Candidate-only concepts:

- fixture path candidate.
- top-level shape concept.
- project-authored `source_id`.
- field-family coverage aligned with `02B`.
- deterministic smoke-only purpose.
- source / provenance metadata.
- evidence-log and risk-register references.
- explicit non-evidence warnings.

Forbidden in this boundary:

- no fixture file creation.
- no real Tenhou, real haifu, external logs or platform data.
- no player/account identifiers.
- no model output.
- no real labels.
- no training use.
- no evaluation-strength use.
- no broad ingestion path.

## Test And Validation Proposal Boundary

A future proposal may define, but not create, a test and validation plan.

Candidate-only test ideas:

- schema validation test candidate.
- fixture validation test candidate.
- no-real-data assertion.
- no-account / session / cookie / token assertion.
- no-model-output assertion.
- required top-level field assertion.
- source / provenance reference assertion.
- evidence-log reference assertion.
- risk-register reference assertion.
- candidate validation command.

Forbidden now:

- no tests.
- no fixtures.
- no test execution beyond `git diff --check` for this docs-only task.
- no real data commands.
- no Tenhou commands.
- no `system.exe`, `libai.so` or third-party binary commands.
- no training, self-play, league or runner commands.

## Future Implementation Approval Conditions

Future implementation may be considered only after all items below are true:

1. This proposal boundary is reviewed in a separate docs-only review gate.
2. An explicit implementation task becomes the first unchecked item in
   `docs/10_next/10_NEXT.md`.
3. Human / Web ChatGPT approval is recorded.
4. The Codex prompt explicitly allows limited code, fixture or test changes.
5. Source inventory remains clean and source category remains approved for the
   exact implementation scope.
6. No real / external / platform source is introduced.
7. A rollback plan is documented.
8. Evidence-log and risk-register update plans are documented.
9. Validation commands are listed.
10. Stop conditions are documented.
11. P7-P12 non-entry remains explicit.

If any item is missing, implementation remains blocked.

## Proposal Decision Vocabulary

Use only these statuses for proposal-boundary decisions:

| decision_status | meaning | implementation_approved |
|---|---|---:|
| `proposal_defined_for_review` | A proposal boundary or candidate is documented for later review. | no |
| `not_implementation_approval` | Artifact is explicitly not approval to implement. | no |
| `implementation_not_ready` | Required approval or scope is missing. | no |
| `implementation_candidate_requires_review` | Candidate may be reviewed later, but cannot be implemented now. | no |
| `blocked_by_source_policy` | Source rights, storage, privacy or platform policy blocks use. | no |
| `blocked_by_real_data` | Real/external/platform data would be required; current scope forbids it. | no |
| `deferred_later_stage` | Work belongs to a future P6 gate or P7-P12. | no |
| `requires_human_approval` | Human / Web ChatGPT approval is required. | no |
| `implementation_allowed_only_after_explicit_10_NEXT_task` | Implementation can be considered only if explicitly first in `10_NEXT`. | no |

No status in this vocabulary means implementation approved.

## P7-P12 Non-Entry Boundary

This proposal boundary does not approve:

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

Each later stage requires independent scope, entry criteria, risk review and
first-task approval.

## Proposal Boundary Risks

| risk | mitigation | blocker_status | owner_doc_or_followup | notes |
|---|---|---|---|---|
| Proposal mistaken for implementation approval. | State this document and any future proposal are not approval. | blocker for implementation | this document, future review, `10_NEXT` | No code, tests or fixtures now. |
| Proposal too broad in file scope. | Require allowed and forbidden file lists. | blocker for implementation | future proposal | Exact file paths required later. |
| Proposal expands to parser / ingestion. | Forbid parser, reader and ingestion paths. | blocker for implementation | this document, future review | No data path now. |
| Proposal introduces real data assumptions. | Limit to project-authored synthetic/local source category. | blocker for implementation | `02A`, future proposal | Real/external/platform sources remain closed. |
| Proposal creates fixture without approval. | Keep fixture file creation forbidden until explicit `10_NEXT` task. | blocker for implementation | `02F`, this document | No fixture now. |
| Proposal creates tests without approval. | Keep tests forbidden until explicit future task. | blocker for implementation | this document | No tests now. |
| Proposal bypasses source inventory. | Require `02A` / `02D` dependency in every proposal. | blocker for implementation | `02A`, future review | Inventory is prerequisite, not approval. |
| Proposal treats synthetic fixture as model evidence. | Evidence grade and warnings are required. | governance blocker | evidence log / ranking protocol | Synthetic fixture is non-strength evidence. |
| Proposal leaks into feature extraction / label generation. | Mark feature and label work deferred and not approved. | blocker for P7 boundary | future feature/label review | P7 remains closed. |
| Proposal creates CLI / broad ingestion. | Forbid CLI and broad file ingestion. | blocker for implementation | future boundary | No CLI now. |
| Proposal enters P7-P12. | Non-entry boundary remains explicit. | blocker for later stages | stage contract | Separate stage approvals required. |
| Proposal lacks rollback plan. | Future proposal must include rollback criteria. | blocker for implementation | future proposal | Required before code. |
| Proposal lacks validation commands. | Future proposal must list candidate validation commands. | blocker for implementation | future proposal | Commands still need later approval. |
| Proposal lacks evidence / risk updates. | Future proposal must include evidence and risk update plans. | blocker for implementation | evidence log / risk register | Required before implementation. |

## Planning Decision

```text
P6 replay schema and synthetic fixture implementation proposal boundary is
defined for review before code. It does not approve replay schema
implementation, fixture implementation, tests, parser, dataset reader, data
ingestion, feature extraction or label generation.
```

## Next Task Recommendation

```text
Review P6 minimal replay schema and synthetic fixture implementation proposal before code.
```

The proposal-boundary review has now been completed in `02K` with no blocker,
but implementation remains closed. `02L` now prepares the docs-only minimal
implementation proposal for review before code. The follow-up must review that
proposal only. It must not implement P6, replay schema code, dataclasses,
pydantic models, JSON schema, parsers, dataset readers, fixture files, tests,
ingestion, feature extraction, label generation, CLI, broad file ingestion,
model-output integration, latency measurement, fixed-position exact-match,
metric implementation, registry code changes, promotion criteria changes,
training, tuning, self-play, league, runner behavior, real Tenhou, real haifu,
external logs, platform data or P7-P12.

## Review Status

`docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`
reviews this proposal boundary and records:

```text
Review can close, but P6 implementation remains closed.
```

The review does not approve P6 implementation, replay schema implementation,
fixture implementation, tests, data ingestion, parser, dataset reader, feature
extraction, label generation, real data access, model-output integration, CLI,
training, self-play, league, runner behavior or P7-P12 work.

## Evidence Grade

```text
P6 replay schema and synthetic fixture implementation proposal boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not evidence of:

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
