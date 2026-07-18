# 04AB_P8_FIXED_EVALUATION_BREADTH_IMPLEMENTATION_REVIEW

## Decision

```text
A. Review can close.

ACCEPTED as current-scope complete:
the exact `04AA` 32-seed fixed learning-rate evaluation extension.

APPROVED for next exact implementation task:
record a frozen-policy all-project outcome census on exact seeds 0..31 before
any further optimizer, estimator, critic or training-scale change.
```

Zero planning, proposal or review gates remain before the census code.

## Reviewed Commit

```text
375a193  Expand MahJax MLP fixed evaluation
```

## Conformance Review

- Only the existing `04AA` source/test plus direct governance changed.
- The seven-symbol public API, four rates, imitation initialization, exact
  training seeds, five updates, raw objectives and parameter deltas are intact.
- Fixed zero-update evaluation covers exact disjoint seeds `20..51` under
  identical environment/rule-policy RNG for initial and every branch.
- Complete transition/action/reward/score diagnostics are pinned. Initial/rate
  sums are `-501/-650/-635/-501/-501`; positive counts are `1/0/0/1/1`,
  negative counts are `16/18/17/16/16`, and changed seeds are
  `(32,39,43,44,50)/(32,39,44,50)/()/()`.
- `0.01` and `0.005` behavior identity is correctly false. `0.001/0.0001`
  change parameters but retain initial fixed greedy behavior.
- Results remain frozen and array-free. No selected-rate field, evaluation
  update, persistence, real data, production evaluation or P9-P12 path exists.

## Validation

```text
9 focused tests OK
450 explicit repository tests OK; 2 existing environment-gated skips
compileall pass
pip check: no broken requirements
git diff/check pass
independent algorithm and frozen-policy census probes pass
```

## Algorithm Probes Rejected

All probes retain five training seeds and 32 fixed zero-update evaluation
seeds. They are diagnostic failures, not implementation approvals:

```text
causal running-mean return baseline: sum -673; worse than raw -650
naive linear critic: critic loss grows about 0.18 -> 1.16e9; rejected unstable
imitation-anchor KL lambda 1: sum -650; behavior identical to raw
imitation-anchor KL lambda 100: total objective grows to about 456; rejected
standard Adam at lr 0.001: sum -653; no improvement over raw
```

No baseline, critic, KL coefficient or optimizer is selected or approved.

## Critical Seed-Selection Finding

The frozen reviewed imitation policy was independently run with all four seats
sharing the policy, categorical legal sampling and no update on exact seeds
`0..31`.

```text
nonzero seeds: (1,3,5,7,11,24,25,26,27,31)
zero seeds:    (0,2,4,6,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,28,29,30)
census nonzero rate: 10 / 32 = 0.3125
existing training seeds: (1,3,5,7,11)
existing training-seed nonzero rate: 5 / 5 = 1.0
```

The existing training tuple is outcome-selected: it contains every nonzero seed
from `0..15` and excludes all zero-outcome seeds in that interval. This was
useful for proving an update path, but it is not an unbiased training sample.
Further algorithm comparisons on only this tuple would confound update quality
with seed/outcome selection.

## Direct Census Implementation Approval

Exact files:

```text
src/mjlabai/rl/mahjax_categorical_mlp_frozen_policy_outcome_census_smoke.py
tests/rl/test_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke.py
```

Direct governance synchronization is allowed. No existing source/test logic or
public API may change.

Exact public API:

```text
MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SMOKE_VERSION
MAHJAX_CATEGORICAL_MLP_FROZEN_POLICY_OUTCOME_CENSUS_SEEDS
MAHJAX_CATEGORICAL_MLP_CENSUS_REFERENCE_TRAINING_SEEDS
MahJaxCategoricalMlpFrozenPolicyOutcomeCensusSmokeError
MahJaxCategoricalMlpFrozenPolicyOutcomeSeedResult
MahJaxCategoricalMlpFrozenPolicyOutcomeCensusResult
run_mahjax_categorical_mlp_frozen_policy_outcome_census_smoke
```

Implementation must:

1. obtain the reviewed imitation parameters once and never update them;
2. run exact seeds `tuple(range(32))` once each with all four seats sharing the
   frozen policy and the reviewed legal categorical collector;
3. record per seed the transition count, cumulative raw-return vector, final
   scores and deterministic SHA-256 action-trace digest;
4. pin all per-seed values plus exact zero/nonzero seed tuples above;
5. compare exact reference training seeds `(1,3,5,7,11)` to the census and
   expose `5/5` versus `10/32` without selecting a replacement split;
6. return frozen array-free summaries and explicit selection-bias warnings;
7. perform zero gradient updates and no persistence or I/O.

## Forbidden Scope

- no new training/evaluation split or seed selection in this task;
- no policy, value, baseline, critic, KL, optimizer or parameter update;
- no rate/estimator sweep, training scale-up or evaluation-driven selection;
- no persistence, artifact, path, CLI, external/real data or Tenhou;
- no production self-play/evaluation, league, promotion or strength claim;
- no P9-P12.

## Evidence Grade

```text
P8 exact implementation-review, failure-probe and frozen-policy seed/outcome
census task-approval evidence only; not improvement, robust evaluation or
strength evidence.
```
