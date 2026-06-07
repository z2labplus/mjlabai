# 02Q_P6_NEXT_CURRENT_SCOPE_DATA_SYSTEM_TASK_AFTER_MINIMAL_REPLAY_SCHEMA_ACCEPTANCE

## Scope

This document defines the next P6 current-scope data-system task after the
minimal replay schema and project-authored synthetic/local replay fixture were
accepted as current-scope complete in `02P`.

This is a docs-only task-definition gate. It does not:

- add production code.
- add tests.
- add fixtures or data files.
- modify `src/mjlabai/data/replay_schema.py`.
- modify `tests/fixtures/data/synthetic_replay_smoke.json`.
- modify `tests/data/test_replay_schema.py`.
- modify `tests/data/test_synthetic_replay_fixture_schema.py`.
- close full P6.
- approve the next implementation task.
- implement parser, dataset reader, data ingestion, feature extraction or label
  generation.
- read real Tenhou, real haifu, external logs or platform data.
- use account, session, cookie, token or private-log data.
- add model-output integration, CLI or broad file ingestion.
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.

North-star relationship:

```text
This task-definition gate supports the long-term stable-dan > 10.68 target by
keeping P6 data-system work bounded, auditable and staged before any broader
data, training or later-stage work. It is not strength evidence.
```

## Accepted Current Scope From 02P

Accepted current scope:

- minimal replay schema module current-scope complete.
- project-authored synthetic/local replay fixture current-scope complete.
- two minimal local tests current-scope complete.
- directly related governance synchronization current-scope complete.

Not accepted:

- full P6 closure.
- additional replay schema expansion.
- additional fixtures.
- additional tests.
- parser.
- dataset reader.
- data ingestion.
- feature extraction.
- label generation.
- real data.
- CLI.
- model-output integration.
- training, self-play or league.
- P7-P12.
- model-strength evidence.
- Tenhou ranked evidence.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.

## Candidate Next Tasks

| candidate_task | task_type | why_considered | risk | too_early? | recommendation |
|---|---|---|---|---|---|
| Define P6 replay schema validation error taxonomy and reporting boundary. | docs-only taxonomy / reporting boundary | The minimal schema helper now raises validation errors; a future taxonomy could make later reporting more consistent. | It may pull the project toward code-level error APIs or implementation changes too soon. | Slightly early before P6 current-scope closure criteria exist. | Defer until after closure criteria clarify whether another P6 current-scope item is required. |
| Define P6 synthetic replay fixture coverage review checklist. | docs-only review checklist | A checklist could help review future synthetic fixtures without using real data. | It may imply additional fixture work before deciding whether current P6 should close. | Slightly early. | Defer; useful if the next closure criteria say more fixture review is needed. |
| Define P6 current-scope data-system closure criteria after minimal replay schema acceptance. | docs-only closure criteria | The exact minimal schema/fixture work is accepted, but full P6 is not closed. Closure criteria prevent P6 from extending indefinitely and clarify what remains before any transition. | If written too broadly, it could become a hidden approval for parser, reader or ingestion work. | No. This is the safest next planning step. | Recommended next task. |
| Define P6 data-system evidence taxonomy for schema/fixture smoke artifacts. | docs-only evidence taxonomy | P6 evidence labels should remain conservative across schema, fixture and future data-system tasks. | Evidence taxonomy may be premature unless closure criteria show a specific evidence gap. | Slightly early. | Defer as a possible follow-up if closure criteria reveal taxonomy drift. |
| Define P6 next implementation approval criteria for additional synthetic-only data-system work. | docs-only approval criteria | If more synthetic-only implementation is needed, approval criteria will be required. | Too close to approving implementation before deciding whether current-scope P6 should close. | Yes. | Defer until closure criteria justify additional implementation. |

## Recommended Next Task

```text
Define P6 current-scope data-system closure criteria after minimal replay schema acceptance.
```

## Rationale

The minimal replay schema module, project-authored synthetic/local replay
fixture and two minimal local tests are already accepted as current-scope
complete. The project should now avoid turning P6 into an endless chain of
schema, fixture and review gates.

Closure criteria are the most conservative next task because they:

