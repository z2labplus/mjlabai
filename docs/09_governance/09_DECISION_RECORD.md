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

## 2026-05-29 — DR-0016 — Stable-Dan Reports Require Sample-Size Guardrails

Decision:

```text
Stable-dan reporting must separate statistical threshold outcome from project-level claim readiness.
Default sample-size guardrails are internal governance defaults, not Tenhou official standards or proof.
```

Context:

- Stable-dan point estimate, bootstrap CI and LuckyJ threshold helper are implemented.
- A `clear_pass` threshold outcome can still be based on too little data for project-level claims.
- Future reports need a standard schema so counts, CI, threshold outcome and sample-size status are always present.

Rationale:

- Separating `clears_threshold` from `can_enter_threshold_review` prevents overclaiming.
- Report schema makes future evaluation outputs easier to audit.
- Explicit notes keep the report framed as offline statistics, not Tenhou ranked proof.

Consequences:

- `assess_stable_dan_sample_size(...)` returns report and threshold-review readiness.
- `build_stable_dan_evaluation_report(...)` combines point estimate, bootstrap CI, threshold outcome and sample-size assessment.
- Default report minimum is `total_games >= 100` and `fourth_count >= 10`.
- Default threshold-review minimum is `total_games >= 1000` and `fourth_count >= 50`.
- Default maximum undefined rate is `0.05`.
- The next task is placement-count aggregation for stable-dan evaluation inputs.

Linked docs:

- `src/mjlabai/eval/stable_dan.py`
- `tests/eval/test_stable_dan.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0015 — Stable-Dan Threshold Pass Requires Bootstrap Lower Bound

Decision:

```text
Stable-dan threshold comparison defaults to LuckyJ stable dan 10.68.
A clear pass requires bootstrap lower_bound > threshold and acceptable undefined_rate.
Point estimate alone must never set clears_threshold=True.
```

Context:

- Stable-dan point estimate and bootstrap CI are implemented.
- The project target is stable dan above LuckyJ 10.68.
- Without a helper, callers may accidentally compare only the point estimate and overclaim strength.

Rationale:

- Lower-bound comparison is more conservative than point-estimate comparison.
- High undefined bootstrap rate means the interval is unreliable even if the lower bound looks strong.
- Encoding the outcomes in one helper makes future reports easier to audit.

Consequences:

- `compare_stable_dan_to_threshold(...)` returns `clear_pass`, `point_estimate_only`, `clear_fail`, `unreliable` or `inconclusive`.
- `bootstrap_and_compare_stable_dan_threshold(...)` combines bootstrap CI and threshold comparison.
- The next task is minimum sample-size and reporting schema for stable-dan evaluation results before using helper output for project-level LuckyJ claims.

Linked docs:

- `src/mjlabai/eval/stable_dan.py`
- `tests/eval/test_stable_dan.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0014 — Require Bootstrap Lower-Bound Logic Before LuckyJ Stable-Dan Claims

Decision:

```text
Implement stable-dan bootstrap confidence intervals as percentile empirical multinomial resampling.
Do not compare against LuckyJ 10.68 from point estimate alone; the next helper must use the bootstrap lower bound.
```

Context:

- The deterministic stable-dan calculator is implemented and tested.
- The project target is stable dan above LuckyJ 10.68, but point estimates alone can overstate strength.
- Bootstrap resamples can produce undefined stable dan when sampled fourth-place count is zero.

Rationale:

- Percentile empirical multinomial bootstrap is simple, dependency-free and tied directly to observed placement counts.
- Undefined resamples must be visible in the result because high undefined rate makes the CI unreliable.
- A threshold helper should encode the project rule that lower-bound evidence matters more than point-estimate optimism.

Consequences:

- `bootstrap_stable_dan_ci(...)` reports point estimate, CI bounds, confidence level, bootstrap count, successful resamples, undefined resamples and undefined rate.
- Undefined resamples are skipped and counted, never converted into infinite stable dan.
- If all resamples are undefined, `StableDanBootstrapUndefinedError` is raised.
- The next task is a LuckyJ 10.68 threshold comparison helper using the bootstrap lower bound.

Linked docs:

