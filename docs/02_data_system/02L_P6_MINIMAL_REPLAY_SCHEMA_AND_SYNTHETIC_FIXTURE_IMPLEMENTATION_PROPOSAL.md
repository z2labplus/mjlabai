# 02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL

## Scope

This document prepares a P6 minimal replay schema and synthetic fixture
implementation proposal for review before code.

It is a docs-only proposal draft. It does not:

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
- call OpenAI, LLM or model APIs.
- call Akochan `system.exe`, `libai.so` or any third-party binary.
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

North-star relationship:

```text
A minimal replay schema and synthetic fixture can eventually support the
long-term stable-dan > 10.68 target only by making future data-system work
lawful, deterministic, auditable and testable before training or evaluation.
This proposal draft is not implementation approval and is not strength
evidence.
```

## Prior Boundary Context

This proposal draft depends on the current P6 planning chain:

- `docs/02_data_system/02A_DATA_SOURCES.md` defines the data-source
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
- `docs/02_data_system/02J_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY.md`
  defines the implementation proposal boundary before code.
- `docs/02_data_system/02K_P6_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_BOUNDARY_REVIEW.md`
  reviews that proposal boundary with no blocker.

The documents above are prerequisites for this proposal draft. They do not
approve P6 implementation, replay schema code, fixture creation, tests, data
ingestion, parser / dataset-reader work, feature extraction, label generation
or P7-P12 work.

## Proposal Purpose

The purpose of this proposal is to name the smallest future implementation
candidate that could be reviewed next, while keeping code closed now.

The proposed future implementation, if later approved by human / Web ChatGPT
review and an explicit first `10_NEXT` task, would create only:

- one minimal replay schema module.
- one project-authored synthetic/local replay fixture.
- one or two minimal schema / fixture validation tests.
- synchronized docs, evidence and risk entries.

This proposal does not create those artifacts. It only prepares them for
review.

## Target Stage

```text
P6 data system / docs-only proposal drafting
```

P6 exists to make future replay, feature, label and data-quality work lawful,
reproducible and auditable before P7 supervised learning, P8 reinforcement
learning, P9 search, P10 league, P11 large-scale training or P12 Tenhou target
validation.

## Candidate Implementation Classes

| candidate | proposal_status | implementation_allowed_now | future_allowed_if_later_approved | explicitly_excluded |
|---|---|---:|---|---|
| A. minimal replay schema code | prepared_for_review_before_code | no | static schema representation and validation helper for project-authored synthetic/local fixture only | parser, dataset reader, ingestion, feature extraction, label generation, model output, CLI |
| B. project-authored synthetic/local replay fixture | prepared_for_review_before_code | no | one tiny deterministic repo-local synthetic fixture | real Tenhou, real haifu, external logs, platform data, real player/account identifiers |
| C. minimal schema validation test | prepared_for_review_before_code | no | one unit test for static schema validation behavior | broad data reads, real data, parser validation, feature/label tests |
| D. minimal fixture validation test | prepared_for_review_before_code | no | one unit test for fixture JSON shape and synthetic-only guardrails | ingestion, real-data fixture checks, model-output checks |
| E. evidence / risk / docs synchronization | prepared_for_review_before_code | no | evidence log, risk register, changelog, handoff, docs index and `10_NEXT` updates | model-strength claims, source approval, P7-P12 entry |

Excluded classes remain excluded from the future minimal implementation:

- parser.
- dataset reader.
- data ingestion.
- feature extraction.
- label generation.
- real / external / platform source integration.
- CLI or broad file ingestion.
- model-output integration.
- training, tuning, self-play, league or runner behavior.
- P7-P12 work.

## Proposed File Candidates

These paths are candidates only. They must not be created until a later review
explicitly approves implementation.