- keep the next step docs-only.
- do not approve new implementation.
- clarify whether current P6 has enough synthetic/local groundwork to close
  the current scope.
- separate current-scope closure from full data-system ambitions such as
  parser, dataset reader, ingestion, feature extraction and label generation.
- keep real Tenhou, real haifu, external logs, platform data and P7-P12
  closed.
- force any future implementation to pass a later explicit approval decision
  instead of slipping in through planning language.

## Allowed Scope For Next Task

The next task may:

- review the current accepted P6 artifacts.
- define current-scope P6 data-system closure criteria.
- define an exit readiness checklist for the current synthetic/local P6 scope.
- classify optional deferred items.
- clarify what must remain closed after current-scope P6 closure.
- update handoff, docs index, `10_NEXT`, technical plan and governance docs.
- run existing validation commands only:
  - `git diff --check`
  - `python3 -m unittest tests/data/test_replay_schema.py`
  - `python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py`

## Forbidden Scope For Next Task

The next task must not:

- add production code.
- add tests.
- add fixtures.
- add data files.
- modify `src/mjlabai/data/replay_schema.py`.
- modify `tests/fixtures/data/synthetic_replay_smoke.json`.
- modify `tests/data/test_replay_schema.py`.
- modify `tests/data/test_synthetic_replay_fixture_schema.py`.
- expand replay schema implementation.
- implement parser.
- implement dataset reader.
- implement data ingestion.
- implement feature extraction.
- implement label generation.
- read real Tenhou.
- read real haifu.
- read external logs.
- read platform data.
- use account, session, cookie, token or private-log data.
- create platform automation, scraping, evasion, anti-detection or account
  tooling.
- add model-output integration.
- add CLI.
- add broad file ingestion.
- add latency measurement.
- add fixed-position exact-match computation.
- implement metrics.
- modify metric registry code, units, directions or definitions.
- modify promotion criteria or evidence taxonomy definitions.
- call OpenAI, LLM, model, Akochan `system.exe`, `libai.so` or third-party
  binary paths.
- download or use unknown model weights, `*.pth`, `*.pt`, `checkpoint` or
  `snapshot` files.
- vendor or copy third-party source, binaries, `params/` or build artifacts.
- train, tune, self-play, run league or runner behavior.
- enter P7-P12.
- claim model strength, Tenhou ranked evidence, stable-dan ranked-game
  evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.
- write current-scope closure criteria as full P6 closure.
- write closure criteria as implementation approval.

## Validation Commands For Next Task

The next task must run at least:

```bash
git diff --check
python3 -m unittest tests/data/test_replay_schema.py
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py
```

The next task must not run:

- real-data commands.
- Tenhou commands.
- self-play.
- league.
- training.
- model-output integration.
- Akochan `system.exe`.
- `libai.so`.
- third-party binary commands.
- unknown model artifact commands.

## Stop Conditions

Stop before commit if any of the following appears:

- code, test, fixture or data-file modification.
- real, external or platform data.
- account, session, cookie, token or private-log content.
- parser, reader or ingestion behavior.
- feature or label behavior.
- model-output path.
- CLI or broad file ingestion.
- metric implementation or registry code changes.
- validation failure.
- governance mismatch.
- overclaim.
- P7-P12 drift.
- model-strength, Tenhou ranked, stable-dan ranked-game, LuckyJ `10.68` or
  candidate-promotion claim.

## Evidence Grade

```text
P6 next current-scope data-system task definition after minimal replay schema
acceptance evidence only.
```

## Planning Decision

```text
The next P6 current-scope data-system task is defined as a docs-only follow-up
after minimal replay schema acceptance.
```

The selected next task is:

```text
Define P6 current-scope data-system closure criteria after minimal replay schema acceptance.
```

This does not approve new implementation, parser, dataset reader, ingestion,
feature extraction, label generation, real data, model-output integration or
P7-P12.

## Explicit Non-Evidence

This task-definition document is not evidence of:

- full P6 closure.
- new implementation approval.
- parser.
- dataset reader.
- data ingestion.
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
- model strength.
- Tenhou ranked performance.
- stable-dan ranked-game evidence.
- LuckyJ `10.68` comparison.
- candidate-promotion evidence.
- P7-P12 entry approval.
