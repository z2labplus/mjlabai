# 04F_ALGORITHM_CANDIDATE_TABLE

North star: find the route most likely to produce a Tenhou AI with stable dan greater than LuckyJ 10.68.

## Candidate table fields

Use this table for every candidate algorithm or framework.

| Field | Meaning |
|---|---|
| Candidate | Name of algorithm/system/framework. |
| Type | Research paper, closed system, open-source baseline, framework, evaluation reference. |
| Core idea | The method we might reuse. |
| Public strength evidence | Tenhou dan/stable dan, benchmark, self-play result, paper result, or repo claim. |
| Fit to Tenhou target | High/Medium/Low. Does it optimize Tenhou-like rank and four-player riichi? |
| Reproducibility | High/Medium/Low. Can local Codex build or inspect it? |
| Data dependency | Tenhou logs, Mahjong Soul logs, self-play, expert logs, unknown. |
| Compute dependency | Local CPU/GPU, single GPU, multi-GPU, cluster-scale, unknown. |
| Key risk | Main reason it may fail or mislead us. |
| Minimal experiment | Smallest useful experiment to test it. |
| Gate decision | Watch / Baseline / Mainline candidate / Reject. |

## Initial candidate table

| Candidate | Type | Core idea | Public strength evidence | Fit | Reproducibility | Minimal experiment | Initial decision |
|---|---|---|---|---|---|---|---|
| LuckyJ | Closed target system | Tencent Mahjong AI; likely uses advanced imperfect-information RL ideas including ACH-related work. | Reported Tenhou 10 dan and stable rank 10.68. | High | Low | Use as target benchmark; collect all public metrics and table of required surpass conditions. | Target to beat, not implementation seed. |
| Suphx | Research system | SL foundation + self-play RL + global reward prediction + oracle guiding + optional run-time policy adaptation. | Reported Tenhou 10 dan and stable rank 8.74; low fourth-place and deal-in rates. | High | Medium | Reproduce the training/eval decomposition: SL policy, Tenhou stable-dan estimator, GRP, oracle-guided ablation. | Main research route. |
| Mortal | Open-source baseline / reference | Fast Rust riichi AI powered by deep RL; mjai-compatible ecosystem. | Public open-source project; usable for review/play tools, but no lawful, verifiable and usable trained model artifact is currently available. | Medium-High | Low for runnable baseline; Medium as source reference | Keep as source-code, mjai-interface, methodology and engineering reference. Re-open F1 only if a lawful artifact with version/tag, usage constraints and checksum is provided. | Paused as runnable baseline; reference only. |
| Akochan | Open-source baseline / reviewer candidate | C++ Japanese Mahjong AI with self-match, JSON/mjai/log review and legal-action related components. | Public repo; Ubuntu GitHub Actions F1 run generated `system.exe` and passed minimal `legal_action` plus `mjai_log` samples. | Medium | Medium-High for Ubuntu build/minimal-run; Low for local macOS build | Implement minimal F2 wrapper skeleton for fixed `legal_action` / `mjai_log` samples under the documented no-vendor, no-training, no-Tenhou constraints. | F2 task defined; wrapper skeleton next. |
| Kanachan | Open-source framework | Mahjong Soul-oriented data/annotation/training framework; emphasizes large-scale data and expressive models. | Public repo targets beating NAGA/Suphx; designed around Mahjong Soul records. | Medium | Medium | Inspect schema, convert concepts to Tenhou-compatible feature/training design. | Research reference, not direct Tenhou baseline yet. |
| Archer | Open-source/development framework | Top-tier Mahjong AI framework with Tenhou/Majsoul tooling focus. | Repo claims reaching Tenhou 10 dan on Phoenix. | High | Medium | Build or inspect release; check whether evaluation logs/weights/protocol are reproducible. | Baseline candidate after verification. |

## Scoring rubric

Each candidate receives 0-5 points in each dimension.

