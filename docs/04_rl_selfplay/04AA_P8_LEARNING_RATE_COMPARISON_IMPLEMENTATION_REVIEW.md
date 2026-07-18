# 04AA_P8_LEARNING_RATE_COMPARISON_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04Z` four-rate raw-return learning-rate comparison.

APPROVED for next exact implementation task:
expand the fixed zero-update evaluation from seeds 20..35 to exact seeds
20..51 in the existing learning-rate comparison source and test only.
```

Zero planning, proposal or review gates remain before that code change.

## Reviewed Commit

```text
41b98d3  Compare MahJax MLP learning rates
```

## Conformance Review

- Only the two `04Z`-approved source/test files plus direct governance changed.
- The public surface is the exact approved seven symbols. Results are frozen,
  contain no parameter arrays and expose no selected-rate field.
- Four branches begin from identical immutable imitation arrays, use exact
  rates `(0.01,0.005,0.001,0.0001)` and remain independent and pairwise
  distinct after training.
- Every branch executes exact seeds `(1,3,5,7,11)`, five legal terminal rounds
  and five updates. Complete trajectories, objectives and deltas are pinned.
- Rate `0.01` reuses the reviewed actor-indexed raw-return helper. Other rates
  change only the fixed multiplier in the identical raw-return objective.
- Initial and branch parameters receive zero-update mixed-policy evaluation on
  disjoint seeds `20..35` with identical environment and rule-policy RNG.
- Exact sums are `-320/-454/-454/-320/-320`. Rates `0.01/0.005` change seed
  `32`; rates `0.001/0.0001` change parameters but not fixed greedy behavior.
- Warnings prohibit rate selection, ranking, scale-up, improvement and strength
  claims. No I/O, persistence, checkpoint, external/real data, production
  self-play/evaluation, league or P9-P12 path exists.

## Validation

```text
9 focused tests OK
450 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent seeds 36..51 evaluation-breadth probe pass
```

## Independent Evaluation-Breadth Findings

The same five trained parameter sets were evaluated without updates on exact
new seeds `36..51`:

```text
initial: sum -181, positive 0, negative 8
0.01:    sum -196, positive 0, negative 9, changed (39,43,44,50)
0.005:   sum -181, positive 0, negative 8, changed (39,44,50)
0.001:   sum -181, positive 0, negative 8, changed ()
0.0001:  sum -181, positive 0, negative 8, changed ()
```

Combined exact seeds `20..51` therefore yield:

```text
initial: sum -501, positive 1, negative 16
0.01:    sum -650, positive 0, negative 18, changed (32,39,43,44,50)
0.005:   sum -635, positive 0, negative 17, changed (32,39,44,50)
0.001:   sum -501, positive 1, negative 16, changed ()
0.0001:  sum -501, positive 1, negative 16, changed ()
```

The new seeds disprove fixed behavior identity between `0.01` and `0.005`.
They do not select either smaller rate: unchanged greedy behavior remains
insensitivity at this update scale, not improvement or policy quality.

## Direct Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_learning_rate_comparison_smoke.py
tests/rl/test_mahjax_categorical_mlp_learning_rate_comparison_smoke.py
```

Direct governance synchronization is allowed. No new source/test file is
approved. Existing public symbols and exact training contract stay unchanged.

Implementation must:

1. set the fixed evaluation seeds to exact `tuple(range(20, 52))`;
2. evaluate initial and all four existing trained branches with zero updates;
3. preserve identical environment/rule RNG for every seed and branch;
4. pin complete transition/action/reward/score diagnostics for all 32 seeds;
5. pin combined sums, counts and changed seeds exactly as recorded above;
6. preserve identical initialization, five training seeds, five updates,
   objective formulas, parameter deltas and all forbidden-scope warnings;
7. make no rate selection, ranking, promotion or strength claim.

## Forbidden Scope

- no new rate, training seed, update, estimator, optimizer or adaptive tuning;
- no evaluation-driven update, early stopping, checkpoint selection or scale-up;
- no baseline/critic, discount, GAE, entropy, clipping or reward shaping;
- no persistence, artifact, path, CLI, external/real data or Tenhou;
- no production self-play/evaluation, league, promotion or strength claim;
- no P9-P12.

## Evidence Grade

```text
P8 exact implementation-review and bounded evaluation-breadth task-approval
evidence only; not rate selection, improvement, robust evaluation or strength.
```
