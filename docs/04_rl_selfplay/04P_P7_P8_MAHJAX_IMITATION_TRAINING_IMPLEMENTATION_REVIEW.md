# 04P_P7_P8_MAHJAX_IMITATION_TRAINING_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04O` in-memory MahJax bundled-rule-policy imitation training smoke.

APPROVED for next exact implementation task:
one held-out-seed MahJax round comparing the same project model before and
after the reviewed in-memory training.
```

No proposal, boundary or second review gate remains before that code.

## Reviewed Commit

```text
1ae9755  Train first MahJax imitation policy smoke
```

## Conformance Review

- The exact nine-symbol API, one source file and one focused test file match
  `04O`; no package export was added.
- Seed 0 and seed 1 independently collect 54 train and 64 evaluation decisions
  from public observations. Every teacher label is checked against the exact
  environment-owned bool 87-action mask.
- The encoder is the reviewed public-only 630-feature encoder. No hidden hand
  or private environment-state feature enters the model.
- Model seed 123 initializes exact `(630,87)` float32 weights and 87 zero
  biases. Exactly 16 deterministic full-batch masked-cross-entropy updates run
  at learning rate `0.1`, with no shuffle, minibatch or early stop.
- All 16 pre-update train losses are finite and strictly decreasing. Train and
  evaluation loss fall, accuracies do not fall, and both parameter groups
  change.
- The public function returns one frozen diagnostic summary. It exposes no
  sample, parameter, path, dataset, model artifact or checkpoint.
- Warnings and evidence grade prevent policy-quality, model-strength, Tenhou,
  stable-dan, LuckyJ and promotion claims.

## Validation

```text
10 focused tests OK
346 repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff --check pass
independent API/numeric/determinism probe pass
```

Exact result:

```text
train/eval examples = 54 / 64
train loss = 1.70919883 -> 1.38197553
eval loss = 1.76650584 -> 1.54172158
train accuracy = 0.29629630 -> 0.51851851
eval accuracy = 0.234375 -> 0.5
weight/bias delta L2 = 0.67900646 / 0.23012902
```

## Direct Held-Out Round Approval

The next exact task must prove the trained in-memory parameters can drive the
reviewed public-observation/legal-mask environment path on a seed not used for
training or evaluation-label diagnostics. It may refactor the training module
only enough to return parameters through a private in-process helper; public
training API and frozen summary behavior must remain unchanged.

Exact implementation files:

```text
src/mjlabai/supervised/mahjax_rule_policy_imitation_training_smoke.py
tests/supervised/test_mahjax_rule_policy_imitation_training_smoke.py
src/mjlabai/environment/mahjax_trained_imitation_policy_round_smoke.py
tests/environment/test_mahjax_trained_imitation_policy_round_smoke.py
```

Direct governance synchronization is allowed. No package export is required.

Exact new public API:

```text
MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SMOKE_VERSION
MAHJAX_TRAINED_IMITATION_POLICY_ROUND_SEED
MahJaxTrainedImitationPolicyRoundSmokeError
MahJaxTrainedImitationPolicyRoundResult
run_mahjax_trained_imitation_policy_round_smoke
```

The implementation must:

1. preserve `run_mahjax_rule_policy_imitation_training_smoke()` exactly;
2. add one private in-process helper that returns initial/trained arrays plus
   the same frozen summary, with no public export or persistence;
3. use held-out environment seed 2, distinct from train seed 0 and evaluation
   label seed 1;
4. run the same project model before and after training in separate identical
   seed-2 single-round environments using only the public 630-feature encoder;
5. apply the exact environment-owned 87-action legal mask before every argmax
   and record every selected action with its complete legal tuple;
6. hard-cap each rollout at 256, require terminal/no truncation, and read final
   scores only from global `state.round_state.score`;
7. return frozen initial/trained traces and raw outcome diagnostics, plus the
   reviewed training summary and an explicit trajectory-changed diagnostic;
8. require deterministic exact seed-2 acceptance values from the independent
   probe: initial 88 transitions, trained 94 transitions, both terminal, no
   truncation, global scores `(250,250,250,250)`, initial first action 12,
   trained first action 71 and unequal action traces.

Tests must cover exact API/types/seeds, unchanged training summary, private
parameter handoff, complete legality, 256 caps, terminal/global-score result,
exact acceptance values, deterministic equality, changed trajectory, source
bounds, warnings and full regressions.

## Forbidden Scope

- no parameter/data/checkpoint/artifact persistence, loader, path or CLI;
- no real Tenhou, real haifu, external log, platform data/account/automation;
- no hidden state, opponent-private feature or tile-notation expansion;
- no reward/RL update, self-play learning, league or production evaluation;
- no training beyond exact seed-0 54 examples and 16 full-batch updates;
- no strength, stable-dan, LuckyJ or candidate-promotion claim;
- no broad P8 or P9-P12.

## Evidence Grade

```text
P7/P8 local synthetic rule-policy imitation training implementation-review
evidence and held-out environment-use task approval only.
```
