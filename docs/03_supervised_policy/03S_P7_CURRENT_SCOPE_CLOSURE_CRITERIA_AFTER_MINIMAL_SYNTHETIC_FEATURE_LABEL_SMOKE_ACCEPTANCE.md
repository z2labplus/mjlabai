# 03S P7 Current-Scope Closure Criteria After Minimal Synthetic Feature-Label Smoke Acceptance

## Scope

This document defines P7 current-scope closure criteria after the minimal
synthetic/local supervised feature-label smoke implementation was accepted in
`03Q` and the next current-scope task was selected in `03R`.

This is a docs-only closure-criteria definition. It does not close P7 current
scope, does not close full P7, does not approve broader P7 implementation,
does not add production code, tests, fixtures or data files, and does not
approve training, source ingestion, parser / dataset reader / ingestion,
actual feature extraction, actual label generation, supervised dataset
construction, model architecture / trainer work, real data, model-output
integration, self-play, league or P8-P12 entry.

North-star relationship: clear P7 closure criteria keep the supervised-learning
path from growing without bounds before training is lawful, auditable and
useful for the Tenhou stable-dan target. This document is not model-strength
evidence, Tenhou ranked evidence, stable-dan ranked-game evidence, LuckyJ
`10.68` comparison or candidate-promotion evidence.

## Accepted Current-Scope P7 Inventory

The following P7 current-scope items are accepted as complete for their
documented scope:

- P7 scope / entry criteria / first-task definition in `03E`.
- P7 scope / entry criteria review in `03F`.
- P7 supervised-learning data/source readiness inventory in `03G`.
- P7 supervised-learning data/source readiness inventory review in `03H`.
- P7 feature and label readiness boundary in `03I`.
- P7 feature and label readiness boundary review in `03J`.
- P7 supervised-learning risk and evidence taxonomy in `03K`.
- P7 supervised-learning risk and evidence taxonomy review in `03L`.
- minimal P7 synthetic/local supervised fixture and feature-label smoke
  proposal in `03M`.
