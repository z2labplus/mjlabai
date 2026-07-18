# 04X_P8_TWO_ROUND_ALL_PROJECT_TRAINING_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04W` seeds-(1,3) two-round sequential shared all-project training
smoke.

APPROVED for next exact implementation task:
one five-round shared all-project training plus independent 16-seed mixed-policy
before/after evaluation smoke.
```

Zero planning/review gates remain before code.

## Reviewed Commit

```text
9cfdb4d  Train MahJax MLP across two four-seat rounds
```

## Conformance Review

- Only the approved private rollout helper, one new module/test and direct
  governance changed.
- Explicit seed is private; the public `04V` seed-1 result remains unchanged and
  all nine existing tests pass.
- The sequence exposes exactly six approved symbols and a frozen array-free
  result.
- One explicit two-item loop executes seeds `(1,3)` in order. Each round is
  independently initialized, fully legal, terminal and nonzero for all seats.
- The reviewed actor-indexed update helper is called once per round; update-1
  arrays are assigned directly before seed 3.
- Fresh versus carried seed-3 objective and nonzero initial-to-final deltas
  prove parameter continuity. Exact objectives/deltas/outcomes match `04W`.
- Post-update-2 seed-3 replay remains identical. No third round/update, replay,
  persistence, rule participant, evaluation path or strength claim was added.

## Validation

```text
9 new focused tests OK
9 prior all-project-update tests OK
422 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent public-result and training/evaluation probes pass
```

## Independent Training/Evaluation Finding

One exploratory bounded probe carries the same shared MLP through exact
all-project training seeds `(1,3,5,7,11)` with one reviewed `0.01` update after
each legal terminal round. It then evaluates project seat 0 greedily against
three fixed bundled-rule seats on disjoint seeds `20..35`, using identical
environment/rule RNG for before/after parameters.

All five training outcomes are nonzero. Independent evaluation finds:

```text
before_project_raw_sum = -320
after_project_raw_sum = -454
before_positive_round_count = 1
after_positive_round_count = 0
before_negative_round_count = 8
after_negative_round_count = 9
changed_evaluation_seeds = (32,)
seed_32_project_raw = 74 -> -60
```

The update sequence changes behavior but degrades this tiny fixed diagnostic.
That is actionable failure evidence: the project must not interpret repeated
raw-return objective decreases as policy improvement. The next exact task
records this before/after experiment in repository tests before any reward/
variance-reduction change is considered.

## Direct Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_five_round_training_evaluation_smoke.py
tests/rl/test_mahjax_categorical_mlp_five_round_training_evaluation_smoke.py
```

Direct governance synchronization is allowed. Existing source/tests/exports,
dependencies and artifacts remain unchanged.

Exact public API:

```text
MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_EVALUATION_SMOKE_VERSION
MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_TRAINING_SEEDS
MAHJAX_CATEGORICAL_MLP_FIXED_EVALUATION_SEEDS
MAHJAX_CATEGORICAL_MLP_FIVE_ROUND_LEARNING_RATE
MahJaxCategoricalMlpFiveRoundTrainingEvaluationSmokeError
MahJaxCategoricalMlpFiveRoundTrainingEvaluationResult
run_mahjax_categorical_mlp_five_round_training_evaluation_smoke
```

### Exact training contract

1. obtain reviewed imitation parameters once;
2. execute exact ordered seeds `(1,3,5,7,11)` in one five-item loop;
3. all four seats share the project MLP and sample legal-masked categorical
   actions with each seed's deterministic independent initialization/action RNG;
4. require each round terminal/legal/nonzero and apply the reviewed actor-
   indexed raw-return helper exactly once after terminal;
5. carry arrays directly and pin each transition count, outcome, objective pair,
   four parameter deltas and final initial-to-end deltas;
6. no update may use evaluation seeds or evaluation results.

### Exact independent evaluation contract

1. evaluation seeds are exact disjoint tuple `20..35`;
2. in every evaluation round, project seat `0` acts greedily from the candidate
   MLP after environment legal masking; seats `(1,2,3)` use the pinned bundled
   rule policy;
3. split identical environment/rule RNG per seed for initial and trained models;
4. perform no gradient/update during evaluation;
5. record complete project action traces, transition counts, project cumulative
   raw rewards and global scores before/after;
6. pin exact changed seed `(32,)`, aggregate counts/sums and seed-32 degradation;
7. return frozen summaries/traces only; arrays remain private.

### Required tests

- exact seven-symbol API/constants/frozen array-free result;
- exact five training seeds/updates, legal terminal trajectories and continuity;
- exact five training outcomes/objectives/per-step/final parameter deltas;
- disjoint 16 evaluation seeds and no evaluation update;
- exact before/after project rewards/scores/traces and changed seed `(32,)`;
- exact aggregate `-320 -> -454`, positive/negative counts and seed-32 result;
- deterministic repeat and runtime/training failure translation;
- source proves two bounded loops, helper reuse, rule participants only in
  evaluation and no I/O/persistence;
- warnings explicitly classify the observed evaluation regression and deny
  improvement/strength.

## Forbidden Scope

- no sixth training round/update, adaptive seed selection or hyperparameter sweep;
- no baseline/critic/discount/GAE/entropy/reward-shaping change in this task;
- no checkpoint selection, early stopping or evaluation-driven update;
- no replay, persistence, saved dataset/model/checkpoint/artifact/path/CLI;
- no external/real data, Tenhou, haifu or platform data;
- no production self-play/evaluation, league, promotion or strength claim;
- no P9-P12.

## Evidence Grade

```text
P8 two-round implementation-review evidence and exact bounded five-round
training/fixed-evaluation failure-diagnostic task approval only.
```
