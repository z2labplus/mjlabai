# 05G_RACING_FUNNEL_EVALUATION

## Purpose

本文件定义赛马漏斗中每一阶段的评测指标。核心原则：

```text
越早期越低成本，越后期越接近 Tenhou 稳定段位。
```

## Primary metrics

所有阶段最终都服务于这些指标：

| Metric | Direction | Why |
|---|---:|---|
| Stable dan estimate | higher | 北极星强度指标。 |
| Tenhou-like pt EV / hanchan | higher | 直接反映段位收益。 |
| Average placement | lower | 综合实力。 |
| 4th rate | lower | Tenhou 高段惩罚核心。 |
| 1st rate | higher if 4th safe | 攻击收益。 |
| Deal-in rate | lower if EV-safe | 防守和押引质量。 |
| Win rate | higher if rank-safe | 进攻效率。 |
| South/Oorasu 4th-avoid rate | higher | 天凤高段稳定性关键。 |
| Legal action rate | exactly 100% | 工程底线。 |
| Latency | lower / within budget | 实战可部署性。 |
| Reproducibility | required | 本地 Codex 持续开发基础。 |

## Non-primary metrics

这些指标只能辅助判断，不能单独决定路线：

- supervised loss。
- 动作预测准确率。
- repo star 数。
- 论文名气。
- 少量样本胜率。
- 单个精彩牌谱。

## Stage metrics

### F0 — Evidence review

输出：

- public evidence score。
- Tenhou fit score。
- reproducibility risk。
- missing evidence list。

不允许输出：

```text
该算法已经最好。
```

只能输出：

```text
值得进入下一阶段 / 暂停 / 仅作参考。
```

### F1 — Reproducibility audit

必须记录：

- repo / paper / artifact。
- commit / version。
- license。
- build steps。
- 是否有 weights。
- 是否有 sample logs。
- 本地失败原因。

通过线：

```text
可运行最小样例 OR 可形成明确 adapter/reproduction plan。
```

### F2 — Interface and legality

必须记录：

- 输入 state schema。
- 输出 action schema。
- legal action rate。
- 每手日志字段。
- latency p50 / p95 / p99。

通过线：

```text
legal action rate = 100%
AND 可以在固定局面集上稳定运行
```

### F3 — Offline scenario set

必须覆盖：

- discard。
- riichi。
- call。
- push/fold。
- defense。
- South-round rank awareness。
- Oorasu fourth-place avoidance。

输出：

- 场景通过率。
- 高风险错误案例。
- 与当前 baseline 的差异。
- 是否值得进入小规模联赛。

### F4 — Small league

用途：发现方向性问题。

建议报告：

```text
Games:
Rules:
Opponent pool:
Candidate version:
Average rank:
1st/2nd/3rd/4th:
pt EV:
4th rate delta:
Deal-in rate:
Latency:
Decision: Continue / Pivot / Stop
```

### F5 — Medium league

用途：判断是否给主线资源。

必须增加：

- bootstrap confidence interval。
- seat rotation。
- seed control。
- regression suite。
- failure case sampling。

通过线：

```text
pt EV improvement is stable
AND 4th rate is not worse
AND no critical scenario regression
```

### F6 — Mainline candidate

必须满足：

```text
Primary metric improves over current main baseline.
Fourth-place control is preserved or improved.
Legal action rate is 100%.
Latency is within deployment budget.
Results are reproducible from documented version/checkpoint.
Rollback path exists.
```

### F7 — LuckyJ target validation

最终只看 Tenhou-like 强度，不看名气。

最低目标：

```text
Stable dan estimate > 10.68
```

更严格目标：

```text
lower bootstrap confidence bound > 10.68
```

若样本不足，只能标记为：

```text
provisional evidence
```

不能标记为已经超过 LuckyJ。

## Promotion summary template

```text
Candidate:
Current funnel stage:
Next stage requested:
Evaluation version:
Game count / scenario count:
Rules:
Opponent pool:
Key metrics:
- stable dan estimate:
- pt EV:
- average rank:
- 1st / 2nd / 3rd / 4th:
- 4th rate:
- deal-in rate:
- legal action rate:
- latency p95:
Confidence / uncertainty:
Major failure cases:
Decision:
Reason:
Docs updated:
Next task:
```
