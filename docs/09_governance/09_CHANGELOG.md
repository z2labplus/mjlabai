# 09_CHANGELOG

## 2026-05-29 — v2.11

- Reviewed P5 stable-dan evaluation groundwork completion.
- Added `docs/05_evaluation/05I_STABLE_DAN_GROUNDWORK_REVIEW.md`.
- Marked stable-dan evaluation groundwork as complete for the current P5 scope.
- Explicitly kept P5 overall open.
- Recorded current stable-dan completion basis:
  - deterministic stable-dan calculator.
  - bootstrap confidence interval.
  - LuckyJ `10.68` threshold comparison helper.
  - sample-size guardrails and report schema.
  - placement-count aggregation helper.
  - CLI-free synthetic smoke fixture.
  - stable-dan evaluation API documentation.
- Recorded current limits: no model-strength evidence, no real Tenhou ranked result, no real model game samples, no league harness, no replay parser, no real Tenhou data and no final LuckyJ proof.
- Set the next P5-only task to `Define P5 offline evaluation metric registry and result envelope schema.`
- No code, tests, CLI, file ingestion path, league harness, match runner, training, self-play, Tenhou connection or external-data reader was added.

## 2026-05-29 — v2.10

- Added stable-dan evaluation API documentation.
- Added `docs/05_evaluation/05H_STABLE_DAN_EVALUATION_API.md`.
- Updated `docs/00_DOCS_INDEX.md` to include the new API document.
- Documented the synthetic fixture:
  - `tests/fixtures/eval/stable_dan_placements_smoke.json`.
  - 100 synthetic records with `first=30`, `second=30`, `third=20`, `fourth=20`.
  - Not Tenhou data, not real haifu, not external log and not model result.
- Documented the API-only flow:
  - `aggregate_placement_records(...)`.
  - `bootstrap_stable_dan_ci(...)`.
  - `compare_stable_dan_to_threshold(...)`.
  - `build_stable_dan_evaluation_report(...)`.
  - `StableDanEvaluationReport.to_dict()`.
- Documented key report fields and sample-size / threshold / claim guardrails.
- Clarified that the current report schema does not include `model_name`, `dataset_name`, `evaluation_context` or caller notes; those must remain outside the report until a future schema task extends it.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan_report_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_placement_counts.py`: 18 tests passed.
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 45 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- No code, CLI, file ingestion path, league harness, match runner, training, self-play, Tenhou connection or external-data reader was added.
- Set the next task to `Review P5 stable-dan evaluation groundwork completion and define the next P5-only evaluation task.`

## 2026-05-29 — v2.9

- Added CLI-free stable-dan evaluation report smoke fixture from placement inputs.
- Added `tests/fixtures/eval/stable_dan_placements_smoke.json`.
  - Project-authored synthetic fixture only.
  - 100 records: `first=30`, `second=30`, `third=20`, `fourth=20`.
  - Not Tenhou data, not an external haifu/log, not a league result and not a model result.
- Added `tests/eval/test_stable_dan_report_smoke.py`.
- Smoke path verifies:
  - `aggregate_placement_records(...)`.
  - deterministic phoenix stable dan point estimate `11.5`.
  - `bootstrap_stable_dan_ci(...)`.
  - `compare_stable_dan_to_threshold(...)`.
  - `build_stable_dan_evaluation_report(...)`.
  - `StableDanEvaluationReport.to_dict()` JSON serialization.
- The smoke report can be reported under current sample-size guardrails but cannot enter threshold review because `total_games=100` is below the project-internal threshold-review minimum of `1000`.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan_report_smoke.py`: 1 test passed.
  - `python3 -m unittest tests/eval/test_placement_counts.py`: 18 tests passed.
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 45 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- No CLI, file ingestion path, league harness, match runner, training, self-play, Tenhou connection or external-data reader was added.
- Set the next task to `Add stable-dan evaluation API documentation with example usage from synthetic placements.`

## 2026-05-29 — v2.8

- Added placement-count aggregation helper for stable-dan evaluation inputs.
- Added `src/mjlabai/eval/placement_counts.py` with:
  - `StableDanPlacementCounts`.
  - `aggregate_placement_counts(...)`.
  - `aggregate_placement_records(...)`.
  - `calculate_stable_dan_from_placements(...)`.
