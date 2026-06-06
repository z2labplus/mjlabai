# 00_HANDOFF

## Project card

Project name: MjLabAI Tenhou Mahjong AI

North-star target:

```text
Train a Japanese Mahjong AI whose long-term Tenhou performance exceeds Tencent LuckyJ.
Minimum target: Tenhou stable dan > 10.68.
```

## Current status

The project documentation now includes:

- North-star goal and LuckyJ benchmark.
- Tenhou-oriented success metrics.
- Data, supervised policy, self-play RL, evaluation, inference and governance structure.
- Algorithm candidate table for Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer.
- Algorithm ranking protocol.
- v0.4 racing-funnel mechanism for staged algorithm selection.
- P0-P12 project roadmap from rule setup through LuckyJ 10.68 validation.
- v0.1 technical execution plan: technical-plan-first execution, paper-as-future-summary.

Current stage interpretation:

```text
P0 / P1 / P2 are basically established.
P3 baseline reproducibility audit produced current Mortal/Akochan funnel evidence.
The active project work has just closed P5 evaluation groundwork for the
current synthetic/local scope.
Mortal F1 runnable-baseline path is paused because no lawful, verifiable and usable trained model artifact is currently available.
Akochan F1 is Conditional Pass after successful Ubuntu GitHub Actions build/minimal-run evidence, with license and local macOS build limits still open.
Akochan F2 task definition is complete.
Minimal Akochan F2 wrapper skeleton is implemented and passes fake-executable smoke tests.
Akochan F2 fixed-sample real-exe wrapper validation has passed: workflow run `26629344590` at commit `29f5e1ed19407d169f85524e05438ac8938d2dc2` built `ai_src/libai.so`, root `libai.so` and `system.exe`; fake wrapper tests passed 14 tests; real `legal_action` and real `mjai_log` wrapper tests both passed.
This is fixed-sample wrapper/integration evidence only. It is not Akochan strength evidence, not mjlabai strength evidence, and not authorization for broad adapter work, self-play, match, training or Tenhou integration.
The project has completed the final P5 closure review for the current
synthetic/local evaluation groundwork scope. The deterministic Tenhou
stable-dan calculator from room-specific formulas is implemented and tested.
The stable-dan bootstrap confidence interval is implemented and tested with percentile empirical multinomial resampling.
The stable-dan threshold comparison helper is implemented and tested with LuckyJ stable dan `10.68` as the default target line.
The stable-dan reporting schema and minimum sample-size guardrails are implemented and tested.
The placement-count aggregation helper is implemented and tested for offline stable-dan evaluation inputs.
The CLI-free stable-dan evaluation report smoke fixture is implemented and tested from synthetic placement inputs.
The stable-dan evaluation API documentation is added with example usage from synthetic placements.
The stable-dan evaluation groundwork subtrack is complete for the current P5 scope.
The P5 offline evaluation metric registry and result envelope schema are implemented and documented.
The offline evaluation envelope smoke test now verifies that a synthetic stable-dan report can be represented as an `OfflineEvaluationResultEnvelope`.
The P5 legal-action / invalid-action metric specification is defined in `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`.
The P5 action canonicalization schema for legal-action metric fixtures is defined in `docs/05_evaluation/05L_ACTION_CANONICALIZATION_SCHEMA.md`.
The synthetic legal-action metric fixture schema smoke test is implemented in `tests/eval/test_legal_action_fixture_schema_smoke.py` against `tests/fixtures/eval/legal_action_metric_smoke.json`; it validates fixture shape only and does not calculate legal/invalid rates or implement an evaluator.
The P5 legal-action metric synthetic evaluator boundary is defined in `docs/05_evaluation/05K_LEGAL_ACTION_METRIC_SPEC.md`: future implementation may use only project-authored synthetic/local fixtures, current `dahai` scope and strict matching; it must preserve explicit count/rate denominator rules and all-false safety flags, and must not use real Tenhou, real haifu, external logs, platform data, model code, third-party binaries, training, self-play or league paths.
The P5 synthetic legal-action metric evaluator is implemented for the project-authored fixture only in `src/mjlabai/eval/legal_action_metric.py`, with tests in `tests/eval/test_legal_action_metric.py`. The fixture now includes an explicit synthetic `parse_failure` record that keeps `action_type = "dahai"` and uses `tsumogiri: null` only to exercise the current strict parse-failure branch. It computes the current synthetic fixture as `legal=1`, `invalid=1`, `missing=1`, `parse_failure=1`, `skipped=1`, `evaluated=4`, and rates `1/4`, `1/4`, `1/4`, `1/4`. It also maps the result into `OfflineEvaluationResultEnvelope` with all safety flags false and synthetic-only warnings. `docs/05_evaluation/05M_LEGAL_ACTION_SYNTHETIC_EVALUATOR_REVIEW.md` records that this minimum outcome coverage is complete only for the current P5 synthetic-only `dahai` + strict scope. This is legality diagnostic infrastructure only, not a broad evaluator, canonicalizer, legal-action checker, CLI, league, runner, model-output path, Tenhou integration or strength evidence.
`docs/05_evaluation/05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md` defines the P5 tiny benchmark harness boundary before implementation. It is docs-only: future legal-action rate, latency and fixed-position diagnostics may use only synthetic/local inputs and compatible `OfflineEvaluationResultEnvelope` records.
`tests/fixtures/eval/tiny_benchmark_harness_smoke.json` and `tests/eval/test_tiny_benchmark_harness_fixture_schema_smoke.py` add a P5 tiny benchmark harness synthetic fixture schema smoke test. The fixture is project-authored synthetic/local only and describes legal-action diagnostic shape, latency diagnostic plan shape and fixed-position synthetic decision shape without implementing a harness, measuring latency, calculating fixed-position exact-match, calling model code or reading real Tenhou / real haifu / external logs / platform data. It is not model-strength evidence, Tenhou evidence, stable-dan evidence, LuckyJ `10.68` comparison or candidate-promotion evidence.
`docs/05_evaluation/05O_TINY_BENCHMARK_FIXTURE_SCHEMA_REVIEW.md` reviews that fixture schema smoke coverage and records that it is complete only for the current P5 schema-only synthetic/local boundary. The fixture schema is sufficient as a front-door input boundary for a future P5-only tiny benchmark harness implementation task, but no harness implementation, production code, tests, fixtures, latency measurement, model-output integration, real-data path, CLI, league, runner or P6-P12 work was added by the review gate.
`src/mjlabai/eval/tiny_benchmark_harness.py` implements the P5 tiny benchmark harness for the project-authored synthetic fixture only, with tests in `tests/eval/test_tiny_benchmark_harness.py`. The harness loads only `tests/fixtures/eval/tiny_benchmark_harness_smoke.json`, validates and summarizes its legal-action diagnostic shape, latency plan shape and fixed-position synthetic record shape, and can emit an `OfflineEvaluationResultEnvelope` with `evaluation_type = "tiny_benchmark_harness"`, `wrapper_smoke_success = true`, `sample_size = 1`, all safety flags false and synthetic/local warnings. It does not measure latency, calculate legal-action metrics inside the harness, compute fixed-position exact-match, connect model output, add CLI/file ingestion, read real Tenhou / real haifu / external logs / platform data, or provide model-strength, stable-dan or LuckyJ `10.68` evidence.
`docs/05_evaluation/05Q_TINY_BENCHMARK_HARNESS_IMPLEMENTATION_REVIEW.md` reviews the P5 tiny benchmark harness implementation and records that it can close for the current project-authored synthetic/local fixture scope with no blocker. The evidence grade remains P5 synthetic/local tiny benchmark harness implementation review evidence only.
`docs/05_evaluation/05R_OFFLINE_ENVELOPE_COVERAGE_FOR_TINY_BENCHMARK_DIAGNOSTICS_REVIEW.md` reviews the P5 offline result envelope coverage for synthetic tiny benchmark diagnostics. It records that the current envelope can represent the diagnostic with `evaluation_type = "tiny_benchmark_harness"`, `wrapper_smoke_success = true`, `sample_size = 1`, `latency_ms = None`, all-false safety flags, synthetic/local warnings and evidence references. No blocker was found, and the evidence grade remains P5 synthetic/local offline envelope coverage review evidence only.
`docs/05_evaluation/05S_METRIC_REGISTRY_CONSISTENCY_REVIEW.md` reviews P5 metric registry consistency across stable-dan, legal-action and tiny benchmark diagnostics. It records that current registry names, units, directions, status/source notes and evidence grades are consistent for the current P5 scope. It also records that future tiny benchmark names such as latency percentiles and fixed-position exact-match remain fixture planning names, not current registered/emitted metrics. No blocker was found, and no registry code, production code, tests or fixtures were changed by the review.
`docs/05_evaluation/05T_SYNTHETIC_LOCAL_EVIDENCE_TAXONOMY_AND_PROMOTION_GUARDRAILS_REVIEW.md` reviews P5 synthetic/local evidence taxonomy and promotion guardrails. It records that evidence labels, non-evidence warnings, promotion/ranking guardrails and stage-boundary wording are consistent across the current P5 stable-dan, legal-action, tiny benchmark, offline envelope and metric registry artifacts. No blocker was found, and no promotion criteria, taxonomy definitions, production code, tests or fixtures were changed by the review.
`docs/05_evaluation/05U_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_CHECKLIST.md` defines P5 evaluation groundwork closure criteria and an exit readiness checklist. It records the current P5 scope, current-scope complete subtracks, required remaining P5 items, deferred items and non-entry conditions for P6-P12. P5 is near closure, but it remains open until a closure review gate confirms readiness.
`docs/05_evaluation/05V_P5_EVALUATION_GROUNDWORK_CLOSURE_CRITERIA_AND_EXIT_READINESS_REVIEW.md` reviews the P5 closure criteria and exit readiness checklist. The review found no blocker: the `05U` scope is correct, the current P5 subtrack inventory is complete enough for finalization, closure criteria are sufficient, the exit readiness checklist is executable, deferred items are correctly classified and P6-P12 non-entry conditions are sufficient. The closure criteria review can close, but P5 remains open pending final P5 handoff/evidence index finalization and a later final closure review.
`docs/05_evaluation/05W_P5_HANDOFF_AND_EVIDENCE_INDEX_FINALIZATION.md` finalizes the P5 handoff and evidence index for final closure review. It records a finalization-ready handoff summary, a P5 evidence index, required remaining items, deferred items and governance synchronization status. No blocker was found. P5 handoff and evidence index are finalized for final closure review, but P5 remains open until the final closure review gate.
`docs/05_evaluation/05X_FINAL_P5_CLOSURE_REVIEW.md` is the final P5 closure review gate. It records that all P5 closure criteria pass, no blocker was found, required remaining P5 items have narrowed to closure decision recording, deferred later-stage items do not block current P5 closure, and required validation tests were rerun. P5 is closed for the current synthetic/local evaluation groundwork scope.
P5 closure does not approve P6-P12 entry, P6 data-system work, training, self-play, league, real Tenhou, model-output integration, CLI, broad ingestion, latency measurement, fixed-position exact-match, metric implementation, registry code changes, promotion criteria changes or model-strength claims.
`docs/12_technical_plan/12B_POST_P5_TRANSITION_REVIEW.md` records the post-P5 transition review. It confirms that P5 is closed for the current synthetic/local evaluation groundwork scope and that the project may start only a docs-only task to define P6 data-system scope, entry criteria and first task before implementation.
`docs/02_data_system/02C_P6_DATA_SYSTEM_SCOPE_ENTRY_CRITERIA_AND_FIRST_TASK.md` defines P6 data-system scope, entry criteria, future exit criteria and first next task before implementation. It records that P6 exists to make future replay, feature, label and data-quality work lawful, reproducible and auditable before any supervised learning, RL, search, league or LuckyJ validation work begins. This is docs-only planning evidence: no replay schema code, data ingestion, feature extraction, label generation, dataset reader, CLI, model-output integration, real Tenhou, real haifu, external-log ingestion, platform-data ingestion, training, self-play, league, runner behavior, P7-P12 work or model-strength claim was added. P6 implementation remains closed until a later explicit implementation boundary is approved.
`docs/02_data_system/02A_DATA_SOURCES.md` defines the P6 data-source provenance and rights inventory before replay schema implementation. It records inventory fields, approval-status vocabulary, source-category approvals, required-before-ingestion checks, future evidence requirements, rights/provenance risks and replay-schema implementation boundaries. Project-authored synthetic/local fixtures and repository docs may be used only in their current docs/smoke context; real Tenhou, real haifu, external logs, platform data, accounts, third-party binaries, model weights, model outputs, self-play outputs and league outputs remain unapproved. This inventory is docs-only definition evidence, not ingestion approval, replay schema implementation, P6 implementation approval, model-strength evidence or LuckyJ `10.68` comparison.
`docs/02_data_system/02D_P6_DATA_SOURCE_PROVENANCE_AND_RIGHTS_INVENTORY_REVIEW.md` reviews that inventory before replay schema implementation. The review found no blocker and can close, but P6 implementation, replay schema implementation, source ingestion, feature extraction, label generation and P7-P12 remain closed. This is P6 inventory review evidence only, not source approval, ingestion approval, data-system implementation approval, model-strength evidence or LuckyJ `10.68` comparison.
`docs/02_data_system/02B_REPLAY_SCHEMA.md` defines the P6 replay schema documentation boundary after source inventory review. It records allowed documentation scope, forbidden scope, source-inventory dependencies, replay field families, validation expectations, future implementation entry criteria and replay-schema risks. This is P6 replay schema documentation boundary definition evidence only: P6 implementation, replay schema implementation, source ingestion, feature extraction, label generation and P7-P12 remain closed.
`docs/02_data_system/02E_P6_REPLAY_SCHEMA_DOCUMENTATION_BOUNDARY_REVIEW.md` reviews the P6 replay schema documentation boundary before implementation. The review found no blocker and can close, but P6 implementation, replay schema implementation, source ingestion, data ingestion, dataset readers, feature extraction, label generation and P7-P12 remain closed. This is P6 replay schema documentation boundary review evidence only, not source approval, ingestion approval, schema implementation, data-system implementation approval, model-strength evidence or LuckyJ `10.68` comparison.
`docs/02_data_system/02F_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY.md` defines the P6 synthetic/local replay fixture boundary before schema implementation. It records project-authored and repo-local fixture requirements, allowed and forbidden fixture-boundary scope, source/provenance dependencies, replay field-family alignment, future shape families, future implementation entry criteria, validation expectations and fixture risks. This is docs-only boundary definition evidence: fixture implementation, replay schema implementation, data ingestion, dataset readers, feature extraction, label generation and P7-P12 remain closed.
`docs/02_data_system/02G_P6_SYNTHETIC_LOCAL_REPLAY_FIXTURE_BOUNDARY_REVIEW.md` reviews the P6 synthetic/local replay fixture boundary and records that the review can close with no blocker, but fixture implementation remains closed. P6 implementation, replay schema implementation, replay fixture implementation, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
`docs/02_data_system/02H_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST.md` defines the P6 replay schema and fixture implementation readiness checklist before code. It records candidate implementation classes, replay schema code readiness, synthetic/local replay fixture readiness, parser/dataset reader readiness, feature/label readiness, data-ingestion readiness, decision vocabulary, dependency map, P7-P12 non-entry boundaries and risks. This is checklist-definition evidence only: P6 implementation, replay schema implementation, fixture implementation, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
`docs/02_data_system/02I_P6_REPLAY_SCHEMA_AND_FIXTURE_IMPLEMENTATION_READINESS_CHECKLIST_REVIEW.md` reviews the P6 replay schema and fixture implementation readiness checklist before code. The review found no blocker and can close, but P6 implementation, replay schema implementation, fixture implementation, data ingestion, dataset readers, parsers, feature extraction, label generation and P7-P12 remain unapproved.
The next project task is to define the P6 replay schema and synthetic fixture implementation proposal boundary before code. That task must remain docs-only and must not implement fixture files, replay schema code, data ingestion, feature extraction, label generation, model-output integration, CLI, broad file ingestion, training, self-play, league, real Tenhou, external-log ingestion, platform-data ingestion, P7-P12 work or model-strength claims.
```

