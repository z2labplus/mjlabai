# 04R_P8_MAHJAX_MIXED_POLICY_ROUND_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04Q` trained-project/rule-policy mixed single-round smoke.

APPROVED for next exact implementation task:
one on-policy MahJax raw-outcome policy-gradient update smoke.
```

Zero proposal, boundary or additional review gates remain before code.

## Reviewed Commit

```text
4d7ef8d  Run MahJax trained versus rule policy round
```

## Conformance Review

- Exact six-symbol API, one source/test pair, no package export/dependency.
- Reviewed trained parameters remain private/in memory; public training summary
  is embedded unchanged and no parameter/data artifact is returned.
- Seed-0 root RNG separates environment initialization and rule-policy streams.
- Seat 0 is always the trained project policy; seats 1-3 are always the bundled
  rule policy. All 54 steps record matching policy identity.
- One environment-step JIT, one project-score JIT, one rule-policy JIT and one
  explicit 256-cap loop match approval.
- Every selected action belongs to its stored complete legal tuple.
- Exact terminal raw/cumulative rewards and authoritative global seat scores
  match the independent probe; no shaping/evaluation conversion occurs.
- Source contains no persistence, multi-game loop, RL update, league, real-data
  or strength surface.

## Validation

```text
10 focused tests OK
365 repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff --check pass
independent policy-identity/legality/outcome/determinism probe pass
```

## Direct On-Policy Update Approval

Exact files:

```text
src/mjlabai/rl/mahjax_one_round_policy_gradient_smoke.py
tests/rl/test_mahjax_one_round_policy_gradient_smoke.py
```

The reviewed private imitation-training helper and public observation encoder
may be imported read-only. No existing production file, package export or
dependency change is required. Direct governance synchronization is allowed.

Exact public API:

```text
MAHJAX_ONE_ROUND_POLICY_GRADIENT_SMOKE_VERSION
MAHJAX_ONE_ROUND_POLICY_GRADIENT_SEED
MAHJAX_ONE_ROUND_POLICY_GRADIENT_LEARNING_RATE
MahJaxOneRoundPolicyGradientSmokeError
MahJaxOneRoundPolicyGradientResult
run_mahjax_one_round_policy_gradient_smoke
```

The implementation must:

1. obtain reviewed trained parameters in memory, with no persistence/export;
2. split `PRNGKey(1)` into independent environment-init, bundled-rule-policy
   and project categorical-action RNG streams;
3. assign project policy seat 0 and bundled rule policy seats 1-3;
4. on project turns, encode only public 630 features, mask 87 logits by the
   environment legal mask, and sample on-policy with `jax.random.categorical`;
5. store only project decision features, masks and selected legal actions in
   memory, while recording complete mixed-policy legality/identity trace;
6. hard-cap at 256 and require exact seed-1 pre-update round: 37 transitions,
   8 project decisions, terminal/no truncation, project actions
   `(20,84,16,30,27,26,3,13)`, cumulative raw reward seat 0 `-39`, final raw
   `(-39,39,0,0)` and global scores `(211,289,250,250)`;
7. define return scale only as cumulative raw seat-0 reward divided by `100.0`,
   yielding `-0.39`; no reward shaping, baseline, discount or bootstrapping;
8. define one on-policy objective
   `-return_scale * mean(selected_legal_log_probability)` and use one JIT
   `value_and_grad` update at exact learning rate `0.1`;
9. require finite initial/post-update objective, exactly one update and nonzero
   parameter deltas; pin independent values initial `-0.86367577`, post
   `-0.88331068`, weight delta L2 `0.04220101`, bias delta L2 `0.01279154`;
10. rerun the same seed/RNG with updated parameters, require every action legal,
    terminal/no truncation, and report the deterministic post-update trace/raw
    outcome without claiming improvement. The reviewed probe keeps the same
    37-step action trace and raw outcome at this small update;
11. return only one frozen diagnostic summary, no arrays/data/checkpoint.

Tests must cover API/frozen result, distinct RNG streams, exact participant
identity, public features/legal masks/categorical sampling, exact pre/post
round and update values, finite objective/deltas, one update, determinism, cap,
warnings, source structure, no persistence and full regressions.

## Forbidden Scope

- no second update, epoch loop, replay, baseline/critic, discount/GAE;
- no self-play learning: opponents remain fixed bundled rule policies;
- no multiple seeds/rounds, seat rotation, evaluation, league or promotion;
- no persistence, checkpoint/model artifact, loader, path or CLI;
- no real Tenhou/haifu, external/platform data or automation;
- no hidden/private state or reward shaping;
- no policy-quality, strength, stable-dan or LuckyJ claim;
- no P9-P12.

## Evidence Grade

```text
P8 local mixed-policy implementation-review evidence and exact one-round
on-policy raw-outcome gradient-update task approval only.
```
