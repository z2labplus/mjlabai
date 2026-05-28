# 07F_ALGORITHM_TABLE_BUILD_TASK

## Current task

建立 Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer 的算法候选表，并把它变成本地 Codex 可执行任务。

## Scope

只做文档与评测设计，不训练模型，不重构代码。

## Files to update

- `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`
- `docs/05_evaluation/05F_ALGORITHM_SELECTION_BENCHMARK.md`
- `docs/09_governance/09_EVIDENCE_LOG.md`
- `docs/10_next/10_NEXT.md`

## Codex execution steps

1. 读取 `AGENTS.md`。
2. 读取 `docs/00_HANDOFF.md`。
3. 读取 `docs/04_rl_selfplay/04F_ALGORITHM_CANDIDATE_TABLE.md`。
4. 读取 `docs/05_evaluation/05F_ALGORITHM_SELECTION_BENCHMARK.md`。
5. 不修改代码。
6. 补全候选表字段。
7. 标记每个候选的缺失证据。
8. 输出下一步最小任务。

## Acceptance criteria

完成后必须得到：

- 一个候选算法矩阵。
- 一个评分规则。
- 一个最小实验序列。
- 一个明确的第一 baseline 推荐。
- 一个更新后的 `10_NEXT.md`。

## Expected first recommendation

除非后续证据推翻，第一 baseline 应为：

> Mortal：因为它开源、可运行、Tenhou 标准四麻兼容性强，并且有高速模拟器与 mjai 接口，适合作为本地评测闭环起点。

## Out of scope

- 不直接复现 LuckyJ。
- 不声称 Suphx 或 LuckyJ 可完整复现。
- 不进行真实平台自动化。
- 不把论文指标当作最终强度结论。