## Current methodology

The project uses a strict local Codex workflow:

```text
1. Load rules first.
2. Execute only the first unchecked task in docs/10_next/10_NEXT.md.
3. Do not skip stages.
4. Do not train or modify code unless the current task explicitly asks for it.
5. After each real task, update changelog, evidence/risk notes when needed, handoff and 10_NEXT.
```

Current execution charter:

```text
docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md
```

Role split:

- Web ChatGPT Pro: solution design, research, review and decision support.
- Local Codex App: code, tests and documentation landing.
- Git + docs: only source of truth.

## Algorithm selection stance

Current interpretation:

```text
Do not fully train every candidate algorithm.
Use a racing funnel:
F0 candidate registration
F1 reproducibility audit
F2 interface/legal-action adapter
F3 offline scenario evaluation
F4 small self-play league
F5 medium promotion league
F6 mainline candidate gate
F7 LuckyJ target validation
```

Roles:

- LuckyJ: final benchmark target, not implementation seed.
- Suphx: main methodology blueprint, split into reproducible modules.
- Mortal: paused as a runnable baseline; retained as source-code, mjai-interface, methodology and engineering reference.
- Archer: high-potential Tenhou baseline candidate requiring verification.
- Akochan: secondary baseline/reviewer candidate; F1 Conditional Pass on Ubuntu GitHub Actions; F2 fixed-sample wrapper validation passed through real-exe workflow run `26629344590`. It remains an interface/reviewer candidate, not a strength baseline. Any broader evaluator/reviewer integration must be a separate task with license boundary review.
- Kanachan: data/model architecture reference; not direct Tenhou baseline until adapted.

