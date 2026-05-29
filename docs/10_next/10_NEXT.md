# 10_NEXT

## Rule

Only do the first unchecked task. Do not execute backlog items unless they become the first unchecked task.

## Current next task

- [ ] Run the manual GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit` and review whether the wrapper succeeds against real Ubuntu-built system.exe for fixed legal_action/mjai_log samples.

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
- Do not vendor or save Akochan `system.exe`, `libai.so`, `params/` or third-party build artifacts.
- For the next step, run only the manual `Akochan F2 Wrapper Real Exe Audit` workflow and review its logs.
- Do not run self-play, match, `system.exe test`, training or real Tenhou commands.
- Do not upload or save `system.exe`, `libai.so`, `params/`, third-party source or other third-party build artifacts.
- Do not modify unrelated files.

## Completed

- [x] 2026-05-28 Mortal F1 initial reproducibility audit: repository metadata and selected source/docs were inspected through the GitHub connector; local clone/build/minimal run were blocked by GitHub DNS, missing Rust/Cargo, missing Docker/conda/torch and missing model artifact.
- [x] 2026-05-28 Mortal F1 blocker-resolution attempt: source tarball for commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2` was downloaded through `codeload.github.com` with explicit host resolution and checksum `6531f46ba2f2b40a69528bf5362f9c89294ad72521aec4f59e208400c379e62c`; official gist evidence says there is currently no plan to release trained model parameters, so the official mjai inference sample was not run.
- [x] 2026-05-29 Technical-plan-first execution charter added: `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` now defines Web ChatGPT Pro vs local Codex roles, Git + docs source of truth, current technical route and update rules.
- [x] 2026-05-29 Mortal F1 continuation decision: no lawful, verifiable and usable Mortal trained model artifact is currently available, so Mortal is paused as a runnable baseline. Mortal remains a source-code, mjai-interface, methodology and engineering reference. Unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files must not be used. The next baseline F1 path moves to Akochan.
- [x] 2026-05-29 Akochan F1 reproducibility audit: `critter-mj/akochan` at commit `53188a0b926fbab38177f88c3cd87d554cf412af` is public and inspectable; custom license permits private research but restricts redistribution/modification/commercial use; no external neural-network weights are required; JSON/mjai/log/legal-action entry points look promising; local build failed on macOS ARM due missing/incompatible LLVM/OpenMP/Boost toolchain, so minimal run was not executed and F1 is Blocked.
- [x] 2026-05-29 Akochan F1 blocker-resolution attempt: Docker was unavailable, native Linux was unavailable, and the macOS Homebrew build path lacked usable LLVM/Boost/OpenMP files. Official MacOS and Linux Makefile attempts in `/tmp/mjlabai_akochan_build_audit` failed before producing `libai.so` or `system.exe`, so no minimal `legal_action`, `legal_action_log_all`, `mjai_log` or `stats_mjai` sample was run. Akochan remains F1 Blocked.
- [x] 2026-05-29 Added manual GitHub Actions workflow `Akochan F1 Build Audit`: `.github/workflows/akochan-f1-build-audit.yml` provides an Ubuntu Linux runner path for the fixed Akochan commit, installs build dependencies inside the runner, clones Akochan in the runner temp directory, attempts `Makefile_Linux` builds, and only if `system.exe` exists attempts minimal non-training `legal_action` and `mjai_log` samples. This does not by itself pass F1; Akochan remains F1 Blocked until a workflow run succeeds and evidence is reviewed.
- [x] 2026-05-29 Reviewed first GitHub Actions workflow run: run `26615920289` failed during workflow validation before any Ubuntu build because `runner.temp` was used in job-level `env`. The workflow was corrected to configure `AKOCHAN_DIR` and `SUMMARY_FILE` through `$GITHUB_ENV`; no Akochan build or minimal sample evidence was produced by the failed run.
- [x] 2026-05-29 Ran corrected GitHub Actions workflow `Akochan F1 Build Audit`: run `26617347785` at commit `b6b69e08fd009052cb3bbd16c779ac6e2139591b` succeeded on `ubuntu-latest`; `ai_src/libai.so`, root `libai.so` and `system.exe` were generated; both minimal non-training samples succeeded: `legal_action` and `mjai_log haifu_log_sample.json 0 2`. Akochan F1 is upgraded to Conditional Pass because reproducibility is proven on Ubuntu, while custom license and local macOS build limits remain.
- [x] 2026-05-29 Defined Akochan F2 interface/legal-action adapter task in `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`: documented wrapper-only boundary, state/action mapping draft, audit log schema, license guardrails, F2 acceptance criteria and failure conditions. No adapter code was written.
- [x] 2026-05-29 Implemented minimal Akochan F2 wrapper skeleton for fixed `legal_action` / `mjai_log` samples: added a small Python package, wrapper class, audit-log dataclasses, synthetic fixtures, fake executable smoke tests and normalized `dahai` action schema. Local test command `python3 -m unittest tests/adapters/test_akochan_wrapper.py` passed 4 tests. The fake executable is only a test substitute, not real Akochan evidence, and no third-party source, binary or artifact was stored.
- [x] 2026-05-29 Added Akochan F2 real executable wrapper validation path: `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml` manually builds Akochan in a temporary Ubuntu runner, points `AKOCHAN_SYSTEM_EXE` at the runner-temp `system.exe`, and runs wrapper tests against fixed `legal_action` / `mjai_log` samples. Added `tests/adapters/test_akochan_wrapper_real_exe.py`, which skips locally unless `AKOCHAN_SYSTEM_EXE` is provided. Local fake tests passed and local real-exe tests skipped as expected. No third-party source, binary or build artifact was stored or uploaded.

## Backlog

- [ ] Apply F0-F7 stage labels to Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer inside `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md` if any evidence changes.
- [ ] If a lawful, verifiable and usable Mortal trained model artifact is provided later, re-open Mortal F1 artifact verification before any F2 adapter task.
- [x] Define Akochan F2 interface/legal-action adapter task: specify state/action mapping, legal-action checker boundary, log schema, wrapper-only integration constraints and license guardrails before writing adapter code.
- [x] Implement minimal Akochan F2 wrapper skeleton for fixed legal_action/mjai_log samples under the documented no-vendor, no-training, no-Tenhou constraints.
- [x] Add Akochan F2 real executable wrapper validation path without uploading or saving third-party binaries or artifacts.
- [ ] Run the manual GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit` and review whether the wrapper succeeds against real Ubuntu-built system.exe for fixed legal_action/mjai_log samples.
- [ ] Verify Archer evidence before treating it as a strong Tenhou baseline.
- [ ] Inspect Kanachan schema/model ideas for Tenhou transfer value.
- [ ] Decompose Suphx into reproducible experiment cards: SL policy, self-play RL, global reward prediction, oracle guiding, runtime adaptation.
- [ ] Implement Tenhou stable-dan calculator from room-specific formulas.
- [ ] Add bootstrap confidence interval for stable-dan estimate.
- [ ] Create tiny benchmark harness for legal action rate, latency and fixed-position decisions.
- [ ] Update `09_EVIDENCE_LOG.md` whenever new external evidence is added.
