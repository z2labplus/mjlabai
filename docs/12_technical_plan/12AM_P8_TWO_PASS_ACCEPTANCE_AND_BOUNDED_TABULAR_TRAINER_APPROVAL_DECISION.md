# 12AM_P8_TWO_PASS_ACCEPTANCE_AND_BOUNDED_TABULAR_TRAINER_APPROVAL_DECISION

## Decision

```text
ACCEPTED as current-scope complete.
Approved for next exact bounded implementation task.
```

The exact `12AK` implementation reviewed in `12AL` is accepted only for its
fixed two-pass synthetic/local table-state scope.

The next executable task is:

```text
Implement exact bounded P8 synthetic/local tabular trainer smoke only.
```

This is the first approved loop-based training smoke in P8. No proposal,
boundary or additional approval may be inserted before implementation.

## Why This Outcome

The reviewed fixed sequence proves repeated state continuity. A bounded
trainer is now the smallest non-repetitive increment: it applies the reviewed
table updater over a variable but strictly capped in-memory tuple of synthetic
traces. This provides executable training-loop behavior without adding a
model/network, optimizer, environment, replay buffer, file ingestion,
persistence, self-play or production training system.

Another fixed-pass wrapper is forbidden.

## Exact Approved Files

The implementation may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_tabular_trainer_smoke.py`
- `tests/rl/test_synthetic_tabular_trainer_smoke.py`
- direct docs/governance synchronization required by repository rules.

No fixture, data file, dependency, CLI, path reader, persistence or artifact
file is approved.

## Exact Public API

The new module may export only:

```text
SYNTHETIC_TABULAR_TRAINER_SMOKE_VERSION
MAX_SYNTHETIC_TABULAR_TRAINING_PASSES
SyntheticTabularTrainerSmokeError
SyntheticTabularTrainingResult
train_synthetic_policy_table_smoke
```

It must reuse:

- `SyntheticPolicyTableEntry`
- `SyntheticPolicyTableUpdateResult`
- `SyntheticPolicyTableUpdateSmokeError`
- `apply_synthetic_policy_table_update_smoke`

It must not copy any single-step, trace or table-update calculation.

## Exact Input Boundary

The helper signature is:

```text
train_synthetic_policy_table_smoke(
    initial_entries,
    training_traces,
    *,
    learning_rate,
    discount_factor,
)
```

`initial_entries` must be the exact two-entry tuple accepted by the reviewed
table helper.

`training_traces` must be an exact tuple containing from 1 through 8 exact
four-record trace tuples. The hard cap is exposed only as:

```text
MAX_SYNTHETIC_TABULAR_TRAINING_PASSES = 8
```

Each pass consumes the final table entries from the previous pass. All record
IDs across all validated passes must be pairwise distinct.

Lists, mappings, strings, bytes, bytearrays, paths, generators, tuple
subclasses and arbitrary iterables are rejected for the outer tuple. Inner
trace validation remains owned by the reviewed table/trace helpers.

## Exact Semantics

The trainer must:

1. validate the exact outer tuple and `1 <= pass_count <= 8`.
2. initialize current entries from `initial_entries`.
3. iterate traces once in input order using one bounded standard-library loop.
4. call `apply_synthetic_policy_table_update_smoke` once per pass.
5. use each pass result's final entries as the next pass's initial entries.
6. wrap helper failures with one-based pass index and chained cause.
7. reject duplicate record IDs across all validated pass results.
8. return one frozen deterministic result without mutating any input.

No shuffle, retry, early stopping, convergence criterion, random sampling,
minibatch, optimizer, gradient, checkpoint or resume behavior is approved.

## Exact Result

`SyntheticTabularTrainingResult` must be frozen and contain only:

```text
trainer_version
pass_count
max_passes
initial_entries
final_entries
pass_results
record_ids
training_applied
safety_guardrails_all_satisfied
evidence_grade
warnings
```

Requirements:

- `1 <= pass_count <= 8` and `max_passes = 8`.
- initial/final entries are exact frozen two-entry tuples.
- `pass_results` is a tuple of reviewed table-update results in input order.
- `record_ids` is a flat tuple of `4 * pass_count` validated distinct IDs.
- `training_applied = true`.
- `safety_guardrails_all_satisfied = true`.

Warnings must include at least:

- bounded synthetic/local tabular training smoke only.
- maximum eight ordered in-memory passes.
- no shuffle, minibatch, optimizer, checkpoint or resume.
- not a model/network training system.
- not an environment, episode, replay buffer or self-play.
- not production training or evaluation.
- not model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

## Exact Test Requirements

The focused test module must cover:

1. exact one-pass training output.
2. exact two-pass state values `(2,10) -> (4,6.25) -> (6,3.75)`.
3. lower/upper pass limits: empty and nine rejected, eight accepted.
4. exact outer tuple/type and tuple-subclass rejection.
5. inner trace errors wrapped with one-based pass index and cause.
6. exact table-state continuity across passes for both keys.
7. pairwise-distinct IDs across every accepted pass.
8. helper call count equals pass count, deterministic order and no duplicated
   formula/trace/table logic.
9. deterministic repeated output, complete input immutability and frozen
   output.
10. exact result fields/shapes/counts, evidence grade and warnings.
11. package imports, narrow API and absence of file/persistence/environment/
    replay/self-play/model/network/optimizer/checkpoint/evaluation APIs.

Validation must include the 101 currently approved tests, the new focused
tests, compile checks and `git diff --check`.

## Forbidden Scope

This approval does not permit:

- more than eight passes or an unbounded/while loop.
- shuffle, minibatch, retry, early stopping, convergence or scheduling.
- mutable/dynamic table API, mapping API, persistence, dataset or dataloader.
- replay buffer, environment, episode, gameplay, legality or action selection.
- self-play, model/network, tensor, autograd, gradient or optimizer.
- checkpoint/resume/artifact creation or use.
- production training/evaluation, metrics or candidate selection.
- path/CLI, dependency, timing, concurrency, GPU/distributed or third-party
  binary/service use.
- real Tenhou/haifu, external logs, platform data, accounts or secrets.
- broad P8, league, strength claims or P9-P12.

## Rollback And Stop Conditions

If implementation needs any unapproved file, input shape, behavior,
dependency or evidence claim, stop before commit and record one exact blocker
without silently widening scope.

## Evidence Grade

Current decision evidence:

```text
P8 fixed two-pass current-scope acceptance and bounded synthetic/local
tabular-trainer task approval evidence only.
```

Future passing implementation evidence:

```text
P8 bounded synthetic/local tabular training-loop smoke evidence only.
```

Neither is model/network training, environment, self-play, production
training, model-strength, Tenhou ranked, stable-dan, LuckyJ comparison,
candidate-promotion or P9-P12 evidence.

## Gate Accounting

```text
fixed two-pass current-scope acceptance = satisfied by this decision
bounded trainer approval = satisfied by this decision
exact file/API/input/output/test boundaries = satisfied by this decision
remaining mandatory gate count before trainer implementation = 0
```

No gate is satisfied for broader P8.
