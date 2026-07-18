# 12AK_P8_POLICY_TABLE_ACCEPTANCE_AND_TWO_PASS_SEQUENCE_APPROVAL_DECISION

## Decision

```text
ACCEPTED as current-scope complete.
Approved for next exact minimal implementation task.
```

The exact `12AI` implementation reviewed in `12AJ` is accepted only for its
fixed two-key synthetic/local table-update scope.

The next executable task is:

```text
Implement exact minimal P8 synthetic/local fixed two-pass policy-table update
sequence smoke only.
```

No proposal, boundary or additional approval may be inserted before that
implementation.

## Why This Outcome

The current helper proves one immutable table-state transition. The next
material increment is exactly two chained table updates where pass 1 final
entries become pass 2 initial entries. This exercises repeated parameter-state
continuity without introducing a variable epoch, trainer, replay buffer,
environment, model or persistence layer.

Adding unrelated fields or another one-pass wrapper is rejected as repetitive.

## Exact Approved Files

The implementation may create or modify only:

- `src/mjlabai/rl/__init__.py`
- `src/mjlabai/rl/synthetic_policy_table_update_sequence_smoke.py`
- `tests/rl/test_synthetic_policy_table_update_sequence_smoke.py`
- direct docs/governance synchronization required by repository rules.

No fixture, data file, dependency, CLI, path reader or persistence file is
approved.

## Exact Public API

The new module may export only:

```text
SYNTHETIC_POLICY_TABLE_UPDATE_SEQUENCE_SMOKE_VERSION
SyntheticPolicyTableUpdateSequenceSmokeError
SyntheticPolicyTableUpdateSequenceResult
apply_synthetic_policy_table_update_sequence_smoke
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
apply_synthetic_policy_table_update_sequence_smoke(
    initial_entries,
    trace_inputs,
    *,
    learning_rate,
    discount_factor,
)
```

`initial_entries` must be the exact two-entry tuple accepted by the reviewed
table helper.

`trace_inputs` must be an exact outer tuple containing exactly two exact
four-record trace tuples. The first inner trace updates the supplied entries.
The second inner trace must begin from the exact final A/B values produced by
the first table update. All eight record IDs must be pairwise distinct.

Lists, mappings, strings, bytes, bytearrays, paths, generators, tuple
subclasses and arbitrary iterables are rejected for the outer tuple and each
inner tuple through the reviewed helper boundaries.

## Exact Semantics

The helper must:

1. validate the exact two-trace outer tuple shape.
2. call `apply_synthetic_policy_table_update_smoke` explicitly for pass 1.
3. use pass 1 `final_entries` as pass 2 `initial_entries`.
4. call the same table helper explicitly for pass 2.
5. wrap table-helper failures with one-based pass index and chained cause.
6. reject duplicate record IDs across the two validated pass results.
7. return one frozen deterministic result without mutating any input.

The two calls must be explicit and fixed. No variable loop, third pass,
dynamic epoch count, early stopping, optimizer state or in-place update is
approved.

## Exact Result

`SyntheticPolicyTableUpdateSequenceResult` must be frozen and contain only:

```text
sequence_version
pass_count
initial_entries
intermediate_entries
final_entries
pass_results
sequence_applied
safety_guardrails_all_satisfied
evidence_grade
warnings
```

Required values and shapes:

- `pass_count = 2`.
- initial/intermediate/final entries are exact frozen two-entry tuples.
- `pass_results` is an exact tuple of two reviewed table-update results.
- `sequence_applied = true`.
- `safety_guardrails_all_satisfied = true`.

Warnings must include at least:

- synthetic/local fixed two-pass policy-table update sequence smoke only.
- not a variable epoch, trainer or production training loop.
- not a persistent policy, model or checkpoint.
- not an environment, episode or replay buffer.
- not self-play.
- not model-strength evidence.
- not stable-dan or LuckyJ comparison.
- not candidate-promotion evidence.

## Exact Test Requirements

The focused test module must cover:

1. exact pass 1 intermediate and pass 2 final A/B values.
2. exact outer tuple type/length and tuple-subclass rejection.
3. exact inner trace shape rejection through pass-indexed errors.
4. exact pass 1 to pass 2 table-value continuity for both keys.
5. pairwise-distinct record IDs across all eight records.
6. exactly two table-helper calls and no duplicated formulas/trace/table logic.
7. pass 1 and pass 2 error wrapping with chained causes.
8. deterministic repeated output, input immutability and frozen outputs.
9. exact result fields/shapes, evidence grade and warnings.
10. package imports and narrow public API.
11. absence of third pass, variable epoch/trainer, mapping/persistence/path/
    fixture/environment/replay/self-play/model/optimizer/training APIs.

Validation must include the 90 currently approved tests, the new focused
tests, compile checks and `git diff --check`.

## Forbidden Scope

This approval does not permit:

- a third pass, variable pass count, epoch loop, trainer or early stopping.
- mutable/dynamic table, mapping API, persistence, dataset or dataloader.
- replay buffer, environment, episode, gameplay, legality or action selection.
- self-play, model/network, tensor, autograd, gradient or optimizer.
- production training/evaluation, checkpoint or artifact creation/use.
- path/CLI, dependency, nondeterminism, timing, concurrency, GPU/distributed
  work or third-party binary/service use.
- real Tenhou/haifu, external logs, platform data, accounts or secrets.
- broad P8, league, strength claims or P9-P12.

## Rollback And Stop Conditions

If implementation needs any unapproved file, input shape, behavior,
dependency or evidence claim, stop before commit and record one exact blocker
without silently widening scope.

## Evidence Grade

Current decision evidence:

```text
P8 exact fixed policy-table current-scope acceptance and two-pass sequence
task approval evidence only.
```

Future passing implementation evidence:

```text
P8 synthetic/local fixed two-pass policy-table update sequence smoke evidence
only.
```

Neither is environment, self-play, production training, model-strength,
Tenhou ranked, stable-dan, LuckyJ comparison, candidate-promotion or P9-P12
evidence.

## Gate Accounting

```text
fixed policy-table current-scope acceptance = satisfied by this decision
next exact task approval = satisfied by this decision
next exact file/API/input/output/test boundaries = satisfied by this decision
remaining mandatory gate count before the exact sequence implementation = 0
```

No gate is satisfied for broader P8.
