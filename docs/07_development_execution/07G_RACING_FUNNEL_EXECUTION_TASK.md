# 07G_RACING_FUNNEL_EXECUTION_TASK

## Current task

把算法选择流程固化为“赛马漏斗机制”，并用于后续本地 Codex 开发。

## Scope

本任务只更新文档和下一步计划，不训练任何模型，不启动大规模实验。

## Files to read

- `docs/00_HANDOFF.md`
- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/04_rl_selfplay/04G_ALGORITHM_RACING_FUNNEL.md`
- `docs/05_evaluation/05G_RACING_FUNNEL_EVALUATION.md`
- `docs/09_governance/09_STAGE_TASK_CONTRACT.md`
- `docs/10_next/10_NEXT.md`

## Files to update after execution

- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/09_governance/09_CHANGELOG.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/09_governance/09_RISK_REGISTER.md`
- `docs/10_next/10_NEXT.md`

## Codex instructions

1. Do not train models.
2. Do not modify source code unless explicitly asked later.
3. Do not compare algorithms using incompatible metrics.
4. Do not promote a candidate without evidence.
5. Apply the funnel stages F0-F7.
6. Make Mortal the default first reproducibility audit target unless a stronger local reason appears.
7. Keep LuckyJ as the target line, not an implementation seed.
8. Keep Suphx as methodology blueprint, split into reproducible modules.

## Acceptance criteria

完成后应得到：

- 每个候选的 funnel stage。
- 每个候选的下一步最小实验。
- 当前第一 baseline 的复现任务。
- 更新后的 `10_NEXT.md`。
- 更新后的 changelog 和 evidence/risk notes。

## Expected next action

当前建议下一步：

```text
决定 Mortal F1 continuation path：
如果能提供合法 trained model artifact，则记录来源/version/usage/checksum 后继续最小 mjai 推理样例；
如果不能提供，则暂停 Mortal runnable baseline，并选择下一个 baseline 做 F1。
不训练，不调参，不接入真实平台。
```
