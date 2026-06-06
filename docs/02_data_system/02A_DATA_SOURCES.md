# 02A_DATA_SOURCES

## Scope

This document defines the P6 data-source provenance and rights inventory before
any replay schema implementation, data ingestion, feature extraction, label
generation or training path.

It is a planning document only. It does not approve:

- replay schema code.
- dataset readers.
- feature extraction.
- label generation.
- data ingestion.
- real Tenhou, real haifu, external-log or platform-data access.
- account, session, cookie or token handling.
- platform automation, scraping, evasion or anti-detection tooling.
- model-output integration.
- CLI or broad file ingestion.
- third-party binary, `system.exe`, `libai.so`, `params/`, checkpoint or
  model-weight usage.
- training, tuning, self-play, league, runner behavior or P7-P12 entry.
- model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claims.

## Post-P5 / P6 Planning Context

P5 is closed for the current synthetic/local evaluation groundwork scope. The
post-P5 transition review allowed P6 data-system docs-only planning before any
implementation. `02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
defines P6 scope and states that P6 implementation remains closed.

This inventory is the next guardrail before replay schema implementation. It
exists because future replay, feature, label and data-quality work cannot be
lawful or reproducible unless the project first records each source's origin,
rights, allowed use, storage policy, approval status and evidence references.

This inventory supports the north-star target indirectly: trustworthy data
systems are required before later supervised learning, RL, evaluation and
LuckyJ validation can be meaningful. The inventory itself is not model-strength
evidence and is not a LuckyJ comparison.

Review status:

```text
docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md
records that this inventory review can close with no blocker, but P6
implementation, replay schema implementation and data ingestion remain closed.
```

Synthetic/local replay fixture boundary:

```text
docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md
defines the project-authored synthetic/local replay fixture boundary before
schema implementation. It does not approve fixture implementation, source
ingestion, replay schema implementation or any real/external/platform source.

docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md
reviews that boundary with no blocker and keeps fixture implementation, source
approval, source ingestion, replay schema implementation and real/external/
platform sources closed.

docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md
defines readiness criteria before any replay schema code, fixture creation,
parser, dataset reader, ingestion, feature extraction or label generation can
be considered. It does not change source approval policy and does not approve
any real/external/platform source.

docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md
reviews that checklist with no blocker. The review does not change source
approval policy and does not approve ingestion, replay schema implementation,
fixture implementation or any real/external/platform source.

docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md
defines the proposal boundary that any future replay schema or synthetic
fixture implementation proposal must satisfy before code. It does not change
source approval policy, does not approve ingestion and does not approve any
real/external/platform source.
```

## Inventory Field Schema

Every future data source must be represented with the fields below before it can
be considered for ingestion, training or evaluation.

| field | meaning | allowed values | required status |
|---|---|---|---|
| `source_id` | Stable identifier for the source. | ASCII id such as `project_synthetic_stable_dan_placements_smoke`. | Required. |
| `source_name` | Human-readable source name. | Non-empty text. | Required. |
| `source_category` | Source family. | `project_synthetic_fixture`, `repository_documentation`, `third_party_code_reference`, `real_tenhou_ranked_logs`, `real_haifu_or_external_logs`, `platform_or_account_data`, `model_selfplay_or_league_output`, `third_party_binary_or_weight`. | Required. |
| `source_origin` | Where the source comes from. | Project-authored, repository doc path, third-party repository name, platform name or local origin when lawful and non-sensitive. | Required. |
| `source_owner_or_rightsholder` | Owner, author or likely rightsholder. | Project, external project, platform, unknown. | Required. |
| `access_method` | How the source is accessed. | `repo_local_doc`, `repo_local_synthetic_fixture`, `methodology_reference_only`, `not_accessed`, `future_lawful_local_artifact`, `blocked`. | Required. |
| `current_repository_status` | Whether source content is in this repo. | `in_git_small_synthetic`, `in_git_docs`, `not_in_git`, `forbidden_in_git`, `unknown`. | Required. |
| `rights_status` | Rights state. | `project_authored`, `project_owned_docs`, `external_license_review_required`, `platform_terms_review_required`, `unknown`, `blocked`. | Required. |
| `license_or_terms_summary` | License or terms summary. | Short summary or `not reviewed`. | Required. |
| `allowed_use` | What the project may do now. | `docs_context_only`, `synthetic_smoke_context`, `methodology_reference_only`, `none_until_review`, `blocked`. | Required. |
| `forbidden_use` | Uses explicitly forbidden now. | Non-empty list or summary. | Required. |
| `redistribution_status` | Whether content can be redistributed. | `allowed_project_docs`, `allowed_small_synthetic_fixture`, `not_allowed`, `unknown`, `blocked`. | Required. |
| `raw_data_storage_policy` | Where raw data may live. | `small_synthetic_in_git`, `docs_in_git`, `not_stored`, `outside_git_after_review`, `blocked`. | Required. |
| `derived_data_storage_policy` | Where transformed data may live. | `not_applicable`, `small_synthetic_in_git`, `outside_git_after_review`, `blocked_until_review`. | Required. |
| `may_enter_git` | Whether raw or source content may be committed. | `yes_small_project_authored_only`, `docs_only`, `no`, `requires_review`. | Required. |
| `privacy_or_personal_data_notes` | Privacy and personal-data notes. | `none_expected_synthetic`, `docs_only`, `unknown`, `requires_review`, `blocked`. | Required. |
| `platform_account_involvement` | Whether accounts/sessions/tokens are involved. | `none`, `possible`, `yes`, `unknown`, `blocked`. | Required. |
| `platform_terms_risk` | Platform terms risk. | `none_expected`, `requires_review`, `high`, `unknown`, `blocked`. | Required. |
| `automation_or_scraping_risk` | Automation/scraping/evasion risk. | `none_expected`, `requires_review`, `high`, `blocked`. | Required. |
| `ruleset_or_room_context` | Mahjong ruleset/room if applicable. | `phoenix`, `tenhou_four_player`, `synthetic`, `not_applicable`, documented ruleset. | Required when relevant. |
| `expected_schema_family` | Future schema family. | `placement_records`, `legal_action_fixture`, `tiny_benchmark_fixture`, `replay_record_future`, `documentation`, `reference_only`, `blocked`. | Required. |
| `approved_for_planning` | Can be used in docs/planning now. | `yes`, `restricted`, `no`. | Required. |
| `approved_for_ingestion` | Can be ingested by code now. | `yes`, `no`. | Required. |
| `approved_for_training` | Can be used for training now. | `yes`, `no`. | Required. |
| `approved_for_evaluation` | Can be used for evaluation now. | `synthetic_smoke_only`, `docs_context_only`, `no`, `future_review_required`. | Required. |
| `approval_status` | Current approval state. | See approval vocabulary below. | Required. |
| `required_before_ingestion` | Missing prerequisites before ingestion. | Checklist references or `not applicable`. | Required. |
| `evidence_log_reference` | Evidence log reference. | Existing or required future entry id. | Required before ingestion. |
| `risk_register_reference` | Risk register reference. | Existing or required future entry id. | Required before ingestion. |
| `reviewer_or_approval_owner` | Human or governance owner. | `project governance`, named reviewer, `not assigned`. | Required before approval. |
| `notes` | Limitations and non-evidence warnings. | Non-empty text. | Required. |

## Approval Status Vocabulary

Use only the statuses below unless a later governance decision extends the
vocabulary:

- `allowed_for_docs_context`: may be referenced in documentation, but not
  ingested.
- `project_authored_synthetic_fixture`: small project-authored synthetic/local
  fixture already in Git or allowed to remain in Git.
- `unapproved`: no current ingestion/training/evaluation approval.
- `blocked_rights_unknown`: rights or ownership are unknown.
- `blocked_platform_terms`: platform terms risk blocks use.
- `blocked_privacy_unknown`: privacy or personal-data status is unknown.
- `blocked_no_storage_policy`: raw/derived storage policy is missing.
- `blocked_no_evidence_log`: evidence log entry is missing.
- `deferred_later_stage`: not relevant to current P6 planning or belongs to a
  later stage.
- `requires_human_review`: human review needed before any implementation.
- `requires_legal_or_terms_review`: license, rights or platform terms review
  needed.
- `requires_source_specific_task`: needs its own `10_NEXT` task before use.
- `approved_for_future_ingestion_after_review`: can only appear after a later
  source-specific review approves ingestion.

Any real, external, platform-derived or account-related source defaults to
`unapproved`, `blocked_rights_unknown`, `blocked_platform_terms`,
`blocked_privacy_unknown` or `requires_source_specific_task` until a later
source-specific review approves it.

## Source Category Inventory

| source category | examples | current approval | rights / provenance | storage policy | evidence status | notes |
|---|---|---|---|---|---|---|
| Project-authored synthetic/local fixtures | `tests/fixtures/eval/stable_dan_placements_smoke.json`, `tests/fixtures/eval/legal_action_metric_smoke.json`, `tests/fixtures/eval/tiny_benchmark_harness_smoke.json` | Planning: yes. Ingestion: no, except existing repo-local read-only docs/test context. Training: no. Evaluation: current synthetic/local smoke/review context only. | `project_authored`; no external source. | Small synthetic fixtures may remain in Git. No raw real data. | Existing P5/P6 docs and tests. | Not Tenhou data, not real haifu, not model output, not strength evidence. |
| Repository documentation | `docs/**`, P5 closure docs, P6 scope docs | Planning: yes. Ingestion: no. Training: no. Evaluation: docs context only. | Project-owned repository documentation. | Docs in Git. | Existing governance docs. | Planning evidence only; not model-strength evidence. |
| Third-party open-source code references | Mortal, Akochan source/build workflow references, Suphx/Kanachan methodology references | Planning: yes as methodology/interface reference only. Ingestion/training/evaluation: no unless separately scoped. | External licenses or papers; preserve restrictions. | Do not commit third-party source, binaries, `params/` or build artifacts unless a later task explicitly approves. | Existing F1/F2 evidence log for audited references. | Reference-only; not data-source approval. |
| Real Tenhou / ranked logs | Tenhou ranked game logs, account-linked results | Planning: no, except restricted future source-risk discussion. Ingestion/training/evaluation: no. | Rights unapproved; platform/account risk possible. | Do not access, scrape, download, store or commit. | No approved evidence. | Blocked until legal/terms/privacy/source-specific review. |
| Real haifu / external logs | Public or private replay logs from outside the project | Planning: restricted. Ingestion/training/evaluation: no. | Rights unknown unless reviewed. | Do not read, ingest, store or commit before approval. | No approved evidence. | Requires source-specific task and rights review. |
| Platform data / online account data | Account/session/cookie/token data, online platform observations | Planning: no, except risk boundary docs. Ingestion/training/evaluation: no. | Unapproved; privacy/platform terms risk high. | Do not access, store or commit. | No approved evidence. | No account tooling, scraping, evasion or automation. |
| Model outputs / self-play / league outputs | Future model output logs, self-play games, league result logs | Planning: deferred later stage. Ingestion/training/evaluation: no for current P6 planning. | Later-stage outputs need separate provenance and stage approval. | Do not store or use as P6 source now. | No current source approval. | Not a current P6 planning source. |
| Third-party binaries / model weights / params / checkpoints | Akochan `system.exe`, `libai.so`, `params/`, `*.pth`, `*.pt`, checkpoints, snapshots | Planning: risk reference only. Ingestion/training/evaluation: no. | External/unknown provenance unless separately audited. | Do not download, use, vendor, copy or commit unknown artifacts. | Existing wrapper evidence is fixed-sample interface evidence only. | Forbidden as data sources and forbidden in Git. |

## Required Before Ingestion Checklist

No source may enter replay schema implementation, ingestion, training or
evaluation unless every applicable item below is complete:

1. `source_id` assigned.
2. source origin documented.
3. rightsholder documented.
4. license / terms summarized.
5. allowed use documented.
6. forbidden use documented.
7. redistribution status documented.
8. raw-data storage policy documented.
9. derived-data storage policy documented.
10. Git inclusion policy documented.
11. privacy / personal data review completed.
12. platform terms risk reviewed.
13. automation / scraping risk reviewed.
14. evidence log entry created.
15. risk register entry created.
16. checksum / version policy defined.
17. schema family selected.
18. validation command planned.
19. human approval recorded.
20. `docs/10_next/10_NEXT.md` has an explicit implementation task.
21. P6 implementation approval exists.

If any item is missing, the source must not be ingested, used for training, used
for evaluation or consumed by replay schema implementation.

## Evidence Requirements For Future Sources

Any later approved source must add an evidence log entry with:

- source name.
- source id.
- source type.
- date checked.
- source URL or local origin when lawful and non-sensitive.
- license / terms evidence.
- allowed-use summary.
- forbidden-use summary.
- raw storage policy.
- derived storage policy.
- `may_enter_git` value.
- checksum or content-hash policy.
- schema version.
- transform version.
- sample count if later approved.
- validation command if later approved.
- reviewer.
- approval date.
- risk notes.
- known exclusions.
- explicit non-evidence warning.

Evidence for P6 source review is not model-strength evidence, Tenhou ranked
evidence, stable-dan ranked-game evidence, LuckyJ `10.68` comparison evidence
or candidate-promotion evidence.

## Rights / Provenance Risk Review

| risk | mitigation | blocker status | owner doc or follow-up | notes |
|---|---|---|---|---|
| Rights ambiguity | Require owner/rightsholder, license/terms summary and allowed/forbidden use before ingestion. | Blocks ingestion. | `02A`, evidence log, future source task. | Defaults to unapproved. |
| Platform terms ambiguity | Require terms review before platform-derived data access. | Blocks real/platform source use. | `09_RISK_REGISTER`, future compliance review. | No Tenhou/platform access now. |
| Accidental real-data ingestion | Keep current task docs-only and require explicit `10_NEXT` implementation approval. | Blocks implementation. | `10_NEXT`, stage contract. | No reader or ingestion code in this task. |
| Private/personal data exposure | Require privacy review and no account/session/token data. | Blocks platform/account sources. | `09_RISK_REGISTER`. | No cookies, tokens or online accounts. |
| Account/session/cookie/token leakage | Forbid account tooling and secret storage. | Blocks account data use. | stage contract, compliance docs. | No platform automation. |
| Scraping/automation/evasion risk | Forbid scraping, automation, evasion and anti-detection tooling. | Blocks platform access. | `AGENTS.md`, stage contract. | No connector implementation. |
| Raw data committed to Git | Require Git inclusion policy and keep raw real data out of Git. | Blocks storage. | `02A`, future storage policy. | Only small project-authored synthetic fixtures may remain. |
| Third-party artifacts committed to Git | Forbid third-party source, binaries, params and build artifacts without explicit approval. | Blocks artifact storage. | risk register, stage contract. | Includes `system.exe`, `libai.so`, `params/`. |
| Model weights committed or used without provenance | Forbid unknown `*.pth`, `*.pt`, checkpoints and snapshots. | Blocks weight use. | risk register. | No weights used in P6 planning. |
| Source contamination / train-test leakage | Require source ids, schema families, transforms and split policy before implementation. | Blocks future training/evaluation. | future P6 data-quality task. | No train/test split exists yet. |
| Synthetic fixture overclaiming | Label synthetic fixtures as smoke/review context only. | Blocks strength claims. | evidence log, ranking protocol. | Not Tenhou or real haifu. |
| Stage creep into P7-P12 | Keep next task docs-only and forbid training/self-play/league. | Blocks later-stage work. | `10_NEXT`, stage contract. | P7-P12 not open. |
| Treating P6 source inventory as ingestion approval | State inventory definition and review are not approval. | Blocks ingestion. | `02A`, `02D`, `10_NEXT`. | Replay schema boundary definition required next. |
| Treating P6 source inventory as model-strength evidence | Explicit non-evidence warnings in all governance docs. | Blocks claims. | evidence log, handoff. | No LuckyJ claim. |

## Replay Schema Implementation Boundary

Source inventory must be reviewed before replay schema implementation.

This task does not implement replay schema code. A replay schema implementation
task cannot consume any unapproved source. A later implementation task requires:

- reviewed source inventory.
- explicit P6 implementation entry criteria.
- source-specific approval for any non-synthetic input.
- storage and Git policy.
- evidence log and risk register entries.
- a `docs/10_next/10_NEXT.md` first task naming the exact implementation.

Because no blocker was found in `02D`, the follow-up chain defined and reviewed
the replay schema documentation boundary in `02B` / `02E`, then defined and
reviewed the synthetic/local replay fixture boundary in `02F` / `02G`, then
defined and reviewed the readiness checklist in `02H` / `02I`, and `02J`
defines the proposal boundary before code. `02K` reviews that proposal
boundary with no blocker. `02L` prepares a docs-only minimal replay schema
and synthetic fixture implementation proposal for review before code. `02M`
reviews that proposal with no blocker and records that review can close while
implementation remains closed. These reviews, checklists, boundaries and the
proposal do not approve source ingestion, replay schema implementation,
fixture implementation or tests.

## Planning Decision

```text
P6 data-source provenance and rights inventory has been reviewed before replay
schema implementation. No blocker was found. P6 implementation, replay schema
implementation and data ingestion are still not approved.
```

## Next Task Recommendation

```text
Prepare approval decision for minimal P6 replay schema and synthetic fixture implementation task.
```

That task should be a docs-only approval-decision gate. It must not implement
replay schema code, fixtures, tests, data ingestion, dataset readers, parsers,
feature extraction, label generation, model-output integration, CLI, broad file
ingestion, real Tenhou, real haifu, external-log ingestion, platform-data
ingestion, training, self-play, league, runner behavior, P7-P12 or
model-strength claims.

## Evidence Grade

```text
P6 data-source provenance and rights inventory definition evidence only.
```

## Explicit Non-Evidence

This inventory is not:

- P6 implementation approval.
- replay schema implementation.
- data ingestion.
- feature extraction.
- label generation.
- dataset-reader implementation.
- real Tenhou, real haifu, external-log or platform-data access.
- training, tuning, self-play, league or runner behavior.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- P7-P12 entry approval.
