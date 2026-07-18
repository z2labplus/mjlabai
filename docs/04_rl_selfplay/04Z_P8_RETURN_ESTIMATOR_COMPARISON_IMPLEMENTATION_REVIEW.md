# 04Z_P8_RETURN_ESTIMATOR_COMPARISON_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04Y` raw/centered/standardized return-estimator comparison.

APPROVED for next exact implementation task:
compare raw-return learning rates 0.01, 0.005, 0.001 and 0.0001 under the same
five training seeds and fixed evaluation seeds.
```

Zero planning/review gates remain before code.

## Reviewed Commit

```text
fa3471e  Compare MahJax MLP return estimators
```

## Conformance Review

- Only the two `04Y`-approved source/test files plus direct governance changed.
- Exactly three independent branches begin from identical immutable imitation
  arrays; no branch consumes another branch's arrays or evaluation results.
- Raw reuses the reviewed update helper. Centered and standardized implement
  only the exact approved per-round four-seat formulas.
- Every branch runs exact seeds `(1,3,5,7,11)`, five legal terminal rounds and
  five updates. Complete trajectory identity and finite objectives/deltas are
  pinned; final parameter sets are pairwise distinct.
- Initial and all branch parameters receive zero-update fixed evaluation on
  disjoint seeds `20..35` under identical environment/rule RNG.
- Exact aggregates are `-320/-454/-454/-490`; centered parameters differ from
  raw while evaluation behavior is identical, and standardized changes exact
  seeds `(20,27,31,32,35)` while worsening this fixed diagnostic.
- Frozen results contain no arrays. Warnings deny estimator selection,
  superiority, improvement, strength, production evaluation and promotion.
- No I/O, persistence, checkpoint, external/real data, production self-play,
  league or P9-P12 path was added.

## Validation

```text
10 focused tests OK, including a full deterministic repeat
441 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent fixed learning-rate probe pass
```

## Independent Step-Size Findings

The raw estimator was probed with exact fixed learning rates, identical initial
parameters, training seeds and evaluation seeds:

```text
initial: aggregate -320, positive 1, negative 8, changed seeds ()
0.01:    aggregate -454, positive 0, negative 9, changed seeds (32,)
0.005:   aggregate -454, positive 0, negative 9, changed seeds (32,)
0.001:   aggregate -320, positive 1, negative 8, changed seeds ()
0.0001:  aggregate -320, positive 1, negative 8, changed seeds ()
```

All four trained parameter sets have nonzero initial-to-final deltas. Exact
final deltas are:

```text
0.01   (0.0021020556, 0.0004550584, 0.0053585209, 0.0005585462)
0.005  (0.0010509313, 0.0002272493, 0.0026764988, 0.0002789878)
0.001  (0.0002101750, 0.0000453977, 0.0005348558, 0.0000557546)
0.0001 (0.0000210247, 0.0000045383, 0.0000534743, 0.0000055721)
```

This fixed diagnostic shows a greedy behavior-change threshold between tested
rates, not improvement and not an optimal learning rate. Unchanged evaluation
at smaller rates does not establish policy quality.

## Direct Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_learning_rate_comparison_smoke.py
tests/rl/test_mahjax_categorical_mlp_learning_rate_comparison_smoke.py
```

Direct governance synchronization is allowed. Existing source/tests/exports,
dependencies and artifacts remain unchanged.

Exact public API:

```text
MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_COMPARISON_SMOKE_VERSION
MAHJAX_CATEGORICAL_MLP_COMPARISON_LEARNING_RATES
MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_TRAINING_SEEDS
MAHJAX_CATEGORICAL_MLP_LEARNING_RATE_EVALUATION_SEEDS
MahJaxCategoricalMlpLearningRateComparisonSmokeError
MahJaxCategoricalMlpLearningRateComparisonResult
run_mahjax_categorical_mlp_learning_rate_comparison_smoke
```

### Exact comparison contract

1. obtain reviewed imitation parameters once and create four independent
   in-memory raw-return branches from identical arrays;
2. use exact rates `(0.01,0.005,0.001,0.0001)` in that order;
3. each branch runs exact seeds `(1,3,5,7,11)`, one raw actor-indexed update
   after each legal terminal round, for five updates total;
4. the `0.01` branch must reuse the reviewed raw helper exactly; a private
   variable-rate helper may implement the same objective for the other rates;
5. evaluate initial and all four branches without updates on exact seeds
   `20..35`, project seat 0 greedy versus fixed rule seats 1/2/3, with identical
   environment/rule RNG per seed/branch;
6. pin training trajectories, objectives/deltas, evaluation traces/rewards/
   scores, aggregates and changed seeds exactly as probed;
7. prove all branch parameters change and remain distinct; prove 0.01/0.005
   evaluation identity and 0.001/0.0001 identity with the initial behavior;
8. return frozen summaries only; no rate is selected, ranked or promoted.

## Forbidden Scope

- no additional/interpolated/adaptive rate, optimizer or hyperparameter sweep;
- no early stopping, checkpoint selection or evaluation-driven update;
- no centered/standardized estimator in this task;
- no baseline/critic, discount, GAE, entropy, clipping or reward shaping;
- no replay, persistence, saved data/model/checkpoint/artifact/path/CLI;
- no external/real data, Tenhou, haifu or platform data;
- no production self-play/evaluation, league, promotion or strength claim;
- no P9-P12.

## Evidence Grade

```text
P8 return-estimator implementation-review evidence and exact bounded raw-return
step-size sensitivity task approval only.
```
