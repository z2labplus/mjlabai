# 01G_ALGORITHM_SELECTION_PRINCIPLES

## Purpose

本文件定义“如何寻找符合项目目标的算法”。

项目目标不是追逐最新论文，而是筛选能帮助我们在 Tenhou 长期超过 LuckyJ 10.68 稳定段位的路线。

## Algorithm selection rule

一个算法进入候选池前，必须回答：

```text
它是否直接提升 Tenhou 稳定段位、pt EV、平均顺位、四位率控制、攻守转换或高段桌泛化？
```

不能回答这个问题的算法，先不进入主线。

## Candidate sources

优先研究以下类型：

1. 已在 Tenhou / 立直麻将中证明强度的 AI：LuckyJ、Suphx、NAGA、Mortal、Akochan、Kanachan、Archer。
2. 强相关论文：不完全信息博弈、深度强化学习、自我博弈、遗憾最小化、搜索、风险建模。
3. 开源实现：可复现、可运行、可评测、能转化成本地 Codex 任务。
4. 高段牌谱分析工具：可以辅助构建 benchmark、失败案例库、策略差异分析。

## Algorithm fit score

每个候选算法按 100 分打分：

```text
Tenhou 目标一致性：25
已有强度证据：20
可复现程度：20
数据/环境兼容性：15
降低四位率和提升 pt EV 的潜力：10
工程成本可控性：10
```

推荐门槛：

```text
>= 90：核心路线
75-89：优先实验
60-74：观察/小实验
< 60：归档，不进入主线
```

## Must not do

- 不因为“新”就采用。
- 不因为论文指标好看就采用。
- 不采用无法映射到 Tenhou 稳定段位的指标。
- 不把 win rate 当成唯一指标。
- 不绕过平台规则，不做账号规避、反检测、非法自动化。

## Output requirement

每次算法调研后，必须更新：

```text
docs/04_rl_selfplay/04E_ALGORITHM_CANDIDATE_ROUTES.md
docs/07_development_execution/07E_ALGORITHM_DISCOVERY_WORKFLOW.md
docs/08_experiment_analysis/08F_ALGORITHM_CANDIDATE_CARD.md
docs/09_governance/09_EVIDENCE_LOG.md
docs/10_next/10_NEXT.md
```
