# 03F_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK_REVIEW

## Scope

This document reviews `03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` before
any P7 implementation.

This is a docs-only P7 review gate. It does not implement P7, execute the first
P7 task, approve training, approve data ingestion, approve parser /
dataset-reader work, approve feature extraction, approve label generation,
approve model-output integration, approve real Tenhou / real haifu /
external-log / platform-data use, approve CLI / broad ingestion, approve
self-play, approve league behavior or approve P8-P12 entry.

## Evidence Sources

- `AGENTS.md`
- `README.md`
- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/12_technical_plan/12D_POST_FULL_P6_TRANSITION_REVIEW.md`
- `docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`
- `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md`
- `src/mjlabai/data/replay_schema.py` as read-only context
- `tests/fixtures/data/synthetic_replay_smoke.json` as read-only context
- `tests/data/test_replay_schema.py` as read-only context
- `tests/data/test_synthetic_replay_fixture_schema.py` as read-only context
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`

## Scope Review

| review_item | finding | status |
|---|---|---|
| `03E` is docs-only | `03E` defines P7 purpose, scope, entry criteria, exit criteria draft, risk requirements, evidence requirements and first task candidate without adding implementation. | pass |
| P7 implementation remains unapproved | `03E` explicitly keeps training, model architecture implementation, data loader, parser, reader, ingestion, features and labels unapproved. | pass |
| P7 first task remains unexecuted | `03E` recommends a later docs-only review gate and does not execute the first P7 task. | pass |
| P8-P12 remain closed | `03E` requires separate transition reviews, scope, entry criteria, risk review and first-task approval for later stages. | pass |
| No production changes are implied | `03E` does not approve production code, tests, fixtures, data files, CLI, model-output integration or broad ingestion. | pass |
| No model-strength claim is made | `03E` classifies itself as P7 scope / entry criteria / first-task definition evidence only. | pass |

## Post-Full-P6 Context Review

| context_item | review_finding | status |
|---|---|---|
| P5 closure boundary | `03E` correctly treats P5 as closed only for the current synthetic/local evaluation groundwork scope. | pass |
| Full P6 closure boundary | `03E` correctly treats full P6 as closed only for the documented data-system scope: docs/governance/source-rights planning, accepted synthetic/local minimal replay schema and project-authored fixture smoke implementation, and deferred/blocked/later-stage inventory. | pass |
| P6 implementation inheritance | `03E` correctly avoids treating P6 closure as parser, reader, ingestion, feature, label or real-data approval. | pass |
| Post-full-P6 transition | `03E` follows `12D`, which allowed only P7 scope / entry criteria / first-task definition before implementation. | pass |
| P7 implementation status | `03E` correctly records that P7 implementation is not approved. | pass |

## Purpose And North-Star Review

`03E` correctly describes P7 as the supervised-learning stage whose future role
is to prepare a base strategy policy from approved data, features and labels.
It ties that future work to the north-star target only indirectly and avoids
claiming that P7 scoping produces a model, proves strength, compares to LuckyJ
or produces Tenhou ranked evidence.

Review status:

```text
pass
```

## Allowed Docs-Only Scope Review

The allowed scope in `03E` is sufficient for this stage boundary. It covers:

- P7 purpose.
- P7 entry criteria.
- future exit criteria draft.
- upstream artifact status.
- forbidden scope.
- data readiness.
- source rights.
- parser / reader / ingestion dependencies.
- feature extraction readiness.
- label generation readiness.
- model architecture planning.
- training-loop planning.
- validation / evaluation dependency.
- risk review.
- evidence requirements.
- first task candidate.
- P8-P12 boundary.

All items remain definition-only and do not approve implementation.

## Forbidden Scope Review

`03E` sufficiently forbids:

- training implementation.
- model architecture implementation.
- loss / optimizer / trainer implementation.
- data loader implementation.
- dataset construction.
- parser, dataset reader and ingestion.
- feature extraction and label generation.
- real Tenhou, real haifu, external logs and platform data.
- accounts, sessions, cookies and tokens.
- platform automation, scraping, evasion or account tooling.
- model-output integration.
- CLI or broad ingestion.
- self-play, league and runner behavior.
- P8-P12 entry.
- model-strength, Tenhou ranked, LuckyJ `10.68` and candidate-promotion claims.

Review status:

```text
pass
```

## Entry Criteria Review

| criterion_group | current_status_in_03E | review_finding |
|---|---|---|
| full P6 documented closure | satisfied for documented P6 scope only | correctly scoped; not implementation approval |
| post-full-P6 transition | satisfied by `12D` | correctly allows only docs-only P7 scoping |
| P7 scope definition | defined in `03E` | sufficient for review |
| P7 scope review | open before this document | this document closes the review gate with no blocker |
| source-rights status | not satisfied for training data | correctly open |
| selected data source | not selected / not approved | correctly open |
| parser / reader / ingestion | not satisfied | correctly open |
| feature extraction | not approved | correctly open |
| label generation | not approved | correctly open |
| training data policy | not approved | correctly open |
| artifact / checkpoint policy | partially established only | correctly open |
| privacy / platform terms | not satisfied for real data | correctly open |
| implementation approval in `10_NEXT` | not approved | correctly open |
| human / Web review for implementation | not recorded | correctly open |
| P8-P12 non-entry | reaffirmed | sufficient |

