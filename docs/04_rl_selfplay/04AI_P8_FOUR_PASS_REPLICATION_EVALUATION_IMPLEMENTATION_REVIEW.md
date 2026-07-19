# 04AI P8 Four-Pass Replication Evaluation Implementation Review

## Decision

```text
A. Review can close.
```

Commit `17a3722` conforms to the exact `04AH` approval. No code, test,
evidence or scope blocker was found.

## Reviewed Scope

- Commit: `17a3722` (`Evaluate MahJax four-pass policy on replication seeds`).
- Production file:
  `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke.py`.
- Test file:
  `tests/rl/test_mahjax_categorical_mlp_four_pass_causal_baseline_training_evaluation_smoke.py`.
- Ten direct governance documents.
- Approval source: `04AH`.

## Conformance Findings

1. Training remains exactly four ordered passes over seeds `0..31`, for 128
   attempts, learning rate `0.01`, continuous policy parameters and a causal
   prior-record per-seat baseline.
2. No evaluation occurs between passes. The four zero-update calls are only
   initial primary, initial replication, final primary and final replication.
3. Primary evaluation seeds `52..83` remain unchanged and reproduce
   `-312 -> -297`, positives `2 -> 2`, negatives `20 -> 19` and changed seeds
   `(52,58,65,70,72)`.
4. The predeclared replication seeds are exactly `84..115`, pairwise disjoint
   from training and primary evaluation.
5. Replication records `-1056 -> -935`, positives `0 -> 0`, negatives
   `19 -> 18` and changed seeds
   `(84,89,92,94,102,103,104,106,110,113,114)`.
6. Complete initial/final replication transition counts, project action
   traces, raw rewards and four-seat final scores remain in the frozen,
   array-free result.
7. The public six-symbol API remains unchanged. The result schema version is
   explicitly advanced to `v0.2`.
8. `evaluation_update_count` is zero; `selected_pass_index` and
   `selected_checkpoint_id` remain `None`.
9. Source/AST probes find one exact four-pass loop, four `_evaluate` call
   sites, no `while` loop and no path, serialization, subprocess, network or
   external-data import.

## Validation Evidence

```text
Focused: 11 tests OK in 1382.737 seconds
Full explicit suite: 499 tests OK in 5622.879 seconds; 2 existing skips
Compile: OK
Dependency check: OK
git diff --check: OK
AST/source/provenance review: OK
```

The first focused run found one test-only semantic error: project-seat action
trace length had been equated with all-seat transition count. The assertion
was corrected to require a non-empty project trace bounded by total
transitions. The unchanged implementation then passed the complete focused
and full suites.

## Evidence Boundary

The two fixed windows both show bounded aggregate improvement, but this is
still only P8 local deterministic diagnostic evidence. It does not establish:

- robustness across training seed protocols or model initializations;
- generalization or policy quality;
- a selected checkpoint or production trainer;
- model strength, candidate promotion or league superiority;
- Tenhou, stable-dan or LuckyJ 10.68 performance;
- P9-P12 readiness.

Another adjacent fixed evaluation window or fifth training pass is rejected
as the next action because it adds high runtime cost without addressing the
single training-seed-protocol dependency.

## Direct Next Approval

Decision:

```text
Approved for next exact material P8 implementation task.
```

Task:

```text
Implement a predeclared alternate-training-seed sensitivity diagnostic for
the exact four-pass causal-baseline policy.
```

Exact future files:

- `src/mjlabai/rl/mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke.py`
- `tests/rl/test_mahjax_categorical_mlp_four_pass_training_seed_sensitivity_smoke.py`
- direct governance synchronization only.

Exact implementation contract:

1. Reuse the reviewed categorical-MLP initialization, MahJax runtime, causal
   prior-record baseline update and mixed-policy evaluation helpers.
2. Use alternate training seeds exactly `116..147`, in ascending order, for
   exactly four passes / 128 attempts at learning rate `0.01`.
3. Start from the same reviewed initialization and a zero per-seat baseline.
4. Perform no evaluation between passes and no early stopping or selection.
5. Evaluate the alternate final policy with zero updates on the already fixed
   primary `52..83` and replication `84..115` windows only.
6. Compare the alternate final diagnostics with the pinned initial and
   reviewed reference-four-pass summaries by immutable values; do not rerun a
   second reference training branch inside the new smoke.
7. Retain all alternate training/update and final evaluation diagnostics,
   including legal actions, pass summaries, parameter deltas, reward vectors,
   counts and changed seeds.
8. Accept and pin the alternate result regardless of sign. Return no selected
   training protocol, model, pass or checkpoint.
9. The result is training-seed sensitivity evidence only. Two training
   protocols still do not establish robustness or strength.

Forbidden:

- another evaluation window, fifth pass, alternate pass count or seed search;
- tuning, adaptive rates, critic/GAE/entropy/KL/clipping/optimizer changes;
- replay, persistence, checkpoint/model artifact or broad trainer;
- real data, external logs, Tenhou, league or model promotion;
- robust/generalization/strength claims or P9-P12.

No additional proposal, boundary or approval document is required before this
exact code. Zero mandatory gates remain.
