# 04E_ALGORITHM_CANDIDATE_ROUTES

## Purpose

本文件保存算法候选路线。所有路线都必须服务于：Tenhou 稳定段位 > LuckyJ 10.68。

## Route A: Suphx-style route

核心思想：

```text
高段牌谱监督学习 -> 自我对弈强化学习 -> 全局收益预测 -> oracle guiding -> runtime policy adaptation
```

适合我们原因：

- Suphx 是明确面向 Tenhou 的强 AI 路线。
- 重点不是单手和牌率，而是长期稳定段位。
- 可转化为“先模仿、再自我对弈、再加入 value/risk/排名目标”的阶段计划。

风险：

- 需要高质量模拟器。
- 需要大量训练资源。
- oracle guiding 需要谨慎设计，不能让训练依赖实战不可见信息。

## Route B: LuckyJ-inspired route

核心思想：

```text
不完全信息博弈 -> actor-critic + regret minimization -> self-play mixed strategy -> optimistic imperfect-information search
```

适合我们原因：

- LuckyJ 是当前项目最低超越目标。
- 其公开信息指向强化学习、遗憾最小化、自我博弈和不完全信息搜索。
- 对“从强 baseline 继续突破”有启发意义。

风险：

- LuckyJ 没有完整开源实现。
- 公开资料有限，需要拆解为可验证子任务。
- ACH 原论文主要讨论 1v1 Mahjong，迁移到四人 Tenhou 需要实验验证。

## Route C: Open-source baseline route

候选：

```text
Mortal
Akochan
Kanachan
Archer
Phoenix
Akagi/mjai-reviewer 类工具
```

使用方式：

- 先作为评测和工程参考。
- 再作为 baseline 或 teacher。
- 最后决定是否复用架构、数据管线或推理服务。

不直接假设它们能超过 LuckyJ。

## Route D: Evaluation-first route

核心思想：

```text
先建立高置信评测系统，再决定算法投入。
```

优先原因：

- 如果评测不准，算法选择会被误导。
- Tenhou 稳定段位是长周期指标，必须用离线、场景、自我对弈、bootstrap 共同估计。
- 低四位率、南场排名判断、押引质量必须单独评测。

## Route E: Search + risk model route

核心思想：

```text
policy network 给候选动作；risk/value/search 模块修正关键局面。
```

重点局面：

- 立直判断
- 追立判断
- 副露判断
- 终盘危险牌押引
- 南场避四
- 亲番/子番收益差异
- 点棒状况下的 rank EV

## Current recommendation

阶段 1 不直接冲 RL。

推荐顺序：

```text
1. 建立算法候选池和证据表。
2. 复现/接入一个开源 baseline 做评测参照。
3. 建立 Tenhou 规则环境和稳定段位估计。
4. 做高段牌谱监督学习 baseline。
5. 再进入 self-play RL、risk model、search。
```