- proposal review in `03N`.
- exact minimal implementation approval decision in `03O`.
- exact minimal implementation in the approved files only:
  - `src/mjlabai/supervised/feature_label_schema.py`
  - `tests/fixtures/supervised/synthetic_supervised_smoke.json`
  - `tests/supervised/test_feature_label_schema.py`
  - `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- exact minimal implementation review in `03P`.
- current-scope acceptance decision in `03Q`.
- next-task definition after acceptance in `03R`.

The accepted implementation behavior remains limited to JSON-safe
synthetic/local smoke mapping validation, candidate feature family validation,
candidate label family validation, public-information-only placeholder checks,
hidden / future information rejection, unsafe provenance / claim rejection and
non-evidence guardrails.

## P7 Current-Scope Closure Criteria

| criterion | required_before_current_scope_closure | current_status | evidence | blocker | notes |
|---|---:|---|---|---|---|
| C1. P7 scope / entry criteria / first-task definition complete. | yes | ready | `03E` | no | Docs-only scope and first task were defined before implementation. |
| C2. P7 scope / entry criteria review complete. | yes | ready | `03F` | no | Review can close with no blocker. |
| C3. P7 data/source readiness inventory complete. | yes | ready | `03G` | no | No source is approved for training or ingestion. |
| C4. P7 data/source readiness inventory review complete. | yes | ready | `03H` | no | Review can close with no blocker. |
| C5. P7 feature/label readiness boundary complete. | yes | ready | `03I` | no | Planning boundary only; no extraction or generation approval. |
| C6. P7 feature/label readiness boundary review complete. | yes | ready | `03J` | no | Review can close with no blocker. |
| C7. P7 risk/evidence taxonomy complete. | yes | ready | `03K` | no | Defines evidence grades and overclaim risks. |
| C8. P7 risk/evidence taxonomy review complete. | yes | ready | `03L` | no | Review can close with no blocker. |
| C9. Minimal synthetic/local feature-label smoke proposal complete. | yes | ready | `03M` | no | Proposal only; no implementation approval by itself. |
| C10. Proposal review complete. | yes | ready | `03N` | no | Review can close with no blocker. |
| C11. Approval decision complete. | yes | ready | `03O` | no | Approved only the exact next minimal implementation task. |
| C12. Exact minimal implementation complete in approved files only. | yes | ready | implementation files and tests | no | No broader implementation, parser, ingestion, extraction, generation or training. |
| C13. Implementation review complete. | yes | ready | `03P` | no | Review can close with no blocker. |
| C14. Current-scope acceptance decision complete. | yes | ready | `03Q` | no | Accepted only the exact minimal synthetic/local smoke scope. |
| C15. Next-task definition after acceptance complete. | yes | ready | `03R` | no | Selected current-scope closure criteria definition. |
| C16. P7 current-scope closure criteria defined and reviewed. | yes | partial | this document defines criteria; review pending | no | Definition happens in this task; separate review is still required. |
| C17. P7 current-scope handoff/evidence finalization complete. | yes | not_ready | not yet created | no | Required before final current-scope closure review. |
| C18. P7 current-scope risk/evidence consistency review complete if needed. | yes | deferred | risk/evidence docs updated each step | no | Required if review or finalization finds mismatch. |
| C19. Final P7 current-scope closure review gate complete. | yes | not_ready | not yet created | no | This task does not close P7 current scope. |
| C20. Validation commands pass. | yes | pending | required commands listed below | no | Must be rerun by this and later closure-review tasks. |
| C21. No unresolved blocker. | yes | pending | this document records no known blocker | no | Later review may change this status. |
| C22. Deferred / blocked / not accepted items classified. | yes | ready | this document | no | Classification is part of this criteria definition. |
| C23. P8-P12 non-entry boundary clear. | yes | ready | this document and stage contract | no | P8-P12 remain unapproved. |
| C24. No model-strength / Tenhou / LuckyJ / candidate-promotion overclaim. | yes | ready | this document and evidence log | no | Current evidence is closure-criteria definition only. |
| C25. Governance synchronized. | yes | pending | handoff, index, evidence, risk, changelog, decision, stage contract, backlog and plan | no | Must be synchronized by this task. |
| C26. `10_NEXT` hygiene maintained. | yes | pending | `docs/10_next/10_NEXT.md` | no | Next task should be a docs-only criteria review gate. |

## P7 Current-Scope Exit Readiness Checklist

| checklist_item | status | evidence | blocker | required_before_closure | notes |
|---|---|---|---|---:|---|
| P7 readiness chain complete. | ready | `03E` through `03L` | no | yes | Scope, source inventory, feature/label boundary and risk/evidence taxonomy are defined and reviewed. |
| Minimal synthetic/local smoke implementation accepted. | ready | `03O`, implementation files, `03P`, `03Q` | no | yes | Accepted only for exact minimal synthetic/local smoke scope. |
| Validation status. | pending | commands listed below | no | yes | Must pass in this task and later review/finalization gates. |
| Governance synchronization. | pending | docs/governance updates | no | yes | This task updates governance, but review must confirm consistency. |
| Evidence log updated. | pending | `09_EVIDENCE_LOG.md` | no | yes | Evidence grade must remain closure-criteria definition only. |
| Risk register updated. | pending | `09_RISK_REGISTER.md` | no | yes | Main risks are closure overclaim and scope drift. |
| Source/training-data non-approval preserved. | ready | `03G`, `03H`, `03Q`, this document | no | yes | No source is approved for P7 training or ingestion. |
| Parser / reader / ingestion non-approval preserved. | ready | `03G` through `03Q`, this document | no | yes | Parser, reader and ingestion remain outside current scope. |
| Actual feature extraction / label generation non-approval preserved. | ready | `03I`, `03J`, `03Q`, this document | no | yes | Smoke validation is not extraction or generation. |
| Broader P7 implementation non-approval preserved. | ready | `03Q`, `03R`, this document | no | yes | Current scope is exact minimal synthetic/local smoke only. |
| P8-P12 non-entry preserved. | ready | `12D`, `03E`, `03R`, this document | no | yes | Later stages require separate transition review and approval. |
| Current-scope closure criteria review requirement. | not_ready | next task | no | yes | This task defines criteria; a separate review must inspect them. |
| Handoff/evidence finalization requirement. | not_ready | future task | no | yes | Required before final current-scope closure review. |
| Final current-scope closure review requirement. | not_ready | future task | no | yes | Final review is still pending; P7 current scope is not closed. |

## Required Remaining P7 Current-Scope Items

The remaining current-scope items before final current-scope P7 closure should
stay docs/review/closure-only:

1. Review P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance.
2. Finalize P7 current-scope handoff and evidence index.
3. Review P7 current-scope risk/evidence consistency if needed.
4. Run final P7 current-scope closure review gate.
5. If final current-scope closure passes, run a separate post-current-scope P7
   transition review before defining any broader P7 implementation or P8 task.

Parser, reader, ingestion, actual feature extraction, actual label generation,
training, real data, model-output integration and P8-P12 work are not required
current-scope closure items. They remain deferred, blocked, not accepted or
later-stage items.

## Deferred / Blocked / Not Accepted Items

Deferred / not accepted:

- broader P7 implementation.
- additional supervised fixtures.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- model architecture.
- dataloader.
- optimizer.
- loss.
- trainer.
- training loop.
- model-output integration.
- CLI.
- broad ingestion.

Blocked until source/legal/platform approval:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token data.
- real-data parser / reader / ingestion.
- source-specific training data approval.

Later-stage:

- self-play.
- league.
- P8 reinforcement learning.
- P9 search / risk model.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou target validation.

Out of scope / non-evidence:

- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ comparison.
- candidate promotion.

## P8-P12 Non-Entry Conditions

Do not enter P8-P12 while any of the following are true:

- P7 current-scope closure criteria have not been reviewed.
- P7 current-scope handoff / evidence finalization is incomplete.
- final P7 current-scope closure review has not passed.
- an unresolved blocker exists.
- validation fails.
- governance docs disagree about current stage or next task.
- evidence is overclaimed.
- broader P7 implementation is mistaken as approved.
- training data source status is ambiguous.
- parser / reader / ingestion status is ambiguous.
- actual feature / label approval status is ambiguous.
- P8-P12 lacks an independent transition review, scope, entry criteria, risk /
  evidence taxonomy and first-task approval.

## Validation Commands

Current closure-criteria validation should include:

```bash
git diff --check
python3 -m unittest tests/supervised/test_feature_label_schema.py
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

