# 09_DECISION_RECORD

## Purpose

This file records project-level technical and governance decisions.

Each decision should include:

- Date.
- Decision.
- Context.
- Rationale.
- Consequences.
- Linked docs.
- Status.

## 2026-05-29 — DR-0007 — Implement Akochan F2 Skeleton as Fixed-Command Python Wrapper

Decision:

```text
Implement the first Akochan F2 skeleton as a minimal Python wrapper with only two fixed methods:
run_legal_action(input_json) and run_mjai_log(log_path, actor=0, mode=2).
Use fake-executable smoke tests first, then validate against a real external Ubuntu-built system.exe in a later task.
```

Context:

- Akochan F1 is Conditional Pass based on GitHub Actions run `26617347785`.
- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md` defines the no-vendor, no-training, no-Tenhou wrapper boundary.
- The repository previously had no Python package structure.
- F2 needs wrapper behavior, audit-log schema and fixed-sample smoke tests before any real external binary validation.

Rationale:

- A small Python wrapper fits the project's future evaluation tooling while keeping Akochan source and binaries outside the repository.
- Fixed methods avoid unrestricted command execution.
- Fake-executable tests prove wrapper parsing, normalization and audit logging without requiring real Akochan binaries or third-party artifacts.

Consequences:

- `pyproject.toml` and `src/mjlabai` define the initial minimal Python package.
- `AkochanWrapper` requires an explicit executable path or `AKOCHAN_SYSTEM_EXE`.
- The wrapper preserves raw stdout, parses JSON, normalizes mjai-style `dahai` actions and records the required audit-log fields.
- `tests/fixtures/akochan/fake_system_exe.py` is a test substitute only, not Akochan and not strength evidence.
- The next task must validate the wrapper against a real externally built `system.exe` without uploading or saving third-party binaries or artifacts.

Linked docs:

- `src/mjlabai/adapters/akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper.py`
- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0001 — Technical Plan Becomes Execution Charter

Decision:

```text
The project moves from internal-paper-first planning to technical-plan-first execution.
The paper is treated as a future outcome summary, not the current execution driver.
```

Context:

- The project north-star remains Tenhou stable dan > LuckyJ 10.68.
- The current stage is P3 / baseline reproducibility audit.
- Mortal F1 is blocked by missing public trained model artifact and local environment prerequisites.
- The project needs one technical execution charter that coordinates web-side research decisions and local Codex implementation.

Rationale:

- A paper-first workflow can encourage premature narrative, overclaiming and stage skipping.
- A technical-plan-first workflow keeps the project grounded in reproducible baselines, unified evaluation, Tenhou-oriented metrics and documented decisions.
- Git + docs are the only durable way to make web-side research decisions actionable for local Codex execution.

Consequences:

- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` becomes the current technical execution charter.
- Web ChatGPT Pro is responsible for solution design, research, review and decision support.
- Local Codex App is responsible for code, tests and documentation landing.
- LuckyJ remains the target benchmark, not a direct full-reproduction object.
- Codex must continue to execute only the first unfinished task in `docs/10_next/10_NEXT.md`.
- Every real task must update changelog, evidence, risk, handoff and next.

Linked docs:

- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`
- `docs/00_HANDOFF.md`
- `docs/10_next/10_NEXT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0006 — Define Akochan F2 as Wrapper-Only Fixed-Sample Interface Task

Decision:

```text
Akochan F2 begins as a wrapper-only fixed-sample interface/legal-action task.
The next implementation may create a minimal wrapper skeleton, but must not vendor Akochan source or binaries, train, self-play, connect to Tenhou or exceed fixed legal_action/mjai_log samples.
```

Context:

- Akochan F1 is Conditional Pass based on GitHub Actions run `26617347785`.
- The project still has custom-license restrictions and local macOS build limitations.
- The next step needs a precise F2 boundary before any adapter code is written.

Rationale:

- The racing funnel allows increasing scope only after prior evidence, but F2 must remain narrower than evaluation or strength claims.
- A wrapper-only boundary preserves license hygiene and keeps third-party source/binaries outside this repository.
- Fixed `legal_action` and `mjai_log` samples are enough to prove interface viability without self-play, training or Tenhou integration.

Consequences:

- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md` is the controlling F2 task specification.
- Future F2 implementation must record audit logs with external repo/commit, command, hashes, elapsed time and explicit no-training/no-self-play/no-Tenhou flags.
- Future F2 implementation must preserve raw Akochan output and normalize only parseable JSON.
- License review or author permission remains required before modification, redistribution, commercial use, public release or treating Akochan as a mjlabai-owned component.

Linked docs:

- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0005 — Promote Akochan to F1 Conditional Pass on Ubuntu Evidence

Decision:

```text
Akochan F1 is promoted from Blocked to Conditional Pass based on successful Ubuntu GitHub Actions build and minimal non-training samples.
The next task is to define the Akochan F2 interface/legal-action adapter task, not to write adapter code yet.
```

Context:

- The first workflow run failed validation because job-level `env` used an unsupported `runner.temp` context.
- The workflow was corrected to configure temporary paths through `$GITHUB_ENV`.
- Corrected run `26617347785` succeeded on `ubuntu-latest`.
- The run generated `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Minimal `legal_action` and `mjai_log haifu_log_sample.json 0 2` samples both succeeded.
- The custom Akochan license remains restrictive for modification, redistribution, commercial use and public release.
- Local macOS build remains blocked.