- `src/mjlabai/eval/stable_dan.py`
- `tests/eval/test_stable_dan.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0013 — Treat Stable Dan as Point Estimate Until Bootstrap CI Exists

Decision:

```text
Implement Tenhou room-specific stable-dan as a deterministic point estimate now.
Do not use it as statistically reliable strength evidence until bootstrap confidence intervals and sample-size reporting are added.
```

Context:

- The project has closed Akochan F2 fixed-sample wrapper validation and moved into P5 evaluation groundwork.
- The north-star target is stable dan above LuckyJ 10.68, so stable-dan calculation must become a first-class project metric before training or league work.
- The current task implements the room-specific official formula but explicitly excludes bootstrap CI.

Rationale:

- A deterministic point estimate is needed before uncertainty estimation.
- `fourth_count == 0` can make the formula undefined, so the calculator must refuse to fabricate infinite strength.
- The project must keep metric infrastructure separate from model-strength claims.

Consequences:

- `calculate_stable_dan(...)` supports general/ippan, upper/joukyu, expert/tokujou and phoenix/houou aliases.
- `StableDanResult` exposes counts, rates, formula weights and source note for auditability.
- `StableDanUndefinedError` is raised when `fourth_count == 0`.
- The next task is bootstrap confidence intervals for the stable-dan estimate.

Linked docs:

- `src/mjlabai/eval/stable_dan.py`
- `tests/eval/test_stable_dan.py`
- `docs/10_next/10_NEXT.md`
- `docs/05_evaluation/05F_ALGORITHM_RANKING_PROTOCOL.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0011 — Allow Only the Known Akochan mjai_log Status Line in Mixed Stdout

Decision:

```text
AkochanWrapper may parse mixed stdout only when the non-JSON line is exactly `calculating review`.
The wrapper must record skipped_non_json_lines, preserve raw_stdout and parsed_records, and reject unknown non-JSON lines or partial parses.
```

Context:

- GitHub Actions run `26628128871` showed strict JSON stream parsing improved the `mjai_log` failure diagnostics.
- The same run showed the real stdout shape: JSON event records, the non-JSON line `calculating review`, then JSON review output.
- The project needs real `mjai_log` compatibility evidence without silently accepting arbitrary mixed logs.

Rationale:

- The status line is a known Akochan progress/status message, not a JSON record.
- A single exact-string allowlist keeps the parser strict and auditable.
- Recording skipped lines and parse warnings keeps the stdout shape reviewable without uploading third-party artifacts.
- Unknown non-JSON output may indicate a runtime error or unmodeled behavior and must fail.

Consequences:

- `AkochanCommandResult` now includes `skipped_non_json_lines`.
- The parser supports single JSON, JSON Lines, concatenated JSON values, pretty-printed multi-record JSON streams and the single allowlisted mixed status line.
- Parse failures include bounded stdout summary, stdout SHA256, parsed-record count, skipped-status-line count and failure position.
- The next evidence step is rerunning the manual real-exe workflow; this decision is parser implementation evidence only, not strength evidence.

Linked docs:

- `src/mjlabai/adapters/akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper_real_exe.py`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0012 — Close Akochan F2 Fixed-Sample Wrapper Validation and Move to Stable-Dan Metric Work

Decision:

```text
Treat Akochan as F1 Conditional Pass with F2 fixed-sample real-exe wrapper validation passed.
Do not treat this as strength evidence.
Set the next task to implement the Tenhou stable-dan calculator from room-specific formulas.
```

Context:

- GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit` run `26629344590` succeeded.
- The run used mjlabai commit `29f5e1ed19407d169f85524e05438ac8938d2dc2`.
- Ubuntu runner built `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Fake wrapper tests passed 14 tests.
- Real external `system.exe legal_action` wrapper test passed.
- Real external `system.exe mjai_log` wrapper test passed.
- No third-party source, binary, `params/` or build artifact was stored or uploaded.

Rationale:

- F2 fixed-sample wrapper validation has enough evidence to close this narrow integration task.
- The project still lacks the evaluation metric foundation needed to compare future candidates in Tenhou terms.
- Stable dan is part of the north-star target and should be implemented before broader model comparison or strength claims.

Consequences:

- Akochan remains an interface/reviewer candidate, not a proved strength baseline.
- Broader Akochan evaluator/reviewer integration requires a separate task and license boundary review.
- `docs/10_next/10_NEXT.md` now points to the Tenhou stable-dan calculator task.
- No training, self-play, match, league, real Tenhou integration or platform automation is authorized by this decision.

Linked docs:

- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`
- `docs/07_development_execution/07B_TASK_BACKLOG.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0008 — Validate Akochan F2 Wrapper Through Temporary GitHub Actions Real-Exe Workflow

Decision:

```text
Add a manual GitHub Actions workflow and default-skip unittest file to validate the Akochan F2 wrapper against a real Ubuntu-built external system.exe.
The workflow may build Akochan in the runner temp directory and set AKOCHAN_SYSTEM_EXE for tests, but must not upload or store third-party source, binaries, params or build artifacts.
```