- Exported placement aggregation APIs from `src/mjlabai/eval/__init__.py`.
- Added `tests/eval/test_placement_counts.py`.
- Supported placement inputs are only explicit `1`/`2`/`3`/`4` values and whitelisted aliases: `"1"`, `"2"`, `"3"`, `"4"`, `"first"`, `"second"`, `"third"`, `"fourth"`, `"1st"`, `"2nd"`, `"3rd"` and `"4th"`.
- Invalid, ambiguous, zero-based, bool, float and unknown placement inputs now fail explicitly instead of being silently normalized.
- `to_stable_dan_kwargs()` can feed the existing deterministic stable-dan calculator without reading files, running league code or touching Tenhou.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_placement_counts.py`: 18 tests passed.
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 45 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This remains offline evaluation input infrastructure only, not training, self-play, league execution, real Tenhou integration or model-strength evidence.
- Set the next task to `Add CLI-free stable-dan evaluation report smoke fixture from placement inputs.`

## 2026-05-29 — v2.7

- Added minimum sample-size guardrails and stable-dan evaluation report schema.
- Extended `src/mjlabai/eval/stable_dan.py` with:
  - `DEFAULT_MIN_TOTAL_GAMES_FOR_STABLE_DAN_REPORT = 100`.
  - `DEFAULT_MIN_FOURTH_COUNT_FOR_STABLE_DAN_REPORT = 10`.
  - `DEFAULT_MIN_TOTAL_GAMES_FOR_THRESHOLD_REVIEW = 1000`.
  - `DEFAULT_MIN_FOURTH_COUNT_FOR_THRESHOLD_REVIEW = 50`.
  - `DEFAULT_MAX_UNDEFINED_RATE_FOR_STABLE_DAN_REPORT = 0.05`.
  - `StableDanSampleSizeAssessment`.
  - `StableDanEvaluationReport`.
  - `assess_stable_dan_sample_size(...)`.
  - `build_stable_dan_evaluation_report(...)`.
- Report schema includes placement counts/rates, point estimate, bootstrap CI, threshold outcome, sample-size assessment, notes and source note.
- `StableDanEvaluationReport.to_dict()` returns a JSON-serializable dictionary.
- Documented that sample-size defaults are project-internal governance guardrails, not Tenhou official standards or proof of strength.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 45 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This remains evaluation statistics infrastructure only, not training, self-play, league execution, real Tenhou integration or model-strength evidence.
- Set the next task to `Add placement-count aggregation helper for stable-dan evaluation inputs.`

## 2026-05-29 — v2.6

- Added a stable-dan threshold comparison helper for the LuckyJ 10.68 target line.
- Extended `src/mjlabai/eval/stable_dan.py` with:
  - `LUCKYJ_STABLE_DAN_THRESHOLD = 10.68`.
  - `StableDanThresholdComparison`.
  - `compare_stable_dan_to_threshold(...)`.
  - `bootstrap_and_compare_stable_dan_threshold(...)`.
- Clear pass now requires `bootstrap_result.lower_bound > threshold` and `undefined_rate <= max_undefined_rate`.
- If point estimate exceeds the threshold but bootstrap lower bound does not, the outcome is `point_estimate_only` and `clears_threshold=False`.
- If undefined bootstrap resample rate is too high, the outcome is `unreliable` and `clears_threshold=False`.
- Added threshold comparison tests for clear pass, point-estimate-only, clear fail, inconclusive, unreliable, custom threshold, invalid inputs and the bootstrap-and-compare helper.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 32 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This is evaluation statistics infrastructure only, not model-strength evidence, training, self-play, league execution or Tenhou integration.
- Set the next task to `Add minimum sample-size and reporting schema for stable-dan evaluation results.`

## 2026-05-29 — v2.5

- Added bootstrap confidence intervals for the Tenhou stable-dan estimate.
- Extended `src/mjlabai/eval/stable_dan.py` with:
  - `bootstrap_stable_dan_ci(...)`.
  - `StableDanBootstrapResult`.
  - `StableDanBootstrapUndefinedError`.
- Implemented percentile empirical multinomial bootstrap over observed placement counts using Python standard library only.
- Bootstrap output records point estimate, confidence level, lower bound, upper bound, bootstrap count, successful resamples, undefined resamples, undefined rate, method, seed, quantile method and source note.
- Undefined bootstrap resamples with zero fourth-place count are skipped and counted; they are not converted into infinite stable dan.
- If every bootstrap resample is undefined, the API raises `StableDanBootstrapUndefinedError`.
- Updated `tests/eval/test_stable_dan.py` to cover reproducible seeded bootstrap, undefined-resample accounting, validation errors and non-infinite bounds.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 21 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This is evaluation statistics infrastructure only, not model-strength evidence, training, self-play, league execution or Tenhou integration.
- Set the next task to `Add stable-dan threshold comparison helper for LuckyJ 10.68 using bootstrap lower bound.`

## 2026-05-29 — v2.4

- Implemented the Tenhou stable-dan calculator as the next P5 evaluation-foundation task.
- Added `src/mjlabai/eval/stable_dan.py` and `src/mjlabai/eval/__init__.py`.
- Added `tests/eval/test_stable_dan.py`.
- Implemented deterministic four-player room-specific formulas for:
  - general / ippan: first=20, second=10.
  - upper / joukyu: first=40, second=10.
  - expert / tokujou: first=50, second=20.
  - phoenix / houou: first=60, second=30.
- Added `StableDanResult`, `StableDanUndefinedError`, `calculate_stable_dan(...)` and `placement_rates(...)`.
- Recorded placement counts, placement rates, total games, formula name, formula weights and source note in calculator output.
- `fourth_count == 0` now raises `StableDanUndefinedError`; the calculator does not fabricate infinite strength.
- Local validation passed:
  - `python3 -m unittest tests/eval/test_stable_dan.py`: 9 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
- This is deterministic metric infrastructure only, not a training result, league result, self-play result or Tenhou connection.
- Set the next task to `Add bootstrap confidence interval for stable-dan estimate.`

## 2026-05-29 — v2.3

- Closed the Akochan F2 fixed-sample real-exe wrapper validation task.
- Recorded GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit` run `26629344590`.
- Run `26629344590` executed at commit `29f5e1ed19407d169f85524e05438ac8938d2dc2` with commit message `Support Akochan mixed stdout parsing`.
- Workflow result and job result were both success.
- Confirmed Ubuntu runner built `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Confirmed fake wrapper tests passed 14 tests.
- Confirmed real external `system.exe legal_action` wrapper test passed.
- Confirmed real external `system.exe mjai_log` wrapper test passed.
- Confirmed allowlisted mixed stdout parser passed real workflow validation.
- Recorded that this is fixed-sample wrapper/integration evidence only, not Akochan strength evidence and not mjlabai strength evidence.
- Recorded that no training, tuning, self-play, match, Tenhou connection, third-party vendoring, binary storage or artifact upload occurred.
- Recorded that Akochan custom license remains a blocker for modification, redistribution, commercial use or public release without review/permission.
- Recorded GitHub Actions Node.js 20 deprecation warning as workflow maintenance risk, not an F2 validation blocker.
- Set the next task to `Implement Tenhou stable-dan calculator from room-specific formulas.`

## 2026-05-29 — v2.2

- Fixed the Akochan F2 real-exe `mjai_log` mixed stdout parser blocker exposed by workflow run `26628128871`.
- The parser now supports:
  - single JSON values,
  - JSON Lines,
  - concatenated JSON values/objects,
  - pretty-printed multi-record JSON streams,
  - mixed stdout that contains the single allowlisted non-JSON status line `calculating review`.
- Added `skipped_non_json_lines` to `AkochanCommandResult`.
- Parser diagnostics now include bounded stdout summary, stdout SHA256, failure position, parsed-record count and skipped-status-line count.
- Unknown non-JSON lines and partial parses still raise `AkochanOutputParseError`; the only skipped non-JSON line is exactly `calculating review`.
- Fake executable tests now simulate JSON records + `calculating review` + JSON review output, plus an unknown status line that must fail.
- Local validation passed:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Set the next task to rerun the manual `Akochan F2 Wrapper Real Exe Audit` workflow and review real `legal_action` / `mjai_log` results after allowlisted mixed stdout parser support.
- No training, tuning, self-play, Tenhou connection, third-party vendoring, binary storage or artifact upload occurred.

## 2026-05-29 — v2.1

- Fixed the Akochan F2 real-exe `mjai_log` stdout parser blocker exposed by workflow run `26623247276`.
- `AkochanWrapper` now parses:
  - single JSON values,
  - JSON Lines,
  - concatenated JSON values/objects,
  - pretty-printed multi-record JSON streams.
- Added `parsed_records` to `AkochanCommandResult` while preserving `parsed_json` compatibility: one record returns the record, multiple records return the records list.
- Parser diagnostics now include bounded stdout summary, stdout SHA256, failure position and parsed-record count.
- Parser does not accept partial parses: non-whitespace non-JSON residue raises `AkochanOutputParseError`.
- Fake executable tests now simulate JSON Lines, concatenated JSON objects, pretty-printed multi-record JSON streams and invalid mixed stdout.
- Local validation passed:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 12 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Set the next task to rerun the manual `Akochan F2 Wrapper Real Exe Audit` workflow and review real `legal_action` / `mjai_log` results.
- No training, tuning, self-play, Tenhou connection, third-party vendoring, binary storage or artifact upload occurred.

## 2026-05-29 — v2.0

- Reran manual GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit`.
- Run `26623247276` executed at commit `0ddb28575ddd1b624cad34b20d6dc6b79303963c`.
- Confirmed Ubuntu build still generated `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Confirmed fake wrapper smoke tests passed 8 tests in the workflow.
- Confirmed workflow exported `AKOCHAN_SYSTEM_EXE`, `AKOCHAN_WORKING_DIR` and `AKOCHAN_MJAI_LOG_SAMPLE` before real-exe tests.
- Confirmed real `legal_action` wrapper test passed.
- Confirmed the previous `setup_mjai.json` cwd failure is gone for real `mjai_log`.
- Recorded the new blocker: real `mjai_log` stdout reaches the wrapper, but parsing fails with `JSONDecodeError: Extra data` / `AkochanOutputParseError`.
- Set the next task to fix real `mjai_log` stdout parsing/diagnostics, then rerun the workflow.
- Reaffirmed that this is interface/runtime evidence only, not strength evidence, and no third-party source, binary, params or build artifact was uploaded.

## 2026-05-29 — v1.9

- Fixed the Akochan F2 wrapper working-directory boundary exposed by workflow run `26621536548`.
- `AkochanWrapper` now resolves the runtime cwd by priority: explicit `working_dir`, `AKOCHAN_WORKING_DIR`, then `Path(system_exe).resolve().parent`.
- `_run_subcommand` now launches the external executable with `cwd=self.working_dir`.
- `AkochanAuditLog` now records `working_dir`.
- Updated fake executable tests so `mjai_log` requires a synthetic cwd runtime marker, proving cwd handling is exercised.
- Updated the real-exe workflow to export `AKOCHAN_SYSTEM_EXE`, `AKOCHAN_WORKING_DIR` and `AKOCHAN_MJAI_LOG_SAMPLE` before running real wrapper tests.
- Local validation passed:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 8 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Set the next task to rerun the manual `Akochan F2 Wrapper Real Exe Audit` workflow and review whether real `legal_action` and `mjai_log` both pass with `AKOCHAN_WORKING_DIR` set.
- No training, tuning, self-play, Tenhou connection, third-party vendoring, binary storage or artifact upload occurred.

## 2026-05-29 — v1.8

- Triggered manual GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit`.
- Run `26621536548` executed at commit `7d58f969367d3e51c57d859dbfb9433f1ca898a1`.
- Confirmed the workflow built Akochan successfully in the temporary Ubuntu runner: `ai_src/libai.so`, root `libai.so` and `system.exe` were generated.
- Confirmed fake wrapper smoke tests passed in the workflow.
- Confirmed real `legal_action` wrapper test passed against the Ubuntu-built `system.exe`.
- Recorded real `mjai_log` wrapper test failure: `system.exe` could not load `setup_mjai.json` because the wrapper launched it from the mjlabai checkout working directory.
- Set the next task to fix the real-exe cwd/runtime boundary, then rerun the workflow.
- Reaffirmed that this is interface/runtime evidence only, not strength evidence, and no third-party source, binary, params or build artifact was uploaded.

