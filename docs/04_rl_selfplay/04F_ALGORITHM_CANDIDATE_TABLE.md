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
| Mortal | Open-source baseline | Fast Rust riichi AI powered by deep RL; mjai-compatible ecosystem. | Public open-source project; usable for review/play tools. | Medium-High | High | Build locally, run fixed log review, run self-play/benchmark adapter. | First local baseline candidate. |
| Akochan | Open-source baseline | C++ Japanese Mahjong AI with self-match workflow and mjai-compatible components. | Public open-source repo; supports self-match against versions. | Medium | Medium | Build locally, run self-match, compare selected positions with Mortal. | Secondary baseline. |
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

1. Build the evaluation harness first.
2. Use Mortal as the first local baseline if it builds cleanly.
3. Use Suphx as the main algorithmic blueprint.
4. Use LuckyJ as the target threshold.
5. Verify Archer claim before depending on it.
6. Use Akochan and Kanachan as comparative references.

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
| Mortal | F1 Reproduce blocked | 如果能提供合法、可记录来源/version/checksum 的 trained model artifact，则继续补 Rust/Cargo/PyTorch 并重跑官方 mjai 样例；否则暂停 Mortal runnable baseline，转向 Akochan F1。 | 源码 tarball 已获取并校验，但官方 gist 表明没有公开模型参数计划；不得推进 F2。 |
| Archer | Watch -> Reproduce | 验证 Tenhou 10 dan claim、build、weights、日志和协议。 | 潜在价值高，但证据和复现性需要先核验。 |
| Akochan | Watch -> Reproduce | 本地构建与 self-match 检查，作为第二 baseline。 | 可作为对照和局面评审工具。 |
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
