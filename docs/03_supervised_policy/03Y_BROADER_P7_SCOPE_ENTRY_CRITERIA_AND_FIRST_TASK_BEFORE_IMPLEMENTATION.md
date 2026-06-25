# 03Y Broader P7 Scope Entry Criteria And First Task Before Implementation

## Scope

This document defines broader P7 scope, entry criteria and the first task
candidate before implementation.

This is a docs-only broader P7 scope / entry / first-task definition. It is
not implementation, implementation approval, training, source approval, parser
/ reader / ingestion, actual feature extraction, actual label generation,
supervised dataset construction, model architecture / trainer planning
approval, real-data use, model-output integration or P8-P12 entry.

## Broader P7 Purpose

Broader P7 exists to move from the exact minimal synthetic/local feature-label
smoke current scope toward auditable supervised-learning planning.

Its purpose is to define what must be true before any future supervised
learning implementation can safely use approved sources, parser / reader /
ingestion boundaries, actual feature extraction, actual label generation,
dataset construction, split / leakage controls, model / trainer planning and
training evidence requirements.

This supports the north-star target indirectly: a future supervised policy may
become one input to later RL, search, league and Tenhou validation stages, but
this document does not train or evaluate such a policy and is not model-strength
evidence.

## Current Context

| context_item | current_status | notes |
|---|---|---|
| P5 evaluation groundwork | closed for current synthetic/local evaluation groundwork scope | `05X` does not approve P6-P12 or strength claims. |
| Full P6 data-system scope | closed for documented P6 data-system scope only | `02AA` does not approve parser / reader / ingestion, feature extraction, label generation, real data or P7 implementation. |
| P7 current scope | closed for exact current scope only | `03V` closes only the docs-only readiness chain plus accepted minimal synthetic/local feature-label smoke implementation. |
| Full P7 roadmap / inventory | defined and reviewed | `03W` defines it and `03X` records `Review can close`. |
| Full P7 | open | Broader P7 work remains unapproved until later gates. |
| Accepted P7 implementation artifacts | exact minimal synthetic/local smoke only | `src/mjlabai/supervised/feature_label_schema.py`, `tests/fixtures/supervised/synthetic_supervised_smoke.json`, `tests/supervised/test_feature_label_schema.py` and `tests/supervised/test_synthetic_supervised_fixture_schema.py`. |
| P8-P12 | not approved | Later stages require separate transition reviews, scope, entry criteria and first-task approval. |

Current-scope P7 closure does not equal broader P7 implementation approval. It
accepts only JSON-safe synthetic/local smoke mapping validation and guardrails;
it does not create a parser, reader, ingestion path, actual feature extractor,
actual label generator, training dataset, model architecture, trainer or model
artifact.

## Allowed Docs-Only Scope

This broader P7 definition may define:

- broader P7 scope.
- broader P7 non-goals.
- entry criteria before any broader implementation.
- implementation entry criteria before any code or data work.
- required upstream artifacts and statuses.
- source-readiness requirements.
- parser / reader / ingestion readiness requirements.
- actual feature extraction readiness requirements.
- actual label generation readiness requirements.
- supervised dataset construction readiness requirements.
- train / validation / test split and leakage policy requirements.
- model architecture / trainer planning requirements.
- evidence requirements and evidence grades.
- risk controls.
- first task candidate.
- P8-P12 non-entry boundary.

These definitions are planning constraints only. They do not satisfy the
criteria they define.

## Forbidden Scope

This task and the broader P7 definition do not permit:

- production code.
- tests.
- fixtures.
- data files.
- source ingestion.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- training.
- tuning.
- model architecture implementation.
- dataloader, optimizer, loss or trainer.
- checkpoint, weights or snapshot files.
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
- P8-P12 entry.
- model-strength claims.
- Tenhou ranked evidence claims.
- stable-dan ranked-game evidence claims.
- LuckyJ `10.68` comparison.
- candidate promotion evidence.

## Broader P7 Entry Criteria Before Implementation

