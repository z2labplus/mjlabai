# 05F_ALGORITHM_RANKING_PROTOCOL

Goal: determine which algorithm route is best for the project target, not which one is most famous.

## Final answer criterion

The best algorithm is the one that produces the highest statistically reliable Tenhou-target score under the same evaluation harness.

Minimum target:

```text
Tenhou stable dan estimate > 10.68
with enough sample size and confidence interval to rule out luck.
```

## Evaluation ladder

### Level 0 — Evidence review

Collect public evidence:

- Tenhou dan or stable dan.
- Room type: expert room, phoenix room, private lobby, other.
- Game count and time period.
- Rank distribution: 1st/2nd/3rd/4th.
- Win rate and deal-in rate.
- Whether code/weights/logs are available.

This level can rank research value, but it cannot prove what is best for our implementation.

### Level 1 — Local build and replay compatibility

A candidate must pass:

- Builds on local machine or documented container.
- Can read/write a known replay format or be adapted to one.
- Produces legal actions only.
- Logs every decision with state, candidate actions, selected action, value estimate if available.

### Level 2 — Offline decision evaluation

Evaluate on fixed high-value positions:

- Discard decision.
- Riichi decision.
- Chi/Pon/Kan decision.
- Push/fold decision.
- Dangerous tile defense.
- South-round rank-awareness.
- Oorasu fourth-place avoidance.

Primary score is not imitation accuracy alone. Record expected value, rank impact, risk, and disagreement with strong baselines.

### Level 3 — Controlled self-play / tournament

Use a fixed league:

- Baseline A: current main model.
- Baseline B: Mortal or other first reproducible open-source baseline.
- Baseline C: rule-based sanity bot.
- Candidate: new route/checkpoint.

Run enough games with seat rotation and seed control. Report:

- Average placement.
- 1st/2nd/3rd/4th rates.
- Tenhou pt EV.
- Stable dan estimate.
- Deal-in rate.
- Win rate.
- Riichi EV.
- Open-hand EV.
- Fourth-place rescue rate in South/Oorasu.

### Level 4 — Stable-dan estimate with uncertainty

Use the Tenhou formula for the target room.

For four-player ippan/general-style stable dan:

```text
stable_dan = ((first_count * 20 + second_count * 10) / fourth_count - 20) / 10
```

For four-player joukyu/upper-style stable dan:

```text
stable_dan = ((first_count * 40 + second_count * 10) / fourth_count - 20) / 10
```

For four-player phoenix-style stable dan:

```text
stable_dan = ((first_count * 60 + second_count * 30) / fourth_count - 20) / 10
```

For four-player tokujou/expert-style stable dan:

```text
stable_dan = ((first_count * 50 + second_count * 20) / fourth_count - 20) / 10
```

Always report bootstrap confidence intervals. A model does not beat LuckyJ unless the lower confidence bound is above the required threshold or the project explicitly marks the result as provisional.

Stable-dan CI reporting must include:

- point estimate.
- lower bound.
- upper bound.
- confidence level.
- number of bootstrap resamples.
- successful resamples.
- undefined resamples.
- undefined rate.

Undefined bootstrap resamples occur when the resampled fourth-place count is zero. They must be skipped and reported, not converted into infinite stable dan. If undefined rate is high, treat the interval as unreliable until more games are available.

Stable-dan threshold comparison against LuckyJ 10.68 must use the bootstrap lower bound:

- `clear_pass` only when lower bound is greater than `10.68` and undefined rate is acceptable.
- `point_estimate_only` when point estimate is greater than `10.68` but lower bound is not; do not claim a clear pass.
- `clear_fail` when even upper bound does not exceed `10.68`.
- `unreliable` when undefined resample rate is too high.
- `inconclusive` when confidence interval overlaps the threshold.

Stable-dan reports must also pass sample-size reporting guardrails before project-level threshold review:

- report minimum: `total_games >= 100`.
- report minimum: `fourth_count >= 10`.
- threshold-review minimum: `total_games >= 1000`.
- threshold-review minimum: `fourth_count >= 50`.
- maximum undefined bootstrap resample rate: `0.05`.

These defaults are project-internal governance guardrails, not Tenhou official standards or proof of strength. Low-sample reports may be useful diagnostics, but they cannot support a LuckyJ 10.68 project-level claim.

Current implementation status:

- `src/mjlabai/eval/stable_dan.py` implements deterministic point estimates for general/ippan, upper/joukyu, expert/tokujou and phoenix/houou.
- `bootstrap_stable_dan_ci(...)` implements percentile empirical multinomial bootstrap confidence intervals using Python standard library only.
- `compare_stable_dan_to_threshold(...)` compares bootstrap CI results against LuckyJ stable dan `10.68` using lower-bound logic.
- `build_stable_dan_evaluation_report(...)` produces an offline report schema with point estimate, CI, threshold outcome and sample-size assessment.
- `fourth_count == 0` is undefined and raises `StableDanUndefinedError`; do not report infinite stable dan.
- Bootstrap resamples with `fourth_count == 0` are recorded as undefined; if all resamples are undefined, `StableDanBootstrapUndefinedError` is raised.
- The next required evaluation-foundation task is placement-count aggregation for stable-dan evaluation inputs.

### Level 5 — Promotion gate

A candidate can enter the mainline only if:

- It improves the primary metric over current main model.
- It does not hide a fourth-place-rate regression.
- It passes legality and reproducibility checks.
- It has a rollback path.
- It is recorded in experiment log, evidence log, risk register, and changelog.

## Best-algorithm decision template

```text
Candidate:
Version / commit / checkpoint:
Evaluation date:
Evaluation environment:
Rules:
Game count:
Seat rotation:
Baselines:

Results:
- Average placement:
- 1st / 2nd / 3rd / 4th:
- Tenhou pt EV:
- Stable dan estimate:
- Bootstrap CI:
- Win rate:
- Deal-in rate:
- Latency:

Decision:
- Promote / Continue / Pivot / Stop
Why:
Next task:
Docs updated:
```

## Current answer to “which is best?”

We do not decide from names. Current working assumption:

- LuckyJ is the performance target.
- Suphx is the strongest public methodology blueprint.
- Mortal is the likely first reproducible baseline.
- Archer may be strong but needs verification.
- Akochan and Kanachan are useful comparative references.

The best route becomes the one that wins our same-harness evaluation and pushes stable-dan estimate toward `> 10.68`.
