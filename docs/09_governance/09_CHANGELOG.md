# 09_CHANGELOG

## 2026-05-29 — v1.6

- Implemented the minimal Akochan F2 wrapper skeleton for fixed `legal_action` / `mjai_log` samples.
- Added minimal Python package structure under `src/mjlabai` and project metadata in `pyproject.toml`.
- Added `AkochanWrapper.run_legal_action(input_json)` and `AkochanWrapper.run_mjai_log(log_path, actor=0, mode=2)`.
- Added audit-log dataclasses that record external repo/commit, build environment, command, input/output hashes, exit code, stdout/stderr summaries, elapsed time and explicit no-training/no-self-play/no-Tenhou flags.
- Added synthetic test fixtures and `tests/fixtures/akochan/fake_system_exe.py` as a test substitute only; it is not Akochan and is not strength evidence.
- Added unit/smoke tests for JSON parsing, `dahai` normalization, audit logs, environment-variable executable path support and non-JSON stdout failure handling.
- Verified `python3 -m unittest tests/adapters/test_akochan_wrapper.py` passed 4 tests.
- Confirmed no Akochan source, `system.exe`, `libai.so`, `params/`, third-party binary, unknown model artifact or build artifact was stored in this repository.
- Set the next task to run the wrapper against a real GitHub Actions Ubuntu-built external `system.exe` for fixed samples without uploading third-party binaries or artifacts.

## 2026-05-29 — v1.5

- Added `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`.
- Defined the Akochan F2 interface/legal-action adapter task without writing adapter code.
- Documented Akochan's F2 roles: legal-action checker, mjai/log reviewer and baseline/reviewer candidate.
- Defined wrapper-only boundaries: no Akochan source, `system.exe`, `libai.so`, `params/`, third-party binaries or build artifacts may enter this repository.
- Added draft mjai event mapping, normalized action schema, audit-log schema, F2 acceptance criteria and F2 failure conditions.
- Reaffirmed custom-license guardrails: private/internal audit only until license review or permission clears broader use.
- Set the next task to implement a minimal Akochan F2 wrapper skeleton for fixed `legal_action` / `mjai_log` samples under no-vendor, no-training and no-Tenhou constraints.
- Updated next, handoff, docs index, evidence, risk, candidate-table, backlog, stage-contract, technical-plan and decision docs.

## 2026-05-29 — v1.4

