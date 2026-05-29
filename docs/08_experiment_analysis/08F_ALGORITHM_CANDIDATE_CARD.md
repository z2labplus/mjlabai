# 08F_ALGORITHM_CANDIDATE_CARD

## Template

```text
候选算法名称：

角色：
Target / MethodologyBlueprint / BaselineCandidate / SecondaryBaseline / ResearchReference / Watch / Rejected

当前 funnel stage：
F0 Registration / F1 Reproducibility / F2 Adapter / F3 OfflineEval / F4 SmallLeague / F5 MediumLeague / F6 MainlineCandidate / F7 LuckyJValidation

来源：
论文 / GitHub / 官方说明 / 复盘文章 / 工具

核心思想：

它解决的问题：

和项目目标的关系：
是否帮助 Tenhou 稳定段位 > 10.68？如何帮助？

预计提升指标：
- 稳定段位
- Tenhou pt EV
- 平均顺位
- 一位率
- 四位率
- 放铳率
- 南场避四
- 攻守转换

已有证据：

可复现程度：
高 / 中 / 低

需要数据：

需要环境：

需要算力：

工程复杂度：
低 / 中 / 高

主要风险：

下一步最低成本实验：

成功标准：

失败标准：

评分：
Tenhou 目标一致性 /25：
已有强度证据 /20：
可复现程度 /20：
数据/环境兼容性 /15：
降低四位率和提升 pt EV 潜力 /10：
工程成本可控性 /10：
总分 /100：

结论：
继续 / 暂停 / 仅参考 / 进入下一 funnel stage / 进入主线候选
```

## Current candidate roles

| Candidate | Role | Current funnel stage | Next lowest-cost experiment |
|---|---|---|---|
| LuckyJ | Target benchmark | Target line / F7 validation reference | Continue evidence verification; do not implement. |
| Suphx | Methodology blueprint | ReferenceOnly + module decomposition | Create experiment cards for SL, self-play RL, GRP, oracle guiding, runtime adaptation. |
| Mortal | Source-code, mjai-interface, methodology and engineering reference | F1 paused as runnable baseline / ReferenceOnly | Re-open F1 only if a lawful, verifiable and usable trained model artifact is provided with version/tag, usage constraints and checksum. |
| Archer | High-potential baseline candidate | F1 | Verify claims, weights/logs, build path and protocol. |
| Akochan | Next baseline F1 candidate / reviewer | F1 next | Repository, license, dependencies/build path, artifact requirements, minimal documented run viability and I/O/logging fit. |
| Kanachan | Data/model architecture reference | F0/F1 | Review schema/model ideas for Tenhou transfer. |
