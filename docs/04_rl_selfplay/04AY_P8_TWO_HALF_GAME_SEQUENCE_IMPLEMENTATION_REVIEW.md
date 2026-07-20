# 04AY P8 Two-Half-Game Sequence Implementation Review

## Decision

```text
A. Review can close.

ACCEPTED as current implementation scope:
the exact two-half-game sequential seat-0 raw-outcome training and disjoint
two-seed zero-update evaluation implementation in commit 191c243.

NO FURTHER SYNTHETIC-ONLY TRAINING TASK IS APPROVED NOW.
A human decision is required on lawful training data and compute budget before
material P7/P8 scale-up.
```

## Conformance Review

- Public results and nested records are frozen and array-free.
- Existing reviewed collector/update helpers are reused; the environment loop
  and update formula are not duplicated.
- Ordered training seeds `(0,1)` preserve direct parameter continuity and apply
  exactly two fixed `0.01` updates.
- All 427/797 training transitions and 780/820/907/1099 evaluation transitions
  are legal and carry complete global/round-local provenance.
- Evaluation seeds `(2,3)` are disjoint, use initial/final arrays with identical
  seed construction and make zero updates.
- Aggregate seat-0 raw reward is honestly retained as `-632 -> -634`; seed 2
  degrades `-344 -> -387` and seed 3 improves `-288 -> -247`.
- No selected model/seed, early stop, rollback, checkpoint, persistence, real
  data, production self-play, league or P9-P12 path exists.
- Eight focused tests passed in `267.337s`; the one-half-game regression passed
  ten tests in `135.143s`; compile, dependency and diff checks passed.

No implementation blocker remains.

## Mechanism Stop Decision

The raw-return sequence has no aggregate gain. A fixed causal prior-only
baseline probe changed the second update weight from `-2.59` to `-2.06`, but
the disjoint evaluation paths and aggregate `-632 -> -634` remained identical.
Earlier terminal-gradient averaging and round-local credit probes also retained
the same evaluated greedy behavior.

These bounded probes show that adding another synthetic half-game, another
minor return transformation or another docs/code wrapper is not justified.
They do not prove that RL cannot work. They prove only that the current tiny
synthetic/local path has reached its useful evidence limit.

## Material Prerequisites Requiring Human Approval

The repository has no training dataset, checkpoint or model weight. The local
machine is an Apple M4 Mac mini with 24 GB unified memory. It is appropriate for
development and small smoke training, but not a credible north-star-scale
training resource by itself.

Before material P7/P8 scale-up, the owner must approve:

1. **Lawful data source**: project-provided or publicly licensed riichi replay
   data with explicit provenance, rights and allowed-use record. Scraping,
   account automation and unapproved Tenhou/platform ingestion remain forbidden.
2. **Compute budget**: local-only prototype or an explicit external GPU/cloud
   budget, including provider, maximum spend/time and artifact-storage policy.
3. **Execution scope**: whether the next approved task may implement controlled
   real-data ingestion/feature generation and supervised pretraining before
   returning to RL. Synthetic-only work cannot support the north-star claim.

## Next Gate

```text
Obtain human approval for lawful training-data source and compute budget before
material P7/P8 scale-up.
```

Until that decision is recorded:

- do not add a third raw-return half-game or another reward estimator wrapper;
- do not ingest real Tenhou/haifu/external/platform data;
- do not download unknown weights or third-party artifacts;
- do not start expensive training, cloud resources, self-play or league;
- do not enter P9-P12 or make strength/stable-dan/LuckyJ claims.

## Evidence Grade

```text
P8 local two-half-game implementation-review closure and material-resource
decision-gate evidence only.
```