| Dimension | Weight | 5 means |
|---|---:|---|
| Tenhou target fit | 25% | Directly optimizes four-player Tenhou-style rank/stable dan. |
| Strength evidence | 20% | Has high-sample, credible Tenhou or equivalent benchmark evidence. |
| Reproducibility | 20% | Can be built, run, inspected and re-tested locally. |
| Transfer value | 15% | Provides reusable algorithmic ideas for our main system. |
| Engineering cost | 10% | Low integration cost into our local pipeline. |
| Risk control | 10% | Low licensing, compliance, data, and overfitting risk. |

Promotion score:

```text
score = 0.25*TenhouFit + 0.20*StrengthEvidence + 0.20*Reproducibility
      + 0.15*TransferValue + 0.10*EngineeringCost + 0.10*RiskControl
```

## Current priority order

1. Complete P3/F1 reproducibility audits before adapter, training or evaluation-harness implementation.
2. Implement minimal Akochan F2 wrapper skeleton for fixed `legal_action` / `mjai_log` samples under the documented guardrails.
3. Use Suphx as the main algorithmic blueprint.
4. Use LuckyJ as the target threshold.
5. Verify Archer claim before depending on it.
6. Keep Mortal as source-code, mjai-interface, methodology and engineering reference unless a lawful trained model artifact re-opens F1.
7. Use Kanachan as a comparative data/model reference.

## Do not do

- Do not choose an algorithm because it sounds advanced.
- Do not compare algorithms using different environments.
- Do not accept Tenhou rank claims without sample size, room, rules, and reproducibility notes.
- Do not let action-prediction accuracy override stable dan, pt EV, average placement, or fourth-place control.

## v0.4 Funnel-stage assignment

赛马漏斗机制要求：**不是完整训练所有算法，而是分阶段筛选**。

| Candidate | Current funnel stage | Next lowest-cost action | Reason |
|---|---|---|---|
| LuckyJ | Target line | 固定 10.68 稳定段位作为验收线；继续补证据。 | 它是要超过的目标，不是实现起点。 |
| Suphx | Methodology blueprint / ReferenceOnly + module decomposition | 把 GRP、oracle guiding、runtime adaptation 拆成可复现实验卡。 | 公开方法价值高，但不能直接作为本地 baseline。 |
| Mortal | F1 paused as runnable baseline / ReferenceOnly | 不使用来路不明的 `mortal.pth`、`*.pth`、`*.pt`、`checkpoint` 或 `snapshot`。只有在提供合法、可校验、可使用且记录 version/tag、usage constraints 和 checksum 的 trained model artifact 后，才可重新打开 F1。 | 源码 tarball 已获取并校验，但没有可用 trained model artifact；Mortal 仅保留为源码、mjai 接口、方法论和工程参考，不得推进 F2。 |
| Archer | Watch -> Reproduce | 验证 Tenhou 10 dan claim、build、weights、日志和协议。 | 潜在价值高，但证据和复现性需要先核验。 |
| Akochan | F2 task defined | 实现最小 F2 wrapper skeleton，只针对固定 `legal_action` / `mjai_log` 样例，遵守 no-vendor、no-training、no-Tenhou 约束。 | F1 Conditional Pass 已有 Ubuntu GitHub Actions run `26617347785` 证据；`07J_AKOCHAN_F2_INTERFACE_TASK.md` 已定义 wrapper-only 边界、状态/动作映射、日志 schema 与 license guardrails。 |
| Kanachan | Watch / ReferenceOnly | 研究 schema、数据流程、模型结构能否迁移到 Tenhou。 | 更偏 Mahjong Soul 与大数据/模型工程参考。 |

## v0.4 Resource rule

```text
F0/F1/F2 通过之前，不给任何候选大规模训练资源。
F3/F4 通过之前，不进入主线开发。
F5/F6 通过之前，不声称超过 LuckyJ。
```

## 2026-05-28 Mortal F1 audit result

Mortal remains the first local baseline candidate, but F1 is not complete.

Observed facts:

