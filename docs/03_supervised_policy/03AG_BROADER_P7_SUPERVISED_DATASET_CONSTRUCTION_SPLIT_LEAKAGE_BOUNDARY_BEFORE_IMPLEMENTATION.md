# 03AG Broader P7 Supervised Dataset Construction Split Leakage Boundary Before Implementation

## Scope

This document defines the broader P7 supervised dataset construction, split
and leakage boundary before implementation.

It is docs-only boundary definition evidence. It does not implement or approve
supervised dataset construction, split creation, leakage-test implementation,
training-data construction, training, source approval, source ingestion,
parser / reader / ingestion, actual feature extraction, actual label
generation, model architecture, model-output integration, self-play, league or
P8-P12 entry.

## Purpose

The north-star target is a Japanese riichi mahjong AI whose long-term Tenhou
stable dan exceeds LuckyJ `10.68`. Dataset construction, split policy and
leakage controls matter because future supervised learning can only be useful
if examples are sourced lawfully, constructed from approved feature and label
outputs, split without contamination and reported without overclaiming.

This document prevents a common failure mode: treating a parser, a feature
schema, a smoke fixture or a boundary review as permission to build training
data. It defines vocabulary, approval prerequisites, allowed future classes,
forbidden scope, stop conditions, risk controls and evidence requirements
before any implementation can be considered.

## Current Dataset / Split / Leakage Status

Current broader P7 status:

- No supervised dataset construction is approved.
- No supervised examples are generated.
- No feature tensors are emitted.
- No labels, targets or training targets are emitted.
- No train / validation / test split is created.
- No split manifest is created.
- No leakage-test implementation exists.
- No training data is approved.
- No training run is approved.
- No source is approved for P7 training.
- No source is approved for source ingestion.
- No parser / reader / ingestion implementation is approved.
- No actual feature extraction is approved.
- No actual label generation is approved.

Current smoke artifacts have narrow non-training status:

- `tests/fixtures/supervised/synthetic_supervised_smoke.json` is a
  project-authored synthetic/local smoke artifact only. It is not a supervised
  dataset and is not training data.
- `src/mjlabai/supervised/feature_label_schema.py` validates in-memory
  synthetic/local smoke mappings only. It is not actual feature extraction,
  label generation or dataset construction.
- Repository docs are not training data.
- The P6 synthetic replay fixture is not P7 training data.
- P7 smoke validation evidence is not model-strength, Tenhou ranked,
  stable-dan ranked-game, LuckyJ comparison or candidate-promotion evidence.

## Concept Definitions

`supervised dataset construction boundary`:
Defines what a future dataset-construction component may consume, emit, record
and prove before implementation. It is not implementation approval.

`supervised dataset construction`:
Future code that combines approved feature outputs and approved label outputs
into dataset records or manifests. It remains unapproved.

`supervised example`:
One future training/evaluation example containing approved feature content,
approved target content and provenance. No such examples are created now.

`feature tensor`:
A model-input representation derived from approved feature extraction. No
feature tensors are created now.

`label target`:
A supervised target derived from approved label generation. No label targets
are created now.

`training target`:
A label or reward target approved for training use. No training targets are
approved now.

`dataset record`:
A future serialized or in-memory supervised example record. No dataset records
are created now.

`dataset manifest`:
A future inventory of dataset records, schemas, sources, provenance, approvals
and validation results. No dataset manifest is created now.

`split manifest`:
A future inventory of train / validation / test membership and split policy.
No split manifest is created now.

`train / validation / test split`:
Future mutually controlled partitions for model development, model selection
and final evaluation. No split is created now.

`holdout`:
A future partition reserved from training and tuning. No holdout is created
now.

`leakage`:
Any path where information, provenance, target values or duplicated examples
allow train-time, validation-time or test-time behavior to learn or infer
something it should not have.

`hidden-info leakage`:
Using concealed opponent hands, wall order, unrevealed tiles or private
information not available at decision time.

`future-info leakage`:
Using later events, future draws, future discards, terminal results or final
placement as decision-time features.