These commands validate formatting and the existing P7/P6 synthetic/local smoke
artifacts. They do not train a model, ingest data, read real Tenhou or provide
model-strength evidence.

## Planning Decision

```text
P7 current-scope closure criteria are defined after minimal synthetic feature-label smoke acceptance. This does not close P7 current scope, does not approve broader P7 implementation, training, source ingestion, parser, dataset reader, actual feature extraction, actual label generation, model architecture, real data, model-output integration, self-play, league or P8-P12 entry.
```

## Next Task Recommendation

Recommended next task:

```text
Review P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance.
```

That task must be a docs-only review gate. It must not add production code,
tests, fixtures, data files, parser, reader, ingestion, actual feature
extraction, actual label generation, supervised dataset construction,
training, model architecture, model-output integration, real data, CLI,
self-play, league or P8-P12 work.

The closure criteria review is now recorded in
`docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
It records `Review can close` with no blocker and recommends docs-only
handoff/evidence finalization next. That review does not close P7 current
scope, approve broader P7 implementation, approve training, approve source
ingestion, approve parser / reader / ingestion, approve actual feature
extraction, approve actual label generation, approve real data, approve
model-output integration or approve P8-P12.

## Evidence Grade

```text
P7 current-scope closure criteria definition evidence only.
```

## Explicit Non-Evidence

This closure-criteria definition is not:

- P7 current-scope closure.
- P7 full closure.
- broader P7 implementation.
- P7 training.
- source approval.
- training-data approval.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction from logs.
- actual label generation.
- supervised dataset construction.
- model architecture.
- trainer.
- model-output integration.
- CLI.
- broad file ingestion.
- real Tenhou ingestion.
- real haifu ingestion.
- external-log ingestion.
- platform-data ingestion.
- self-play.
- league.
- P8-P12 entry approval.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.