- Repository metadata and selected files were accessible through the GitHub connector at `Equim-chan/Mortal`.
- Current checked commit: `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
- Code license: AGPL-3.0-or-later; logo/assets: CC BY-SA 4.0.
- Project shape: Rust workspace with `libriichi` and `exe-wrapper`, plus Python inference code under `mortal/`.
- Official build path requires Python, Rust/Cargo, PyTorch, and building `libriichi`.
- Official inference path uses a Docker/mjai flow and requires a trained model file prepared separately.
- Input/output fit looks promising: Mortal consumes newline-separated mjai JSON events and emits mjai-style JSON reactions, with optional `meta` fields such as q-values, mask bits, shanten and evaluation time.

Local F1 checks:

| Check | Result |
|---|---|
| Source clone by shell | Failed: local shell could not resolve `github.com`. |
| Rust/Cargo availability | Failed: `rustc` and `cargo` were not found. |
| Docker availability | Failed: `docker` was not found. |
| Conda availability | Failed: `conda` was not found. |
| Python availability | Present: Python 3.9.6, but official environment asks for Python 3.12 and PyTorch is missing. |
| Minimal inference sample | Not run: blocked by source clone, runtime dependencies and missing model artifact. |

Decision:

```text
Mortal does not pass F1 yet.
Keep Mortal at F1 Reproduce blocked.
Next lowest-cost action: fix local source/toolchain/model-artifact blockers and rerun the official mjai minimal inference sample.
```

## 2026-05-28 Mortal F1 blocker-resolution attempt

Additional result:

- Source tarball for commit `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2` was downloaded from `codeload.github.com` using explicit host resolution.
- Source tarball SHA256: `6531f46ba2f2b40a69528bf5362f9c89294ad72521aec4f59e208400c379e62c`.
- `git ls-remote` can work with `http.curloptResolve`, but normal `git clone` still failed due connection/DNS path instability.
- Homebrew is available, but `brew info rust` failed while fetching `https://formulae.brew.sh/api/formula/rust.json` because `formulae.brew.sh` could not be resolved.
- Python 3.12 is available and a venv can be created, but PyTorch is not installed.
- The README-linked gist says there is currently no plan to release trained model parameters.
- No Mortal trained model artifact was obtained, so no model version/tag/license/checksum could be recorded.

Decision remains:

```text
Mortal F1 is blocked.
Do not promote Mortal to F2.
The next decision is whether a lawful trained Mortal model artifact can be provided.
If not, Mortal should be paused as a runnable baseline and the next F1 audit should move to another baseline such as Akochan.
```

## 2026-05-29 Mortal F1 continuation decision

Decision:

```text
No lawful, verifiable and usable Mortal trained model artifact is currently available.
Mortal is paused as a runnable baseline.
Mortal remains a source-code, mjai-interface, methodology and engineering reference.
The next baseline F1 path moves to Akochan reproducibility audit.
```

Artifact rule:

```text
Do not use unknown mortal.pth, *.pth, *.pt, checkpoint or snapshot files.
Any future Mortal artifact must record source, version/tag, usage constraints and checksum before F1 can be re-opened.
```

Consequence:

```text
Do not promote Mortal to F2.
Do not start an adapter for Mortal.
Do not claim Mortal runnable strength in this project.
Run Akochan F1 only as the next separate task.
```

## 2026-05-29 Akochan F1 audit result

Akochan F1 conclusion:

```text
Blocked
```

Observed facts:

