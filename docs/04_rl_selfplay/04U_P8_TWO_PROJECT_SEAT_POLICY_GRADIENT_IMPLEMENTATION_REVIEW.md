# 04U_P8_TWO_PROJECT_SEAT_POLICY_GRADIENT_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close after the exact runtime-error blocker fix.

ACCEPTED as current-scope complete:
the exact `04T` two-project-seat shared-policy raw-outcome update smoke.

APPROVED for next exact implementation task:
one categorical-observation MLP rule-policy imitation training and all-project-
seat nonzero-outcome smoke.
```

Zero planning/review gates remain before code.

## Reviewed Commit

```text
c47bb73  Update shared MahJax policy from two project seats
```

## Blocker And Exact Fix

The successful path conformed, but the new module reused the one-round private
runtime loader without translating its failure. An unavailable MahJax/JAX
runtime would therefore leak the old module's exception type instead of
`MahJaxTwoProjectSeatPolicyGradientSmokeError`.

The exact review fix:

- wraps `_load_pinned_runtime()` in the public new-module error;
- adds one focused regression test with patched training/runtime helpers;
- changes no successful trajectory, objective, update or output behavior.

## Conformance Review After Fix

- Exact two approved source/test files plus direct governance only.
- Exact seven-symbol public API and frozen result.
- Seed `0` splits independent init/rule/project RNG streams.
- Project seats `(0,2)` share reviewed in-memory parameters and produce exactly
  44 legal-masked categorical decisions; fixed rule seats `(1,3)` produce 48
  legal decisions and never enter the project gradient batch.
- One 92-transition terminal round completes before objective/update code.
- Every project log probability is weighted by its acting seat cumulative raw
  reward divided by 100. Exactly one aggregate update occurs at `0.1`.
- Exact raw/cumulative/global outcomes, objectives and deltas match the probe.
- No path, I/O, persistence, replay, checkpoint, evaluation or broad self-play
  surface was added. Evidence warnings prevent overclaim.

## Validation

```text
11 focused tests OK after blocker fix
395 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff --check pass
independent participant/legality/return/objective/delta probe pass
```

## Representation And Self-Play Signal Finding

The existing linear policy receives tile/action IDs as scaled continuous
numbers. Independent all-project probes show:

- categorical and greedy execution of the current linear imitation policy both
  produce zero cumulative raw reward for all tested seeds;
- a legal-win priority guard never triggers because no tested trajectory
  reaches a legal `TSUMO=73` or `RON=74` action;
- expanding the same linear training to eight train and four evaluation rounds
  improves imitation accuracy but still gives zero outcomes in all tested
  all-project rounds.

The actionable blocker is representation/model capacity, not the raw-outcome
formula. A category-aware input and small nonlinear policy are the smallest
material next step.

## Direct Categorical MLP Training Approval

Exact files:

```text
src/mjlabai/supervised/mahjax_categorical_mlp_imitation_training_smoke.py
tests/supervised/test_mahjax_categorical_mlp_imitation_training_smoke.py
```

Direct governance synchronization is allowed. Existing source/test modules,
package exports, dependencies and persisted artifacts must remain unchanged.

Exact public API:

```text
MAHJAX_CATEGORICAL_MLP_IMITATION_SMOKE_VERSION
MAHJAX_CATEGORICAL_MLP_FEATURE_COUNT
MAHJAX_CATEGORICAL_MLP_TRAIN_SEEDS
MAHJAX_CATEGORICAL_MLP_EVAL_SEEDS
MAHJAX_CATEGORICAL_MLP_SELFPLAY_SEEDS
MAHJAX_CATEGORICAL_MLP_TRAINING_EPOCHS
MahJaxCategoricalMlpImitationSmokeError
MahJaxCategoricalMlpImitationResult
encode_mahjax_categorical_observation
run_mahjax_categorical_mlp_imitation_training_smoke
```

### Exact feature contract

The encoder returns exactly 882 finite float32-compatible values from the
current player's MahJax observation only:

1. 37 own-hand tile-count features divided by four;
2. 38-way last-draw one-hot including one missing bucket;
3. latest eight chronological history records, left padded, each with four-way
   actor one-hot, 87-way action one-hot and one tsumogiri bit (`8 * 92`);
4. seven-way clipped `shanten_count + 1` one-hot and one furiten bit;
5. four scores divided by 1000;
6. 12-way round one-hot, honba/kyotaku divided by 10;
7. four-way prevalent-wind and seat-wind one-hots;
8. 37 dora-indicator count features divided by four.

Exact observation keys/shapes remain pinned. No opponent hidden hand or direct
environment-private state may be read.

### Exact training contract

1. collect bundled-rule-policy decisions from train seeds `0..7` and evaluation
   seeds `8..11`, with independent init/policy RNG and legal-label checks;
2. pin 482 train and 221 evaluation examples; no saved dataset;
3. initialize a project-owned `882 -> 64 ReLU -> 87` MLP from exact model seed
   `123`, normal scale `0.03`, zero biases; parameter count `62,167`;
4. train exactly 48 full-batch masked-cross-entropy epochs with in-module Adam:
   learning rate `0.003`, betas `0.9/0.999`, epsilon `1e-8`;
5. pin final train/eval loss `0.36734492 / 1.77358353` and train/eval exact
   accuracy `0.93153530 / 0.58371043` within float tolerance;
6. return a frozen summary only; an unexported private helper may return arrays
   strictly for future in-process reviewed use.

### Exact all-project outcome diagnostic

After training, run exact greedy all-project-seat rounds for seeds `0..15`:

- all four seats use the same frozen trained MLP;
- every action is environment-legal and no update occurs during these rounds;
- pin nonzero-outcome seeds `(0,1,3,5,6,7,10)` and their cumulative raw vectors:
  `(-10,-10,-10,20)`, `(-10,-10,20,-10)`,
  `(-10,-10,-10,20)`, `(32,-32,0,0)`,
  `(-23,37,-7,-7)`, `(-10,-10,-10,20)`, `(0,180,0,-180)`;
- record all transition counts, outcomes and global scores in the frozen result.

This diagnostic proves the initialization can generate nonzero all-project
environment outcomes. It is not an RL update, improvement comparison, league or
model-strength evaluation.

## Required Tests

- exact API/constants/frozen result and 882-feature categorical sentinels;
- exact source separation, counts, model shape/parameter count and 48 epochs;
- legal teacher labels, decreasing train loss, exact metrics and determinism;
- all 16 greedy project-only rounds terminal/legal with exact nonzero seed set;
- no model arrays in public output, path/I/O/persistence/checkpoint/dependency;
- evidence grade and warnings deny strength/self-play evaluation claims.

## Forbidden Scope

- no external/real data, Tenhou, haifu, platform data or source ingestion;
- no saved dataset, model weights, checkpoint, artifact, path or CLI;
- no RL/raw-outcome update in this task and no production self-play trainer;
- no replay, league, promotion, stable-dan or LuckyJ comparison;
- no broad architecture search, hyperparameter sweep or P9-P12.

## Evidence Grade

```text
P8 two-project-seat update implementation-review evidence and exact local
categorical-MLP initialization/outcome-smoke task approval only.
```
