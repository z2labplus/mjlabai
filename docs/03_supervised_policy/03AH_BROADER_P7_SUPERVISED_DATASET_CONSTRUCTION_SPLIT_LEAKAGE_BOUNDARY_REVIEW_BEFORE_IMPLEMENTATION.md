# 03AH Broader P7 Supervised Dataset Construction Split Leakage Boundary Review Before Implementation

## Scope

This document reviews
`docs/03_supervised_policy/03AG_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_BEFORE_IMPLEMENTATION.md`.

It is a docs-only review gate. It does not implement or approve supervised
dataset construction, split creation, leakage-test implementation,
training-data construction, training, source approval, source ingestion,
parser / reader / ingestion, actual feature extraction, actual label
generation, feature tensors, labels, targets, examples, dataset manifests,
model architecture, model-output integration, self-play, league or P8-P12
entry.

## Review Inputs

- `docs/03_supervised_policy/03AG_BROADER_P7_SUPERVISED_DATASET_CONSTRUCTION_SPLIT_LEAKAGE_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AF_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AE_BROADER_P7_FEATURE_AND_LABEL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AD_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AC_BROADER_P7_PARSER_READER_INGESTION_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AB_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_REVIEW_BEFORE_IMPLEMENTATION.md`
- `docs/03_supervised_policy/03AA_BROADER_P7_DATA_SOURCE_READINESS_AND_SOURCE_APPROVAL_BOUNDARY_BEFORE_IMPLEMENTATION.md`
- `src/mjlabai/supervised/feature_label_schema.py`
- `tests/fixtures/supervised/synthetic_supervised_smoke.json`
- `tests/supervised/test_feature_label_schema.py`
- `tests/supervised/test_synthetic_supervised_fixture_schema.py`
- `src/mjlabai/data/replay_schema.py`
- `tests/data/test_replay_schema.py`
- `tests/data/test_synthetic_replay_fixture_schema.py`

The code, tests and fixtures above were read for context only. This review
does not modify them and does not treat them as supervised datasets or
training data.

## Review Questions

| Question | Review finding |
|---|---|
| Is `03AG` scope correct? | Yes. It is explicitly docs-only boundary definition before implementation. |
| Does it state this is not supervised dataset construction approval? | Yes. The scope, boundary, forbidden scope, stop conditions and explicit non-evidence sections repeat that no dataset construction is approved. |
| Does it state this is not split creation approval? | Yes. The split boundary defines future split-policy requirements and says no split or split manifest is created. |
| Does it state this is not leakage-test implementation approval? | Yes. Leakage categories are defined, but exact checks and implementation remain separate future approvals. |
| Does it state this is not training-data approval? | Yes. Training-data approval and training-run approval are separated from source, ingestion, feature, label, dataset and split approvals. |
| Is the purpose sufficient? | Yes. It ties dataset, split and leakage controls to the north-star route while preventing boundary evidence from becoming training or strength claims. |
| Is the current dataset / split / leakage status accurate? | Yes. It records no approved dataset, examples, tensors, labels, splits, manifests, leakage implementation, training data or training run. |
| Are concept definitions clear? | Yes. Dataset construction, examples, tensors, labels, manifests, split units, holdouts and leakage categories are not used interchangeably. |
| Is the dependency map reasonable? | Yes. It preserves source readiness, source approval, parser / reader / ingestion, feature extraction, label generation, dataset boundary, split / leakage policy, implementation review, training-data approval and training-run approval as separate gates. |
| Is the dataset construction boundary sufficient? | Yes. Future dataset code may only consume separately approved feature and label outputs and must stop before training-data and training-run approvals. |
| Is the split boundary sufficient? | Yes. It requires explicit split unit, deterministic / auditable behavior, seed if random, grouping constraints and duplicate controls. |
| Is the leakage boundary sufficient? | Yes. It covers hidden-info, future-info, target, label, source, duplicate, same-game, temporal, model-output, self-play, league, privacy and synthetic-smoke leakage. |
| Are future approval-record fields sufficient? | Yes. They cover component identity, dependencies, schemas, split policy, leakage plan, storage, validation, evidence, risks, decisions, rollback, stop conditions and human / Web ChatGPT approval references. |
| Are candidate dataset / split / leakage classes safe? | Yes. Candidate classes are marked not approved now; real/external/platform/model-output/self-play/league classes are blocked, deferred or later-stage. Validator sub-classes such as duplicate detection, provenance split validation, feature-label alignment validation and temporal-order validation remain future leakage/split approval details, not current implementation. |
| Is allowed future implementation boundary conservative? | Yes. It allows only later exact-scope tasks and examples such as synthetic/local shape smoke or approved-source manifests after all upstream approvals. |
| Is forbidden scope strict enough? | Yes. It blocks dataset implementation, split creation, leakage checks, tensors, labels, targets, examples, manifests, source approval, ingestion, real data, CLI, model code, training, self-play, league, third-party artifacts and P8-P12. |
| Are stop conditions sufficient? | Yes. Stop conditions catch code, tests, fixtures, data files, examples, splits, manifests, leakage checks, real reads, approvals by implication, model-output paths, overclaiming and stage drift. |
| Are risk controls complete for this gate? | Yes. They cover approval confusion, smoke-as-training-data, underdefined split policy, leakage, same-game contamination, real-data drift, smuggled parser / feature work and evidence overclaiming. |
| Are evidence requirements sufficient? | Yes. Future work must record approvals, schemas, provenance, storage, split policy, leakage plan, validation, evidence, risks and decisions. |
| Is the first task candidate reasonable? | Yes. A docs-only review gate was the correct next step and this document performs that review. |
| Is the planning decision conservative? | Yes. It defines boundary only and denies all implementation, approval and strength claims. |
| Is the evidence grade correct? | Yes. It is broader P7 dataset construction, split and leakage boundary definition evidence only. |
| Is governance synchronization consistent? | Yes, subject to this review updating handoff, index, `10_NEXT`, technical plan, evidence log, risk register, changelog, decision record, stage contract, milestones and backlog. |

