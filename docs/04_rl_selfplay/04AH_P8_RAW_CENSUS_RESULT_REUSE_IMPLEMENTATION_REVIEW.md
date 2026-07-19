# 04AH_P8_RAW_CENSUS_RESULT_REUSE_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04AG` process-local immutable raw-census result reuse.

APPROVED for next exact implementation task:
extend the reviewed four-pass causal-baseline diagnostic with one predeclared
second disjoint zero-update evaluation window, seeds 84 through 115.
```

Zero planning, proposal or boundary gates remain before that code.

## Reviewed Commit

```text
756c82d  Reuse immutable MahJax raw census result
```

## Findings

No code, test, state-leak or scope blocker was found.

## Conformance Review

- Only the two exact `04AG` source/test files plus direct governance changed.
- The six-symbol public API and every returned raw-census diagnostic remain
  unchanged.
- The private cache has exact `maxsize=1` and stores only the completed frozen
  array-free result; no parameters, JAX arrays or environment are retained.
- Its key contains exact trainer, runtime loader, training collector and
  evaluation collector callable identities.
- A patched trainer creates a cache miss, executes the failure path, produces
  the approved wrapped error and leaves the cache empty. Exceptions are not
  cached; a prior successful key remains reusable.
- There is no disk cache, serialization, path, environment switch, CLI or
  persistent artifact.
- Raw-census plus causal-baseline comparison passes 20 tests in `850.567s`
  (`856.40s` wall), versus historical separate total `1310.550s`: about
  `454.15s` / `34.7%` lower.
- All 498 tests pass in `5454.853s` with two skips, `435.957s` below the prior
  497-test run despite one additional cache test.

## Validation

```text
20 combined tests OK in 850.567 seconds (856.40 wall)
498 explicit repository tests OK in 5454.853 seconds; 2 existing skips
compileall pass
pip check: no broken requirements
git diff/check pass
fresh-process patched-dependency/cache-empty probe pass
AST maxsize/dependency/public-wrapper checks pass
```

The review reused the implementation suite and did not duplicate the 91-minute
full run because no code changed.

## Direct Replication-Evaluation Approval

The primary `52..83` result is one fixed deterministic diagnostic. Before any
fifth pass, tuning or checkpoint decision, the same predeclared trained policy
must be evaluated on a second disjoint window whose result is accepted
regardless of sign.

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke.py
tests/rl/test_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke.py
```

Direct governance synchronization is allowed. Implementation must:

1. preserve exact four ordered `0..31` passes, 128 attempts, continuous causal
   baseline/policy and no intermediate evaluation or selection;
2. preserve primary initial/final zero-update evaluation on exact `52..83` and
   all existing diagnostics;
3. add exact replication seeds `84..115`, disjoint from training and primary
   evaluation, evaluated once before and once after training with zero updates;
4. retain complete replication transition counts, project action traces, raw
   rewards, final scores, initial/final sums, positive/negative counts and
   changed seeds;
5. set total evaluation call count to four and update count to zero;
6. pin whatever deterministic replication outcome is observed without using
   its sign for stopping, selection, tuning or acceptance;
7. return no arrays, parameters, checkpoint, selected pass or artifact.

## Forbidden Scope

- no fifth pass, alternate training seeds, shuffle, early stop or tuning;
- no checkpoint/pass/evaluation-window selection or promotion;
- no critic, GAE, entropy, KL, clipping, optimizer or learning-rate change;
- no cache expansion, replay, persistence, path, CLI or file ingestion;
- no real/external data, Tenhou, production self-play/evaluation or league;
- no robust/generalization/strength/stable-dan/LuckyJ claim from two windows;
- no P9-P12.

## Evidence Grade

```text
P8 exact regression-runtime implementation review and bounded replication-
diagnostic task approval only; not model-strength or promotion evidence.
```
