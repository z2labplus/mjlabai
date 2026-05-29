# 12A_TECHNICAL_PLAN_v0.1

## Purpose

本文件是当前项目执行总纲。

项目从这一版开始采用：

```text
技术方案优先，论文未来总结。
```

含义：

- 技术方案用于指导当前阶段、任务拆分、实验选择、代码落地和评测闭环。
- 论文不是当前执行主线；论文是未来当路线、证据、评测和结论足够稳定之后的成果总结。
- 任何代码、实验、baseline、训练或评测都必须先能说明它如何服务北极星目标。

North-star target:

```text
Train a Japanese riichi mahjong AI whose long-term Tenhou performance exceeds Tencent LuckyJ.
Minimum benchmark: above Tenhou 10 dan and stable dan > 10.68.
```

## Current Stage

当前项目处于：

```text
P3 / baseline reproducibility audit.
Mortal = F1 paused as runnable baseline / ReferenceOnly.
Akochan = F2 wrapper skeleton implemented; real-executable workflow/test path added; manual workflow run pending.
```

本技术方案不改变当前阶段，不允许跳过 Mortal/Akochan/Archer 等 baseline 的 F1/F2 复现与接口审计。

## Role Split

### Web ChatGPT Pro

网页端 ChatGPT Pro 负责高层方案与研究判断：

- 技术方案设计。
- 外部资料调研。
- 候选算法评审。
- 实验路线评审。
- 风险与合规判断。
- 关键技术决策。
- 论文结构和未来成果总结。

网页端输出不能直接替代项目事实。任何网页端结论都必须落到 Git + docs 后，才成为项目事实来源。

### Local Codex App

本地 Codex App 负责本地执行与落地：

- 读取项目规则。
- 执行 `docs/10_next/10_NEXT.md` 的第一项任务。
- 修改代码。
- 运行测试。
- 做本地可复现审计。
- 更新文档。
- 记录 evidence、risk、changelog 和 next。

Codex 不负责跳阶段，不负责无证据声称模型更强，不负责绕过平台规则。

## Source of Truth

唯一事实来源是：

```text
Git + docs
```

具体规则：

- Git worktree 中的文档和代码是当前项目状态。
- 网页端 ChatGPT Pro 的结论只有被 Codex 写入 docs 后才生效。
- 口头讨论、聊天记录、外部网页摘要不能单独作为项目事实。
- 每个技术决策必须写入对应 primary doc，并同步 handoff / changelog / next。
- 外部证据必须进入 `docs/09_governance/09_EVIDENCE_LOG.md`。
- 新风险必须进入 `docs/09_governance/09_RISK_REGISTER.md`。

## Main Technical Route

当前主路线是组合路线，不是单论文完整复现路线：

```text
Suphx-style SL + RL
+ Tenhou stable dan / pt EV reward
+ ACH-inspired policy improvement
+ risk model / search
+ baseline racing funnel
```

解释：

- Suphx-style SL + RL: 使用监督学习建立基础策略，再用自我对弈强化学习提升长期 Tenhou-like 指标。
- Tenhou stable dan / pt EV reward: 奖励与评测必须围绕稳定段位、Tenhou pt EV、平均顺位和四位率控制。
- ACH-inspired policy improvement: 借鉴 Actor-Critic Hedge / regret-minimization-inspired policy improvement 思路，但不得假设可直接迁移到四人 Tenhou。
- risk model / search: 把押引、危险牌、南场避四、Oorasu 排名判断作为后续增强重点。
- baseline racing funnel: Mortal / Archer / Akochan / Kanachan 等候选必须按 F0-F7 漏斗逐级验证。

## LuckyJ Position

LuckyJ 是目标基准，不是直接完整复现对象。

项目对 LuckyJ 的使用方式：

- 固定最低目标线：Tenhou stable dan > 10.68。
- 收集公开指标，定义验收条件。
- 不假设能得到 LuckyJ 实现细节、训练数据、权重或平台流程。
- 不为了复现 LuckyJ 而跳过本地评测、baseline、数据系统和合规边界。

