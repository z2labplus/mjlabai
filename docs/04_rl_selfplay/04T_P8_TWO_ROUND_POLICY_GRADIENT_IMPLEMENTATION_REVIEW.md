# 04T_P8_TWO_ROUND_POLICY_GRADIENT_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04S` two-round sequential on-policy raw-outcome training smoke.

APPROVED for next exact implementation task:
one seed-0 two-project-seat shared-policy raw-outcome update smoke with fixed
rule-policy seats as a bridge toward non-degenerate self-play.
```

Zero planning/review gates remain before code.

## Reviewed Commit

```text
1141765  Train MahJax policy across two raw-outcome rounds
```

## Findings

No correctness, scope, evidence or validation blocker was found.

## Conformance Review

- Only the four exact `04S` source/test files plus direct governance documents
  changed. No dependency or package-export change was added.
- The one-round public six-symbol API/result remains unchanged. Its collector
  and update extraction is private and all original focused tests pass.
- One explicit two-item loop executes exact seeds `(1,5)` in order. The direct
  assignment `weights, biases = update.weights, update.biases` carries the
  first update into the second collection/update.
- Each round uses independent environment, fixed-rule and project-action RNG
  streams. Every selected action is checked against the environment legal mask.
- Only cumulative raw seat-0 reward divided by 100 enters the same reviewed
  masked selected-log-probability objective. Exactly two updates occur at `0.1`.
- Exact seed-1 and seed-5 transitions, actions, raw/cumulative outcomes, global
  scores, objectives and parameter deltas match the approved probes.
- The result is frozen and contains diagnostics only. No arrays, path, I/O,
  persistence, replay, checkpoint, evaluation or strength surface was added.

## Independent Continuity Probe

The same seed-5 categorical samples occur before and after the seed-1 update,
but the frozen-trajectory initial objective changes from `-0.85021764` with the
imitation parameters to `-0.85308558` with the directly carried seed-1 updated
parameters. The seed-1 weight/bias deltas are nonzero
`0.04220101 / 0.01279154`. This independently confirms round-2 parameter use;
the implementation does not restart from the imitation parameters.

## Validation

```text
19 focused tests OK
384 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff --check pass
independent API/continuity/legality/objective/delta/outcome probe pass
```

## Current-Scope Acceptance

The exact two-round implementation is accepted only as P8 local bounded
environment-outcome training-smoke evidence. It proves two sequential updates
on one continuous in-memory project policy against fixed bundled rule
opponents. It does not prove policy improvement, self-play strength, production
training, evaluation, league performance, stable dan or LuckyJ comparison.

## Direct Two-Project-Seat Update Approval

An independent all-project-seat probe over fixed seeds `0..15` produced legal
terminal rounds but zero cumulative raw rewards for every seat in every round.
An immediate all-project raw-outcome update would therefore be a zero-gradient
smoke and is not approved as material progress.

The smallest non-degenerate bridge uses shared project parameters in seats
`(0,2)` and fixed bundled rule policies in seats `(1,3)`. Independent seed-0
probing yields a legal terminal round with nonzero raw outcomes and a finite
shared-policy update.

Exact files:

```text
src/mjlabai/rl/mahjax_two_project_seat_policy_gradient_smoke.py
tests/rl/test_mahjax_two_project_seat_policy_gradient_smoke.py
```

Direct governance synchronization is allowed. No existing production module,
public API, package export or dependency needs to change.

Exact public API:

```text
MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SMOKE_VERSION
MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_SEED
MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_PROJECT_SEATS
MAHJAX_TWO_PROJECT_SEAT_POLICY_GRADIENT_LEARNING_RATE
MahJaxTwoProjectSeatPolicyGradientSmokeError
MahJaxTwoProjectSeatPolicyGradientResult
run_mahjax_two_project_seat_policy_gradient_smoke
```

The implementation must:

1. start from the reviewed in-memory imitation parameters;
2. use exact seed `0`, shared project parameters for seats `(0,2)` and fixed
   bundled rule policies for seats `(1,3)`;
3. split independent initialization, rule-policy and project-action RNG streams;
4. run one bounded 256-transition MahJax round; project seats sample from
   public-feature, legal-masked categorical logits and rule seats never learn;
5. record complete actor/action/legal/policy traces and project decision data;
6. use each project decision's acting seat cumulative raw reward divided by
   `100`, with objective
   `-mean(return_scale[actor] * selected_legal_log_probability)`;
7. apply exactly one shared weight/bias update at learning rate `0.1` after the
   terminal round; no per-seat or mid-round update;
8. pin 92 transitions, seat counts `(21,22,23,26)`, project decision counts
   `(21,23)`, 44 project decisions, final raw `(-10,-10,-10,30)`, cumulative
   `(-10,-10,-10,20)` and global scores `(240,240,240,270)`;
9. pin project return scales `(-0.1,-0.1)`, objective
   `-0.19244556 -> -0.19273609` and weight/bias deltas
   `0.00523261 / 0.00124493`;
10. return one deterministic frozen diagnostic summary without parameter arrays.

Tests must cover exact API/frozen output, exact participants and RNG split, one
round/one update cap, both project seats acting, fixed rule seats not updating,
all actions legal, actor-indexed raw returns, exact outcomes/objectives/deltas,
deterministic equality, source bounds and no I/O/persistence/replay.

## Forbidden Scope

- no four-project-seat update, second round, variable trainer or seat rotation;
- no replay, buffer, baseline, critic, discount, GAE, bootstrap or shaping;
- no production self-play, evaluation, league, promotion or comparison;
- no path, CLI, persistence, checkpoint, artifact or new dependency;
- no real data, Tenhou, haifu, external log or platform automation;
- no improvement, policy-quality, model-strength, stable-dan or LuckyJ claim;
- no P9-P12.

## Evidence Grade

```text
P8 two-round sequential training implementation-review evidence and exact
two-project-seat shared-policy bridge-update task approval only.
```