`source leakage`:
Using source identifiers, provenance or source-specific formatting shortcuts
as predictors instead of mahjong information.

`table/game leakage`:
Allowing records from the same table, game or hand to cross train/validation
/ test boundaries when that can reveal correlated outcomes.

`player/seat leakage`:
Allowing player, seat or identity shortcuts to leak target information across
splits.

`duplicate leakage`:
Allowing exact or near-duplicate records across splits.

`label leakage`:
Allowing labels or label-derived fields to appear in features.

`target leakage`:
Allowing targets, final outcomes or target proxies to appear in model inputs.

`temporal leakage`:
Using future time windows to predict earlier decision contexts.

`training data approval`:
A later explicit decision that a source and constructed dataset can be used for
training. It is separate from source readiness, source approval, parser /
reader / ingestion approval, feature approval and label approval.

`training run approval`:
A later explicit decision that a model/trainer may consume approved training
data. It is separate from dataset construction approval.

## Dependency Map

Future supervised dataset construction must follow this order:

```text
source readiness
-> source-specific approval or explicit synthetic/local boundary
-> parser / reader / ingestion approval
-> actual feature extraction approval
-> actual label generation approval
-> supervised dataset construction boundary
-> split / leakage policy boundary
-> supervised dataset construction proposal
-> supervised dataset construction approval decision
-> exact implementation files
-> dataset construction implementation
-> dataset construction review
-> training-data approval
-> training run approval
```

This document defines the supervised dataset construction boundary and split /
leakage policy boundary layer only. It does not satisfy earlier dependencies
and does not approve later implementation or training layers.

## Dataset Construction Boundary

Future supervised dataset construction may be considered only after separate
approval and exact `10_NEXT` scope. A future component must:

- consume only approved feature outputs and approved label outputs.
- never call parser / reader / ingestion unless that behavior is separately
  approved.
- never perform actual feature extraction or actual label generation by
  implication.
- never read raw real data, real Tenhou, real haifu, external logs, platform
  data, account data, session data, cookies or tokens.
- never call model code, training code, self-play, league or third-party
  binaries.
- preserve `source_id`, source approval refs, feature schema version, label
  schema version, transform version and provenance.
- record dataset record schema, dataset manifest schema and validation
  commands.
- record `split_id`, split policy, split unit, random seed if any and leakage
  validation plan.
- record evidence refs, risk refs and decision refs.
- stop before training-data approval and training-run approval.
- avoid storing raw real data in git unless a later rights/privacy/storage
  approval explicitly permits it.

This task creates no dataset records, no examples, no feature tensors, no
labels, no targets, no manifests and no split files.

## Split Boundary

Future split work must define the split unit before any split is created.
Possible future split units include:

- `source_id`.
- `game_id`.
- `hand_id`.
- `table_id`.
- `player_id`.
- time window.
- synthetic fixture id.
- source-specific grouping.

Future split policy must be deterministic and auditable. If randomness is
used, it must record a random seed, implementation version and reproducibility
metadata. Same game, hand, table, source group or duplicate cluster must not
cross train / validation / test boundaries unless a later approval explicitly
states why it is safe. Source-specific constraints must be documented before
implementation.

Synthetic/local smoke fixtures are not training splits. This task creates no
split and no split manifest.

## Leakage Boundary

Future leakage policy must explicitly guard against:

- hidden-info leakage.
- future-info leakage.
- target leakage.
- label fields entering features.
- final outcome entering decision-time features.
- source or provenance shortcuts.
- exact duplicate and near-duplicate leakage.
- same-game / same-table / same-hand contamination.
- train / validation / test contamination.
- temporal leakage.
- model-output leakage.
- self-play or league-output leakage.
- real-data privacy leakage.
- account / session / cookie / token leakage.
- documentation/context leakage where docs text is used as training data.
- synthetic-smoke-as-training-data leakage.

Leakage-test implementation is not approved here. A future implementation task
must define exact checks, exact files, exact allowed inputs and exact
validation commands before code is written.

## Future Approval Record Fields

A future supervised dataset construction, split or leakage approval record
must include at least:

