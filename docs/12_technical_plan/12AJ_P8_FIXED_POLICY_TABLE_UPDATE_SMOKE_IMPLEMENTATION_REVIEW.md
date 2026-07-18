# 12AJ_P8_FIXED_POLICY_TABLE_UPDATE_SMOKE_IMPLEMENTATION_REVIEW

## Scope

This document reviews only commit
`27a1ad9b52627934781f8c0a1a8850692a5c679d` against the exact `12AI`
approval. It does not modify production code or tests and does not approve a
broader P8 scope.

Reviewed implementation files:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_table_update_smoke.py`
- `tests/rl/test_synthetic_policy_table_update_smoke.py`

## Findings

No correctness, scope, provenance, evidence or test blocker was found.

## Approval Compliance

| Requirement | Evidence | Result |
|---|---|---|
| Exact approved files | one table module, one package export update and one focused test module | Pass |
| Exact public API | version, frozen entry, table error, frozen result and apply helper only in module `__all__` | Pass |
| Exact table input | runtime requires an exact tuple of exactly two exact entry objects | Pass |
| Exact entry fields | identifiers are exact strings; values are exact finite floats | Pass |
| Exact trace input | the reviewed trace helper enforces the exact four-record tuple and all trace guardrails | Pass |
| A/B key binding | both table keys must equal reviewed trace keys in order | Pass |
| Initial-value binding | both table values must exactly equal reviewed trace initial values | Pass |
| Helper reuse | the table helper calls the reviewed trace helper exactly once; no update formula is duplicated | Pass |
| Error surface | trace failures are wrapped with chained cause | Pass |
| Determinism / immutability | frozen inputs/results, normalized new entries and repeated-call equality are tested | Pass |
| Exact output | frozen result has only the `12AI` fields, two initial/final entries, safe grade and warnings | Pass |
| Package export | all five approved table symbols import through `mjlabai.rl` | Pass |
| Forbidden scope | no mapping/dynamic table/persistence/path/dependency/environment/replay/self-play/model/trainer API | Pass |

## Validation Evidence

Passed:

```text
python3 -m unittest tests/rl/test_synthetic_policy_table_update_smoke.py      # 11
python3 -m unittest tests/rl/test_synthetic_policy_update_trace_smoke.py      # 11
python3 -m unittest tests/rl/test_synthetic_policy_update_sequence_smoke.py   # 10
python3 -m unittest tests/rl/test_synthetic_policy_update_smoke.py            # 12
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke_extension.py  # 15
python3 -m unittest tests/supervised/test_synthetic_parser_reader_smoke.py            # 11
python3 -m unittest tests/supervised/test_feature_label_schema.py                     # 11
python3 -m unittest tests/supervised/test_synthetic_supervised_fixture_schema.py       # 1
python3 -m unittest tests/data/test_replay_schema.py                                   # 7
python3 -m unittest tests/data/test_synthetic_replay_fixture_schema.py                 # 1
python3 -m compileall -q src/mjlabai/rl tests/rl
git diff --check
```

Total approved unit tests: 90.

Independent in-memory probes passed for:

- exact final values `(4.0, 6.25)`.
- exactly one trace-helper call.
- tuple-subclass rejection.
- normalized new initial entries and complete input non-mutation.
- trace-error wrapping with chained cause.
- absence of file, dependency, nondeterminism and persistence APIs.

No external input, file path, model, environment or platform service was used.

## Review Decision

```text
A. Review can close.
```

The exact fixed two-key table implementation conforms to `12AI`. No
production code or test fix is required.

## Evidence Grade

```text
P8 exact synthetic/local fixed two-key policy-value table update smoke
implementation review closure evidence only.
```

This is not a persistent policy/model/checkpoint, environment, replay buffer,
self-play system, RL training loop, model-strength evidence, Tenhou ranked
evidence, stable-dan evidence, LuckyJ comparison, candidate-promotion evidence
or P9-P12 evidence.

## Next-Step Constraint

The next task must decide current-scope acceptance and directly approve one
materially progressive executable P8 task if accepted. It must not create
another sibling proposal or boundary.

```text
remaining mandatory gate count before a new exact code task = 1
exit criterion = accept or reject the reviewed scope and bind the exact next
                 executable outcome, files, tests and stop conditions
```

Broad P8, environment/gameplay, self-play, model/optimizer, production
training/evaluation, real/external/platform data and P9-P12 remain unapproved.
