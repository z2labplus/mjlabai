# 06E_IMPERFECT_INFORMATION_SEARCH

## Purpose

记录搜索与不完全信息推理路线。

麻将不是完全信息游戏。强 AI 不能只输出“最像高手的切牌”，还要估计：

```text
他家听牌概率
危险牌放铳概率
放铳点数分布
自手和牌概率
流局收益
半庄 rank EV / Tenhou pt EV
```

## Search role

搜索模块不替代 policy model，而是在高价值局面纠错：

```text
policy network -> 候选动作
risk/value models -> 每个动作的风险和 rank EV
search / rollout -> 关键动作再评估
final selector -> 选择 Tenhou pt EV 最优动作
```

## First version scope

第一版只做轻量搜索：

- 输入当前局面和候选动作。
- 输出动作级风险、局收支 EV、rank EV。
- 只在关键局面触发：立直、追立、副露、危险牌、南场排名战。

## Promotion gate

搜索模块只有在以下指标改善时才能进入主线：

```text
平均顺位下降
四位率下降
Tenhou pt EV 提升
南场避四成功率提升
高危险牌错误押牌减少
推理延迟仍可接受
```
