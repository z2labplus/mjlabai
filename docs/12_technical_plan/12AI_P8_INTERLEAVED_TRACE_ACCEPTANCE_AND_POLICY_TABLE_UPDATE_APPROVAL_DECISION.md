# 12AI_P8_INTERLEAVED_TRACE_ACCEPTANCE_AND_POLICY_TABLE_UPDATE_APPROVAL_DECISION

## Decision

```text
ACCEPTED as current-scope complete.
Approved for next exact minimal implementation task.
```

The exact `12AG` implementation reviewed in `12AH` is accepted only for its
fixed four-record A/B/A/B synthetic/local numerical trace scope.

The next executable task is:

```text
Implement exact minimal P8 synthetic/local fixed two-key policy-value table
update smoke only.
```

This decision is the only approval gate for that task. No proposal, boundary
or additional approval may be inserted before implementation.

## Why This Outcome

The reviewed trace already proves independent value continuity for two keys.
The next useful increment is to bind those keys to one immutable, explicitly
provided two-entry policy-value table and return the updated table. This tests
a minimal parameter-state transition without adding a generic batch, epoch,
trainer, model, environment, replay buffer or persistence layer.

Merely extending the trace with more records is rejected as repetitive.

## Exact Approved Files

The implementation may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_table_update_smoke.py`
- `tests/rl/test_synthetic_policy_table_update_smoke.py`
- direct docs/governance synchronization required by repository rules.

No fixture, data file, dependency, CLI, path reader or persistence file is
approved.

## Exact Public API

The new module may export only:

```text
SYNTHETIC_POLICY_TABLE_UPDATE_SMOKE_VERSION
SyntheticPolicyTableEntry
SyntheticPolicyTableUpdateSmokeError
SyntheticPolicyTableUpdateResult
apply_synthetic_policy_table_update_smoke
```

It must reuse:

- `SyntheticPolicyUpdateInput`
- `SyntheticPolicyUpdateTraceResult`
- `SyntheticPolicyUpdateTraceSmokeError`
- `apply_synthetic_policy_update_trace_smoke`

It must not copy the single-step formula or reimplement the four-record trace.

## Exact Input Boundary

The helper signature is:

```text
apply_synthetic_policy_table_update_smoke(
    initial_entries,
    input_records,
    *,
    learning_rate,
    discount_factor,
)
```

`initial_entries` must be an exact tuple of exactly two frozen
`SyntheticPolicyTableEntry` objects in key-A/key-B order. Each entry has only:

```text
state_id
action_id
action_value
```

Entry identifiers must be exact strings and must match the trace's validated
two state-action keys in order. `action_value` must be an exact finite float
and must exactly match the trace's corresponding initial action value.

`input_records` must be the exact four-record tuple accepted by the reviewed
trace helper. The table helper must not weaken or duplicate those checks.

Lists, mappings, strings, bytes, bytearrays, paths, generators, tuple
subclasses and arbitrary iterables are rejected for both tuple inputs.

## Exact Semantics

The helper must:

1. validate the exact two-entry tuple shape and exact entry field types.
2. call `apply_synthetic_policy_update_trace_smoke` exactly once.
3. wrap a trace failure as `SyntheticPolicyTableUpdateSmokeError` with the
   original trace error chained as the cause.
4. require entry keys to exactly equal trace keys A/B in order.
5. require entry values to exactly equal trace initial values A/B.
6. construct two new frozen final entries using the trace final values.
7. return one frozen deterministic result without mutating either input.

No table lookup, insertion, deletion, dynamic key count, repeated epoch,
optimizer state, persistence or in-place update is approved.

## Exact Result

`SyntheticPolicyTableUpdateResult` must be frozen and contain only:

```text
table_update_version
entry_count
initial_entries
final_entries
trace_result
update_applied
safety_guardrails_all_satisfied
evidence_grade
warnings
```

Required fixed values and shapes:

- `entry_count = 2`.
- `initial_entries` and `final_entries` are exact two-entry tuples in A/B
  order and are newly normalized frozen entries.
- `trace_result` is the reviewed trace helper result.
- `update_applied = true`.
- `safety_guardrails_all_satisfied = true`.

Warnings must include at least:

- synthetic/local fixed two-key policy-value table update smoke only.
- not a persistent policy, model or checkpoint.
- not an environment, episode or replay buffer.
- not self-play.
- not a variable batch, epoch or production training loop.
- not model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

## Exact Test Requirements

The focused test module must cover:

1. exact initial/final A/B table values using the reviewed trace.
2. exact tuple length/type and tuple-subclass rejection for both inputs.
3. exact frozen entry type and exact string/finite-float field requirements.
4. exact A/B key order and mismatch rejection.
5. exact initial-value continuity and mismatch rejection for both entries.
6. exactly one trace-helper call and no duplicated update formula/trace logic.
7. trace-error wrapping with chained cause.
8. deterministic repeated output, input immutability and frozen outputs.
9. exact result fields/shapes, evidence grade and warnings.
10. package imports and narrow public API.
11. absence of path/fixture/persistence/dependency/environment/episode/replay/
    self-play/model/optimizer/trainer/training APIs.

Validation must include the 79 currently approved tests, the new focused
tests, compile checks and `git diff --check`.

## Forbidden Scope

This approval does not permit:

- variable table size, mutable table, mapping API or persistence.
- generic batch/epoch/trainer, replay buffer, dataset or dataloader.
- environment, episode, gameplay, observation, legality or action selection.
- self-play, model/network, tensor, autograd, gradient or optimizer.
- production training/evaluation, checkpoint or artifact creation/use.
- path/CLI, dependency, nondeterminism, timing, concurrency, GPU/distributed
  work or third-party binary/service use.
- real Tenhou/haifu, external logs, platform data, accounts or secrets.
- broad P8, league, strength claims or P9-P12.

## Rollback And Stop Conditions

If implementation needs any unapproved file, input shape, behavior,
dependency or evidence claim:

- stop before commit.
- do not widen scope silently.
- record one exact blocker and create only one exact fix/defer task.
- remove only task-owned changes if rollback is required.

## Evidence Grade

Current decision evidence:

```text
P8 exact interleaved-trace current-scope acceptance and fixed policy-table
update task approval evidence only.
```

Future passing implementation evidence:

```text
P8 synthetic/local fixed two-key policy-value table update smoke evidence
only.
```

Neither is environment, self-play, production training, model-strength,
Tenhou ranked, stable-dan, LuckyJ comparison, candidate-promotion or P9-P12
evidence.

## Gate Accounting

```text
interleaved-trace current-scope acceptance = satisfied by this decision
next exact task approval = satisfied by this decision
next exact file/API/input/output/test boundaries = satisfied by this decision
remaining mandatory gate count before the exact table implementation = 0
```

No gate is satisfied for broader P8.
