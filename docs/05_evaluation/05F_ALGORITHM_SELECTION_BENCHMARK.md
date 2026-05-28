# 05F_ALGORITHM_SELECTION_BENCHMARK

## Purpose

本文件定义：如何判断某个算法路线是否真的更好。

结论先行：

> 最好的算法不是论文看起来最强，也不是代码最流行，而是在统一 Tenhou-like 评测中最能提升稳定段位、pt EV，并降低四位率的算法。

## Evaluation hierarchy

### Level 0 — Evidence score

用途：快速筛选候选。

问题：

- 是否有 Tenhou 实战证据？
- 是否有公开论文或可核验说明？
- 是否有可运行代码？
- 是否有模型权重？
- 是否支持四麻半庄、Tenhou-like pt？

Level 0 只能决定“是否值得研究”，不能证明“最好”。

### Level 1 — Reproducibility score

用途：判断是否能成为本地 baseline。

成功标准：

- 可安装。
- 可跑通最小样例。
- 可输入牌谱或 mjai log。
- 可输出动作。
- 版本可锁定。

### Level 2 — Offline decision quality

用途：低成本判断候选是否值得进入训练或自我对弈。

指标：

- discard action agreement
- chi / pon / kan / riichi agreement
- 押引场景正确率
- 终盘安全牌选择
- 南场避四判断
- rank-pt EV proxy

注意：动作预测准确率不能作为最终指标。

### Level 3 — Tenhou-like self-play league

用途：判断策略是否真的变强。

统一条件：

- 同一规则
- 同一随机种子池
- 同一对手池
- 同一对局数量
- 同一推理延迟限制
- 同一日志格式

核心指标：

| Metric | Direction | Why |
|---|---:|---|
| pt EV / hanchan | higher | 最接近 Tenhou 段位收益 |
| stable dan estimate | higher | 北极星指标 |
| 4th rate | lower | Tenhou 高段惩罚核心 |
| average rank | lower | 总体实力指标 |
| deal-in rate | lower if EV-safe | 防守能力 |
| 1st rate | higher if not increasing 4th | 攻击收益 |

### Level 4 — Regression and ablation

用途：防止模型靠单一场景刷分。

必须检查：

- 早巡牌效是否退化
- 中巡押引是否退化
- 终盘防守是否退化
- 南场排名判断是否退化
- 副露与立直是否出现异常偏置
- 延迟是否超标

### Level 5 — Compliant external validation

用途：最终接近真实平台强度。

原则：

- 必须遵守平台规则与项目合规文档。
- 不把项目建立在规避平台限制上。
- 优先使用自建环境、公开牌谱、私有房间或允许的测试方式。

## Stable dan proxy

在 Phoenix / Houou-like 半庄规则下，可以先用近似 pt EV 判断方向：

```text
EV = 90 * P1 + 45 * P2 + 0 * P3 - loss(dan) * P4
```

十段四位损失可按 180 作为高段压力近似。

如果使用段位 d 的近似四位损失：

```text
loss(dan) = 15 * (dan + 2)
stable_dan_proxy = (90 * P1 + 45 * P2) / (15 * P4) - 2
```

注意：这是内部比较 proxy，不等同于官方最终稳定段位。最终报告必须同时给出真实 pt EV 与不确定性区间。

## Promotion rule

一个算法或改动进入主线，必须满足：

```text
pt EV 显著提升
AND 四位率不显著恶化
AND 关键场景无明显回退
AND 可复现
AND 推理成本可接受
```

建议阈值：

- 小实验：至少 2,000 半庄自我对弈，用于发现明显问题。
- 中实验：至少 20,000 半庄，用于版本晋级判断。
- 大实验：至少 100,000 半庄，用于主模型晋级判断。

每次报告必须包含：

- 对局数
- 随机种子范围
- 对手池版本
- 规则配置
- 模型 checkpoint
- 置信区间 / bootstrap 结果
- 失败案例样本

## Current best-selection answer

当前不能直接宣布某个算法“效果最好”。现阶段应这样判断：

1. 公开强度证据：LuckyJ > Suphx > Archer/Mortal/Akochan/Kanachan。
2. 可复现工程价值：Mortal > Akochan/Archer > Kanachan > Suphx/LuckyJ。
3. 最值得作为主路线的方法论：Suphx + LuckyJ-inspired ACH + Tenhou pt/self-play evaluation。
4. 最值得先跑的 baseline：Mortal。
5. 最值得作为最终目标锚点：LuckyJ 10.68。

因此，第一阶段的结论是：

> 用 Mortal/Akochan/Archer/Kanachan 建工程与评测；用 Suphx/LuckyJ/ACH 指导训练路线；最终只用 Tenhou-like pt EV 和稳定段位估计决定谁进入主线。

## v0.4 Link to racing funnel

本文件定义“如何比较算法”。

具体执行顺序以以下文件为准：

```text
docs/04_rl_selfplay/04G_ALGORITHM_RACING_FUNNEL.md
docs/05_evaluation/05G_RACING_FUNNEL_EVALUATION.md
```

关键结论：

```text
算法效果最好 = 在同一 Tenhou-like 评测 harness 下，稳定段位估计、pt EV、平均顺位、四位率综合表现最好。
```

在 F6/F7 之前，任何结果只能称为“候选优势”或“阶段性证据”，不能称为“已经最好”。
