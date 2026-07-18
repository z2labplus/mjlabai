# 04O_P4_P8_LINEAR_POLICY_BRIDGE_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04N` MahJax public-observation/masked-linear-policy round bridge.

APPROVED for next exact implementation task:
one in-memory P7/P8 supervised imitation training smoke using two local
MahJax bundled-rule-policy trajectories.
```

Zero proposal, boundary or review gates remain before actual training code.

## Reviewed Commit

```text
d56271a  Connect project linear policy to MahJax
```

## Conformance Review

- The module and package expose exactly the approved nine symbols.
- Only exact public decision-time observation dict keys/shapes are encoded;
  missing/extra keys, shape drift and non-finite features fail.
- Feature order/scaling is fixed and produces exactly 630 float32 values.
- The project model has exact `(630,87)` weights, 87 biases and 54,897
  random-initialized immutable parameters.
- Root RNG separates environment and model initialization.
- Source has two JIT calls, one explicit 256-cap loop and no hidden-state,
  label, loss, gradient, optimizer, checkpoint, file or multi-game path.
- All 87 scores are finite and masked by the authoritative environment legal
  mask before deterministic argmax; every selected action is rechecked.
- Seed 0 deterministically terminates in 91 legal transitions, no truncation,
  zero raw/cumulative rewards and global scores `(250,250,250,250)`.
- Warnings correctly identify random/untrained parameters and prohibit policy-
  quality, model-strength, stable-dan, LuckyJ and promotion claims.

## Validation

```text
11 focused tests OK
336 repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff --check pass
independent normalized encoder/model/trace/result probe pass
```

## Direct Training Approval

The next exact task is the first environment-backed parameter training in this
project. It must create no files or artifacts beyond source/test/governance and
must keep all decision samples in memory.

Exact implementation files:

```text
src/mjlabai/supervised/mahjax_rule_policy_imitation_training_smoke.py
tests/supervised/test_mahjax_rule_policy_imitation_training_smoke.py
```

No package export is required. Direct governance synchronization is allowed;
dependency pins remain unchanged.

Exact public API:

```text
MAHJAX_IMITATION_TRAINING_SMOKE_VERSION
MAHJAX_IMITATION_TRAIN_SEED
MAHJAX_IMITATION_EVAL_SEED
MAHJAX_IMITATION_MODEL_SEED
MAHJAX_IMITATION_TRAINING_EPOCHS
MAHJAX_IMITATION_LEARNING_RATE
MahJaxImitationTrainingSmokeError
MahJaxImitationTrainingResult
run_mahjax_rule_policy_imitation_training_smoke
```

The implementation must:

1. use pinned MahJax/JAX and exact `red_mahjong`, `single`, `dict`, `auto`;
2. collect one seed-0 training round and one seed-1 evaluation round entirely
   in memory using the bundled red `rule_based_player`;
3. for every decision, reuse public `encode_mahjax_public_observation`, store
   exact 630 features, the exact 87-entry bool legal mask and the bundled-policy
   legal action label before applying the environment transition;
4. hard-cap each collection round at 256 and require terminal/no truncation;
5. require exactly 54 seed-0 training examples and 64 seed-1 evaluation
   examples with no cross-seed mixing;
6. initialize `(630,87)` float32 weights from `PRNGKey(123)` normal scale
   `0.01` and 87 zero biases;
7. use masked multiclass cross-entropy over only legal actions;
8. perform exactly 16 deterministic full-batch gradient-descent epochs with
   learning rate `0.1`, one JIT `value_and_grad` train step and no shuffle;
9. calculate train/eval masked losses and exact imitation accuracies before
   and after training, plus loss history and parameter-delta norms;
10. return only a frozen diagnostic summary, not weights, data or checkpoint.

Acceptance values from an independent pinned-runtime probe:

```text
train_count = 54
eval_count = 64
initial_train_loss ~= 1.70919883
final_train_loss ~= 1.38197553
initial_eval_loss ~= 1.76650584
final_eval_loss ~= 1.54172158
initial_train_accuracy ~= 0.29629630
final_train_accuracy ~= 0.51851851
initial_eval_accuracy = 0.234375
final_eval_accuracy = 0.5
weight_delta_l2 ~= 0.67900646
bias_delta_l2 ~= 0.23012902
```

Tests must require all 16 pre-update loss-history values to be finite and
strictly decreasing, both train/eval final loss lower than initial, both
accuracies nondecreasing, parameters changed, deterministic equal-run summary,
exact sample/provenance separation, exact source structure and full regressions.

## Forbidden Scope

- no real Tenhou, real haifu, external log, platform data/account/automation;
- no file/dataset/checkpoint/model artifact persistence or CLI;
- no hidden/opponent-private observation state;
- no reward/RL update, environment outcome objective or self-play learning;
- no minibatch, shuffle, scheduler, early stop, hyperparameter sweep or GPU;
- no production training/evaluation, league or candidate promotion;
- no strength, stable-dan or LuckyJ claim;
- no broad P8 or P9-P12.

## Evidence Grade

Reviewed bridge:

```text
P4/P8 untrained model-output environment bridge review-closure evidence.
```

Approved training:

```text
P7/P8 local synthetic rule-policy imitation training smoke evidence only.
```