| candidate_path | purpose | allowed_future_content | forbidden_future_content | implementation_allowed_now | required_before_creation | rollback_or_removal_condition | notes |
|---|---|---|---|---:|---|---|---|
| `src/mjlabai/data/replay_schema.py` | Minimal static replay schema representation and synthetic-only validation helper. | schema version constant, small immutable / standard-library-only schema objects, JSON-safe `to_dict`, synthetic fixture validation helper. | parser, dataset reader, ingestion, feature extraction, label generation, real data reads, CLI, model-output integration. | no | Web ChatGPT / human review plus explicit first `10_NEXT` implementation task. | Remove if it reads files broadly, parses real logs, accepts unapproved sources or implies feature/label generation. | Future code must use only Python standard library. |
| `tests/fixtures/data/synthetic_replay_smoke.json` | One tiny project-authored synthetic/local replay fixture. | deterministic fake replay record with source/provenance guardrails and explicit non-evidence warnings. | real Tenhou, real haifu, external logs, platform data, real player/account identifiers, model output, training labels. | no | Explicit fixture implementation approval and no-real-data checklist. | Remove if any field can be traced to real gameplay, platform data, private data or model output. | Fixture must be small and repo-local only. |
| `tests/data/test_replay_schema.py` | Minimal schema validation unit test. | validation of schema version, required fields, JSON-safe serialization and synthetic-only guardrails. | parser tests, ingestion tests, feature tests, label tests, model-output tests, real-data tests. | no | Schema implementation approval and exact test boundary in `10_NEXT`. | Remove if it broadens into parser / reader / ingestion behavior. | Future command candidate only. |
| `tests/data/test_synthetic_replay_fixture_schema.py` | Minimal fixture shape unit test. | validation of fixture source note, provenance, no-real-data guardrails and required top-level fields. | real-source fixture validation, external-log reads, broad file ingestion, model-output assertions. | no | Fixture implementation approval and exact test boundary in `10_NEXT`. | Remove if it reads any path except the approved synthetic fixture. | Future command candidate only. |

## Minimal Replay Schema Code Candidate Boundary

Future code, if later approved, may define only a minimal schema concept for a
project-authored synthetic/local replay fixture.

Candidate concepts:

- schema version constant, for example `replay_schema_v0.1`.
- top-level replay record concept.
- source / provenance reference concept.
- synthetic/local guard concept.
- validation helper for in-memory mappings or the single approved synthetic
  fixture.
- JSON-safe serialization helper.
- explicit non-evidence warnings.

Future code must not define:

- parser for real Tenhou, real haifu, external logs or platform data.
- dataset reader.
- ingestion pipeline.
- raw real-data storage.
- feature extraction.
- label generation.
- model-output path.
- CLI or broad file ingestion.
- P7-P12 stage behavior.

If approved later, code must stay limited to static schema representation and
validation for the project-authored synthetic/local fixture only.

## Minimal Synthetic/Local Fixture Candidate Boundary

Future fixture work, if later approved, may create one small
project-authored synthetic/local fixture at:

```text
tests/fixtures/data/synthetic_replay_smoke.json
```

Candidate fixture properties:

- project-authored synthetic `source_id`.
- top-level fixture shape with `schema_version`, `fixture_id`,
  `source_note`, `warnings`, `source_provenance`, `records` and
  `evidence_refs`.
- one tiny deterministic replay record candidate.
- field-family coverage aligned with `02B`: replay identity, provenance,
  ruleset / room context, participant placeholders, event sequence stub,
  action context stub, terminal result stub and validation metadata.
- explicit warnings that the fixture is synthetic/local only, not Tenhou
  data, not real haifu, not external log, not platform data, not model output,
  not training data, not model-strength evidence and not LuckyJ `10.68`
  comparison.

Future fixture work must not include:

- real gameplay log content.
- real player, account, session, cookie, token or private-log identifiers.
- platform data.
- external log lines.
- model output.
- labels from real data.
- supervised-learning examples.
- training-use semantics.
- strength-evaluation semantics.

Future fixture work must include evidence-log and risk-register references if
implementation is approved later.

## Minimal Validation Test Candidate Boundary

Future tests, if later approved, may include only schema / fixture smoke
validation.

Candidate schema validation checks:

- schema version is present and expected.
- required top-level record fields exist.
- validation helper rejects missing required fields.
- serialization is JSON-safe.
- no parser, ingestion or feature/label behavior is exposed.

Candidate fixture validation checks:

- fixture is project-authored synthetic/local only.
- fixture has no real Tenhou, real haifu, external-log or platform-data
  claims.
- fixture has no account, session, cookie, token or private-log identifiers.
- fixture has no model output.
- fixture is not training data and not strength evidence.
- source/provenance references are present.
- required top-level fields are present.
- fixture is deterministic and tiny.

Candidate JSON round-trip checks may be considered only for the approved
synthetic fixture. They must not become broad file ingestion.

No tests are created by this proposal.

## Allowed Future Minimal Implementation Scope If Later Approved

A later implementation task may be considered only if review explicitly
approves it as the first unchecked `10_NEXT` task. If approved, the minimal
scope is:

- one minimal replay schema module.
- one project-authored synthetic/local fixture.
- one or two minimal schema / fixture smoke tests.
- docs, evidence, risk, handoff, docs index and `10_NEXT` synchronization.

The future implementation must still exclude:

