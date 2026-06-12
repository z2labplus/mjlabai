# 03N Minimal P7 Synthetic/Local Supervised Fixture And Feature-Label Smoke Proposal Review

## Scope

This document reviews
`docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md`.

This is a docs-only P7 proposal review gate. It does not implement P7, approve
P7 first-task execution, create fixtures, add tests, add production code, add
data files, approve source use, approve parser / dataset reader / ingestion,
approve feature extraction, approve label generation, train, tune, self-play,
run league, connect model outputs, read real Tenhou / real haifu / external
logs / platform data, add CLI / broad ingestion, or enter P8-P12.

North-star relationship: this review helps the long-term Tenhou stable dan
`> 10.68` target only by keeping future supervised-learning smoke work
auditable before implementation. It is not model-strength evidence, Tenhou
ranked evidence, stable-dan ranked-game evidence, LuckyJ `10.68` comparison or
candidate-promotion evidence.

## Reviewed Artifacts

Primary artifact:

- `docs/03_supervised_policy/03M_MINIMAL_P7_SYNTHETIC_LOCAL_SUPERVISED_FIXTURE_AND_FEATURE_LABEL_SMOKE_PROPOSAL_BEFORE_IMPLEMENTATION.md`

P7 context:

- `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/03_supervised_policy/03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW.md`
- `docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`
- `docs/03_supervised_policy/03I_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03J_P7_FEATURE_AND_LABEL_READINESS_BOUNDARY_REVIEW.md`
- `docs/03_supervised_policy/03K_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03L_P7_SUPERVISED_LEARNING_RISK_AND_EVIDENCE_TAXONOMY_REVIEW.md`

P6 / P5 context:

- `docs/02_data_system/02A_DATA_SOURCES.md`
- `docs/02_data_system/02B_REPLAY_SCHEMA.md`
- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/05_evaluation/05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md`
- `docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md`

Read-only implementation context:

- `src/mjlabai/data/replay_schema.py`
- `tests/fixtures/data/synthetic_replay_smoke.json`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

Governance context:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

## Scope Review

`03M` scope is correct for the current P7 gate.

It clearly states that the task is docs-only proposal definition before
implementation, and that it does not create a fixture, test, production
module, data file, parser, dataset reader, ingestion path, feature extractor,
label generator, training dataset, trainer, model-output path, CLI or model
artifact.

It also keeps P7 implementation, P7 first-task execution, training, source
ingestion, parser / dataset reader / ingestion, feature extraction, label
generation, model architecture / trainer / dataloader, real Tenhou, real
haifu, external logs, platform data and P8-P12 outside the current scope.

Review finding: no blocker.

## Minimal Future Implementation Candidate Review

`03M` limits any future implementation candidate to:

- one project-authored synthetic/local supervised fixture.
- one minimal feature / label schema or validation helper.
- one fixture schema smoke test.
- one feature / label boundary smoke test.
- direct docs / governance synchronization.

These are candidate classes only. They are not created, implemented or
approved by `03M` or this review.

Review finding: no blocker.

## Candidate Exact Files Review

`03M` names these exact future candidate paths:

- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`

The file list is narrow, synthetic/local-oriented and excludes parser,
dataset-reader, ingestion, training, model architecture, model-output and
real-data paths. `03M` explicitly says these paths are candidate paths only,
are not created, and require a later `10_NEXT` first-task approval before any
creation. Additional files require separate approval.

Review finding: no blocker.

## Candidate Synthetic / Local Fixture Boundary Review

`03M` defines a sufficient future fixture boundary. It requires the future
candidate fixture to be project-authored, synthetic/local, tiny,
deterministic, repo-local and explicitly marked as not Tenhou data, not real
haifu, not external logs, not platform data, not model output, not
human-labeled real play, not self-play or league output, not model-strength
evidence and not LuckyJ `10.68` comparison.

It also forbids real Tenhou logs, real haifu, external logs, platform data,
online accounts, sessions, cookies, tokens, scraped data, third-party binary
output, Akochan `system.exe` output, `libai.so` output, unknown model weights,
model outputs, self-play outputs, league outputs, unapproved human labels and
labels from an unapproved generator.

The proposal cross-links the boundary to `03G`, `03H`, `03I`, `03J`, `03K`
and `03L`, and explicitly says the future fixture must not be used as a
training dataset.

Review finding: no blocker.

## Candidate Feature / Label Smoke Boundary Review

`03M` limits future feature / label smoke checks to shape and guardrail
validation:

- field names.
- JSON-serializable primitive values.
- explicit schema version.
- public-information-only placeholders.
- explicit absence of hidden information.
- explicit absence of future information.
- source/provenance fields.
- warnings and non-evidence text.
- compatibility with the candidate synthetic fixture shape.

It forbids actual feature extraction, label generation, parsing, dataset
reading, ingestion, supervised dataset construction, training-schema approval,
model code, policy-quality evaluation, supervised accuracy, model-output
integration, real Tenhou, real haifu, external logs and platform data.

Review finding: no blocker.

## Candidate Validation Commands Review

`03M` correctly separates future implementation validation candidates from
current proposal validation.

