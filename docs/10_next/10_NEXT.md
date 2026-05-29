# 10_NEXT

## Rule

Only do the first unchecked task. Do not execute backlog items unless they become the first unchecked task.

## Current next task

- [ ] Resolve Akochan F1 blocker: establish a supported build environment, preferably Linux with `g++`/Boost/OpenMP or a corrected macOS Homebrew LLVM/OpenMP/Boost toolchain, then rerun Akochan build plus minimal `legal_action` and/or `mjai_log` sample.

Current execution charter:

```text
docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md
```

Limits:

- Do not train models.
- Do not tune hyperparameters.
- Do not start self-play.
- Do not connect to real Tenhou.
- Do not create platform automation, scraping, evasion or account tooling.
- Do not download or use unknown model weights, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.
- Do not vendor or copy third-party source into this repository.
- Do not write an adapter or enter F2 before F1 minimal build/run evidence exists.
- Do not modify unrelated files.

## Completed

- [x] 2026-05-28 Mortal F1 initial reproducibility audit: repository metadata and selected source/docs were inspected through the GitHub connector; local clone/build/minimal run were blocked by GitHub DNS, missing Rust/Cargo, missing Docker/conda/torch and missing model artifact.
- [x] 2026-05-28 Mortal F1 blocker-resolution attempt: source tarball for commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2` was downloaded through `codeload.github.com` with explicit host resolution and checksum `6531f46ba2f2b40a69528bf5362f9c89294ad72521aec4f59e208400c379e62c`; official gist evidence says there is currently no plan to release trained model parameters, so the official mjai inference sample was not run.
- [x] 2026-05-29 Technical-plan-first execution charter added: `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` now defines Web ChatGPT Pro vs local Codex roles, Git + docs source of truth, current technical route and update rules.
- [x] 2026-05-29 Mortal F1 continuation decision: no lawful, verifiable and usable Mortal trained model artifact is currently available, so Mortal is paused as a runnable baseline. Mortal remains a source-code, mjai-interface, methodology and engineering reference. Unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files must not be used. The next baseline F1 path moves to Akochan.
- [x] 2026-05-29 Akochan F1 reproducibility audit: `critter-mj/akochan` at commit `53188a0b926fbab38177f88c3cd87d554cf412af` is public and inspectable; custom license permits private research but restricts redistribution/modification/commercial use; no external neural-network weights are required; JSON/mjai/log/legal-action entry points look promising; local build failed on macOS ARM due missing/incompatible LLVM/OpenMP/Boost toolchain, so minimal run was not executed and F1 is Blocked.

## Backlog

- [ ] Apply F0-F7 stage labels to Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer inside `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md` if any evidence changes.
- [ ] If a lawful, verifiable and usable Mortal trained model artifact is provided later, re-open Mortal F1 artifact verification before any F2 adapter task.
- [ ] If Akochan F1 passes after build/minimal-run blocker resolution, define Akochan F2 interface/legal-action adapter task.
- [ ] Verify Archer evidence before treating it as a strong Tenhou baseline.
- [ ] Inspect Kanachan schema/model ideas for Tenhou transfer value.
- [ ] Decompose Suphx into reproducible experiment cards: SL policy, self-play RL, global reward prediction, oracle guiding, runtime adaptation.
- [ ] Implement Tenhou stable-dan calculator from room-specific formulas.
- [ ] Add bootstrap confidence interval for stable-dan estimate.
- [ ] Create tiny benchmark harness for legal action rate, latency and fixed-position decisions.
- [ ] Update `09_EVIDENCE_LOG.md` whenever new external evidence is added.
