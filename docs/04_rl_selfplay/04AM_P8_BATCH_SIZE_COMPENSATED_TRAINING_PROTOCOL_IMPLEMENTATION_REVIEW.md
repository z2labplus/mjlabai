# 04AM P8 Batch-Size-Compensated Training-Protocol Implementation Review

## Decision

```text
A. Review can close.
```

Commit `8df8d9d` conforms to the exact `04AL` approval. No code, test,
evidence or scope blocker was found.

## Reviewed Scope

- Commit: `8df8d9d` (`Diagnose MahJax batch-size compensated gradients`).
- Modified mean-path source:
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke.py`.
- New compensated source:
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke.py`.
- New focused test:
  `tests/rl/test_mahjax_categorical_mlp_four_pass_batch_size_compensated_training_protocol_smoke.py`.
- Direct governance synchronization.
- Approval source: `04AL`.

## Conformance Findings

1. The existing public mean-gradient run remains explicit at multiplier `1.0`
   for both reviewed protocols. Its public API and frozen behavior are not
   replaced by the compensated run.
2. The new path contains one fixed multiplier, `32.0`, at base learning rate
   `0.01`, producing the predeclared effective mean-gradient rate `0.32`.
   There is no multiplier/rate candidate list, adaptive scaling or search.
3. Both independent branches start from identical reviewed parameters and use
   only exact ordered training seeds `0..31` and `116..147`.
4. Each branch performs exactly four passes. Each pass collects all 32
   frozen-policy trajectories before one leave-one-out batch update, for 256
   trajectories and eight updates total.
5. Every trajectory/seat baseline uses the other 31 same-seat normalized
   returns. Per-seat advantage sums remain centered.
6. No evaluation occurs between passes. Final zero-update evaluation uses only
   primary `52..83` and replication `84..115`, for four calls and zero
   evaluation updates.
7. Complete trajectories, actions, baselines, advantages, objectives,
   parameter deltas and final outcomes remain frozen and array-free. Training
   actions are legal and all rounds terminate.
8. Reference primary/replication deltas are `+54/+121`, with changed seeds
   `(58,61)` and `(103,113)`. Alternate deltas are `-60/0`, with changed
   primary seed `(73,)` and no changed replication seed.
9. The implementation records both favorable and adverse outcomes. Protocol,
   model, pass and checkpoint selections all remain `None`.
10. Source/provenance checks find no open-ended loop, path/file I/O, network,
    subprocess, replay, persistence, artifact or real-data behavior.

## Validation Evidence

```text
Recorded deterministic probe: completed in 2421.62 seconds
Recorded focused: 10 tests OK in 2431.292 seconds (2440.35 seconds wall)
Recorded fast synthetic RL regression: 122 tests OK in 0.034 seconds
Recorded compile: OK
Recorded dependency check: OK
Current commit/source/provenance review: OK
Current git diff 8df8d9d^..8df8d9d --check: OK
```

The approximately 2400-second execution/focused test and the full suite are
not rerun in this review, as required by `10_NEXT`.

## Evidence Boundary

The fixed `32x` update changes policy behavior, but its sign depends on the
predeclared training protocol. The reference branch improving both windows is
not reproduced by the alternate branch, whose primary window degrades and
replication window is unchanged. This is protocol-sensitivity evidence, not a
robust improvement, useful checkpoint, model-strength result, candidate
promotion, Tenhou/stable-dan/LuckyJ evidence or P9-P12 readiness.

The favorable reference branch must not be selected. Multiplier/rate search,
another training-seed protocol, another evaluation window and another pass
would increase post-hoc selection risk without identifying why the two fixed
protocols disagree, so they are rejected.

## Direct Next Approval

Decision:

```text
Approved for next exact material P8 implementation task.
```

Task:

```text
Implement an exact first-pass two-protocol aggregate-gradient alignment
diagnostic from identical initial parameters.
```

Exact future files:

- Modify
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_leave_one_out_batch_training_protocol_smoke.py`
  only to factor the existing private leave-one-out gradient calculation into
  a reusable private helper while preserving both reviewed public runs.
- Add
  `src/mjlabai/rl/mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke.py`.
- Add
  `tests/rl/test_mahjax_categorical_mlp_first_pass_training_protocol_gradient_alignment_smoke.py`.
- Direct governance synchronization only. Do not modify existing expensive
  focused tests unless a real compatibility blocker is found.

Exact implementation contract:

1. Start both branches from the same reviewed categorical-MLP imitation
   parameters. Use exact ordered seeds `0..31` and `116..147` once each.
2. Collect exactly 32 frozen-policy trajectories per protocol. Compute the
   same reviewed other-31 per-seat baselines, actor-indexed advantages,
   trajectory objectives and aggregate mean gradients.
3. Apply no parameter update and perform no primary/replication evaluation.
   The task measures training-signal geometry only.
4. Record each protocol's per-parameter-group gradient L2 norms, global L2
   norm, global dot product and global cosine similarity. Record finite/nonzero
   checks and the complete reviewed trajectory/provenance diagnostics needed
   to verify exact inputs and legal actions.
5. Compute cosine from flattened logical parameter groups without changing
   dtype, optimizer, objective, baseline, action policy or model parameters.
6. Return a frozen, array-free result. Pin the observed values regardless of
   sign or magnitude. Select no protocol, model, multiplier, pass, checkpoint
   or gradient direction.
7. Use one deterministic probe and focused/fast checks. Do not run either
   2400-second four-pass smoke or the full suite.

Forbidden:

- any parameter update, learning-rate/multiplier/temperature/entropy/KL/
  clipping/optimizer search;
- a third protocol, seed search, extra pass or evaluation window;
- policy sampling/exploration changes, critic, GAE or replay;
- persistence, artifact, external/real data, Tenhou, league or P9-P12;
- model/protocol selection or robustness/generalization/strength claims.

This diagnostic directly tests whether the two fixed protocol batches produce
aligned or conflicting first-step learning signals. It is a causal next
question raised by the observed protocol sensitivity and is materially more
informative than another scale/seed search.

No additional proposal, boundary, review-before-code or approval document is
required. Zero mandatory gates remain before the exact code.
