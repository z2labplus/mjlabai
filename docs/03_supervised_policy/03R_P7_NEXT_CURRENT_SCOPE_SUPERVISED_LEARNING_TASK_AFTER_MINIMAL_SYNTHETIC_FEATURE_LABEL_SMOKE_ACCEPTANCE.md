# 03R P7 Next Current-Scope Supervised-Learning Task After Minimal Synthetic Feature-Label Smoke Acceptance

## Scope

This document defines the next P7 current-scope supervised-learning task after
the minimal synthetic/local feature-label smoke implementation was accepted in
`03Q`.

This is a docs-only task-definition gate. It does not add implementation,
modify implementation logic, add tests, add fixtures, add data files, approve
broader P7 implementation, approve training, approve a training-data source,
approve source ingestion, approve parser / dataset reader / ingestion, approve
actual feature extraction, approve actual label generation, approve model
architecture / trainer work, approve real data, approve model-output
integration or approve P8-P12.

North-star relationship: defining the next P7 current-scope task helps the
project avoid endless supervised-learning groundwork churn before training.
It keeps the path toward a future supervised base policy auditable, but it is
not model-strength evidence, Tenhou ranked evidence, stable-dan ranked-game
evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

## Current Accepted P7 Scope

`03Q` records:

```text
Accepted as current-scope complete.
```

Accepted current scope is limited to:

- exact minimal helper / schema smoke in
  `src/mjlabai/supervised/feature_label_schema.py`.
- exact project-authored synthetic/local supervised fixture in
  `tests/fixtures/supervised/synthetic_supervised_smoke.json`.
- exact smoke tests in:
  - `tests/supervised/test_feature_label_schema.py`
  - `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- direct docs / governance synchronization.

Accepted behavior is limited to:

- JSON-safe synthetic/local smoke mapping validation.
- candidate feature family validation.
- candidate label family validation.
- public-information-only placeholder checks.
- hidden / future information rejection.
- unsafe provenance / claim rejection.
- non-evidence guardrails.

## Current Unresolved / Not Approved P7 Scope

The following remain unresolved, unapproved or explicitly outside the accepted
current scope:

- broader P7 implementation.
- training.
- training-data source.
- source ingestion.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction from logs.
- actual label generation.
- supervised dataset construction.
- model architecture.
- dataloader.
- optimizer.
- loss.
- trainer.
- checkpoint.
- weights.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account, session, cookie or token handling.
- model-output integration.
- CLI.
- broad ingestion.
- self-play.
- league.
- P8-P12.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ comparison.
- candidate promotion.

## Candidate Next Tasks

| candidate_task | fit_with_current_state | risk | stage_creep_risk | implementation_required | docs_only_possible | recommendation | notes |
|---|---|---|---|---:|---:|---|---|
| Define P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance. | High. P7 has completed a docs-only readiness chain plus one exact accepted synthetic/local smoke implementation. | Low if framed as criteria only. | Low if the task explicitly forbids implementation and P8-P12. | no | yes | Recommended. | This directly addresses the risk that P7 continues indefinitely through more readiness / schema / review churn. |
| Define another P7 readiness boundary. | Medium. More readiness boundaries could be useful later, but the current chain already covers source readiness, feature/label readiness, risk/evidence taxonomy and synthetic smoke acceptance. | Medium. | Medium. | no | yes | Not recommended now. | More boundary work may be premature until current-scope closure criteria clarify what is actually missing. |
| Define another minimal P7 implementation proposal. | Medium-low. It could add another small smoke path, but implementation would remain unapproved and may distract from current-scope closure. | Medium-high. | High. | no for proposal; yes later if approved. | yes for proposal only | Not recommended now. | A new implementation proposal should wait until closure criteria show it is required. |
| Run a P7 blocker / transition review. | Medium. Useful if a blocker is found. | Low. | Low. | no | yes | Fallback only. | No blocker was found in `03Q`, so a blocker review is not the best next step. |
| Defer pending human / Web ChatGPT decision. | Medium. Conservative but stalls progress. | Low. | Low. | no | yes | Not recommended. | The repository has enough evidence to choose a docs-only closure-criteria task while keeping implementation closed. |

## Recommended Next Task

Recommended next task:

```text
Define P7 current-scope closure criteria after minimal synthetic feature-label smoke acceptance.
```

That task is now defined in
`docs/03_supervised_policy/03S_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
`03S` defines criteria, exit readiness, remaining docs/review/closure items and
non-entry conditions only. It does not close P7 current scope or approve
broader P7 implementation, training, source ingestion, parser / reader /
ingestion, actual feature extraction, actual label generation, real data,
model-output integration, self-play, league or P8-P12.

