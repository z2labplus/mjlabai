# 02M_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL_REVIEW

## Scope

This document reviews:

```text
docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md
```

It is a docs-only P6 minimal implementation proposal review gate before code.
It does not:

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
- call OpenAI, LLM or model APIs.
- call Akochan `system.exe`, `libai.so` or any third-party binary.
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

North-star relationship:

```text
This review supports the long-term stable-dan > 10.68 target only by checking
whether the proposed minimal P6 schema / fixture implementation remains lawful,
synthetic/local, auditable and small enough to consider in a later approval
decision. It is not implementation approval and is not strength evidence.
```

## Reviewed Artifacts

Primary review target:

- `docs/02_data_system/02L_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_PROPOSAL.md`

P6 planning chain:

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

## Proposal Scope Review

`02L` correctly limits itself to a proposal draft before code. It names a
minimal future candidate, but it repeatedly states that implementation is not
approved.

| scope question | finding | blocker | notes |
|---|---:|---:|---|
| Is `02L` docs-only? | yes | no | It is proposal-drafting evidence only. |
| Does `02L` avoid approving P6 implementation? | yes | no | Scope and planning decision keep implementation closed. |
| Does `02L` avoid approving replay schema implementation? | yes | no | It describes candidate code only. |
| Does `02L` avoid approving fixture implementation? | yes | no | It describes a candidate fixture only. |
| Does `02L` avoid approving tests? | yes | no | It describes future validation candidates only. |
| Does `02L` avoid approving ingestion, parser or dataset-reader work? | yes | no | Those classes are explicitly excluded. |
| Does `02L` avoid approving feature extraction and label generation? | yes | no | Both remain excluded / deferred. |
| Does `02L` avoid real Tenhou, real haifu, external logs and platform data? | yes | no | The proposal limits future work to project-authored synthetic/local content. |
| Does `02L` avoid model-output integration, CLI, training, self-play, league, runner behavior and P7-P12? | yes | no | These remain forbidden. |

Review finding:

```text
02L scope is correct.
```

## Candidate Implementation Classes Review

| candidate | covered_in_02L | current_status | implementation_allowed_now | review_finding |
|---|---:|---|---:|---|
| minimal replay schema code | yes | prepared_for_review_before_code | no | candidate only; no dataclass, pydantic model or JSON schema is approved. |
| project-authored synthetic/local replay fixture | yes | prepared_for_review_before_code | no | candidate only; no fixture file is approved. |
| minimal schema validation test | yes | prepared_for_review_before_code | no | candidate only; no test is approved. |
| minimal fixture validation test | yes | prepared_for_review_before_code | no | candidate only; no test is approved. |
| evidence / risk / docs synchronization | yes | prepared_for_review_before_code | no | necessary future synchronization plan; not implementation. |
| parser / dataset reader | yes | excluded | no | sufficiently excluded. |
| feature extraction / label generation | yes | excluded | no | sufficiently excluded. |
| data ingestion | yes | excluded | no | sufficiently excluded. |
| real / external / platform source integration | yes | excluded | no | sufficiently excluded. |
| CLI / broad file ingestion | yes | excluded | no | sufficiently excluded. |
| model-output integration | yes | excluded | no | sufficiently excluded. |
| training / self-play / league / P7-P12 | yes | excluded | no | sufficiently excluded. |

Review finding:

```text
Candidate implementation classes are sufficient and conservative.
No candidate is approved for implementation.
```

## Proposed File Candidates Review

`02L` names exact candidate paths:

- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

Each path has allowed future content, forbidden future content,
`implementation_allowed_now = no`, required-before-creation conditions and
rollback / removal conditions.

Review finding:

```text
Proposed file candidates are clear enough for a later approval decision.
They remain candidate paths only. No file creation is approved by this review.
```

## Minimal Replay Schema Code Candidate Boundary Review

`02L` permits only future static schema representation and validation concepts
for a project-authored synthetic/local replay fixture if a later task approves
implementation. It forbids:

- real Tenhou, real haifu, external-log or platform-data parsers.
- dataset readers.
- ingestion pipelines.
- raw real-data storage.
- feature extraction.
- label generation.
- model-output paths.
- CLI or broad file ingestion.
- P7-P12 behavior.

Review finding:

```text
Minimal replay schema code candidate boundary is narrow enough for a later
approval decision. It does not implement code and does not approve code now.
```

## Minimal Synthetic / Local Fixture Candidate Boundary Review

`02L` proposes one future fixture candidate:

```text
tests/fixtures/data/synthetic_replay_smoke.json
```

The candidate fixture must be project-authored, synthetic/local, tiny,
deterministic and explicit that it is not Tenhou data, real haifu, external
log, platform data, model output, training data, strength evidence or LuckyJ
comparison evidence.

It must not contain:

- real gameplay logs.
- real player, account, session, cookie, token or private-log identifiers.
- platform data.
- external log lines.
- model output.
- labels from real data.
- supervised-learning examples.
- training-use semantics.
- strength-evaluation semantics.

Review finding:

```text
Minimal synthetic/local fixture candidate boundary is conservative enough for
a later approval decision. It does not create or approve a fixture now.
```

## Minimal Validation Test Candidate Boundary Review

`02L` proposes only schema / fixture smoke validation candidates. Future tests,
if later approved, may validate schema version, required fields, JSON-safe
serialization, synthetic-only guardrails and fixture provenance. They must not
become parser tests, ingestion tests, feature tests, label tests, model-output
tests or real-data tests.

Review finding:

```text
Minimal validation test candidate boundary is sufficient. No tests are created
or approved by this review.
```

## Allowed Future Minimal Scope Review

If a later approval decision explicitly permits implementation as the first
`10_NEXT` task, the future minimal scope may include only:

- one minimal replay schema module.
- one project-authored synthetic/local fixture.
- one or two minimal schema / fixture smoke tests.
- docs, evidence, risk, handoff, docs index and `10_NEXT` synchronization.

Review finding:

```text
Allowed future minimal scope is narrow and suitable for an approval-decision
task. It is not active implementation permission.
```

## Forbidden Future Expansion Review

`02L` explicitly stops future implementation if it requires or introduces:

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

Review finding:

```text
Forbidden future expansion list is sufficiently strict.
```

## Future Validation Command Review

`02L` lists these future command candidates:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

The last two commands are future candidates only. The referenced test files do
not exist unless a later approved implementation task creates them.

Review finding:

```text
Future validation commands are correctly marked as candidates. This review
runs only documentation validation such as git diff --check.
```

## Evidence / Risk / Docs Update Plan Review

`02L` requires any later implementation to update:

- evidence log.
- risk register.
- changelog.
- decision record, if a decision is made.
- handoff.
- docs index.
- `10_NEXT`.
- technical plan.

Review finding:

```text
Evidence, risk and docs synchronization plan is sufficient for a later
approval decision and eventual implementation task.
```

## Rollback Plan Review

`02L` requires rollback if future implementation expands into parser, reader,
ingestion, feature extraction, label generation, model-output integration, CLI
or real data access; if the fixture contains real / external / platform /
private / model-output content; if tests imply ingestion, parser, features,
labels, training or model strength; or if docs overclaim implementation,
source approval or strength evidence.

Review finding:

```text
Rollback plan is sufficient.
```

## Stop Conditions Review

`02L` requires stopping before implementation if forbidden sources, account
data, parser / ingestion / dataset-reader work, feature extraction, label
generation, model-output integration, broad ingestion, third-party artifacts,
model API calls, overclaiming, missing approval or P7-P12 drift appear.

Review finding:

```text
Stop conditions are sufficient.
```

## Human / Web ChatGPT Approval Requirement Review

`02L` explicitly requires human / Web ChatGPT review before code. It also
requires a later explicit first `10_NEXT` implementation task with exact
allowed files and forbidden expansions before Codex may implement the replay
schema module, synthetic fixture or tests.

Review finding:

```text
Human / Web ChatGPT approval requirement is clear.
Implementation is not approved by this review.
```

## P7-P12 Non-Entry Boundary Review

`02L` keeps P7-P12 closed. It does not approve supervised learning, RL,
search/risk model, model league, large-scale training, Tenhou target
validation, model-output integration, real data, training, self-play, league
or runner behavior.

Review finding:

```text
P7-P12 non-entry boundary is sufficient.
```

## Governance Synchronization Review

This review requires synchronized updates to:

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

Review finding:

```text
Governance synchronization is required and sufficient.
```

## Review Decision

```text
Review can close; P6 implementation remained closed until the later 02N
approval decision.
```

No blocker was found in the `02L` proposal. The proposal is sufficiently
bounded for a later approval-decision task. This review does not approve that
implementation task and does not create any implementation artifact.

Closed after this review:

- P6 minimal replay schema and synthetic fixture implementation proposal review.

Still closed after this review:

- P6 implementation.
- replay schema implementation.
- replay fixture implementation.
- test implementation.
- data ingestion.
- dataset readers.
- parsers.
- feature extraction.
- label generation.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- model-output integration.
- CLI or broad file ingestion.
- metric implementation.
- registry code changes.
- promotion criteria changes.
- training, tuning, self-play, league and runner behavior.
- P7-P12.

## Next Task Recommendation

The next task should be:

```text
Implement minimal P6 replay schema and project-authored synthetic fixture only.
```

`docs/02_data_system/02N_P6_MINIMAL_REPLAY_SCHEMA_AND_SYNTHETIC_FIXTURE_IMPLEMENTATION_APPROVAL_DECISION.md`
records that the approval-decision gate is complete and that the next task is
approved only for the exact minimal implementation scope.

The next task must stay limited to the exact allowed files, exact allowed
scope, forbidden expansions, validation commands and stop conditions in
`02N`. It must not add parser, dataset reader, ingestion, feature extraction,
label generation, CLI, model-output integration, real data access, training,
self-play, league, runner behavior or P7-P12 work.

## Evidence Grade

```text
P6 minimal replay schema and synthetic fixture implementation proposal review evidence only.
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
- CLI or broad file ingestion.
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