## 2026-05-29 — v1.7

- Added `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`.
- The new workflow is manual `workflow_dispatch` only and builds Akochan at commit `53188a0b926fbab38177f88c3cd87d554cf412af` inside a temporary `ubuntu-latest` GitHub runner.
- The workflow sets `AKOCHAN_SYSTEM_EXE` to the runner-temp `system.exe` and `AKOCHAN_MJAI_LOG_SAMPLE` to the runner-temp `haifu_log_sample.json`, then runs mjlabai wrapper tests against the real external executable.
- Added `tests/adapters/test_akochan_wrapper_real_exe.py` with default skip behavior when `AKOCHAN_SYSTEM_EXE` is absent; `mjai_log` also skips when `AKOCHAN_MJAI_LOG_SAMPLE` is absent.
- Updated the wrapper stdout parser to accept either one JSON document or newline-delimited JSON objects.
- Verified local fake tests with `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 4 tests passed.
- Verified local real-exe tests with `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without a real external executable.
- Confirmed the new workflow/test path does not upload or store Akochan source, `system.exe`, `libai.so`, `params/`, third-party binaries or build artifacts.
- Set the next task to manually run `Akochan F2 Wrapper Real Exe Audit` and review whether the wrapper succeeds against the real Ubuntu-built `system.exe`.

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