- parser / reader / ingestion.
- real / external / platform source use.
- feature extraction.
- label generation.
- model-output integration.
- CLI or broad file ingestion.
- latency measurement, fixed-position exact-match, metric implementation,
  registry code changes or promotion criteria changes.
- training, tuning, self-play, league or runner behavior.
- P7-P12 entry.

## Forbidden Future Expansion

The future minimal implementation must stop if it requires or introduces:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- accounts, sessions, cookies, tokens or private logs.
- platform automation, scraping, evasion or anti-detection tooling.
- parser for real logs.
- dataset reader.
- ingestion pipeline.
- feature extraction.
- label generation.
- model-output integration.
- CLI or broad file ingestion.
- training, tuning, self-play, league or runner behavior.
- P7-P12 work.
- metric implementation, registry code changes or promotion criteria changes.
- OpenAI / LLM / model API calls.
- Akochan `system.exe`, `libai.so`, `params/` or third-party binaries.
- third-party source, binary artifacts, model weights, checkpoints or
  snapshots.
- model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claims.

## Future Validation Command Candidates

Future implementation may propose these commands after the files exist:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

These are future command candidates only. The test files do not exist unless a
later implementation task creates them. This proposal does not create or run
those future tests.

## Evidence / Risk / Docs Update Plan

If a later implementation is approved, it must update:

- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`, if a decision is made.
- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Evidence grade for any later minimal implementation must remain synthetic/local
data-system smoke evidence only unless a separate approved review changes it.

## Rollback Plan

If a later implementation is approved, rollback must remove or revert:

- the replay schema module if it expands into parser, reader, ingestion,
  feature extraction, label generation, model-output integration, CLI or real
  data access.
- the fixture if it contains real Tenhou, real haifu, external-log,
  platform-data, account/private identifier or model-output content.
- tests if they imply ingestion, parser, feature, label, training or model
  strength.
- docs if they overclaim implementation approval, source approval or strength
  evidence.

The task must stop if:

- forbidden sources or artifacts are introduced.
- validation fails.
- git status contains unapproved files.
- human / Web ChatGPT approval is missing.

## Stop Conditions

Stop before implementation if any of the following appear:

- real Tenhou, real haifu, external log or platform data.
- account, session, cookie, token or private-log data.
- parser, ingestion pipeline or dataset reader.
- feature extraction or label generation.
- model-output integration.
- CLI or broad file ingestion.
- third-party binary, source, params, weights, checkpoint or snapshot.
- OpenAI / LLM / model API call.
- tests or docs implying model strength, Tenhou evidence, stable-dan ranked
  evidence, LuckyJ `10.68` comparison or candidate promotion.
- documentation claims P6 implementation is approved without later review.
- P7-P12 is treated as current execution.

## Human / Web ChatGPT Approval Requirement

This proposal must be reviewed by human / Web ChatGPT before code.

Codex must not implement the replay schema module, synthetic fixture or tests
until:

- the review explicitly approves implementation.
- `docs/10_next/10_NEXT.md` makes implementation the first unchecked task.
- the prompt lists exact allowed files.
- the prompt repeats forbidden expansions.
- the prompt confirms P7-P12 remain closed.

## P7-P12 Non-Entry Boundary

This proposal does not approve:

- P7 supervised learning.
- P8 reinforcement learning.
- P9 search / risk model.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou target validation.
- training, tuning, self-play, league or runner behavior.
- model-output integration.
- real Tenhou / real haifu / external-log / platform-data access.
- model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claims.

## Planning Decision

```text
P6 minimal replay schema and synthetic fixture implementation proposal is
prepared for review before code. It does not approve replay schema
implementation, fixture implementation, tests, parser, dataset reader, data
ingestion, feature extraction or label generation.
```

## Review Status

`docs/02_data_system/02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW.md`
reviews this proposal before code.

Review decision:

```text
Review can close, but P6 implementation remains closed.
```

The review found no blocker and records that the proposal is sufficiently
bounded for a later approval-decision task. It does not approve replay schema
implementation, fixture implementation, tests, parser, dataset reader, data
ingestion, feature extraction or label generation.

## Next Task Recommendation

```text
Prepare approval decision for minimal P6 replay schema and synthetic fixture implementation task.
```

That next task must be a docs-only approval-decision gate. It must not
implement replay schema code, fixture files, tests, parser, dataset reader,
data ingestion, feature extraction, label generation, real-data access,
model-output integration, CLI, training, self-play, league, runner behavior or
P7-P12.

## Evidence Grade

```text
P6 minimal replay schema and synthetic fixture implementation proposal drafting evidence only.
```

## Explicit Non-Evidence

This proposal is not evidence of:

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
