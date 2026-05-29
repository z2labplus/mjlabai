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

## 2026-05-29 — Akochan F1 audit risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Akochan license is a custom Japanese usage agreement rather than a standard open-source license. | License / Compliance | High | High | Restrict current use to private research audit; get legal/Web ChatGPT Pro review and likely author permission before redistribution, AI-part modification, commercial use or public release. | Open |
| Local macOS ARM build is blocked by missing or incompatible LLVM/OpenMP/Boost toolchain. | Engineering | High | High | Use a supported Linux build environment with `g++`, Boost and OpenMP, or install/verify Homebrew LLVM/OpenMP/Boost before retrying F1 build. | Open |
| Normal `git clone` still depends on unreliable local GitHub DNS. | Infrastructure | Medium | High | Fix DNS/proxy or document explicit host-resolution only as a temporary audit workaround; do not treat source access as fully reproducible until normal clone works. | Open |
| Akochan exposed promising JSON/legal-action/mjai surfaces before any minimal run had succeeded. | Reproducibility | High | High | Require successful `legal_action` and/or `mjai_log` evidence before F2. | Mitigated by GitHub Actions run `26617347785`; local macOS remains blocked |
| Repository-included `params/` text files are necessary runtime artifacts and may be mistaken for code-only dependency. | Reproducibility / Data | Medium | Medium | Treat `params/` as required artifacts tied to commit `53188a0b926fbab38177f88c3cd87d554cf412af`; record checksums if separated from the repository. | Open |

## 2026-05-29 — Akochan F1 blocker-resolution risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Preferred Docker Linux build path is unavailable because Docker is not installed. | Infrastructure / Engineering | High | High | Provision Docker or another approved temporary Linux environment outside the repository before retrying F1. | Open |
| Homebrew reports formula prefixes but the expected LLVM/Boost/OpenMP files are absent. | Engineering | High | High | Verify or reinstall Homebrew LLVM, Boost and libomp explicitly before using the macOS build path; do not run global installs without user approval. | Open |
| Repeated F1 attempts may leave external temporary clone/build directories behind. | Hygiene | Low | Medium | Keep all third-party source in `/tmp` or `../_external`, record paths, and clean temporary clones after evidence is captured. | Open |

## 2026-05-29 — Akochan GitHub Actions build-audit risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| GitHub Actions workflow succeeds in Ubuntu but local macOS remains unable to build Akochan. | Reproducibility | Medium | Medium | Treat a successful workflow as Ubuntu-runner evidence only; record runner OS, commit and commands before deciding F1 status. | Open |
| Workflow logs may include too much third-party output. | Governance | Low | Medium | Workflow writes short summaries with `head -c` limits for sample output and uploads no artifacts. | Open |
| A workflow definition may be mistaken for successful F1 evidence before it is run. | Governance / Evaluation | High | Medium | Keep candidate status tied to actual workflow run IDs and logs, not workflow existence. | Mitigated by successful run `26617347785` |
| GitHub workflow syntax/context errors can block F1 before any Ubuntu build starts. | Infrastructure / Governance | Medium | Medium | Record failed workflow run IDs, fix workflow validation issues locally, and do not count failed validation runs as build evidence. | Mitigated by fix and successful run `26617347785` |
| GitHub Actions `actions/checkout@v4` currently emits a Node.js 20 deprecation warning. | Infrastructure / Maintenance | Medium | Medium | Track the warning and update workflow action/runtime before GitHub removes Node.js 20 support. | Open |
| Akochan F1 evidence is Ubuntu-runner evidence, not local macOS reproducibility. | Reproducibility | Medium | High | Treat F1 as Conditional Pass; keep local macOS build blocked unless Docker or verified Homebrew LLVM/Boost/OpenMP is added later. | Open |

## 2026-05-29 — Akochan F2 interface risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| F2 wrapper accidentally vendors or stores Akochan source, `system.exe`, `libai.so`, `params/` or third-party build artifacts. | License / Governance | High | Medium | Keep wrapper-only boundary; use external path or GitHub Actions temporary directory; add checks that fail if third-party artifacts are added to the repository. | Open |
| F2 implementation drifts from fixed samples into self-play, match, training or real Tenhou commands. | Scope / Compliance | High | Medium | Limit next task to fixed `legal_action` and `mjai_log` samples; audit log must record training/self-play/Tenhou flags as false. | Open |
| Akochan custom license is misunderstood as a standard open-source license. | License / Compliance | High | High | Keep private/internal audit only; require license review or author permission before modification, redistribution, commercial use or public release. | Open |
| Legal-action checker output is mistaken for playing strength evidence. | Evaluation | Medium-High | Medium | Label F2 as interface/legal-action only; do not claim model strength without F3+ evaluation evidence. | Open |
| Wrapper output schema may over-normalize and lose raw mjai/Akochan fields. | Engineering | Medium | Medium | Preserve raw output in `raw` and require parseable JSON plus output hashes. | Open |

## 2026-05-29 — Akochan F2 wrapper skeleton risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Fake-executable smoke tests are mistaken for real Akochan compatibility or strength evidence. | Evaluation / Governance | High | Medium | Document fake executable as a test substitute only; require a separate run against real externally built `system.exe` before claiming real compatibility. | Open |
| The wrapper can call an external executable path, so a wrong local path could point to an unaudited binary. | Reproducibility / Security | Medium-High | Medium | Require explicit `system_exe` or `AKOCHAN_SYSTEM_EXE`, record external commit/build environment in audit logs, and avoid unknown binaries or artifacts. | Open |
| Real Ubuntu-built `system.exe` may produce output that differs from the fake executable shape. | Engineering | Medium | Medium | Preserve raw stdout, keep parse warnings, and make the next task a fixed-sample real `system.exe` validation without artifact upload. | Open |
| The initial wrapper skeleton may be expanded too quickly into broad adapter, match, league or Tenhou integration work. | Scope / Compliance | High | Medium | Keep `10_NEXT` on the single real fixed-sample validation step; no self-play, match, training or Tenhou commands. | Open |
