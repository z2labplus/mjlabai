# 12D_POST_FULL_P6_TRANSITION_REVIEW

## Scope

This document records the post-full-P6 transition review after the final full
P6 closure review gate.

This is a docs-only transition review. It does not execute P7, approve P7
implementation, approve P7 first-task execution, approve P8-P12 entry, add
production code, add tests, add fixtures, add data files, modify replay schema
code, modify existing data tests, implement parser / dataset reader /
ingestion / feature extraction / label generation, connect model output, add
CLI / broad file ingestion, read real Tenhou / real haifu / external logs /
platform data, use accounts / sessions / cookies / tokens, run training /
tuning / self-play / league / runner behavior, call model APIs or third-party
binaries, or make model-strength claims.

The review only determines whether the project may start a later docs-only
task to define P7 scope, entry criteria and first task before implementation.

## Full P6 Closed Scope

Full P6 is closed only for the documented P6 data-system scope recorded in
`docs/02_data_system/02AA_FINAL_FULL_P6_CLOSURE_REVIEW.md`.

Included closed scope:

- docs/governance/source-rights planning.
- accepted synthetic/local minimal replay schema.
- project-authored synthetic fixture smoke implementation.
- deferred / blocked / later-stage inventory.

Not included in full P6 closure:

- parser.
- dataset reader.
- data ingestion.
- feature extraction.
- label generation.
- real Tenhou.
- real haifu.
- external logs.
- platform data.
- source approval beyond the project-authored synthetic fixture.
- CLI.
- broad file ingestion.
- model-output integration.
- training / tuning.
- self-play.
- league / runner behavior.
- P7-P12.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate promotion.

## Candidate Next Directions

| candidate_direction | fit | risk | stage_creep | implementation_required | docs_only_possible | recommendation |
|---|---|---|---|---|---|---|
| Define P7 scope, entry criteria and first task before implementation. | High: full P6 is closed and P7 needs independent scoping before any supervised-learning work. | Medium if wording is mistaken for P7 execution. | Low if the next task is explicitly docs-only and forbids implementation. | No. | Yes. | Recommended. |
| Prepare P7 transition readiness inventory before scope definition. | Medium: conservative, but much of the readiness inventory is already represented by full P6 closure and this transition review. | Low. | Low. | No. | Yes. | Acceptable fallback, but likely redundant. |
| Continue P6 documentation-only maintenance / archive review. | Low: full P6 closure already passed for documented scope. | Low but may create indefinite P6 churn. | Low. | No. | Yes. | Do not choose now unless a blocker appears. |
| Define a post-P6 governance checkpoint before P7. | Medium: safe, but this transition review already serves that checkpoint. | Low. | Low. | No. | Yes. | Not needed as a separate next task. |
| Defer P7 planning pending human/Web ChatGPT decision. | Medium: maximally conservative. | Low, but stalls progress after closure. | Low. | No. | Yes. | Not needed because this review can select a docs-only P7 scoping task. |

## P7 Scoping Decision

```text
Yes, define P7 scope / entry criteria / first task as docs-only next task.
```

Rationale:

- Full P6 is closed for the documented P6 data-system scope.
- P7-P12 remain unapproved until independent scope, entry criteria, risk
  review and first-task boundaries are documented and reviewed.
- The next task will be docs-only.
- The next task will not execute P7.
- The next task will not approve P7 implementation.
- The next task will not train, tune, self-play or run league behavior.
- The next task will not use real data, parser, dataset reader, ingestion,
  feature extraction, label generation, model-output integration, CLI or broad
  ingestion.
- P7 scope can be defined without executing it.

## Why Not P7 Implementation Yet

P7 supervised learning requires independent scope, entry criteria, risk review,
source/data readiness, feature/label readiness and first-task approval.

Full P6 closure does not provide:

- training dataset approval.
- parser approval.
- dataset reader approval.
- data ingestion approval.
- feature extraction approval.
- label generation approval.
- real Tenhou approval.
- real haifu approval.
- external-log approval.
- platform-data approval.
- model-output integration approval.
- model-strength evidence.

Therefore only docs-only P7 scoping can be considered next. P7 implementation
must wait for a later task that explicitly approves implementation scope after
the P7 scope / entry criteria / first-task definition is written and reviewed.

## Recommended Next Task

Recommended next task:

```text
Define P7 scope, entry criteria and first task before implementation.
```

This is a planning task only. It must not execute P7 or approve P7
implementation.

## Allowed Scope For Next Task

The next task may:

- define P7 purpose and north-star relationship.
- define P7 entry criteria.
- define P7 forbidden scope.
- define P7 required inputs.
- define P7 risk review requirements.
- define P7 first task candidate.
- define evidence requirements for future P7 work.
- update handoff, docs index, `10_NEXT`, technical plan and governance docs.
- run existing validation commands only.

## Forbidden Scope For Next Task

The next task must not:

- add production code.
- add tests.
- add fixtures.
- add data files.
- modify replay schema code.
- modify existing data tests.
- train models.
- tune hyperparameters.
- start self-play.
- run league or runner behavior.
- use real Tenhou.
- use real haifu.
- use external logs.
- use platform data.
- use account / session / cookie / token data.
- implement parser.
- implement dataset reader.
- implement data ingestion.
- implement feature extraction.
- implement label generation.
- connect model output.
- add CLI.
- add broad file ingestion.
- call OpenAI / LLM / model APIs.
- call Akochan `system.exe`, `libai.so` or third-party binaries.
- use unknown model weights, `*.pth`, `*.pt`, checkpoints or snapshots.
- vendor third-party source, binaries, `params/` or build artifacts.
- enter P8-P12.
- make model-strength claims.
- make Tenhou ranked claims.
- make stable-dan ranked-game claims.
- make LuckyJ `10.68` comparison claims.
- make candidate-promotion claims.

## Validation Commands For Next Task

The next task should run:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

It must not run real-data, Tenhou, self-play, league, training,
model-output-integration, Akochan `system.exe`, `libai.so`, third-party binary
or unknown model artifact commands.

## Planning Decision

```text
Post-full-P6 transition review is complete. Full P6 is closed only for the
documented P6 data-system scope. P7-P12 remain unapproved unless a later
docs-only P7 scope / entry criteria / first task task is completed and
separately reviewed. This task does not approve P7 implementation, training,
self-play, league, real data, parser, reader, ingestion, feature extraction,
label generation, model-output integration, CLI or model-strength claims.
```

## Evidence Grade

```text
Post-full-P6 transition review evidence only.
```

## Explicit Non-Evidence

This transition review is not:

- P7-P12 entry approval.
- P7 implementation.
- P7 first-task execution.
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
- CLI.
- broad file ingestion.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
