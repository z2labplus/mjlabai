# 04G_ALGORITHM_RACING_FUNNEL

## Purpose

本文件定义我们的算法选择流程：**赛马漏斗机制**。

目标不是完整训练所有候选算法，而是用低成本、分阶段、可回滚的方式，筛出最可能让项目达到：

```text
Tenhou 稳定段位 > LuckyJ 10.68
```

## Core principle

不要问：

```text
哪个算法听起来最强？
```

要问：

```text
哪个路线在统一 Tenhou-like 评测中，最可能稳定提升 pt EV、稳定段位，并降低四位率？
```

## What this is NOT

赛马漏斗不是：

- 不是把 Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer 都完整训练到最强。
- 不是按论文名气排序。
- 不是谁 repo star 多谁优先。
- 不是只看动作预测准确率。
- 不是只看短期冲段或少量对局胜率。

这样做成本太高，而且会把项目带偏。

## What this IS

赛马漏斗是：

```text
候选登记 -> 证据评审 -> 可复现检查 -> 接口适配 -> 离线场景测试 -> 小规模联赛 -> 中规模联赛 -> 主线晋级
```

每一阶段只给通过者更多资源。失败者不立刻删除，但降级为参考或暂停。

## Candidate roles

| Candidate | Role in funnel | What to do | What not to do |
|---|---|---|---|
| LuckyJ | Final target / benchmark line | 作为最低超越目标：十段、稳定段位 10.68；记录其公开指标与验收条件。 | 不把 LuckyJ 当作可复现起点；不假设能直接得到实现细节。 |
| Suphx | Main methodology blueprint | 拆成可复现实验模块：SL policy、self-play RL、global reward prediction、oracle guiding、runtime policy adaptation。 | 不把 Suphx 论文结果直接等同于我们的强度；不跳过评测闭环。 |
| Mortal | First reproducible local baseline | 优先本地跑通，用于建立日志、动作接口、评测 harness、延迟测试和 baseline 对战。 | 不默认 Mortal 最终最强；它首先是工程闭环起点。 |
| Archer | High-potential Tenhou baseline candidate | 验证 Tenhou 相关 claim、build、weights、log、协议和复现路径。 | 不在证据未核验前把它当成主线强度基准。 |
| Akochan | Secondary baseline / reviewer | 作为传统强 AI、C++ baseline、局面评审和对照工具。 | 不优先消耗大训练资源。 |
| Kanachan | Data/model architecture reference | 研究大规模数据、模型结构、训练工程；评估能否迁移到 Tenhou。 | 不直接当 Tenhou baseline，除非完成规则与数据适配。 |

## Funnel stages

### F0 — Candidate registration

目的：建立候选卡，不跑训练。

必须填写：

- 候选名称。
- 类型：论文、闭源目标、开源 baseline、框架、评测参考。
- 核心思想。
- 公开强度证据。
- Tenhou 目标贴合度。
- 可复现性。
- 数据需求。
- 算力需求。
- 最大风险。
- 最小实验。

通过条件：候选信息足以判断是否进入 F1。

### F1 — Reproducibility audit

目的：判断能不能成为本地可用 baseline 或研究模块。

检查：

- 仓库或论文是否可访问。
- license 是否允许研究和本地使用。
- 是否有安装说明。
- 是否有权重或示例。
- 是否能在本地或容器中跑最小样例。
- 是否能输出可记录的动作。

通过条件：至少能形成本地复现计划；无法复现者只能保留为方法论参考。

### F2 — Interface and legality adapter

目的：让候选进入统一评测接口。

检查：

- 输入状态格式能否转为我们的内部 state。
- 输出动作是否能映射为合法日麻动作。
- legal action rate 是否为 100%。
- 每手是否能记录日志。
- 推理延迟是否可测。

通过条件：可以跑固定局面，并稳定输出合法动作。

### F3 — Offline scenario evaluation

目的：低成本筛掉明显不适合路线。

重点局面：

- 切牌。
- 立直。
- 副露。
- 押引。
- 终盘防守。
- 南场排名判断。
- Oorasu 避四。

通过条件：关键场景没有明显灾难性错误，并且至少在一个核心指标上有价值。

### F4 — Small self-play league

目的：用小规模对战发现方向性问题。

建议规模：

```text
2,000 半庄以内或同等低成本规模
```

评估：

- 平均顺位。
- 一位率。
- 四位率。
- pt EV。
- 放铳率。
- 合法动作率。
- 延迟。

通过条件：没有明显四位率恶化或推理不稳定。

### F5 — Medium promotion league

目的：决定是否给更多训练和集成资源。

建议规模：

```text
20,000 半庄级别
```

通过条件：

- pt EV 相对当前 baseline 有稳定提升。
- 四位率不显著恶化。
- 关键场景无明显回退。
- bootstrap 结果支持继续投入。

### F6 — Mainline candidate gate

目的：进入项目主线。

建议规模：

```text
100,000 半庄级别或等价强度统计
```

进入主线必须满足：

```text
稳定段位估计提升
AND pt EV 提升
AND 四位率不恶化
AND legal action rate = 100%
AND 推理延迟可接受
AND 可复现
AND 有回滚路径
AND 文档、证据、风险全部更新
```

### F7 — LuckyJ target validation

目的：最终验收是否接近或超过目标。

验收线：

```text
Tenhou stable dan estimate > 10.68
```

必须报告：

- 样本量。
- 房间/规则。
- 1/2/3/4 位率。
- pt EV。
- 稳定段位估计。
- bootstrap confidence interval。
- 对手池。
- 版本/commit/checkpoint。
- 失败案例。

## Resource allocation rule

资源按阶段递增：

```text
F0/F1: 文档和复现检查
F2/F3: 接口与离线评测
F4: 小规模算力
F5: 中等算力
F6/F7: 大规模算力和严格统计
```

任何候选不能跳级拿到大规模训练资源。

## Current funnel priority

当前默认顺序：

```text
1. 先完成 F0 候选表。
2. Mortal 进入 F1/F2，作为第一个本地 baseline。
3. Archer 进入 F1，重点验证 Tenhou claim 和复现材料。
4. Akochan 进入 F1/F2，作为第二 baseline。
5. Kanachan 进入 F0/F1，重点研究数据和模型结构迁移。
6. Suphx 进入方法拆解，不作为直接可运行 baseline。
7. LuckyJ 固定为目标线，不进入实现赛马。
```

## Decision labels

每个候选只允许以下状态之一：

```text
Register
Watch
Reproduce
Adapter
OfflineEval
SmallLeague
MediumLeague
MainlineCandidate
Mainline
ReferenceOnly
Paused
Rejected
```

## Discussion rule

以后讨论任何新算法，都必须先回答：

```text
它处于赛马漏斗哪一层？
下一层最低成本实验是什么？
它是否可能提升 Tenhou 稳定段位、pt EV 或四位率？
```