Future implementation validation candidates:

```bash
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Current proposal / review validation:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Review finding: no blocker.

## Future Implementation Approval Conditions Review

`03M` includes sufficient future implementation approval conditions:

- proposal review must close with no blocker.
- `docs/10_next/10_NEXT.md` must explicitly name the exact implementation
  task as the first unchecked item.
- exact candidate files must be approved.
- additional files must be absent or separately approved.
- task remains synthetic/local only.
- no source approval, source ingestion, parser, reader, ingestion, feature
  extraction, label generation or training is introduced.
- no real Tenhou, real haifu, external logs, platform data, accounts,
  sessions, cookies or tokens are read.
- no third-party binaries, weights, params or artifacts are used or stored.
- no model-output integration, CLI or broad file ingestion is introduced.
- evidence grade and non-evidence warnings are preserved.
- validation commands, rollback, stop conditions and governance sync are
  explicit.
- Web ChatGPT review or equivalent human approval confirms the boundary.

Review finding: no blocker.

## Stop Conditions Review

`03M` stop conditions are sufficient. They stop the future task on unapproved
files, production behavior beyond approved candidate files, real data,
account/session/cookie/token handling, parser / reader / ingestion behavior,
feature extraction, label generation, supervised dataset construction,
model-output integration, CLI, training, tuning, checkpointing, self-play,
league, third-party artifacts, overclaiming, P8-P12 drift or validation
failure.

Review finding: no blocker.

## Proposal Risk Review

`03M` covers the required risks:

- proposal mistaken for implementation approval.
- fixture candidate mistaken as created fixture.
- synthetic fixture mistaken as training dataset.
- feature-label smoke mistaken as actual extraction or generation.
- real data accidentally introduced.
- parser / reader / ingestion creep.
- training creep.
- model-strength overclaim.
- P8/P10/P12 creep.
- unapproved file creep.

Each risk has a mitigation and remains visible for later approval decision
preparation.

Review finding: no blocker.

## Evidence Grade / Non-Evidence Review

`03M` uses the correct evidence grade:

```text
P7 minimal synthetic/local supervised fixture and feature-label smoke proposal evidence only.
```

It explicitly states that the proposal is not P7 implementation, P7 first-task
execution, fixture creation, test creation, production code, data-file
creation, source approval, training-data approval, parser, dataset reader,
ingestion, feature extraction, label generation, supervised dataset
construction, model-output integration, CLI, broad file ingestion, training,
tuning, checkpointing, model-artifact evidence, self-play, league, real Tenhou
ingestion, real haifu ingestion, external-log ingestion, platform-data
ingestion, model-strength evidence, Tenhou ranked evidence,
stable-dan ranked-game evidence, LuckyJ `10.68` comparison,
candidate-promotion evidence or P8-P12 entry approval.

Review finding: no blocker.

## Governance Synchronization Review

Governance documents are consistent with `03M`:

- P7 implementation remains unapproved.
- P7 first-task execution remains unapproved.
- candidate files are not created.
- fixture creation remains unapproved.
- tests creation remains unapproved.
- production code remains unapproved.
- training data source remains unapproved.
- source ingestion remains unapproved.
- parser / reader / ingestion remains unapproved.
- feature extraction remains unapproved.
- label generation remains unapproved.
- P8-P12 remains unapproved.
- no model-strength claim is recorded.
- no real-data approval is recorded.
- no training approval is recorded.

`docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`,
`docs/09_governance/09_STAGE_TASK_CONTRACT.md`,
`docs/10_next/10_NEXT.md`, `docs/00_HANDOFF.md`, the docs index, changelog,
evidence log, risk register, decision record, milestones and backlog now point
to the next docs-only approval-decision preparation task after this review.

Review finding: no blocker.

## Validation Results

Validation commands:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Result:

```text
pass
```

## Review Decision

```text
Review can close.
```

No blocker was found. `03M` is sufficiently narrow, conservative and auditable
for the current P7 minimal synthetic/local supervised fixture and feature-label
smoke proposal review gate.

## Next Task Recommendation

Recommended next task:

```text
Prepare approval decision for minimal P7 synthetic/local supervised fixture and feature-label smoke implementation task.
```

This next task must still be docs-only approval-decision preparation. It must
not implement P7, create fixtures, create tests, create production code, add
data files, approve P7 first-task execution, approve source use, approve
parser / dataset reader / ingestion, approve feature extraction, approve label
generation, train, tune, self-play, run league, connect model output, read
real Tenhou / real haifu / external logs / platform data, add CLI / broad
ingestion, make model-strength claims or enter P8-P12.

## Evidence Grade

```text
P7 minimal synthetic/local supervised fixture and feature-label smoke proposal review evidence only.
```

## Explicit Non-Evidence

This review is not:

- P7 implementation.
- P7 first-task execution.
- fixture creation.
- tests creation.
- production code.
- data file creation.
- P8-P12 entry approval.
- training.
- tuning.
- self-play.
- league.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- parser.
- dataset reader.
- data ingestion.
- feature extraction implementation.
- label generation implementation.
- source approval.
- training-data approval.
- model-output integration.
- CLI.
- broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