Rationale:

- F1 requires reproducible build/minimal-run evidence, not model strength.
- The Ubuntu runner evidence is enough to stop treating Akochan as build-blocked.
- Remaining license and local-platform limitations mean this should be Conditional Pass rather than full unqualified Pass.

Consequences:

- `docs/10_next/10_NEXT.md` now points to defining the Akochan F2 interface/legal-action adapter task.
- F2 task definition must specify wrapper-only integration boundaries, state/action mapping, legal-action checker scope, decision log schema and license guardrails.
- Do not train, tune, self-play, connect to Tenhou or claim Akochan strength from this F1 result.
- Do not redistribute Akochan source/binaries or modify AI-part source without license review or permission.

Linked docs:

- `.github/workflows/akochan-f1-build-audit.yml`
- `docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0004 — Use Manual GitHub Actions Ubuntu Runner for Akochan F1 Build Evidence

Decision:

```text
Add a manual GitHub Actions workflow to provide an Ubuntu Linux build environment for Akochan F1 build/minimal-run evidence.
```

Context:

- Local macOS ARM cannot currently build Akochan.
- Docker is not installed locally.
- Homebrew LLVM, Boost and OpenMP are not available through expected local paths.
- The project still needs a reproducible Linux build environment before Akochan can leave F1 Blocked.

Rationale:

- GitHub Actions `ubuntu-latest` gives a temporary Linux environment without polluting the local machine.
- A manual `workflow_dispatch` keeps execution explicit and avoids automatic repeated third-party builds.
- The workflow can install build dependencies inside the temporary runner, clone the fixed Akochan commit outside the repository, build, and run minimal non-training samples.

Consequences:

- `.github/workflows/akochan-f1-build-audit.yml` becomes the supported build-environment path for the next Akochan F1 evidence attempt.
- Akochan remains F1 Blocked until a workflow run succeeds and logs are reviewed.
- The workflow must not train, tune, self-play, connect to Tenhou, write adapters, enter F2, upload third-party source or publish binaries.

Linked docs:

- `.github/workflows/akochan-f1-build-audit.yml`
- `docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0003 — Keep Akochan at F1 Blocked Until Build and Minimal JSON/Log Sample Pass

Decision:

```text
Akochan does not pass F1 yet.
Keep Akochan at F1 Blocked and do not define F2 adapter work until a supported build environment produces `system.exe` and a minimal `legal_action` and/or `mjai_log` sample succeeds.
```

Context:

- `critter-mj/akochan` is public and inspectable at commit `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Akochan has promising JSON, mjai, pipe, log review and legal-action entry points.
- No external neural-network weight artifact appears required; the repository includes required text parameters under `params/`.
- Local macOS ARM build failed with both the macOS and Linux Makefiles.
- No `system.exe` was produced, so no minimal run could be executed.
- The custom license allows private research audit, but redistribution, AI-part modification, commercial use and public release are restricted.

Rationale:

- F1 requires local reproducibility evidence, not only source inspection.
- Promising I/O surfaces are not enough to justify F2 adapter work without a successful build and minimal run.
- The license needs tighter review before any public/commercial or modified-source usage.

Consequences:

- `docs/10_next/10_NEXT.md` now points to resolving the Akochan build/toolchain blocker.
- Akochan remains a baseline/reviewer candidate, not a runnable baseline yet.
- The next attempt should use a supported Linux toolchain or a corrected macOS Homebrew LLVM/OpenMP/Boost toolchain.
- Do not run self-play, train, tune, connect to Tenhou or write an adapter while resolving this F1 blocker.

Linked docs:

- `docs/07_development_execution/07I_AKOCHAN_F1_REPRO_AUDIT.md`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0002 — Pause Mortal Runnable Baseline and Move F1 Path to Akochan

Decision:

```text
Pause Mortal as a runnable baseline because the project currently has no lawful, verifiable and usable Mortal trained model artifact.
Keep Mortal as source-code, mjai-interface, methodology and engineering reference.
Move the next baseline F1 reproducibility audit path to Akochan.
```

Context:

- Mortal source and selected docs were inspected during F1, but the official mjai inference path requires a trained model artifact.
- No model version/tag, usage constraints or checksum can currently be recorded for a usable Mortal trained model artifact.
- Official evidence already recorded in the project says trained Mortal parameters are not currently planned for public release.
- The project must not use unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.

Rationale:

- F1 requires reproducibility evidence, including artifact provenance, usage constraints and checksum before local inference results can be trusted.
- Using unknown model files would create reproducibility, license, safety and governance risk.
- Keeping Mortal as a reference preserves useful mjai/interface and engineering lessons without pretending it is a runnable baseline.
- Akochan is the next lowest-cost baseline F1 path already listed in the racing funnel.

Consequences:

- Mortal is not promoted to F2.
- Mortal runnable-baseline work stays paused unless a lawful, verifiable and usable trained model artifact is provided later.
- Any future Mortal artifact must be verified in F1 before adapter work or evaluation work begins.
- `docs/10_next/10_NEXT.md` now points to Akochan F1 reproducibility audit as the single next task.
- This decision does not start the Akochan audit and does not authorize training, model downloads, real Tenhou access or platform automation.

Linked docs:

- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```
