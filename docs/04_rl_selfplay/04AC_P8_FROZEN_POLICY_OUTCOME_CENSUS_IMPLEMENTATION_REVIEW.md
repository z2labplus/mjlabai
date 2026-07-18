# 04AC_P8_FROZEN_POLICY_OUTCOME_CENSUS_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04AB` frozen-policy all-project outcome census on seeds 0..31.

APPROVED for next exact implementation task:
compare the existing outcome-selected training tuple (1,3,5,7,11) with the
predeclared contiguous tuple (0,1,2,3,4) under identical initialization,
five raw-return update attempts and fixed zero-update evaluation on 20..51.
```

Zero planning, proposal or review gates remain before that comparison code.

## Reviewed Commit

```text
87ea0c3  Implement MahJax frozen-policy census
```

## Conformance Review

- Only the two exact `04AB` files plus direct governance changed.
- The public surface is the approved seven symbols; no existing API changed.
- Reviewed imitation parameters are loaded once and remain unchanged.
- Exact seeds `0..31` run once each through the reviewed all-project legal
  categorical collector with zero policy, value, critic or optimizer updates.
- All 32 records pin transition count, cumulative raw returns, final scores and
  SHA-256 action-trace digest. Zero-outcome records remain in the denominator.
- Nonzero seeds are exactly `(1,3,5,7,11,24,25,26,27,31)`; the exact zero
  complement is retained. Census rate is `10/32`; reference training rate is
  `5/5` for `(1,3,5,7,11)`.
- Results are frozen and array-free. No replacement split, persistence, path,
  real-data, production evaluation or P9-P12 behavior exists.

No code or test blocker was found.

## Validation

```text
9 focused tests OK in 315.269 seconds
459 explicit repository tests OK in 2919.760 seconds; 2 existing skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent contiguous-seed comparison probe pass
```

## Independent Selection-Bias Probe

Both branches start from identical reviewed imitation parameters, use learning
rate `0.01`, attempt exactly five actor-indexed raw-return updates and receive
the same fixed zero-update mixed-policy evaluation on seeds `20..51`.

```text
initial fixed-evaluation raw sum: -501

outcome-selected branch training seeds: (1,3,5,7,11)
nonzero training outcomes: 5 / 5
fixed-evaluation raw sum: -650
positive / negative rounds: 0 / 18
changed evaluation seeds: (32,39,43,44,50)

contiguous branch training seeds: (0,1,2,3,4)
nonzero training outcomes: 2 / 5
zero-return no-op seeds: (0,2,4)
fixed-evaluation raw sum: -501
positive / negative rounds: 1 / 16
changed evaluation seeds: ()
```

The contiguous result is not evidence that this tuple is optimal or stronger.
It shows that the previously observed degradation depends materially on an
outcome-selected training tuple and therefore must not be interpreted as a
clean algorithm comparison.

## Direct Comparison Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_training_seed_protocol_comparison_smoke.py
tests/rl/test_mahjax_categorical_mlp_training_seed_protocol_comparison_smoke.py
```

Direct governance synchronization is allowed. Existing source/test logic and
public APIs must not change.

The implementation must:

1. load reviewed imitation parameters once and create two independent identical
   in-memory branches;
2. use exact outcome-selected seeds `(1,3,5,7,11)` and exact contiguous seeds
   `(0,1,2,3,4)` without filtering, replacement or adaptive selection;
3. collect one legal all-project terminal trajectory per seed and invoke the
   reviewed actor-indexed raw-return update exactly once per trajectory at
   learning rate `0.01`; zero-return trajectories must produce exact no-op
   parameter deltas while still counting as update attempts;
4. pin all training trajectories, raw returns, objectives and parameter deltas;
5. evaluate initial and both final parameter sets with zero updates on exact
   fixed seeds `20..51` under identical environment/rule RNG;
6. pin initial/selected/contiguous sums `-501/-650/-501`, counts and changed
   seeds shown above;
7. return frozen array-free diagnostics and state explicitly that this is a
   selection-bias comparison, not seed selection or model-strength evidence.

## Forbidden Scope

- no third seed protocol, seed search, replacement sampling or selected branch;
- no learning-rate, estimator, optimizer, critic or reward change;
- no extra update, early stopping, persistence, checkpoint or artifact;
- no real/external data, Tenhou, production self-play/evaluation or league;
- no improvement, superiority, stable-dan, LuckyJ or promotion claim;
- no P9-P12.

## Evidence Grade

```text
P8 exact implementation-review and bounded training-seed selection-bias
comparison approval evidence only; not policy-quality or strength evidence.
```