Main technical route:

```text
Suphx-style SL + RL
+ Tenhou stable dan / pt EV reward
+ ACH-inspired policy improvement
+ risk model / search
+ baseline racing funnel
```

LuckyJ remains the target benchmark, not a direct full-reproduction object.

## Current next task

See:

```text
docs/10_next/10_NEXT.md
```

Latest Mortal F1 audit summary:

- GitHub connector could inspect `Equim-chan/Mortal` at commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
- License is AGPL-3.0-or-later for code.
- Official inference path is mjai/Docker-oriented and requires a separate trained model artifact.
- System DNS still cannot resolve GitHub domains, but Mortal source tarball was obtained through `codeload.github.com` with explicit host resolution and checksum `6531f46ba2f2b40a69528bf5362f9c89294ad72521aec4f59e208400c379e62c`.
- Normal `git clone` still failed; local `rustc`, `cargo`, `docker`, `conda` and PyTorch were not available.
- Official gist evidence says there is currently no plan to release trained model parameters.
- Minimal inference sample was not run; Mortal must remain at F1 Reproduce blocked.
- Current project decision: because there is no lawful, verifiable and usable Mortal trained model artifact, Mortal is paused as a runnable baseline.
- Do not use unknown `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` files.
- Mortal remains useful as source-code, mjai-interface, methodology and engineering reference.

