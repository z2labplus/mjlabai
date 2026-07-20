# 04AN P8 First-Pass Gradient-Alignment Implementation Review

## Decision

```text
A. Review can close.
```

Commit `e94e4fe` conforms to the exact `04AM` approval. No code, test,
evidence or scope blocker was found.

## Reviewed Scope

- Commit: `e94e4fe` (`Diagnose MahJax first-pass gradient conflict`).
- Private helper refactor in the reviewed leave-one-out batch source.
- New first-pass gradient-alignment source and focused test.
- Direct governance synchronization.
- Approval source: `04AM`.

## Conformance Findings

1. The private refactor extracts the existing baseline/advantage/objective/
   gradient-sum calculation. The reviewed update helper still performs exact
   `gradient_multiplier * gradient / 32` arithmetic; both public mean branches
   still pass explicit `1.0`.
2. The new diagnostic starts both protocols from identical reviewed imitation
   parameters and uses only exact ordered seeds `0..31` and `116..147` once.
3. Each protocol collects exactly 32 frozen-policy trajectories and computes
   the reviewed other-31 same-seat baselines and aggregate mean gradients.
4. The new path imports/calls neither the update helper nor evaluation helper.
   It applies zero training updates and makes zero evaluation calls.
5. Complete transition, actor, action, legal-action, reward, score, digest,
   baseline, advantage, objective and parameter-shape provenance is retained.
   All actions are legal, all rounds terminate and per-seat advantages center.
6. Reference/alternate per-group gradient norms are finite and nonzero. Global
   norms are `0.0284640377` and `0.0268703934`.
7. Global dot product is `-0.0001429308562`; cosine is `-0.1868768328`. The
   exact first-step aggregate signals conflict rather than align.
8. The result is frozen and array-free. Protocol, model, multiplier, pass,
   checkpoint and gradient-direction selections all remain `None`.
9. Source/static checks find no open-ended loop, update/evaluation call, path/
   file I/O, serialization, network, subprocess, replay or artifact behavior.

## Validation Evidence

```text
Deterministic probe: completed in 596.96 seconds
Focused: 9 tests OK in 598.815 seconds (603.98 seconds wall)
Fast synthetic RL regression: 122 tests OK in 0.033 seconds
Claim-control regression: 7 tests OK in 0.001 seconds
Compile: OK
Dependency check: OK
Static compatibility/scope checks: OK
git diff --check: OK
Commit/source/provenance review: OK
```

The 599-second diagnostic, either 2400-second four-pass diagnostic and the full
suite are not rerun in this review.

## Evidence Boundary

Negative first-step cosine provides a mechanism-level explanation for the
fixed `32x` protocol sensitivity: the two predeclared batches push the same
initial policy in conflicting aggregate directions. It does not prove that a
projection method improves the policy, that either protocol is representative,
or that any model is strong. No protocol, direction or checkpoint is selected.

Scale/rate/seed/optimizer search would exploit the observed branches without
resolving the conflict and remains rejected. A fixed conflict-aware aggregate
update is the next material falsifiable question.

## Direct Next Approval

Decision:

```text
Approved for next exact material P8 implementation task.
```

Task:

```text
Implement one exact symmetric conflict-projected aggregate-gradient update and
fixed-window diagnostic from the reviewed two first-pass protocol batches.
```

Exact future files:

- Add
  `src/mjlabai/rl/mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke.py`.
- Add
  `tests/rl/test_mahjax_categorical_mlp_first_pass_symmetric_conflict_projected_update_smoke.py`.
- Direct governance synchronization only. Do not modify existing source/test
  files unless a real compatibility blocker is found.

Exact implementation contract:

1. Reuse the exact `04AM`/`e94e4fe` identical initialization, ordered `0..31`
   and `116..147` first batches, trajectory collector, other-31 baselines,
   objectives and aggregate mean gradients.
2. Compute original global dot product once. Because the reviewed value is
   negative, apply exactly this symmetric projection from the original pair:

   ```text
   reference_projected = reference - dot(reference, alternate)
                         / squared_norm(alternate) * alternate
   alternate_projected = alternate - dot(reference, alternate)
                         / squared_norm(reference) * reference
   combined = (reference_projected + alternate_projected) / 2
   ```

   Use no sequential projection, random order, clipping, epsilon, candidate
   formula or projection search.
3. Apply exactly one update from the shared initial parameters:

   ```text
   updated = initial - 0.32 * combined
   ```

   `0.32` is the already reviewed fixed `32x` effective mean-gradient rate;
   this is not a rate search.
4. Record original/projected per-group/global norms, original and projected
   dot/cosine, combined norms and parameter deltas. Keep all finite/nonzero/
   formula-conformance diagnostics frozen and array-free.
5. Evaluate the one updated policy exactly once on final zero-update primary
   `52..83` and replication `84..115`. Compare to reviewed initial vectors/
   sums only. Accept and pin outcomes regardless of sign.
6. Retain complete training and evaluation transition/action/reward/score
   provenance needed to verify legal execution and exact windows.
7. Return no selected protocol, model, multiplier, projection, pass or
   checkpoint. Do not call the existing four-pass/mean/32x public runs.
8. Run one deterministic probe, focused tests and fast checks only. Do not run
   any existing expensive focused test or the full suite.

Forbidden:

- alternative projection formula/order, coefficient, epsilon or threshold;
- multiplier/rate/optimizer/entropy/temperature/exploration search;
- third protocol, seed search, second update/pass or third evaluation window;
- critic, GAE, clipping, replay, persistence or artifact;
- external/real data, Tenhou, league, model selection or P9-P12;
- robustness/generalization/policy-quality/model-strength claims.

No additional proposal, boundary, review-before-code or approval document is
required. Zero mandatory gates remain before the exact code.
