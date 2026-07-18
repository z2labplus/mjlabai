# 04L_P4_MAHJAX_SINGLE_ROUND_ROLLOUT_APPROVAL

## Decision

```text
ACCEPTED as current-scope complete:
the exact MahJax integration implementation reviewed in `04K`.

APPROVED for next exact implementation task:
one deterministic, hard-capped, local MahJax single-round rollout smoke.
```

Zero proposal, boundary or review gates remain before this code.

## Executable Basis

An independent, non-repository exploratory probe used the pinned
`mahjax==0.1.2`, `jax==0.4.30` and `jaxlib==0.4.30` runtime with:

```python
environment = mahjax.make(
    "red_mahjong",
    round_mode="single",
    observe_type="dict",
    next_round_style="auto",
)
step_fn = jax.jit(environment.step)
```

For seed 0, selecting the lowest `True` action from each environment-owned
legal mask produced:

```text
first JIT step compile: about 7.35 seconds on the checked CPU host
transitions: 94
terminated: true
truncated: false
final raw rewards: (0.0, 0.0, 0.0, 0.0)
final scores: (250, 250, 250, 250) in MahJax hundred-point units
```

The eager exploratory attempt was stopped after sustained compile overhead;
the approved implementation must use `jax.jit(environment.step)`. This is an
engineering execution requirement, not a latency metric or benchmark claim.

## Exact Files

Only these implementation files may change, plus direct governance
synchronization:

```text
src/mjlabai/environment/__init__.py
src/mjlabai/environment/mahjax_single_round_rollout_smoke.py
tests/environment/test_mahjax_single_round_rollout_smoke.py
```

`pyproject.toml` pins must remain unchanged.

## Exact Public API

```text
MAHJAX_SINGLE_ROUND_ROLLOUT_SMOKE_VERSION
MAHJAX_SINGLE_ROUND_TRANSITION_CAP
MahJaxSingleRoundRolloutSmokeError
MahJaxSingleRoundStep
MahJaxSingleRoundRolloutResult
run_mahjax_single_round_rollout_smoke
```

`MAHJAX_SINGLE_ROUND_TRANSITION_CAP` must equal 256.

## Rollout Semantics

`run_mahjax_single_round_rollout_smoke(seed: int = 0)` must:

1. accept only exact int seeds from 0 through `2**32 - 1`;
2. verify the pinned MahJax package/environment identity;
3. construct only the reviewed `red_mahjong`, `single`, `dict`, `auto`
   environment;
4. initialize from `jax.random.PRNGKey(seed)`;
5. compile only `environment.step` with `jax.jit`;
6. use one explicit `for` bounded by 256 and no `while` loop;
7. before every transition, require a nonterminal/nontruncated state and an
   exact 87-entry bool legal mask with at least one `True`;
8. choose only the lowest-index legal action;
9. record one frozen step diagnostic containing pre-step index, acting player,
   complete legal-action-index tuple and selected action;
10. apply exactly one public `step_fn(state, jnp.int32(action))` and block until
    the state is ready;
11. require exact monotonic `step_count` progress;
12. accumulate all four raw reward components without shaping;
13. stop only on public `terminated` or `truncated` status;
14. require seed 0 to terminate without truncation before the cap;
15. return frozen trace, final state diagnostics, raw rewards, cumulative raw
    rewards, final scores, evidence grade and warnings.

If the cap is exhausted, a mask/state invariant fails, or the pinned runtime
differs, raise `MahJaxSingleRoundRolloutSmokeError` with the original cause
chained where applicable. Do not silently increase the cap or change policy.

## Seed-0 Acceptance Values

The focused test must pin:

```text
transition_count = 94
final_step_count = 94
terminated = true
truncated = false
final_rewards = (0.0, 0.0, 0.0, 0.0)
cumulative_rewards = (0.0, 0.0, 0.0, 0.0)
final_scores = (250, 250, 250, 250)
```

Every trace entry must have a player from 0 through 3, an exact increasing
pre-step index, a non-empty sorted legal tuple, and
`selected_action == legal_actions[0]`.

## Required Tests

1. Exact six-symbol export surface and frozen result/step objects.
2. Exact package/environment identity and unchanged dependency pins.
3. Seed-0 exact transition/final values above.
4. Trace length equals transition count and indices are monotonic.
5. Every selected action is the lowest complete environment legal tuple item.
6. All players/actions/legal counts are in bounds.
7. Final termination occurs before the 256-step cap without truncation.
8. Raw and cumulative rewards are unshaped four-tuples.
9. Equal seed-0 calls return equal normalized diagnostics.
10. Invalid seed types/ranges are rejected before environment execution.
11. A test-local cap override to 1 raises the cap-exhaustion error.
12. Source has exactly one explicit `for`, zero `while`, one `jax.jit` step
    creation and no path/network/model/training/self-play behavior.
13. Existing integration, environment and full repository regressions pass.

## Forbidden Scope

- no model or policy callback;
- no learning, update, optimizer, gradient or checkpoint;
- no multiple rounds/games, parallel environments or batching;
- no random/stochastic action policy beyond environment initialization;
- no project action adapter or canonicalizer;
- no reward shaping or RL objective;
- no replay/persistence/file/CLI path;
- no GPU/remote service;
- no real Tenhou, real haifu, external log, platform data/account/automation;
- no production self-play/evaluation/league;
- no policy-quality, model-strength, stable-dan, LuckyJ or promotion claim;
- no broad P8 or P9-P12 work.

## Evidence Grade

The implementation may provide only:

```text
P4 pinned local single-round environment rollout smoke evidence.
```

It is not full Tenhou-rule conformance, self-play, training, evaluation or
model-strength evidence.