Current expected direction:

```text
Define P6 replay schema and synthetic fixture implementation proposal boundary
before code. Do not execute P6 implementation directly. Do not expand into
replay schema code, replay fixture implementation, data ingestion, dataset
readers, parsers, feature extraction, label generation, training, self-play,
league evaluation, Tenhou integration, artifact upload, broad adapter work,
CLI, broad file ingestion, model-output integration, latency measurement,
fixed-position exact-match computation, metric implementation, registry code
changes, promotion criteria changes, P7-P12 or model-strength claims without a
later explicit implementation approval.
```

Latest Akochan F1 audit summary:

- GitHub repository `critter-mj/akochan` is public and inspectable.
- Clone URL: `https://github.com/critter-mj/akochan.git`.
- Default branch: `master`.
- Audited commit: `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Normal `git clone` failed because local DNS could not resolve `github.com`; clone with explicit `http.curloptResolve` succeeded in `/tmp/mjlabai_akochan_audit_20260529_084246`.
- License is a custom Japanese usage agreement, not a standard OSI license. Private research audit is allowed, but redistribution, AI-part modification, commercial use and public release are restricted and need review/permission.
- Build path is C++11 Makefile-based: build `ai_src` into `libai.so`, then root into `system.exe`.
- Dependencies include g++/clang++, OpenMP, Boost.System/Boost.Asio, pthread on Linux, Homebrew LLVM/Boost on macOS and repository-included `params/` text files.
- No external neural-network `*.pth`/`*.pt`/checkpoint/snapshot artifact was detected; 709 text parameter files are included under `params/`.
- Source exposes promising `mjai_log`, `stats_mjai`, `game_server`, `legal_action`, `legal_action_log_all`, `pipe`, `pipe_detailed` and `mjai_client` entry points.
- Local macOS ARM build failed: MacOS Makefile expects `/opt/homebrew/opt/llvm/bin/clang++`; Linux Makefile is incompatible with this macOS target due `/proc/cpuinfo`, `-mcmodel=medium` and `-fopenmp`.
- `mjai` CLI was not installed.
- No `system.exe` was produced, so minimal run was not executed.
- F1 conclusion: Blocked.

Latest Akochan F1 blocker-resolution attempt:

- Docker is not installed: `docker: command not found`.
- Host is macOS 26.2 / Darwin 25.2.0 on arm64.
- `/usr/bin/g++`, `/usr/bin/clang++` and `/usr/bin/make` exist, but `g++`/`clang++` are Apple clang 21.0.0.
- Homebrew exists, but usable Boost, LLVM and OpenMP/libomp files were not present under the expected `/opt/homebrew/opt/*` paths.
- Akochan was cloned outside the repository to `/tmp/mjlabai_akochan_build_audit` and checked out at `53188a0b926fbab38177f88c3cd87d554cf412af`.
- `make -f Makefile_MacOS` in `ai_src` failed because `/opt/homebrew/opt/llvm/bin/clang++` was missing.
- `make -f Makefile_Linux` in `ai_src` failed because `/proc/cpuinfo` is absent on macOS and Apple clang rejected `-mcmodel=medium` and `-fopenmp`.
- Root Makefile attempts failed for the same missing LLVM / unsupported OpenMP reasons.
- No `libai.so` or `system.exe` was generated, so no minimal `legal_action`, `legal_action_log_all`, `mjai_log` or `stats_mjai` sample was run.
- F1 conclusion remains: Blocked.

GitHub Actions support added:

- Added `.github/workflows/akochan-f1-build-audit.yml`.
- Workflow name: `Akochan F1 Build Audit`.
- Trigger: manual `workflow_dispatch` only.
- Inputs:
  - `akochan_commit`, default `53188a0b926fbab38177f88c3cd87d554cf412af`.
  - `run_minimal_samples`, default `true`.
- Runner: `ubuntu-latest`.
- The workflow installs Ubuntu build dependencies inside the temporary runner, clones `critter-mj/akochan` into the runner temp directory, checks out the requested commit, attempts `cd ai_src && make -f Makefile_Linux` and then `make -f Makefile_Linux` at the root.
- If `system.exe` is generated and `run_minimal_samples` is true, it runs only minimal non-training samples: `legal_action` and `mjai_log haifu_log_sample.json 0 2`.
- The workflow does not upload third-party source, `system.exe`, binaries or build artifacts.
- This workflow support entry was superseded by successful run `26617347785`, which moved Akochan to F1 Conditional Pass.

First GitHub Actions run review:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26615920289`.
- Result: failed during GitHub workflow validation before any Ubuntu runner build started.
- Cause: `.github/workflows/akochan-f1-build-audit.yml` used `runner.temp` inside job-level `env`, which GitHub did not accept at lines 27 and 28.
- Local fix: `AKOCHAN_DIR` and `SUMMARY_FILE` are now configured in a runtime shell step via `$GITHUB_ENV`; the final summary step has a fallback if the summary file was not created.
- Evidence impact: no `system.exe`, `legal_action` or `mjai_log` evidence was produced by the failed run. Akochan remains F1 Blocked.

Corrected GitHub Actions run review:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26617347785`.
- Commit: `b6b69e08fd009052cb3bbd16c779ac6e2139591b`.
- Result: success on `ubuntu-latest`.
- Generated: `ai_src/libai.so`, root `libai.so` and `system.exe`.
- Minimal samples:
  - `legal_action`: success; emitted legal `dahai` JSON actions.
  - `mjai_log haifu_log_sample.json 0 2`: success; emitted parsed mjai/log JSON output.
- Guardrails: no training, tuning, self-play, Tenhou connection, adapter work, artifact upload or third-party vendoring.
- New risk note: GitHub emitted a Node.js 20 deprecation warning for `actions/checkout@v4`; this is workflow maintenance risk, not an Akochan F1 blocker.
- F1 conclusion: Conditional Pass. Akochan can move to F2 task definition, but custom license limits and Ubuntu-only build evidence must remain documented.

Akochan F2 task definition:

- Added `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`.
- Defined Akochan roles for F2: legal-action checker, mjai/log reviewer and baseline/reviewer candidate.
- Defined the interface boundary: Akochan source, `system.exe`, `libai.so`, `params/` and third-party build artifacts must not enter this repository.
- Future wrapper should call an external path or a GitHub Actions temporary build path.
- Defined draft mapping for mjai events: `start_game`, `start_kyoku`, `tsumo`, `dahai`, `chi`, `pon`, `kan`, `reach`, `hora`, `ryukyoku`, `end_kyoku`.
- Defined draft normalized internal action schema for `legal_action` outputs.
- Defined mandatory audit-log fields: tool name, external repo/commit, build environment, command, input/output hashes, exit code, stdout/stderr summaries, elapsed time and flags proving no training/self-play/Tenhou command was run.
- Reaffirmed license guardrails: private/internal audit only; no source modification, redistribution, commercial use or public release without review/permission.
- No adapter code was written in the F2 definition task.

Akochan F2 wrapper skeleton:

- Added a minimal Python package under `src/mjlabai`.
- Implemented `AkochanWrapper.run_legal_action(input_json)` and `AkochanWrapper.run_mjai_log(log_path, actor=0, mode=2)`.
- The wrapper accepts a real external `system.exe` path only through an explicit constructor argument or `AKOCHAN_SYSTEM_EXE`.
- The wrapper exposes only the two fixed subcommands: `legal_action` and `mjai_log`; it does not provide free-form command execution.
- Added audit-log dataclasses with required fields: tool name, external repo/commit, build environment, command, input/output hashes, exit code, stdout/stderr summaries, elapsed time and explicit no-training/no-self-play/no-Tenhou flags.
- Added a synthetic fixed `legal_action` fixture and a tiny synthetic mjai-log fixture.
- Added `tests/fixtures/akochan/fake_system_exe.py` as a test substitute only. It is not Akochan and is not model-strength evidence.
- Local smoke test `python3 -m unittest tests/adapters/test_akochan_wrapper.py` passed 14 tests after the allowlisted mixed stdout parser fix.
- No Akochan source, `system.exe`, `libai.so`, `params/`, third-party binary, unknown model artifact or build artifact was stored in this repository.

Akochan F2 fixed-sample real-exe wrapper validation closeout:

- Workflow: `Akochan F2 Wrapper Real Exe Audit`.
- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26629344590`.
- Commit: `29f5e1ed19407d169f85524e05438ac8938d2dc2`.
- Commit message: `Support Akochan mixed stdout parsing`.
- Result: success.
- Job result: success.
- Successful evidence:
  - Ubuntu runner built `ai_src/libai.so`.
  - Ubuntu runner built root `libai.so`.
  - Ubuntu runner built `system.exe`.
  - Fake wrapper tests passed 14 tests.
  - Real `system.exe legal_action` wrapper test passed.
  - Real `system.exe mjai_log` wrapper test passed.
  - Allowlisted mixed stdout parser was verified by the real workflow.
- Guardrails:
  - No training.
  - No tuning.
  - No self-play, match or league command.
  - No real Tenhou connection.
  - No Akochan source, `system.exe`, `libai.so`, `params/`, third-party binary or build artifact was stored or uploaded.
- Interpretation:
  - Akochan status is F1 Conditional Pass plus F2 fixed-sample wrapper validation passed.
  - This is not playing-strength evidence.
  - This does not make Akochan a mainline baseline or prove mjlabai strength.
  - Akochan custom license still restricts modification, redistribution, commercial use and public release.
  - GitHub Actions reported a Node.js 20 deprecation warning; this is workflow maintenance risk and does not affect the F2 validation result.

Akochan F2 real executable validation path:

- Added `.github/workflows/akochan-f2-wrapper-real-exe-audit.yml`.
- Workflow name: `Akochan F2 Wrapper Real Exe Audit`.
- Trigger: manual `workflow_dispatch` only.
- Input:
  - `akochan_commit`, default `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Runner: `ubuntu-latest`.
- The workflow checks out mjlabai, installs Ubuntu build dependencies, clones `critter-mj/akochan` into the runner temporary directory, checks out the fixed commit, builds `ai_src/libai.so`, root `libai.so` and `system.exe`, installs mjlabai with `python -m pip install -e .`, then runs both fake wrapper tests and real-executable wrapper tests.
- Added `tests/adapters/test_akochan_wrapper_real_exe.py`.
- Real-executable tests skip locally unless `AKOCHAN_SYSTEM_EXE` is set. The `mjai_log` test also requires `AKOCHAN_MJAI_LOG_SAMPLE`.
- Local validation:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed after the allowlisted mixed stdout parser fix.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped, as expected without a real external executable.
- The wrapper parser now supports single JSON values, JSON Lines, concatenated JSON values, pretty-printed multi-record JSON streams and mixed stdout with the single allowlisted status line `calculating review`.
- The parser preserves `raw_stdout`, exposes `parsed_records`, records `parse_warnings` and `skipped_non_json_lines`, and rejects unknown non-JSON lines or partial parses.
- First workflow run `26621536548` was run and reviewed; it failed only at the real `mjai_log` wrapper test because `system.exe` could not load `setup_mjai.json` from the current working directory.
- Working-directory fix has been implemented locally:
  - `AkochanWrapper` supports explicit `working_dir`, then `AKOCHAN_WORKING_DIR`, then defaults to `Path(system_exe).resolve().parent`.
  - `_run_subcommand` passes `cwd=self.working_dir` to `subprocess.run`.
  - `AkochanAuditLog` records `working_dir`.
  - Fake tests verify default, explicit and environment-variable working-directory behavior.
  - The workflow now exports `AKOCHAN_WORKING_DIR=${AKOCHAN_DIR}` before real-exe tests.
- The workflow does not upload artifacts; any Akochan clone/build output remains in the temporary GitHub runner.

First Akochan F2 real executable workflow run:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26621536548`.
- Commit: `7d58f969367d3e51c57d859dbfb9433f1ca898a1`.
- Result: failure.
- Successful evidence:
  - Akochan source cloned at `53188a0b926fbab38177f88c3cd87d554cf412af`.
  - `ai_src/libai.so`, root `libai.so` and `system.exe` built successfully.
  - Fake wrapper smoke tests passed.
  - Real `legal_action` wrapper test passed.
- Failed evidence:
  - Real `mjai_log` wrapper test failed.
- Failure detail:
  - `AkochanWrapperError: Akochan command failed with exit code -6: error:load_json_from_file setup_mjai.json`.
  - `system.exe` asserted while loading `setup_mjai.json`.
- Interpretation:
  - The wrapper called external `system.exe` from the mjlabai checkout working directory.
  - Akochan expects runtime config files such as `setup_mjai.json` to be visible from the process working directory.
  - Next fix should set the subprocess working directory to the executable directory or an explicitly provided external working directory.
- Evidence status:
  - This is real `legal_action` wrapper compatibility evidence.
  - This is not successful real `mjai_log` wrapper compatibility evidence.
  - This is not strength evidence.

Akochan F2 working-directory fix:

- Wrapper behavior:
  - Constructor priority is explicit `working_dir`, then `AKOCHAN_WORKING_DIR`, then `Path(system_exe).resolve().parent`.
  - Missing or non-directory working directories fail with a clear error.
  - The external subprocess is launched with `cwd=self.working_dir`.
  - Audit logs include the actual `working_dir`.
- Test behavior:
  - `fake_system_exe.py` now requires a synthetic `fake_setup_mjai.json` in cwd for `mjai_log`, proving the cwd boundary is exercised.
  - Local fake tests passed 8 tests.
  - Local real-exe tests skipped 2 tests as expected without real Akochan.
- Current evidence gap:
  - Workflow run `26623247276` confirmed `AKOCHAN_WORKING_DIR` removes the `setup_mjai.json` failure.
  - The first parser blocker was improved locally, but workflow run `26628128871` exposed the known `calculating review` status line.

Second Akochan F2 real executable workflow run:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26623247276`.
- Commit: `0ddb28575ddd1b624cad34b20d6dc6b79303963c`.
- Result: failure.
- Successful evidence:
  - Akochan source cloned at `53188a0b926fbab38177f88c3cd87d554cf412af`.
  - `ai_src/libai.so`, root `libai.so` and `system.exe` built successfully.
  - Fake wrapper smoke tests passed 8 tests.
  - `AKOCHAN_SYSTEM_EXE`, `AKOCHAN_WORKING_DIR` and `AKOCHAN_MJAI_LOG_SAMPLE` were configured.
  - Real `legal_action` wrapper test passed.
  - Real `mjai_log` no longer failed on `setup_mjai.json`.
- Failed evidence:
  - Real `mjai_log` wrapper test failed while parsing stdout.
- Failure detail:
  - `AkochanOutputParseError: Akochan stdout was not parseable JSON or JSON Lines: Extra data: line 2 column 1`.
- Interpretation:
  - The cwd/runtime-file blocker is mitigated.
  - The next issue is understanding and parsing the real multi-record `mjai_log` stdout shape while preserving raw output and bounded summaries.
- Evidence status:
  - This is real `legal_action` compatibility evidence and cwd-fix evidence.
  - This is not successful real `mjai_log` wrapper compatibility evidence.
  - This is not strength evidence.

Akochan F2 strict JSON stream parser fix:

- Parser behavior:
  - single JSON value returns that value with `parsed_records=[value]`;
  - JSON Lines and concatenated/pretty multi-record JSON streams return `parsed_json=records` and `parsed_records=records`;
  - any non-whitespace non-JSON residue fails instead of being accepted as a partial parse.
- Diagnostics:
  - parse failures include bounded stdout summary, stdout SHA256, failure position and parsed-record count.
- Local tests:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 12 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Current evidence gap:
  - Workflow run `26628128871` must be interpreted before real `mjai_log` compatibility can be closed.

Third Akochan F2 real executable workflow run:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26628128871`.
- Commit: `9f51aff1ab403e8053ab71fe1db7587bf7af01cf`.
- Result: failure.
- Successful evidence:
  - Ubuntu runner built `ai_src/libai.so`, root `libai.so` and `system.exe`.
  - Fake wrapper tests passed 12 tests.
  - Real `legal_action` wrapper test passed.
  - Real `mjai_log` launched with `AKOCHAN_WORKING_DIR` and produced parseable JSON records before the status line.
- Failed evidence:
  - Real `mjai_log` wrapper test failed on mixed stdout containing JSON records, then `calculating review`, then JSON review output.
- Interpretation:
  - Strict JSON stream support is not enough for real `mjai_log`.
  - The parser may skip only the exact known status line `calculating review`, record that skip, and continue strict JSON stream parsing.
  - Unknown non-JSON lines and partial parses must remain failures.

Akochan F2 allowlisted mixed stdout parser fix:

- Parser behavior:
  - single JSON value returns that value with `parsed_records=[value]`;
  - JSON Lines and concatenated/pretty multi-record JSON streams return `parsed_json=records` and `parsed_records=records`;
  - mixed stdout may skip only the exact non-JSON status line `calculating review`;
  - `skipped_non_json_lines` records skipped allowlisted lines;
  - unknown non-JSON residue and partial parses still fail.
- Diagnostics:
  - parse failures include bounded stdout summary, stdout SHA256, failure position, parsed-record count and skipped-status-line count.
- Local tests:
  - `python3 -m unittest tests/adapters/test_akochan_wrapper.py`: 14 tests passed.
  - `python3 -m unittest tests/adapters/test_akochan_wrapper_real_exe.py`: 2 tests skipped as expected without real Akochan.
- Real workflow validation:
  - Workflow run `26629344590` verified real `legal_action` and real `mjai_log` wrapper tests both pass after allowlisted mixed stdout parser support.

Fourth Akochan F2 real executable workflow run:

- Run URL: `https://github.com/z2labplus/mjlabai/actions/runs/26629344590`.
- Commit: `29f5e1ed19407d169f85524e05438ac8938d2dc2`.
- Result: success.
- Successful evidence:
  - Ubuntu runner built `ai_src/libai.so`.
  - Ubuntu runner built root `libai.so`.
  - Ubuntu runner built `system.exe`.
  - Fake wrapper tests passed 14 tests.
  - Real `legal_action` wrapper test passed.
  - Real `mjai_log` wrapper test passed.
- Interpretation:
  - Akochan F2 fixed-sample real-exe wrapper validation is complete.
  - This is fixed-sample integration evidence only, not strength evidence.
  - Further evaluator/reviewer integration must be a separate scoped task with license guardrails.

## Do not forget

- The final metric is not loss.
- The final metric is not action prediction accuracy.
- The final metric is Tenhou-like strength: stable dan, pt EV, average placement and fourth-place control.
- No candidate can be promoted without evidence and a rollback path.
- Current next work is a P6 data-system docs-only replay schema and synthetic
  fixture implementation proposal boundary definition: do not implement fixture
  files, replay schema code, ingest data, train, tune, self-play or connect to
  real Tenhou.
- Technical decisions from Web ChatGPT Pro must be written into Git + docs before becoming project facts.
