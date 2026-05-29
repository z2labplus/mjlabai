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

## 2026-05-28 — v0.5 documentation sync risks

| Risk | Severity | Mitigation | Status |
|---|---|---|---|
| `docs/10_next/10_NEXT.md` referenced missing `templates/prompts/09_ALGORITHM_RACING_FUNNEL.md`, which could block the next local Codex step. | Medium | Replaced the missing template reference with existing `docs/07_development_execution/07G_RACING_FUNNEL_EXECUTION_TASK.md`. | Mitigated |

## 2026-05-28 — Mortal F1 audit risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Local shell cannot resolve `github.com` or `raw.githubusercontent.com`, blocking source clone and model artifact retrieval. | Infrastructure | High | High | Fix DNS/proxy/network configuration or provide an approved local source archive with recorded commit and checksum. | Open |
| Required runtime/build tools are missing locally: Rust/Cargo, Docker, conda and PyTorch. | Engineering | High | High | Choose one reproducibility path, either Docker or native build, then install only the minimal dependencies needed for F1 inference. | Open |
| Mortal model weights are not included in the repository and must be obtained separately. | Reproducibility | Medium-High | High | Record model source, version/tag, checksum, license/usage constraints and exact config before running inference. | Open |
| Mortal code is AGPL-3.0-or-later, which may affect future integration, service deployment or redistribution. | License | Medium | Medium | Keep F1/F2 local research-only until license review confirms integration obligations. | Open |

## 2026-05-28 — Mortal F1 blocker-resolution risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Mortal source tarball can be retrieved only through explicit host resolution while normal system DNS and normal `git clone` remain unreliable. | Infrastructure | Medium | High | Keep recorded source tarball checksum for audit, but fix system DNS/proxy before treating source access as reproducible. | Open |
| Official Mortal trained model appears unavailable for public local inference; README-linked gist says there is currently no plan to release trained parameters. | Reproducibility | High | High | Require a lawful user-provided artifact with version, usage constraints and checksum, or pause Mortal as runnable baseline and move to another F1 baseline. | Open |
| Installing Rust through Homebrew is blocked by inability to resolve `formulae.brew.sh`. | Engineering | Medium | High | Fix DNS/proxy or use an approved offline/local toolchain; avoid broad dependency installation until model artifact path is decided. | Open |

## 2026-05-29 — Technical-plan-first risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Web-side research conclusions drift away from local Git/docs state. | Governance | High | Medium | Treat Git + docs as the only source of truth; require Codex to land decisions in docs before execution. | Open |
| Paper-first narrative causes premature claims or stage skipping. | Research | High | Medium | Use `12A_TECHNICAL_PLAN_v0.1.md` as execution charter; paper remains a future summary only. | Open |
| Main route becomes too broad and consumes resources before funnel gates. | Planning | Medium-High | Medium | Keep baseline racing funnel and `10_NEXT` single-task rule; do not train or scale until gates justify it. | Open |
| LuckyJ is mistakenly treated as a full-reproduction target instead of benchmark line. | Research | Medium | Medium | Keep LuckyJ role documented as target benchmark, not implementation seed or direct full-reproduction object. | Open |

## 2026-05-29 — Mortal runnable-baseline pause risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Unknown Mortal weight files such as `mortal.pth`, `*.pth`, `*.pt`, `checkpoint` or `snapshot` are mistaken for usable project artifacts. | Reproducibility / Governance | High | Medium | Do not use unknown model artifacts. Any future Mortal artifact must record source, version/tag, usage constraints and checksum before F1 can be re-opened. | Open |
| Pausing Mortal leaves the project without a runnable local baseline until another candidate passes F1. | Planning | Medium | High | Move the next baseline F1 audit to Akochan and keep the audit limited to repository, license, dependency, artifact and minimal-run viability. | Open |
| Mortal reference code is accidentally treated as evidence of runnable strength. | Evaluation | Medium-High | Medium | Keep Mortal labeled as source-code, mjai-interface, methodology and engineering reference only; do not promote to F2 or claim strength without runnable evidence. | Open |
