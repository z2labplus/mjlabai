# 04J_P4_PROVEN_RIICHI_ENVIRONMENT_INTEGRATION_PATH_DECISION

## Decision

```text
ACCEPTED as current-scope complete:
the exact `04H` synthetic transition implementation reviewed in `04I`.

SELECTED integration path:
MahJax v0.1.2, tag v0.1.2, commit
3f9cee195dcbe226c26c9f8802b1a3cb9e2de14f, Apache-2.0.
```

The next task is the exact executable integration smoke defined below. Zero
proposal, boundary or approval gates remain before code.

## Why This Path

Primary-source inspection on 2026-07-18 found:

| Candidate | Finding | Decision |
|---|---|---|
| MahJax | Maintained 2026 riichi environment; PyPI `0.1.2`; Python `>=3.9`; pure-Python package; JAX CPU support for CPython 3.9/macOS arm64; four-player red-mahjong environment with `init`, `legal_action_mask`, `observe`, `step`, rewards and terminal state; Apache-2.0 | Select and pin |
| mjx | PyPI release `0.1.0` from 2022; official package documentation says macOS Apple Silicon is unsupported; available macOS wheels are x86_64 only | Reject for this host |
| MahjongRepository/mahjong | Maintained MIT hand calculator for shanten, winning hands and scoring; not a game environment and does not provide environment-owned legal-action/state-transition/observation lifecycle | Reject as the P4 environment path |

MahJax is alpha software and its API is documented as provisional. Pinning the
package, JAX runtime and exact smoke API is therefore mandatory.

## Source And Rights Evidence

- Source: <https://github.com/nissymori/mahjax>
- Release: <https://github.com/nissymori/mahjax/releases/tag/v0.1.2>
- Pinned commit: <https://github.com/nissymori/mahjax/commit/3f9cee195dcbe226c26c9f8802b1a3cb9e2de14f>
- Package: <https://pypi.org/project/mahjax/0.1.2/>
- License: Apache-2.0 in the source repository and package metadata.
- Package artifact: `mahjax-0.1.2-py3-none-any.whl`, SHA-256
  `f6c9e5c2bc6ef9a2737c56d39118a922fa20400ac9606a7d173a9c1afcbfa50b`.

No source, wheel, binary, dataset, log or model artifact may be copied into
this repository. Installation must use the pinned package dependency only.

## Host Compatibility

The checked host is macOS 26.2 arm64 with CPython 3.9.6.

- MahJax `0.1.2` requires Python `>=3.9` and publishes a `py3-none-any` wheel.
- Pin `jax==0.4.30` and `jaxlib==0.4.30` for the first smoke.
- JAX `0.4.30` requires Python `>=3.9`.
- PyPI publishes
  `jaxlib-0.4.30-cp39-cp39-macosx_11_0_arm64.whl`.
- The first smoke is CPU-only. It must not require GPU, accelerator or remote
  service access.

Installability remains an executable acceptance item: dependency resolution,
import and one state transition must all pass on this host.

## Approved Interface

The integration may use only these public MahJax surfaces:

```python
import jax
import mahjax

env = mahjax.make(
    "red_mahjong",
    round_mode="single",
    observe_type="dict",
    next_round_style="auto",
)
state = env.init(jax.random.PRNGKey(0))
observation = env.observe(state)
next_state = env.step(state, selected_legal_action)
```

The smoke may inspect only:

- `mahjax.__version__`
- `env.id`, `env.version`, `env.num_players`, `env.num_actions`
- `state.current_player`, `state.legal_action_mask`, `state.step_count`
- `state.rewards`, `state.terminated`, `state.truncated`
- the public observation mapping and its keys
- the corresponding fields on `next_state`

The selected action must be the lowest-index `True` entry in the initial
environment-owned `legal_action_mask`. The integration must never synthesize
or override the legal set and must never choose an illegal action.

## Exact Next Implementation

Only these repository files may change for implementation plus direct
governance synchronization:

```text
pyproject.toml
src/mjlabai/environment/__init__.py
src/mjlabai/environment/mahjax_integration_smoke.py
tests/environment/test_mahjax_integration_smoke.py
```

Required direct dependencies:

```text
mahjax==0.1.2
jax==0.4.30
jaxlib==0.4.30
```

The module must expose a frozen result object and one deterministic
`run_mahjax_integration_smoke(seed: int = 0)` function. The result must record
package/environment identity, initial and next step/player fields, legal-action
count, selected legal action, observation keys, rewards/terminal flags and
fixed evidence warnings.

## Required Tests

1. Pinned package and environment identity.
2. Four players and 87-action public action space.
3. Deterministic initialization for seed 0.
4. Non-empty boolean environment-owned legal-action mask.
5. Lowest-index legal action selection.
6. Non-empty public observation mapping with expected core keys.
7. One legal `env.step` increments `step_count` exactly once.
8. The step does not terminate through the illegal-action penalty path.
9. Repeated smoke calls with the same seed return equal frozen diagnostics.
10. Invalid seed types or negative seeds raise the project integration error.
11. No path, CLI, network, account, platform, real-log or model input exists.
12. Full repository regression suite remains green.

## Stop Conditions

Stop and record a concrete blocker if any of these occurs:

- pinned dependencies cannot resolve on CPython 3.9/macOS arm64;
- import or initialization fails;
- the public API differs from the pinned evidence;
- the initial legal mask is empty or cannot drive one legal transition;
- the smoke requires real data, a remote service, platform access or GPU;
- dependency/license metadata differs from this decision.

Do not silently change version, source, environment ID, ruleset, runtime or
API. Any such change requires a new evidence-backed decision.

## Evidence Boundary

The implementation may provide only:

```text
P4 pinned third-party local riichi environment integration smoke evidence.
```

It is not environment conformance to every Tenhou rule, self-play, training,
evaluation, policy quality, model strength, stable-dan, LuckyJ comparison,
candidate promotion or P8-P12 evidence.