The criteria review is recorded in
`docs/03_supervised_policy/03T_P7_CURRENT_SCOPE_CLOSURE_CRITERIA_REVIEW_AFTER_MINIMAL_SYNTHETIC_FEATURE_LABEL_SMOKE_ACCEPTANCE.md`.
Review decision: `Review can close.` The next recommended task is docs-only
P7 current-scope handoff/evidence finalization after closure criteria review.

Reasoning:

- P7 docs-only readiness chain plus one exact minimal synthetic/local smoke
  implementation has been accepted.
- P7 should not be extended indefinitely through more readiness, schema and
  review gates without defining what current-scope closure means.
- Closure criteria definition does not close P7 yet.
- Closure criteria definition does not approve P8-P12.
- Closure criteria definition does not approve implementation, training, real
  data, parser / reader / ingestion, feature extraction or label generation.

## Why Not More Implementation Now

More implementation is not the right next task because:

- the current accepted implementation is only synthetic/local smoke.
- broader P7 implementation remains unapproved.
- no training source is approved.
- no parser, dataset reader or ingestion is approved.
- no actual feature extraction or label generation is approved.
- no supervised dataset construction is approved.
- no training pipeline is approved.
- no model architecture, dataloader, optimizer, loss or trainer is approved.
- no evaluation evidence exists for model strength.

Therefore the next task should define current-scope closure criteria, not
execute another implementation.

## Why Not P8-P12

P8-P12 are not allowed next because:

- P7 current scope has not closed.
- P7 training has not started.
- P7 broad implementation is not approved.
- P8 reinforcement learning requires a separate transition review, scope,
  entry criteria, risk / evidence taxonomy and first-task approval.
- P9 search / risk modeling requires a separate transition review, scope,
  entry criteria, risk / evidence taxonomy and first-task approval.
- P10 model league requires a separate transition review, scope, entry
  criteria, risk / evidence taxonomy and first-task approval.
- P11 large-scale training requires a separate transition review, scope,
  entry criteria, risk / evidence taxonomy and first-task approval.
- P12 Tenhou target validation requires a separate transition review, scope,
  entry criteria, risk / evidence taxonomy, compliance review and first-task
  approval.

## Allowed Scope For Next Task

The recommended next task may:

- define the accepted current-scope P7 inventory.
- define required criteria before current-scope P7 closure.
- define deferred, blocked and not accepted items.
- define an exit readiness checklist.
- define validation commands.
- define P8-P12 non-entry conditions.
- update docs / governance.
- keep the work docs-only.

## Forbidden Scope For Next Task

The recommended next task must not:

- add production code.
- add tests.
- add fixtures.
- add data files.
- implement parser.
- implement dataset reader.
- implement ingestion.
- implement actual feature extraction.
- implement actual label generation.
- construct a supervised dataset.
- train.
- define or implement model architecture.
- implement dataloader, optimizer, loss or trainer.
- use real data.
- connect model output.
- add CLI.
- self-play.
- run league.
- enter P8-P12.
- make model-strength claims.

## Planning Decision

```text
The next P7 current-scope supervised-learning task is defined after minimal synthetic feature-label smoke acceptance. The recommended next task is docs-only P7 current-scope closure criteria definition. This does not approve broader P7 implementation, training, source ingestion, parser, dataset reader, actual feature extraction, actual label generation, model architecture, real data, model-output integration, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
P7 next current-scope supervised-learning task definition evidence only.
```

## Explicit Non-Evidence

This task definition is not:

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