- Triggered the corrected manual GitHub Actions workflow `Akochan F1 Build Audit`.
- Run `26617347785` succeeded at commit `b6b69e08fd009052cb3bbd16c779ac6e2139591b`.
- Confirmed Ubuntu build generated `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Confirmed both minimal non-training samples succeeded: `legal_action` and `mjai_log haifu_log_sample.json 0 2`.
- Upgraded Akochan F1 from Blocked to Conditional Pass, limited to Ubuntu GitHub Actions evidence and subject to custom-license restrictions.
- Set the next task to define the Akochan F2 interface/legal-action adapter task; no adapter code was written.
- Recorded the GitHub Actions Node.js 20 deprecation warning for `actions/checkout@v4` as workflow maintenance risk.
- Updated next, handoff, evidence, risk, candidate-table, audit, backlog, stage-contract, technical-plan and decision docs.

## 2026-05-29 — v1.3

- Reviewed the first `Akochan F1 Build Audit` GitHub Actions run.
- Confirmed run `26615920289` failed during GitHub workflow validation before any Ubuntu build/minimal sample started.
- Fixed `.github/workflows/akochan-f1-build-audit.yml` by moving `AKOCHAN_DIR` and `SUMMARY_FILE` path setup out of job-level `env` and into a shell step that writes to `$GITHUB_ENV`.
- Added a fallback in the final summary step so validation/setup failures still produce a clear GitHub step summary when possible.
- Akochan remains F1 Blocked because the failed run produced no `system.exe`, `legal_action` or `mjai_log` evidence.
- Updated next, handoff, evidence, risk, audit and backlog docs.

## 2026-05-29 — v1.2

- Added manual GitHub Actions workflow `.github/workflows/akochan-f1-build-audit.yml`.
- The workflow provides an Ubuntu `workflow_dispatch` build-audit path for Akochan F1 without changing local machine dependencies.
- The workflow clones `critter-mj/akochan` at commit `53188a0b926fbab38177f88c3cd87d554cf412af` into the runner temp directory, installs build dependencies inside the temporary Ubuntu runner, attempts the Linux Makefile builds and runs only minimal non-training samples if `system.exe` is produced.
- The workflow does not train, tune, self-play, connect to Tenhou, write an adapter, enter F2, upload third-party source, upload binaries or publish artifacts.
- Akochan remains F1 Blocked until a manual workflow run succeeds and its build/minimal-run evidence is reviewed.
- Updated next, handoff, evidence, risk, audit and backlog docs.

## 2026-05-29 — v1.1

- Attempted to resolve the Akochan F1 build/toolchain blocker without training, tuning, self-play, Tenhou access, adapter work or third-party vendoring.
- Confirmed Docker is unavailable on the local machine.
- Re-cloned `critter-mj/akochan` outside the repository at fixed commit `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Confirmed local macOS ARM has Apple clang and make, but no usable Homebrew LLVM/Boost/OpenMP files.
- Retried official `ai_src` and root MacOS/Linux Makefile paths; all failed before producing `libai.so` or `system.exe`.
- No minimal `legal_action`, `legal_action_log_all`, `mjai_log` or `stats_mjai` sample was run because `system.exe` was not generated.
- Kept Akochan at F1 Blocked and narrowed the next task to providing a supported Docker Linux or verified local LLVM/Boost/OpenMP build environment.

## 2026-05-29 — v1.0

- Completed the Akochan F1 reproducibility audit as the next baseline path.
- Added `docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md`.
- Recorded `critter-mj/akochan` repository metadata, audited commit, custom license terms, dependency/build path, artifact needs, minimal-run entry points and I/O/logging fit.
- Confirmed Akochan does not appear to need external neural-network weights, but relies on repository-included text parameters under `params/`.
- Attempted local build in the external temporary clone only; macOS ARM build is blocked by missing/incompatible LLVM/OpenMP/Boost toolchain and Linux Makefile incompatibility.
- Set Akochan F1 conclusion to Blocked and kept Akochan out of F2.
- Updated next-task, handoff, evidence, risk, candidate-table, development-backlog, stage-contract, technical-plan and decision docs.

## 2026-05-29 — v0.9

- Completed the Mortal F1 continuation decision.
- Paused Mortal as a runnable baseline because no lawful, verifiable and usable trained model artifact is currently available.
- Recorded that unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files must not be used.
- Kept Mortal as a source-code, mjai-interface, methodology and engineering reference.
- Moved the next baseline F1 path to Akochan reproducibility audit without starting the Akochan audit in this task.
- Updated next-task, handoff, decision, risk, stage-contract, technical-plan, candidate-table, development-backlog and candidate-role docs.

## 2026-05-29 — v0.8

- Added `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` as the current technical execution charter.
- Shifted the project framing from internal-paper-first to technical-plan-first; papers are future outcome summaries.
- Clarified Web ChatGPT Pro vs local Codex App responsibilities.
- Reaffirmed Git + docs as the only source of truth.
- Recorded the current main route: Suphx-style SL+RL, Tenhou stable dan / pt EV reward, ACH-inspired policy improvement, risk model/search and baseline racing funnel.
- Clarified that LuckyJ is the target benchmark, not a direct full-reproduction object.
- Added `docs/09_governance/09_DECISION_RECORD.md` and recorded DR-0001.
- Updated docs index, handoff, next, evidence and risk notes.

## 2026-05-28 — v0.7

