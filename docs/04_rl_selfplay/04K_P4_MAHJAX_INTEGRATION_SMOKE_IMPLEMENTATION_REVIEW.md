# 04K_P4_MAHJAX_INTEGRATION_SMOKE_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.
```

Commit `7ab90d5` conforms to the exact `04J` approval. No dependency,
correctness, scope, evidence or test blocker was found. Production code and
tests were not modified during review.

## Reviewed Scope

- `pyproject.toml`
- `src/mjlabai/environment/__init__.py`
- `src/mjlabai/environment/mahjax_integration_smoke.py`
- `tests/environment/test_mahjax_integration_smoke.py`
- direct implementation governance synchronization.

No action adapter, generalized rules interface, episode runner, model output,
self-play, training, evaluation, real data, Tenhou/platform path, broad P8 or
P9-P12 work was reviewed or approved.

## Findings

### Dependency And Surface

- Exact pins are `mahjax==0.1.2`, `jax==0.4.30` and `jaxlib==0.4.30`.
- Installed versions satisfy the pins and `pip check` reports no broken
  requirements on CPython 3.9/macOS arm64.
- The module exposes exactly the seven `04J` public symbols.
- The result is frozen and records package/environment identity, players,
  action space, seed, state progress, legal counts, observation keys, rewards,
  terminal flags, evidence grade and warnings.
- Imports and source inspection show no path, subprocess, socket, request,
  model, optimizer, training or platform behavior.

### Public MahJax Behavior

- The code uses only public `mahjax.make`, `env.init`, `env.observe`,
  `state.legal_action_mask` and `env.step` surfaces.
- Environment identity is `red_mahjong`, version `beta`, four players and 87
  actions.
- Both masks are exact 87-entry bool arrays owned by the environment.
- Seed 0 produces initial player 2, step 0 and 12 legal actions.
- The full independent legal tuple is
  `(2, 4, 5, 8, 10, 11, 14, 17, 19, 21, 27, 71)`; the selected action 2 is
  therefore the lowest legal action.
- The public observation has the exact 12 reviewed keys.
- One direct and wrapped transition both produce next player 3, step 1, 13
  legal actions, four zero rewards, `terminated=False` and `truncated=False`.
- Equal seed-0 calls produce equal frozen diagnostics; invalid seeds are
  rejected before runtime use.

## Validation Evidence

```text
python3 -m unittest tests/environment/test_mahjax_integration_smoke.py
Ran 11 tests: OK

python3 -m unittest <all explicit test modules>
Ran 302 tests: OK (skipped=2 existing environment-gated checks)

python3 -m pip check
No broken requirements found.

python3 -m compileall -q src tests
passed

git diff --check
passed
```

The independent direct-MahJax seed-0 probe confirms package/JAX versions,
the full legal tuple and equality of selected action, player/step progress and
next legal count with the project result.

## Evidence Grade

```text
P4 pinned third-party local riichi environment integration implementation
review closure evidence only.
```

This is not complete Tenhou-rule conformance, an episode, self-play, training,
evaluation, policy quality, model strength, stable-dan, LuckyJ, promotion or
P8-P12 evidence.

## Next-Step Constraint

The exact integration may be accepted as current-scope complete. The next
decision must directly approve or defer one materially progressive bounded
single-round MahJax rollout smoke. If approved, it must use only the pinned
local environment, environment-owned legal masks and a hard transition cap,
prove terminal/raw-reward behavior, name exact files/API/tests and leave zero
gates before code.

Another one-step wrapper, sibling boundary or proposal chain is forbidden.
Real Tenhou/platform access, real logs/haifu, model output, production
self-play/training/evaluation, strength claims, broad P8 and P9-P12 remain
unapproved.