The entry criteria are sufficient because they distinguish definition from
satisfaction and keep all implementation prerequisites open until separate
tasks approve them.

## Exit Criteria Draft Review

The exit criteria in `03E` are future-only. They correctly require later
evidence for approved implementation, data/source rights, parser/reader/
ingestion or scoped-out alternatives, feature/label dependencies, training
pipeline work, artifact provenance, offline evaluation mapping and final P7
closure review.

Review status:

```text
pass
```

## Required Inputs Review

`03E` is honest about current required input status:

- no P7 training data source is selected or approved.
- source rights are not approved for training data.
- the current replay schema is minimal, in-memory and synthetic/local.
- parser, dataset reader and ingestion are not implemented or approved.
- feature extraction and label generation are not defined or approved.
- split policy, architecture boundary, training configuration and artifact
  policy are not ready for implementation.

Review status:

```text
pass
```

## Risk Review Requirements

The risk requirements in `03E` are sufficient for this boundary. They cover
stage drift, premature training, real-data use without rights, account/platform
data risk, parser / reader / ingestion scope creep, feature/label leakage,
train/test leakage, model artifact ambiguity, overclaim risk, P8-P12 drift and
LuckyJ comparison overclaim.

This review adds no new unresolved blocker.

## Evidence Requirements Review

The future evidence fields in `03E` are appropriate. They include source,
rights, schema, parser/reader, feature, label, split, architecture, training
config, seeds, dependency versions, validation commands, metric outputs,
artifact checksums, known exclusions, failure modes, evidence grade and
explicit non-evidence warning.

Current evidence grade remains:

```text
P7 scope / entry criteria / first-task review evidence only.
```

## First Task Candidate Review

The first task candidate in `03E` was:

```text
Review P7 scope, entry criteria and first task before implementation.
```

That was the correct next task because the P7 scope definition needed an
independent review before any more detailed P7 planning.

After this review, the next P7-only task should remain docs-only and move to
the most upstream remaining prerequisite:

```text
Define P7 supervised-learning data/source readiness inventory before implementation.
```

Rationale:

- P7 cannot safely define features, labels, model architecture or training
  loops until data/source readiness is inventoried.
- This keeps P7 from starting training before data/source rights and allowed
  use are clear.
- This avoids reopening P6 implementation while still using the full-P6
  closure state as context.

## Later Data / Source Inventory Review Status

`docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md`
later defined the P7 data/source readiness inventory.

`docs/03_supervised_policy/03H_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_REVIEW.md`
later reviewed that inventory and recorded:

```text
Review can close.
```

That later review does not approve P7 implementation, P7 first-task execution,
training data source, source ingestion, parser, dataset reader, ingestion,
feature extraction, label generation, real data, model-output integration,
CLI, self-play, league or P8-P12 entry.

## P8-P12 Non-Entry Review

The P8-P12 boundary in `03E` is sufficient. P7 scoping and this review do not
approve:

- P8 reinforcement learning.
- P9 search / risk model.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou validation.

Each later stage still requires separate transition review, scope, entry
criteria, risk review and first-task approval.

## Governance Synchronization Review

This review requires synchronization across:

- `docs/00_HANDOFF.md`
- `docs/00_DOCS_INDEX.md`
- `docs/10_next/10_NEXT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/03_supervised_policy/03E_P7_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md`
- `docs/07_development_execution/07A_MILESTONES.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_DECISION_RECORD.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`

The synchronized next task must be:

```text
Define P7 supervised-learning data/source readiness inventory before implementation.
```

## Validation Results

Required validation for this review:

```text
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

Validation status:

```text
pass
```

## Review Decision

```text
Review can close.
```

No blocker was found in `03E` for moving to the next docs-only P7 readiness
inventory task.

This decision does not approve P7 implementation, P7 first-task execution,
training, parser, dataset reader, ingestion, feature extraction, label
generation, real Tenhou, real haifu, external logs, platform data, model-output
integration, CLI, self-play, league or P8-P12 entry.

## Next Task Recommendation

```text
Define P7 supervised-learning data/source readiness inventory before implementation.
```

The next task must remain docs-only. It must not add production code, tests,
fixtures, data files, parser, dataset reader, ingestion, feature extraction,
label generation, model-output integration, CLI, broad file ingestion,
training, tuning, self-play, league, runner behavior, real Tenhou, real haifu,
external logs, platform data, account/session/cookie/token handling,
third-party binaries or model-strength claims.

Follow-up status:

```text
docs/03_supervised_policy/03G_P7_SUPERVISED_LEARNING_DATA_SOURCE_READINESS_INVENTORY_BEFORE_IMPLEMENTATION.md
defines the recommended data/source readiness inventory. It does not approve
source use, source ingestion, P7 implementation or training data.
```

## Explicit Non-Evidence

This review is not:

- P7 implementation.
- P7 first-task execution.
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
- feature extraction.
- label generation.
- model-output integration.
- CLI or broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