- Repository: `critter-mj/akochan`.
- URL: `https://github.com/critter-mj/akochan`.
- Default branch: `master`.
- Audited commit: `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Repository is public and inspectable.
- Normal `git clone` failed due local DNS resolution for `github.com`; explicit host-resolution clone succeeded in `/tmp/mjlabai_akochan_audit_20260529_084246`.
- License is a custom Japanese usage agreement. Private research audit is allowed, but redistribution, AI-part modification, commercial use and public release are restricted.
- Build path is C++11 Makefile-based: `ai_src` builds `libai.so`, then root builds `system.exe`.
- Dependencies include g++/clang++, OpenMP, Boost.System/Boost.Asio, pthread on Linux, Homebrew LLVM/Boost on macOS and repository-included `params/`.
- No external neural-network weights were detected; `params/` contains 709 tracked text parameter files.
- Source exposes `mjai_log`, `stats_mjai`, `game_server`, `legal_action`, `legal_action_log_all`, `pipe`, `pipe_detailed` and `mjai_client`.
- Local build failed on macOS ARM:
  - `make -f Makefile_MacOS` failed because `/opt/homebrew/opt/llvm/bin/clang++` was missing.
  - `make -f Makefile_Linux` failed because `/proc/cpuinfo` is absent and Apple clang rejected `-mcmodel=medium` and `-fopenmp`.
- No `system.exe` was produced, so no minimal run was executed.

Decision:

```text
Do not promote Akochan to F2 yet.
Resolve build/toolchain blocker and rerun build plus minimal legal_action and/or mjai_log sample.
```

## 2026-05-29 Akochan F1 blocker-resolution attempt

Conclusion remains:

```text
Blocked
```

New blocker detail:

```text
Docker is not installed.
Native Linux is unavailable.
macOS Homebrew build path lacks usable LLVM/Boost/OpenMP files.
No libai.so or system.exe was generated.
No minimal legal_action / legal_action_log_all / mjai_log / stats_mjai sample was run.
```

Next lowest-cost action:

```text
Provide a supported build environment with Docker Linux or verified local LLVM/Boost/OpenMP,
then rebuild Akochan and run minimal legal_action and/or mjai_log sample.
```

## 2026-05-29 Akochan F1 GitHub Actions build/minimal-run result

Conclusion:

```text
Conditional Pass
```

Evidence:

- Workflow run: `https://github.com/z2labplus/mjlabai/actions/runs/26617347785`.
- mjlabai commit: `b6b69e08fd009052cb3bbd16c779ac6e2139591b`.
- Akochan commit: `53188a0b926fbab38177f88c3cd87d554cf412af`.
- Runner: GitHub-hosted `ubuntu-latest`.
- `cd ai_src && make -f Makefile_Linux`: success.
- `ai_src/libai.so` and root `libai.so`: generated.
- root `make -f Makefile_Linux`: success.
- `system.exe`: generated.
- `legal_action` minimal JSON sample: success.
- `mjai_log haifu_log_sample.json 0 2`: success.

Remaining constraints:

- This is Ubuntu-runner reproducibility evidence; local macOS build remains blocked.
- Akochan has a custom license. Keep current use private/research-only until license review or permission clears broader use.
- This is not strength evidence and does not imply Tenhou performance.

Next lowest-cost action:

```text
Completed by the F2 task definition section below.
```

## 2026-05-29 Akochan F2 interface task definition

Decision:

```text
Akochan F2 task is defined.
No adapter code has been written yet.
```

Primary document:

```text
docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md
```

Defined scope:

- Akochan roles: legal-action checker, mjai/log reviewer and baseline/reviewer candidate.
- Boundary: no Akochan source, `system.exe`, `libai.so`, `params/`, binaries, weights or unknown artifacts enter this repository.
- Future wrapper may call an external path or GitHub Actions temporary build path.
- Draft mjai events: `start_game`, `start_kyoku`, `tsumo`, `dahai`, `chi`, `pon`, `kan`, `reach`, `hora`, `ryukyoku`, `end_kyoku`.
- Future wrapper must preserve raw Akochan output and normalize parseable legal actions.
- Audit log must record command, hashes, exit code, stdout/stderr summaries, elapsed time, license note and no-training/no-self-play/no-Tenhou flags.

Next lowest-cost action:

```text
Implement minimal Akochan F2 wrapper skeleton for fixed legal_action/mjai_log samples under the documented no-vendor, no-training, no-Tenhou constraints.
```