- `component_id`.
- `component_type`.
- `source_id` list.
- source approval refs.
- parser / reader / ingestion approval refs.
- actual feature extraction approval refs.
- actual label generation approval refs.
- approved feature schema versions.
- approved label schema versions.
- forbidden source and information categories.
- dataset record schema.
- dataset manifest schema.
- split manifest schema.
- split policy.
- split unit.
- random seed if random.
- duplicate and near-duplicate policy.
- leakage validation plan.
- hidden-information validation.
- future-information validation.
- target-leakage validation.
- label-leakage validation.
- storage policy.
- `may_enter_git`.
- privacy/platform status.
- exact implementation files.
- validation commands.
- evidence refs.
- risk refs.
- decision refs.
- rollback plan.
- stop conditions.
- human / Web ChatGPT approval reference.
- explicit first unchecked `10_NEXT` implementation task.

## Candidate Dataset / Split / Leakage Classes

| Candidate class | Current status | Approved now | Source dependency | Feature / label dependency | Split dependency | Implementation approval required | Allowed for docs planning | Forbidden until | Risk | Notes |
|---|---|---:|---|---|---|---|---:|---|---|---|
| Project-authored synthetic/local dataset-shape smoke | Candidate only | No | Explicit synthetic/local boundary | Approved synthetic/local feature and label smoke outputs | Synthetic fixture id | Yes | Yes | Exact proposal and approval decision | Low-Medium | May be useful as a future shape-only smoke task. |
| Approved-source supervised dataset manifest | Candidate only | No | Source-specific approval | Approved extraction and generation outputs | Explicit split policy | Yes | Yes | Source, parser, feature, label and dataset approvals | High | Must not include raw real data without storage approval. |
| Approved-source split manifest | Candidate only | No | Source-specific approval | Approved dataset records | Split unit and leakage policy | Yes | Yes | Dataset construction proposal and split approval | High | Must prevent duplicate and same-game contamination. |
| Leakage validation report | Candidate only | No | Depends on approved manifest | Depends on approved features and labels | Depends on split manifest | Yes | Yes | Exact leakage-check approval | High | This document only defines categories, not checks. |
| Real Tenhou supervised dataset | Blocked | No | Real Tenhou source approval | Approved real-data extraction/generation | Strong split policy | Yes | No | Compliance, rights, parser, feature, label, dataset and training approvals | Very High | Not approved. |
| External-log supervised dataset | Blocked | No | External-log rights approval | Approved parser/extraction/generation | Strong split policy | Yes | No | Source and privacy approvals | Very High | Not approved. |
| Platform-data supervised dataset | Blocked | No | Platform approval | Approved parser/extraction/generation | Strong split policy | Yes | No | Compliance and privacy review | Very High | Not approved. |
| Model-output pseudo-label dataset | Deferred | No | Approved model-output source | Pseudo-label policy approval | Leakage policy | Yes | No | Later-stage approval | High | Not current P7 groundwork. |
| Self-play output dataset | Later-stage | No | P8/P10 approvals | RL/self-play policy | League/self-play split policy | Yes | No | P8/P10 approval | High | Not P7 boundary work. |
| League output dataset | Later-stage | No | P10 approvals | League policy | League split policy | Yes | No | P10 approval | High | Not P7 boundary work. |
| Docs-as-training-data dataset | Rejected | No | None | None | None | Not eligible | No | Never without a separate policy reversal | High | Repository docs are governance context, not training data. |

## Allowed Future Implementation Boundary

Only a later approved implementation task may do any implementation. If
approved later, an initial task should remain narrow:

- project-authored synthetic/local-only dataset-shape smoke; or
- approved-source-only dataset manifest construction; or
- approved-source-only split manifest construction; or
- docs-only validator for manifest shape.

Such a task must name exact files, exact inputs, approved feature / label
schemas, provenance fields, split policy, leakage controls, validation
commands, evidence refs and stop conditions. It must stop before training-data
approval and training-run approval.

## Forbidden Dataset / Split / Leakage Scope

The following remain forbidden now:

- supervised dataset construction implementation.
- split creation.
- leakage-test implementation.
- feature tensor generation.
- label, target or training-target generation.
- supervised example generation.
- dataset record or manifest creation.
- training-data approval.
- training-run approval.
- source approval.
- source ingestion.
- parser / reader / ingestion implementation.
- actual feature extraction.
- actual label generation.
- real Tenhou, real haifu, external logs or platform data access.
- account, session, cookie or token handling.
- broad file ingestion.
- CLI data paths.
- model-output integration.
- model architecture, dataloader, optimizer, loss, trainer, checkpoint or
  weights.
- training, tuning, self-play, league, runner behavior or P8-P12 work.
- third-party binary, `system.exe`, `libai.so`, `params/`, unknown `*.pth`,
  `*.pt`, checkpoint or snapshot use.

## Stop Conditions

Stop before commit if any of these appear:

- new production code.
- new tests, fixtures or data files.
- dataset records, feature tensors, labels, targets, examples or splits.
- dataset or split manifest creation.
- leakage-check implementation.
- real or external source file reads.
- source approval, source ingestion approval or parser / reader / ingestion
  approval by implication.
- actual feature extraction or label generation approval by implication.
- training-data approval or training-run approval by implication.
- model-output integration, CLI, broad ingestion, self-play, league or P8-P12
  drift.
- model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ comparison or
  candidate-promotion claims.

## Risk Controls

| Risk | Control |
|---|---|
| Boundary definition is mistaken for dataset approval. | This document repeats that no implementation or approval is granted. |
| Current smoke fixture is treated as training data. | The current smoke fixture is classified as synthetic/local smoke only. |
| Split policy is underdefined before future training. | Split unit, seed, grouping and duplicate policy must be part of future approval. |
| Hidden/future/target leakage enters future features. | Future approval must include explicit leakage validation plan fields. |
| Same game/table/hand crosses splits. | Future split policy must define grouping constraints. |
| Real or external data is read too early. | Real/external/platform sources remain blocked until source-specific approvals. |
| Parser or feature work is smuggled into dataset code. | Future dataset tasks may consume only approved feature and label outputs. |
| Evidence is overclaimed. | Evidence grade is boundary definition only and explicit non-evidence is listed below. |

## Evidence Requirements

Future dataset / split / leakage work must record:

- source approvals.
- parser / reader / ingestion approvals.
- feature extraction approvals.
- label generation approvals.
- exact implementation files.
- exact inputs.
- schema versions.
- provenance fields.
- storage policy.
- split policy.
- leakage validation plan.
- validation commands.
- `git diff --check`.
- relevant unit tests.
- evidence refs.
- risk refs.
- decision refs.

For this docs-only task, validation is limited to documentation consistency and
the existing synthetic/local schema tests.

## First Task Candidate

The next safe task is:

```text
Review broader P7 supervised dataset construction, split and leakage boundary before implementation.
```

That next task should be docs-only. It should review this document, confirm
whether the boundary can close and define the next P7-only task without
implementing dataset construction, split creation, leakage checks, feature
extraction, label generation or training.

## Planning Decision

```text
Broader P7 supervised dataset construction, split and leakage boundary is defined before implementation. This does not approve supervised dataset construction, split creation, leakage-test implementation, training-data construction, training, source approval, source ingestion, parser, dataset reader, ingestion, actual feature extraction, actual label generation, model architecture, model-output integration, self-play, league or P8-P12 entry.
```

## Evidence Grade

```text
Broader P7 supervised dataset construction, split and leakage boundary definition evidence only.
```

## Explicit Non-Evidence

This document is not:

- supervised dataset construction implementation.
- split creation.
- leakage-test implementation.
- source approval.
- source ingestion approval.
- parser / reader / ingestion approval.
- actual feature extraction approval.
- actual label generation approval.
- training-data approval.
- training-run approval.
- model architecture approval.
- trainer approval.
- real Tenhou evidence.
- real haifu evidence.
- external-log evidence.
- platform-data evidence.
- model-output integration evidence.
- self-play or league evidence.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- P8-P12 entry evidence.
