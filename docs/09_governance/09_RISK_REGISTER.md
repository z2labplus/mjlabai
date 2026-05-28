# 09_RISK_REGISTER

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Evaluation overclaims | Research | High | Medium | Require documented sample size and uncertainty | Open |
| Platform automation compliance | Compliance | High | Medium | Offline/self-play first; compliance review before integration | Open |
| Data rights ambiguity | Data | Medium | Medium | Track source, rights and allowed use | Open |
| Hidden information leakage | Evaluation | High | Medium | Add leakage tests to regression suite | Open |
| Optimizing loss instead of Tenhou EV | Research | High | High | Every experiment reports Tenhou-oriented metrics | Open |

## 2026-05-28 — v0.4 algorithm racing-funnel risks

| Risk | Severity | Mitigation |
|---|---|---|
| 完整训练所有候选算法导致算力和时间浪费。 | High | 使用 F0-F7 赛马漏斗，只有通过前一阶段的候选才能获得下一阶段资源。 |
| 不同候选使用不同评测环境，导致比较失真。 | High | 所有候选必须进入统一 Tenhou-like harness，记录规则、对手池、种子、样本量。 |
| 过早相信 repo 或论文强度声明。 | Medium-High | F0/F1 必须记录证据来源、可复现性和缺失证据；未核验前只能 Watch 或 ReferenceOnly。 |
| 只优化动作预测准确率，忽略四位率和 pt EV。 | High | 主指标固定为稳定段位、pt EV、平均顺位、四位率和南场避四。 |
| 早期小样本结果被误认为已经超过 LuckyJ。 | High | F7 之前不得声称超过 LuckyJ；必须报告样本量和 bootstrap confidence interval。 |
