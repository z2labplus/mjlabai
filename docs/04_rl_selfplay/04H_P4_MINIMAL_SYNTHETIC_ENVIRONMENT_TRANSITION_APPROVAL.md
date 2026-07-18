# 04H_P4_MINIMAL_SYNTHETIC_ENVIRONMENT_TRANSITION_APPROVAL

## Decision

```text
P8 two-policy interaction = ACCEPTED as current-scope complete.
Further P8 interaction wrapping = DEFERRED pending environment authority.
P4 environment prerequisite = ACTIVATED.
Next exact P4 implementation task = APPROVED.
```

Repository inspection found no environment package, authoritative state object
or executable transition. `04A` still marks legal-action/scoring/hidden-
information/opponent/logging components planned, while `12S`/`12T` define and
review only authority boundaries. Continuing P8 wrappers would not create a
real transition authority.

Next executable task:

```text
Implement exact minimal P4 synthetic/local environment transition smoke only.
```

No proposal or additional review may precede this code.

## Exact Approved Files

- `src/mjlabai/environment/__init__.py`
- `src/mjlabai/environment/synthetic_transition_smoke.py`
- `tests/environment/test_synthetic_transition_smoke.py`
- direct docs/governance synchronization.

No fixture/data, dependency, CLI/path, persistence, RNG, model, reward,
training, evaluation, self-play or real-data file is approved.

## Exact Public API

```text
SYNTHETIC_ENVIRONMENT_ID
SYNTHETIC_ENVIRONMENT_TRANSITION_SMOKE_VERSION
SYNTHETIC_FOUR_PLAYER_RULESET_ID
SyntheticEnvironmentAction
SyntheticEnvironmentState
SyntheticEnvironmentTransitionResult
SyntheticEnvironmentTransitionSmokeError
apply_synthetic_environment_transition_smoke
```

## Exact Action

`SyntheticEnvironmentAction` is frozen and contains only:

```text
action_id
actor
action_type
tile
tsumogiri
```

Requirements:

- `action_id` is a non-empty exact string.
- `actor` is exact int 0 through 3.
- `action_type` is exactly `dahai`.
- `tile` is a non-empty exact string preserved verbatim.
- `tsumogiri` is exact bool.
- no tile parsing, notation conversion, red-five normalization or broader
  action support is approved.

Strict action matching compares `actor`, `action_type`, `tile` and
`tsumogiri`; `action_id` is audit identity and does not decide legality.

## Exact State

`SyntheticEnvironmentState` is frozen and contains only:

```text
environment_id
environment_version
ruleset_id
episode_id
step_index
acting_seat
legal_actions
terminal
project_authored
synthetic
local_only
uses_real_data
uses_external_log
uses_platform_data
```

The approved pre-state is deliberately one-transition-only:

- fixed environment/ruleset/version constants.
- non-empty episode ID.
- `step_index = 0`.
- `acting_seat` exact int 0 through 3.
- exactly two exact legal `dahai` actions for the acting seat.
- legal action IDs and strict canonical tuples are pairwise distinct.
- `terminal = false`.
- project-authored/synthetic/local flags true.
- real-data/external-log/platform-data flags false.

The helper rejects a terminal input, another step index, dynamic legal-action
count or any provenance mismatch.

## Exact Transition

The helper:

1. validates the exact pre-state and proposed action.
2. derives legality only from the state's two authoritative legal actions.
3. matches strict canonical fields and ignores proposed `action_id` for
   equality.
4. rejects zero or ambiguous matches without changing state.
5. selects the matching legal action as the authoritative applied action.
6. creates one deterministic event ID from episode and step identity.
7. creates a new frozen post-state with `step_index = 1`, next acting seat,
   empty legal actions and `terminal = true`.
8. returns immutable provenance and non-evidence diagnostics.

This exact smoke terminates after one transition only to prove authority,
legality and immutable state progression. It does not implement a hand, draw,
discard consequences, tile ownership, scoring, hidden information, RNG,
multi-step episode, rules engine or real Mahjong gameplay.

## Exact Result

`SyntheticEnvironmentTransitionResult` is frozen and contains only:

```text
transition_version
pre_state
proposed_action
applied_action
legal_action_index
event_id
post_state
transition_applied
terminal_reached
safety_guardrails_all_satisfied
evidence_grade
warnings
```

Warnings must state exact single-transition synthetic/local environment smoke,
four-seat contract identity, strict `dahai` matching only, no Mahjong rules/
hand/scoring/hidden-state/RNG/multi-step episode, no model/reward/training/
self-play/evaluation, no persistence/dependency/real data, and not policy-
quality/strength/Tenhou/stable-dan/LuckyJ/promotion evidence.

## Exact Tests

Focused tests must cover:

1. applying legal action 0.
2. applying legal action 1.
3. rejecting a non-legal strict action.
4. exact state/version/ruleset/provenance validation.
5. exact two legal actions, acting-seat binding and unique IDs/canonical tuples.
6. strict matching fields with `action_id` excluded from equality.
7. verbatim red-indicator tile token preservation without normalization.
8. deterministic event, monotonic post-state, next seat and terminal state.
9. terminal/reused/wrong-index input rejection.
10. deterministic equality, complete input non-mutation and frozen objects.
11. exact fields, flags, evidence grade and warnings.
12. exact package surface with no parser, file, RNG, model or copied RL logic.

Validation must include all 279 explicit repository tests, focused tests,
`compileall` and `git diff --check`.

## Evidence And Stop Boundary

Future passing evidence is only:

```text
P4 exact single-transition synthetic/local environment-contract smoke evidence
only.
```

It is not a complete Mahjong environment, legal-action/rules/scoring engine,
game episode, self-play, RL training/evaluation, model-strength, Tenhou,
stable-dan, LuckyJ or promotion evidence.

Stop and review if the implementation requires another action type, dynamic
legal-set size, multi-step episode, RNG, tile ownership, scoring, hidden state,
model output, external dependency/data or API beyond this document.

## Gate Accounting

```text
P8 two-policy current-scope acceptance = satisfied
P8 environment gap = confirmed
P4 exact transition implementation approval = satisfied
remaining mandatory gate count before implementation = 0
```