| criterion | required_before_implementation | current_status | blocker | evidence | notes |
|---|---:|---|---|---|---|
| P7 current scope closed for exact scope | yes | satisfied | none | `03V` | Current-scope closure is narrow and non-strength. |
| post-current-scope P7 transition review complete | yes | satisfied | none | `12E` | Selected full-P7 roadmap / inventory before broader work. |
| full P7 roadmap / inventory defined | yes | satisfied | none | `03W` | Inventory separates required / deferred / blocked / later-stage / out-of-scope items. |
| full P7 roadmap / inventory reviewed | yes | satisfied | none | `03X` | Review can close; no blocker found. |
| broader P7 scope / entry / first task defined | yes | defined here | pending review | this document | Must be reviewed before any implementation approval. |
| broader P7 scope / entry / first task reviewed | yes | not yet | review gate pending | future `03Z` or equivalent | Next task candidate. |
| source / training-data readiness boundary updated | yes | not satisfied | no source approved | future source readiness update and review | `03G`/`03H` inventory is not source approval. |
| source-specific approval process defined | yes | not satisfied | rights / privacy / platform / storage unresolved | future source approval boundary | Required before any real or external source use. |
| parser / reader / ingestion boundary defined and reviewed | yes, unless explicitly scoped out for synthetic-only task | not satisfied | no approved source or boundary | future boundary + review | No parser / reader / ingestion path exists now. |
| actual feature extraction boundary defined and reviewed | yes | not satisfied | no source/parser/ingestion approval | future feature extraction boundary | Must preserve decision-time public information only. |
| actual label generation boundary defined and reviewed | yes | not satisfied | no approved label source or policy | future label generation boundary | Model-output, self-play and league labels remain unapproved. |
| supervised dataset construction policy defined and reviewed | yes | not satisfied | source/features/labels unapproved | future dataset policy | Must separate smoke fixtures from training data. |
| train / validation / test split policy defined and reviewed | yes | not satisfied | no dataset policy | future split policy | Must prevent same-game, source, temporal and near-duplicate leakage. |
| leakage prevention policy defined and reviewed | yes | partially bounded, not full policy | no full data path | future leakage policy | Must cover hidden information, future information and split leakage. |
| model architecture / trainer planning boundary defined and reviewed | yes before training or model code | not satisfied | no dataset/source/features/labels approved | future model/trainer planning boundary | Planning only; no model code now. |
| evidence / risk requirements defined and synchronized | yes | partially satisfied by `03K`/`03L`; broader sync still needed | future broader task evidence | evidence log / risk register | Future implementation needs task-specific evidence fields. |
| approval decision required before any implementation | yes | not satisfied | no reviewed implementation proposal | future approval decision | `10_NEXT` must explicitly approve exact files and scope. |
| human / Web ChatGPT review required | yes | not satisfied for implementation | review response | future review gate | Broader scope definition must be reviewed first. |
| exact allowed files listed before implementation | yes | not satisfied | no implementation prompt | future approval decision / `10_NEXT` | No implementation prompt is generated here. |
| P8-P12 transition review before later stages | yes | not satisfied | full P7 not closed | future transition reviews | P8-P12 remain closed. |

## Implementation Entry Criteria

No broader P7 implementation may begin unless all applicable items below are
complete and explicitly approved by the first unchecked
`docs/10_next/10_NEXT.md` task:

1. broader P7 scope / entry / first-task definition is reviewed.
2. source / training-data readiness is updated and reviewed.
3. any selected source has a source-specific approval decision.
4. parser / reader / ingestion is defined, reviewed and approved, or explicitly
   scoped out for a synthetic-only task.
5. actual feature extraction boundary is defined, reviewed and approved.
6. actual label generation boundary is defined, reviewed and approved.
7. supervised dataset construction policy is defined and reviewed.
8. train / validation / test split and leakage policy are defined and reviewed.
9. model architecture / trainer planning boundary is defined and reviewed
   before any model or trainer code.
10. risk register and evidence log requirements are updated.
11. human / Web ChatGPT review confirms the approval path.
12. `10_NEXT` names the exact implementation task, exact allowed files, exact
    validation commands and stop conditions.

## Required Upstream Artifacts

Required upstream artifacts and their statuses:

- P5 closure for current synthetic/local evaluation groundwork: complete in
  `05X`.
- Full P6 closure for documented P6 data-system scope: complete in `02AA`.
- P7 current-scope closure for exact scope: complete in `03V`.
- Post-current-scope P7 transition review: complete in `12E`.
- Full P7 roadmap / inventory definition: complete in `03W`.
- Full P7 roadmap / inventory review: complete in `03X`.
- Current exact smoke artifacts: accepted as current-scope complete, but not
  training data.
- Approved P7 training source: none.
- Approved source ingestion: none.
- Approved parser / reader / ingestion: none.
- Approved actual feature extraction: none.
- Approved actual label generation: none.
- Approved supervised dataset construction: none.
- Approved model architecture / trainer: none.

## Blocked Deferred Later-Stage And Out-Of-Scope Items

Blocked until separate approval:

- real Tenhou.
- real haifu.
- external logs.
- platform data.
- account / session / cookie / token handling.
- real-data parser / reader / ingestion.
- source-specific training-data approval.
- third-party binaries, weights, params, checkpoints or snapshots.

Deferred, not approved:

- additional synthetic/local supervised fixtures.
- broader synthetic/local expansion.
- model-output integration.
- CLI.
- broad file ingestion.
- broader implementation proposal preparation.

Later-stage:

- self-play.
- league / runner.
- P8 reinforcement learning.
- P9 search / risk model.
- P10 model league.
- P11 large-scale training.
- P12 Tenhou target validation.

Out of scope / non-evidence:

- model-strength evidence.
- Tenhou ranked performance.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

## First Task Candidate

Recommended next task:

```text
Review broader P7 scope, entry criteria and first task before implementation.
```

This next task must be a docs-only review gate. It must not directly select or
execute implementation, training, parser / reader / ingestion implementation,
actual feature extraction, actual label generation, model architecture /
trainer work or P8-P12 work.

## Why No Broader Implementation Yet

Broader P7 implementation cannot start yet because:

- the broader P7 scope / entry criteria in this document still need review.
- no training source is approved.
- source ingestion is unapproved.
- parser / reader / ingestion are unapproved.
- actual feature extraction is unapproved.
- actual label generation is unapproved.
- supervised dataset construction is unapproved.
- split and leakage policies are not ready.
- model architecture, dataloader, optimizer, loss and trainer are unapproved.
- real data and model-output integration are unapproved.
- current-scope P7 closure approved only the exact minimal synthetic/local
  smoke path.

## Why No Training Yet

Training cannot start yet because:

- no approved training data source exists.
- no source-specific rights / provenance / storage approval exists for
  training data.
- no parser / reader / ingestion path is approved.
- no actual feature extraction or label generation is approved.
- no supervised dataset construction policy exists.
- no train / validation / test split and leakage policy exists.
- no model architecture, dataloader, optimizer, loss, trainer or training
  config is approved.
- no artifact / checkpoint evidence policy is approved for training outputs.
- no `10_NEXT` item explicitly approves a training task.

## Why No P8-P12 Yet

P8-P12 cannot start yet because:

- full P7 is not closed.
- broader P7 implementation is not approved.
- no P7 training has occurred.
- no supervised model candidate exists.
- no model-strength evidence exists.
- no candidate has passed the required racing-funnel gates for later stages.
- each later stage requires separate transition review, scope, entry criteria,
  risk / evidence review and first-task approval.

## Planning Decision

```text
Broader P7 scope, entry criteria and first task are defined before
implementation. This does not approve broader P7 implementation, training,
source ingestion, parser, dataset reader, actual feature extraction, actual
label generation, supervised dataset construction, model architecture, real
data, model-output integration, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
Broader P7 scope, entry criteria and first-task definition evidence only.
```

## Explicit Non-Evidence

This definition is not:

- broader P7 implementation.
- broader P7 implementation approval.
- P7 training.
- source approval.
- training-data approval.
- parser.
- dataset reader.
- ingestion.
- actual feature extraction.
- actual label generation.
- supervised dataset construction.
- model architecture.
- trainer.
- dataloader, optimizer or loss.
- checkpoint, weights or snapshot approval.
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