- Attempted to resolve Mortal F1 local reproducibility blockers without training, tuning, self-play or Tenhou integration.
- Retrieved and checksummed Mortal source tarball for commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2` through explicit host resolution.
- Confirmed normal system DNS and normal `git clone` are still unreliable.
- Confirmed Python 3.12 is available, but PyTorch is missing; Rust/Cargo and Docker remain unavailable.
- Recorded that Homebrew Rust metadata lookup is blocked by `formulae.brew.sh` DNS failure.
- Retrieved and checksummed the README-linked model-release gist metadata; recorded that official trained model parameters are not currently planned for public release.
- Left Mortal at F1 Reproduce blocked and updated `10_NEXT.md` to require a lawful trained model artifact decision before further Mortal runnable-baseline work.
- Updated development backlog so the blocker-resolution task is blocked on model artifact availability and the continuation decision is the planned next task.

## 2026-05-28 — v0.6

- Completed Mortal F1 initial reproducibility audit without training, tuning, self-play or Tenhou integration.
- Recorded that Mortal source/docs are inspectable through the GitHub connector at commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
- Recorded Mortal code license, dependency/build path, Docker/mjai inference path, input/output notes and logging metadata.
- Recorded local blockers: GitHub DNS failure, missing Rust/Cargo, missing Docker/conda/torch and missing model artifact.
- Kept Mortal at F1 Reproduce blocked and updated `10_NEXT.md` to resolve blockers before any F2 adapter work.
- Updated development backlog statuses and added the Mortal F1 blocker-resolution task.
- Updated the stage task contract from rule-load verification to P3 baseline reproducibility audit.

## 2026-05-28 — v0.5

- Added the P0-P12 project roadmap to `07A_MILESTONES.md`.
- Clarified that P0/P1/P2 are basically established and the project is preparing to enter P3 baseline reproducibility audit.
- Updated handoff and next task so Mortal F1 reproducibility audit is the current execution step.
- Replaced the stale `templates/prompts/09_ALGORITHM_RACING_FUNNEL.md` reference with `docs/07_development_execution/07G_RACING_FUNNEL_EXECUTION_TASK.md`.
- Recorded the stale template-path issue as a mitigated documentation risk.

## 2026-05-28 — v0.4

- Added racing-funnel mechanism for algorithm selection.
- Clarified that the project will not fully train every candidate algorithm before comparison.
- Added staged funnel: F0 registration, F1 reproducibility, F2 adapter/legal-action, F3 offline scenarios, F4 small league, F5 medium league, F6 mainline candidate, F7 LuckyJ validation.
- Clarified roles of LuckyJ, Suphx, Mortal, Archer, Akochan and Kanachan.
- Added racing-funnel evaluation metrics and promotion gates.
- Added local Codex prompt for applying the racing funnel.
- Added racing-funnel gate checklist.
- Updated docs index, handoff, risk register and next task.

## 2026-05-28 — v0.3

- Added concrete algorithm candidate table for Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer.
- Added scoring rubric for candidate selection.
- Added algorithm ranking protocol with evaluation ladder and stable-dan uncertainty requirement.
- Added local Codex prompt for building the candidate table.
- Added algorithm ranking gate checklist.
- Updated handoff, docs index and next task.

## 2026-05-28 — v0.2

- Added algorithm selection principles.
- Added algorithm candidate routes: Suphx-style, LuckyJ-inspired, open-source baseline, evaluation-first, search+risk.
- Added imperfect-information search document.
- Added algorithm discovery workflow for local Codex execution.
- Added algorithm candidate card template.
- Added algorithm discovery prompts and algorithm gate checklist.
- Updated `10_NEXT.md` to make algorithm candidate table the next post-rule-load task.
- Updated evidence log with initial sources for LuckyJ, Suphx, ACH, Mortal, Akochan, Kanachan and Archer.

## 2026-05-28 — v0.1

- Initial documentation package created.
