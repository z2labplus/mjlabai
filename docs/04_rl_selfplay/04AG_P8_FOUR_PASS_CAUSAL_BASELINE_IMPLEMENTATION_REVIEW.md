# 04AG_P8_FOUR_PASS_CAUSAL_BASELINE_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04AF` four-pass causal-baseline training/evaluation diagnostic.

APPROVED for next exact implementation task:
add process-local immutable result reuse to the reviewed raw-census smoke so
the later causal-baseline comparison does not recompute that exact reference.
```

Zero planning, proposal or boundary gates remain before that code.

## Reviewed Commit

```text
2d75ee8  Train MahJax with four-pass causal baseline
```

## Findings

No code, test or scope blocker was found.

## Conformance Review

- Only the two exact `04AF`-approved source/test files plus direct governance
  changed.
- The six-symbol public API is exact and the frozen result retains no parameter
  arrays or checkpoint artifact.
- One reviewed initialization is evaluated on exact disjoint seeds `52..83`,
  then receives exact 4 x ordered `0..31`: 128 update attempts total.
- Policy parameters and the prior-record per-seat running baseline remain
  continuous at attempt edges 32, 64 and 96.
- There is no intermediate evaluation, early stopping, pass selection,
  checkpoint selection, replay, persistence, path or CLI.
- Per-pass nonzero updates are `(31,32,32,32)` and nonzero raw outcomes are
  `(10,10,10,11)`. All 128 legal trajectory and update diagnostics are kept.
- Final baseline and parameter deltas match the approved probe.
- Exactly two zero-update evaluations pin `-312 -> -297`, positive rounds
  `2 -> 2`, negative rounds `20 -> 19`, seed 58 `-15 -> 0`, and complete
  changed seeds `(52,58,65,70,72)`.
- The result selects no pass/checkpoint and labels the observation only as one
  bounded deterministic improvement diagnostic.

## Validation Reused From Implementation

```text
10 focused tests OK in 1236.343 seconds
497 explicit repository tests OK in 5890.810 seconds; 2 existing skips
compileall pass
pip check: no broken requirements
git diff/check pass
```

Review-time independent AST/source checks confirm one exact outer range loop,
one exact training-seed loop, two evaluation call sites, one causal-update call
site and no filesystem/network/process imports. A second 98-minute full-suite
run was intentionally not duplicated because review changed no code.

## Direct Test-Runtime Reuse Approval

The 5890.810-second full run is a realized delivery risk. The reviewed
raw-census test executes its expensive deterministic smoke once, and the later
causal-baseline comparison currently executes the same raw reference again.
The next task may remove only that duplicate computation.

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke.py
tests/rl/test_mahjax_categorical_mlp_predeclared_census_training_evaluation_smoke.py
```

Direct governance synchronization is allowed. The implementation must:

1. keep the existing public API and every returned diagnostic unchanged;
2. cache at most one completed frozen array-free result in process memory;
3. key reuse by the exact runtime dependency callables so a patched dependency
   still executes and raises instead of being hidden by the cache;
4. keep exceptions uncached and preserve the existing wrapped-failure test;
5. add exact identity/reuse and dependency-patch tests;
6. demonstrate reuse by running the raw-census and causal-baseline comparison
   test modules together and reporting before/after elapsed time;
7. add no disk cache, serialized fixture, parameter array, checkpoint, path,
   environment switch or changed training/evaluation behavior.

## Forbidden Scope

- no change to seeds, rate, trajectories, updates, rewards or evidence grade;
- no cache of mutable JAX arrays, parameters, environment or failed results;
- no persistent cache, file I/O, artifact, CLI or broad test framework;
- no fifth pass, tuning, new training branch, replay or checkpoint selection;
- no real/external data, Tenhou, production self-play/evaluation or league;
- no strength, stable-dan, LuckyJ or promotion claim; no P9-P12.

## Evidence Grade

```text
P8 exact implementation-review and bounded deterministic diagnostic evidence
only; not robust evaluation, model-strength or promotion evidence.
```
