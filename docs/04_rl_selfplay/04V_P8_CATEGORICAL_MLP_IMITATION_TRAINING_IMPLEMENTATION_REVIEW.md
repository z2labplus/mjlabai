# 04V_P8_CATEGORICAL_MLP_IMITATION_TRAINING_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04U` categorical-feature MLP imitation training and all-project
outcome smoke.

APPROVED for next exact implementation task:
one seed-1 all-project-seat shared categorical-MLP raw-outcome policy-gradient
update.
```

Zero planning/review gates remain before code.

## Reviewed Commit

```text
78a9f7b  Train categorical MahJax imitation policy
```

## Conformance Review

- Only the two exact `04U` source/test files plus direct governance changed.
- The public API has the exact ten approved symbols and returns a frozen result;
  parameter arrays remain available only through an unexported in-process
  helper.
- The encoder validates the exact current-player observation dictionary and
  produces 882 finite features with the approved categorical layout. It does
  not read opponent hands or direct private player state.
- Exact disjoint local teacher seeds `0..7` and `8..11` produce `482/221`
  examples. Every teacher label is checked against its exact environment-owned
  87-action legal mask.
- The model is exactly `882 -> 64 ReLU -> 87`, model seed `123`, normal scale
  `0.03`, zero biases and `62,167` parameters.
- Exactly 48 full-batch Adam epochs use learning rate `0.003`, betas
  `0.9/0.999` and epsilon `1e-8`.
- Final train/evaluation loss is `0.36734492/1.77358353`; exact accuracy is
  `0.93153530/0.58371043`. Both losses improve from their initial values and
  all parameter groups change finitely.
- Greedy shared-project seeds `0..15` all terminate legally. Exact nonzero
  cumulative raw outcomes occur at `(0,1,3,5,6,7,10)` with the approved
  vectors.
- No update occurs during the all-project diagnostic rounds. No path, I/O,
  persistence, saved dataset, model artifact, external data, production
  self-play/evaluation or strength claim exists.

## Validation

```text
9 focused tests OK
404 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent public-result and next-update probes pass
```

## Direct All-Project Update Probe

The same reviewed MLP is used by all four seats. Seed `1` is split into
independent environment-initialization and shared-policy sampling streams. A
legal-masked categorical rollout yields:

```text
transition_count = 77
seat_decision_counts = (21,22,17,17)
cumulative_raw_rewards = (-20,70,-20,-30)
final_raw_rewards = (-20,80,-20,-20)
final_scores = (230,320,230,220)
```

Each selected log probability is weighted by its acting seat's cumulative raw
reward divided by 100. One shared update at learning rate `0.01` changes the
aggregate objective and all four parameter arrays:

```text
objective = 0.09366636 -> 0.09301171
parameter_delta_l2 =
  (0.0009705852,0.0001615889,0.0023494314,0.0002528356)
```

Replaying the exact seed and RNG schedule after this small update preserves the
same legal 77-step trajectory and outcome. This proves only finite executable
credit assignment across four project-controlled seats; it is not improvement
or strength evidence.

## Direct Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_all_project_policy_gradient_smoke.py
tests/rl/test_mahjax_categorical_mlp_all_project_policy_gradient_smoke.py
```

Direct governance synchronization is allowed. Existing production source,
tests, package exports, dependencies and artifacts remain unchanged.

Exact public API:

```text
MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SMOKE_VERSION
MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_SEED
MAHJAX_CATEGORICAL_MLP_ALL_PROJECT_POLICY_GRADIENT_LEARNING_RATE
MahJaxCategoricalMlpAllProjectPolicyGradientSmokeError
MahJaxCategoricalMlpAllProjectPolicyGradientResult
run_mahjax_categorical_mlp_all_project_policy_gradient_smoke
```

### Exact rollout contract

1. obtain the reviewed in-memory categorical MLP parameters through the private
   `04U` helper; do not recreate or persist training data/parameters;
2. use MahJax `red_mahjong` single-round dict observations and exact seed `1`;
3. split independent environment initialization and policy-action RNG streams;
4. all seats use the same shared project MLP and sample from its legal-masked
   categorical distribution; no bundled-rule participant is present;
5. record each public feature, complete legal mask, selected action and actor;
6. require every action legal, monotonic progress, exactly 77 transitions,
   terminal without truncation and the exact raw/global outcome above.

### Exact update contract

For trajectory decision `i` made by actor `a_i`:

```text
seat_return[a] = cumulative_raw_reward[a] / 100
objective = -mean(seat_return[a_i] * log pi(action_i | observation_i, legal_i))
```

- use no baseline, critic, discount, bootstrapping, entropy term, reward shaping
  or replay;
- execute exactly one `jax.value_and_grad` call over all four MLP parameter
  arrays and one update at exact learning rate `0.01`;
- pin the exact objective and four L2 parameter deltas from the probe;
- rerun the same seed/RNG schedule and pin the unchanged legal trajectory,
  outcome and scores;
- return frozen diagnostics only; arrays may not appear in public output.

### Required tests

- exact six-symbol API, constants and frozen array-free result;
- reviewed training-result identity and exact model/seed/learning-rate metadata;
- exact 77-step pre/post actor/action/legal traces and seat counts;
- exact pre/post raw outcomes/global scores and actor-indexed return vector;
- exactly one finite update, objective decrease and exact four parameter deltas;
- every action legal, terminal/no truncation and deterministic repeat;
- runtime/training failure translation into the new public error;
- no path, I/O, persistence, replay, rule participant or hidden-state access;
- warnings deny improvement, evaluation, production self-play and strength.

## Forbidden Scope

- no second update, second seed/round, replay buffer or optimizer loop;
- no baseline/critic/GAE/discount/entropy/reward shaping;
- no saved dataset, parameter, checkpoint, model artifact, path or CLI;
- no external/real data, Tenhou, haifu, platform data or source ingestion;
- no production self-play/evaluation, league, promotion or comparison;
- no model-strength, stable-dan or LuckyJ claim;
- no P9-P12.

## Evidence Grade

```text
P8 categorical-MLP implementation-review evidence and exact one-update local
all-project-seat task approval only.
```
