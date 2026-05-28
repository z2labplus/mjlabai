# 10_NEXT

## Rule

Only do the first unchecked task. Do not execute backlog items unless they become the first unchecked task.

## Current next task

- [ ] Decide Mortal F1 continuation path: either provide a lawful, documented Mortal trained model artifact outside the repository with version/tag, usage constraints and checksum, or pause Mortal as a runnable baseline and move the next baseline F1 audit to Akochan.

Current execution charter:

```text
docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md
```

Limits:

- Do not train models.
- Do not tune hyperparameters.
- Do not connect to real Tenhou.
- Do not create platform automation, scraping, evasion or account tooling.
- Do not modify unrelated files.

## Completed

- [x] 2026-05-28 Mortal F1 initial reproducibility audit: repository metadata and selected source/docs were inspected through the GitHub connector; local clone/build/minimal run were blocked by GitHub DNS, missing Rust/Cargo, missing Docker/conda/torch and missing model artifact.
- [x] 2026-05-28 Mortal F1 blocker-resolution attempt: source tarball for commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2` was downloaded through `codeload.github.com` with explicit host resolution and checksum `6531f46ba2f2b40a69528bf5362f9c89294ad72521aec4f59e208400c379e62c`; official gist evidence says there is currently no plan to release trained model parameters, so the official mjai inference sample was not run.
- [x] 2026-05-29 Technical-plan-first execution charter added: `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` now defines Web ChatGPT Pro vs local Codex roles, Git + docs source of truth, current technical route and update rules.

## Backlog

- [ ] Apply F0-F7 stage labels to Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer inside `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md` if any evidence changes.
- [ ] If Mortal F1 passes, define Mortal F2 interface/legal-action adapter task.
- [ ] Verify Archer evidence before treating it as a strong Tenhou baseline.
- [ ] Run Akochan F1 reproducibility audit as second baseline path.
- [ ] Inspect Kanachan schema/model ideas for Tenhou transfer value.
- [ ] Decompose Suphx into reproducible experiment cards: SL policy, self-play RL, global reward prediction, oracle guiding, runtime adaptation.
- [ ] Implement Tenhou stable-dan calculator from room-specific formulas.
- [ ] Add bootstrap confidence interval for stable-dan estimate.
- [ ] Create tiny benchmark harness for legal action rate, latency and fixed-position decisions.
- [ ] Update `09_EVIDENCE_LOG.md` whenever new external evidence is added.