Context:

- Akochan F1 is Conditional Pass from GitHub Actions run `26617347785`.
- The minimal Akochan F2 wrapper skeleton passes fake-executable smoke tests.
- Fake-executable tests prove wrapper behavior only; they do not prove compatibility with real `system.exe`.
- The project must keep Akochan source and binaries outside the repository because of license and governance constraints.

Rationale:

- A manual workflow gives a reproducible Ubuntu environment without requiring local Docker or macOS toolchain changes.
- Default-skip real-exe tests keep local unit tests reliable when no real external executable is available.
- Runner-temp build and no artifact upload preserve the no-vendor/no-binary boundary.

Consequences:

- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml` is the controlled real-exe validation path.
- `tests/adapters/test_akochan_wrapper_real_exe.py` skips locally unless `AKOCHAN_SYSTEM_EXE` exists; the `mjai_log` test also requires `AKOCHAN_MJAI_LOG_SAMPLE`.
- The next task is to manually run the workflow and review its run ID/logs.
- Until that workflow succeeds and is reviewed, the project has no real `system.exe` wrapper compatibility evidence.
- This remains interface evidence only, not strength evidence.

Linked docs:

- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`
- `tests/adapters/test_akochan_wrapper_real_exe.py`
- `src/mjlabai/adapters/akochan_wrapper.py`
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

## 2026-05-29 — DR-0009 — Run External Akochan system.exe From an Audited Working Directory

Decision:

```text
AkochanWrapper must launch external system.exe with a controlled subprocess working directory.
The resolution priority is: explicit working_dir constructor argument, AKOCHAN_WORKING_DIR, then Path(system_exe).resolve().parent.
Each wrapper audit log must record the actual working_dir.
```

Context:

- GitHub Actions run `26621536548` built Akochan and passed fake wrapper tests plus real `legal_action`.
- The same run failed real `mjai_log` because `system.exe` attempted to load `setup_mjai.json` from the mjlabai checkout working directory.
- Akochan runtime files live beside the external executable in the temporary Akochan checkout/build directory.

Rationale:

- Defaulting cwd to the executable directory matches the temporary Ubuntu build layout and keeps runtime files visible.
- Supporting `AKOCHAN_WORKING_DIR` gives a reproducible override for symlinks or wrapper paths that differ from the real Akochan runtime root.
- Recording `working_dir` in audit logs makes the runtime boundary inspectable without storing third-party source or binaries.

Consequences:

- `src/mjlabai/adapters/akochan_wrapper.py` now validates and records `working_dir`.
- Fake tests cover default, explicit and environment-variable working-directory behavior.
- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml` exports `AKOCHAN_WORKING_DIR=${AKOCHAN_DIR}` before real-exe tests.
- The next evidence step is rerunning the manual workflow; this decision alone is not real `mjai_log` compatibility evidence and not strength evidence.

Linked docs:

- `src/mjlabai/adapters/akochan_wrapper.py`
- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`
- `tests/adapters/test_akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper_real_exe.py`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

## 2026-05-29 — DR-0010 — Parse Akochan stdout as a Strict JSON Stream

Decision:

```text
AkochanWrapper should parse stdout as either a single JSON value or a strict stream of JSON values.
It may support JSON Lines, concatenated JSON values and pretty-printed multi-record JSON streams, but it must not treat partial parsing as success.
```

Context:

- GitHub Actions run `26623247276` showed real `mjai_log` no longer fails on `setup_mjai.json`.
- The same run failed because real `mjai_log` stdout triggered `JSONDecodeError: Extra data`.
- The previous parser only handled a single JSON value and simple per-line JSON records.

Rationale:

- Akochan `mjai_log` can emit multiple JSON records in one stdout stream.
- Strict JSON stream parsing handles compact, line-delimited and pretty-printed records without allowing silent truncation.
- Bounded diagnostics make GitHub Actions failures reviewable without dumping large raw stdout.

Consequences:

- `AkochanCommandResult` now includes `parsed_records`.
- Successful calls preserve `raw_stdout`, `parsed_json`, `parsed_records` and `parse_warnings`.
- Parse failures include bounded stdout summary, stdout SHA256, failure position and parsed-record count.
- The next evidence step is rerunning the manual real-exe workflow; this decision is parser implementation evidence only, not strength evidence.

Linked docs:

- `src/mjlabai/adapters/akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper.py`
- `tests/adapters/test_akochan_wrapper_real_exe.py`
- `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`
- `docs/10_next/10_NEXT.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

Status:

```text
Accepted
```

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