## Execution Rule

Codex 每次只执行：

```text
docs/10_next/10_NEXT.md 的第一项未完成任务。
```

如果网页端或用户提出新方向，先判断它属于哪个阶段、哪个 primary doc、是否应成为新的 `10_NEXT`。不能把新想法直接变成训练、平台接入或大规模实验。

## Update Rule

每次真实任务完成后必须更新：

- `docs/10_next/10_NEXT.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/00_HANDOFF.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`

如果任务产生技术决策，还必须更新：

- `docs/09_governance/09_DECISION_RECORD.md`

如果任务产生代码或实验结果，还必须记录：

- 使用的 commit / version / config。
- 数据来源与许可。
- 模型权重来源、版本、usage constraints 和 checksum。
- 评测规则、样本量、指标和失败案例。

## Current Non-Goals

当前不做：

- 不写训练代码。
- 不下载模型。
- 不接入真实 Tenhou。
- 不创建平台自动化、抓取、账号工具、规避或反检测逻辑。
- 不声称模型超过任何 baseline。
- 不把 LuckyJ 当作可直接复现对象。
- 不跳过 baseline racing funnel。
- 不使用来路不明的 model weights、`*.pth`、`*.pt`、`checkpoint` 或 `snapshot` 文件。
- 不把第三方源码 vendor/copy 进本仓库。
- 不超过 Akochan F2 fixed-sample wrapper 边界；不保存第三方源码、二进制、`params/` 或未知 artifact。

## Current Next Task

当前 `10_NEXT` 的下一步是运行并复审真实外部 `system.exe` 验证 workflow：

```text
Run the manual GitHub Actions workflow `Akochan F2 Wrapper Real Exe Audit` and review whether the wrapper succeeds against real Ubuntu-built system.exe for fixed legal_action/mjai_log samples.
```

Mortal runnable baseline 已暂停，因为当前没有合法、可校验、可使用的 trained model artifact。Mortal 仍保留为源码、mjai 接口、方法论和工程参考。除非未来先补齐 artifact 来源、version/tag、usage constraints 和 checksum 并重新打开 F1，否则不进入 Mortal F2 adapter。

Akochan F1 审计已完成，当前结论为 Conditional Pass：仓库公开且 JSON/mjai/log/legal-action 入口有价值，未发现外部神经网络权重需求；修正后的 GitHub Actions Ubuntu workflow run `26617347785` 成功生成 `libai.so` 和 `system.exe`，并跑通最小 `legal_action` 与 `mjai_log haifu_log_sample.json 0 2` 样例。

Conditional 的原因：Akochan license 是 custom Japanese usage agreement，修改、再分发、商业或公开发布仍需要复审/许可；本机 macOS build 仍未通过，当前可复现证据来自 Ubuntu GitHub Actions runner。

F2 task definition 已写入 `docs/07_development_execution/07J_AKOCHAN_F2_INTERFACE_TASK.md`。最小 wrapper skeleton 已实现，并通过 fake executable smoke tests；该 fake executable 只是测试替身，不是真实 Akochan，也不是强度证据。

真实 external `system.exe` 验证路径已新增：`.github/workflows/akochan-f2-wrapper-real-exe-audit.yml` 会在临时 Ubuntu runner 中构建 Akochan，并用 `tests/adapters/test_akochan_wrapper_real_exe.py` 调用真实 runner-temp `system.exe`。该 workflow 尚未运行，因此目前还没有真实 `system.exe` wrapper 兼容性证据。

下一步允许的范围只包括手动运行该 GitHub Actions workflow，并复审固定 `legal_action` / `mjai_log` 样例是否通过；仍然不训练、不调参、不自我对弈、不接入 Tenhou、不 vendor 或上传第三方源码、二进制、`params/` 或未知 artifact。