## Review Decision

```text
Review can close.
```

`03AG` is sufficient as a broader P7 supervised dataset construction, split
and leakage boundary before implementation. It is conservative enough to close
the review gate because it keeps all approval types separate, records the
current no-dataset / no-split / no-leakage-implementation status, defines
split and leakage vocabulary, preserves dependency order, blocks real/external
data and P8-P12 drift, and keeps evidence claims limited.

This review does not close full P7. It does not approve broader P7
implementation.

## Current Status After Review

- Full P7 remains open.
- Broader P7 implementation remains unapproved.
- No source is approved for P7 training.
- No source ingestion is approved.
- No parser / reader / ingestion implementation is approved.
- No actual feature extraction is approved.
- No actual label generation is approved.
- No feature tensors, labels, targets or examples are approved.
- No supervised dataset construction is approved.
- No dataset manifest or split manifest is approved.
- No train / validation / test split creation is approved.
- No leakage-test implementation is approved.
- No training-data construction is approved.
- No training run is approved.
- No model architecture, dataloader, optimizer, loss, trainer, checkpoint or
  weights are approved.
- No real Tenhou, real haifu, external logs, platform data, accounts,
  sessions, cookies or tokens are approved.
- No model-output integration, self-play, league or P8-P12 entry is approved.

## Next Task Recommendation

The next safe P7-only task is:

```text
Define broader P7 training-data approval and training-run boundary before implementation.
```

This next task must be docs-only. It should define training-data approval and
training-run boundary vocabulary, dependencies, prerequisites, allowed /
forbidden scope, risk controls and evidence requirements before any training
data or training run can be considered.

It must not approve or implement training-data construction, dataset
construction, split creation, leakage-test implementation, parser / reader /
ingestion, actual feature extraction, actual label generation, model
architecture, dataloader, optimizer, loss, trainer, checkpoint, weights, real
data, model-output integration, self-play, league or P8-P12.

## Evidence Grade

```text
Broader P7 supervised dataset construction, split and leakage boundary review evidence only.
```

## Explicit Non-Evidence

This review is not:

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
- P8-P12 entry evidence.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.

## Validation

This review ran the following local validation commands on 2026-06-28:

```bash
git diff --check
# passed with no output

python3 -m unittest tests/supervised/test_feature_label_schema.py
# Ran 11 tests: OK

python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py
# Ran 1 test: OK

python3 -m unittest tests/data/test_replay_schema.py
# Ran 7 tests: OK

python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
# Ran 1 test: OK
```

They validate that the existing synthetic/local P6/P7 schema smoke paths still
pass. They do not access real data, external logs, Tenhou data, haifu datasets,
training, model execution, self-play, league or P8-P12 behavior.
