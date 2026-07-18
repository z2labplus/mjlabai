# 04Y_P8_FIVE_ROUND_TRAINING_EVALUATION_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04X` five-round shared categorical-MLP training plus fixed
mixed-policy failure diagnostic.

APPROVED for next exact implementation task:
compare raw, per-round seat-centered and per-round seat-standardized return
estimators under the same five training seeds and fixed evaluation seeds.
```

Zero planning/review gates remain before code.

## Reviewed Commit

```text
7026a0c  Evaluate five-round MahJax MLP training
```

## Conformance Review

- Only the two `04X`-approved source/test files plus direct governance changed.
- The module exposes exactly seven approved symbols and returns a frozen,
  array-free diagnostic; all model arrays remain private and in memory.
- Exact seeds `(1,3,5,7,11)` execute in order. Every trajectory terminates
  legally and drives exactly one reviewed actor-indexed `0.01` update, for five
  updates total with direct parameter continuity.
- Evaluation seeds `20..35` are disjoint. Initial and trained models receive
  identical environment/rule RNG; project seat 0 is greedy, seats 1/2/3 use
  the pinned rule policy, and evaluation contains no gradient or update.
- Complete training/evaluation traces, rewards, scores, objectives and deltas
  match the independent probe. Only evaluation seed 32 changes.
- The result and tests explicitly report regression `-320->-454`, positive
  rounds `1->0`, negative rounds `8->9` and seed-32 `+74->-60`; they make no
  improvement or strength claim.
- No I/O, persistence, checkpoint, external/real data, production self-play,
  production evaluation, league, promotion or P9-P12 path was added.

## Validation

```text
9 focused tests OK, including a full deterministic repeat
431 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent raw/centered/standardized estimator probes pass
```

## Independent Return-Estimator Findings

The same bounded train/evaluation split was probed without writing artifacts.

### Seat-centered return

For each training round:

```text
raw_seat_return = cumulative_raw_reward / 100
centered_seat_return = raw_seat_return - mean(raw_seat_returns)
decision_return = centered_seat_return[actor]
```

All five trajectories remain the same as the reviewed raw-return path. Final
initial-to-end parameter deltas are:

```text
(0.0020699743, 0.0004389429, 0.0052021975, 0.0005401245)
```

The parameters differ numerically from the raw-return parameters, but all 16
fixed greedy evaluation traces and outcomes are identical to the raw-return
branch: aggregate remains `-454` and changed seed remains `(32,)`.

### Seat-standardized return

For each training round:

```text
centered = raw_seat_return - mean(raw_seat_returns)
standardized = centered / std(centered) when std > 1e-6 else centered
decision_return = standardized[actor]
```

Final initial-to-end parameter deltas are:

```text
(0.0056803911, 0.0015099167, 0.0181233995, 0.0020000334)
```

The fixed evaluation worsens further:

```text
initial_project_raw_sum = -320
raw_after_project_raw_sum = -454
centered_after_project_raw_sum = -454
standardized_after_project_raw_sum = -490
standardized_positive_round_count = 0
standardized_negative_round_count = 11
standardized_changed_seeds = (20,27,31,32,35)
```

These are small fixed diagnostics. They show that neither elementary transform
repairs this failure, not that one estimator is globally better or worse.

## Direct Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_return_estimator_comparison_smoke.py
tests/rl/test_mahjax_categorical_mlp_return_estimator_comparison_smoke.py
```

Direct governance synchronization is allowed. Existing source/tests/exports,
dependencies and artifacts remain unchanged.

Exact public API:

```text
MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_COMPARISON_SMOKE_VERSION
MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_TRAINING_SEEDS
MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_EVALUATION_SEEDS
MAHJAX_CATEGORICAL_MLP_RETURN_ESTIMATOR_LEARNING_RATE
MahJaxCategoricalMlpReturnEstimatorComparisonSmokeError
MahJaxCategoricalMlpReturnEstimatorComparisonResult
run_mahjax_categorical_mlp_return_estimator_comparison_smoke
```

### Exact comparison contract

1. obtain reviewed imitation parameters once and create three independent
   in-memory branches from those identical arrays;
2. train raw, centered and standardized branches on exact ordered seeds
   `(1,3,5,7,11)`, one `0.01` update after each legal terminal round;
3. raw must reuse the reviewed actor-indexed helper; centered/standardized may
   share one private estimator helper implementing only the formulas above;
4. no estimator may consume evaluation results or another branch's arrays;
5. evaluate initial/raw/centered/standardized parameters without updates on
   exact seeds `20..35`, project seat 0 greedy versus fixed rule seats 1/2/3,
   with identical environment/rule RNG per seed and branch;
6. pin complete trajectories, objective/delta summaries, evaluation traces,
   scores/rewards, changed seeds and aggregate `-320/-454/-454/-490` results;
7. prove raw branch equals reviewed `7026a0c`, centered differs in parameters
   but equals raw evaluation behavior, and standardized changes five fixed
   seeds while worsening this diagnostic;
8. return frozen summaries only; arrays remain private and no estimator is
   selected or promoted.

## Required Tests

- exact seven-symbol API/constants/frozen array-free result;
- identical initial arrays and exact independent three-branch ownership;
- exact five legal terminal training rounds and updates per branch;
- exact raw/centered/standardized return formulas, objectives and deltas;
- disjoint fixed evaluation with zero updates and identical RNG/rule policy;
- raw branch regression identity, centered evaluation identity and standardized
  exact changed seeds/outcomes;
- deterministic repeat and failure translation;
- source proves bounded loops/helper reuse and no I/O/persistence;
- warnings deny estimator superiority, improvement and strength evidence.

## Forbidden Scope

- no learning-rate comparison, sixth update, extra estimator or hyperparameter
  sweep;
- no learned baseline/critic, discount, GAE, entropy, clipping or reward shape;
- no checkpoint selection, early stopping or evaluation-driven update;
- no replay, persistence, saved data/model/checkpoint/artifact/path/CLI;
- no external/real data, Tenhou, haifu or platform data;
- no production self-play/evaluation, league, promotion or strength claim;
- no P9-P12.

## Evidence Grade

```text
P8 five-round implementation-review evidence and exact bounded return-estimator
failure-comparison task approval only.
```
