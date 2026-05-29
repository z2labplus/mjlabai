# 09_RISK_REGISTER

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Evaluation overclaims | Research | High | Medium | Require documented sample size and uncertainty | Open |
| Platform automation compliance | Compliance | High | Medium | Offline/self-play first; compliance review before integration | Open |
| Data rights ambiguity | Data | Medium | Medium | Track source, rights and allowed use | Open |
| Hidden information leakage | Evaluation | High | Medium | Add leakage tests to regression suite | Open |
| Optimizing loss instead of Tenhou EV | Research | High | High | Every experiment reports Tenhou-oriented metrics | Open |

## 2026-05-30 — Tiny benchmark fixture schema review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The fixture schema review is mistaken for benchmark harness implementation readiness beyond synthetic/local scope. | Scope / Engineering | High | Medium | `05O` states the schema is only a front-door input boundary for a future P5-only synthetic/local harness and does not implement the harness. | Open |
| The next harness task expands into model-output integration, real data, CLI, league or runner behavior. | Scope / Compliance | High | Medium | `10_NEXT`, `05O` and the stage contract restrict the next task to the project-authored synthetic fixture and forbid model output, real Tenhou, real haifu, external logs, platform data, CLI, broad ingestion, league, runner and P6-P12 work. | Open |
| Fixture schema sufficiency is misread as model strength, stable-dan or LuckyJ evidence. | Evaluation / Governance | High | Medium | `05O`, evidence log and ranking protocol state the evidence grade is P5 synthetic/local fixture schema smoke evidence only, not model strength, Tenhou, stable-dan, LuckyJ or candidate promotion evidence. | Open |

## 2026-05-30 — Tiny benchmark harness fixture schema smoke risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The tiny benchmark fixture schema smoke test is mistaken for a benchmark harness implementation. | Scope / Engineering | High | Medium | Fixture/test docs state it validates shape only and does not add production code, harness, CLI, file ingestion, runner, league, model-output integration or latency measurement. | Open |
| The latency diagnostic plan is mistaken for measured benchmark results. | Evaluation / Engineering | Medium-High | Medium | The fixture contains plan fields only; the schema test rejects measured-result fields and does not import `time` or call timing APIs. | Mitigated in test |
| The fixed-position synthetic record is mistaken for supervised labels, policy quality or strength evidence. | Evaluation / Governance | High | Medium | Fixture interpretation and docs state fixed-position expectations are future diagnostics only, not supervised labels, policy-quality evidence, model-strength evidence or LuckyJ comparison. | Open |
| Future work jumps from schema smoke coverage into harness implementation, real data ingestion or model-output integration without review. | Scope / Compliance | High | Medium | `10_NEXT` sets a review gate as the next task and explicitly forbids benchmark harness implementation, real Tenhou, real haifu, external logs, model-output integration, CLI, broad file ingestion and P6-P12 work. | Open |

## 2026-05-30 — Tiny benchmark harness boundary risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| A future tiny benchmark harness boundary is mistaken for harness implementation or production evaluator readiness. | Scope / Engineering | High | Medium | `05N_TINY_BENCHMARK_HARNESS_BOUNDARY.md` states the task is docs-only and adds no harness, code, tests, fixtures, CLI, file ingestion, runner or league behavior. | Open |
| Legal-action rate, latency or fixed-position diagnostics are used as model strength or LuckyJ evidence. | Evaluation / Governance | High | Medium | `05N`, `05F`, evidence log and `10_NEXT` state these diagnostics are not model-strength evidence, Tenhou ranked evidence, stable-dan evidence, policy-quality evidence, candidate-promotion evidence or LuckyJ `10.68` comparison. | Open |
| A future schema smoke task expands into real Tenhou, real haifu, external logs, model-output integration or third-party binary paths. | Compliance / Scope | High | Medium | `05N` and `10_NEXT` restrict the next task to synthetic/local fixture schema smoke coverage and explicitly forbid real Tenhou, external data, Akochan binaries, model weights, CLI, runner, league and P6-P12 work. | Open |
| Latency diagnostics are misread as GPU, training, self-play or league throughput benchmarks. | Engineering / Evaluation | Medium-High | Medium | `05N` restricts latency to local offline synthetic/local evaluation code paths and requires environment, sample count, timing method and repetitions when implemented later. | Open |

## 2026-05-30 — Legal-action synthetic evaluator review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Current-scope completion is mistaken for complete real-game legal-action evaluation. | Evaluation / Governance | High | Medium | The review document states completion is only for P5 synthetic-only `dahai` + strict scope and lists remaining gaps for reach, calls, kan, hora, ryukyoku, red fives, tile notation and real model outputs. | Open |
| The next tiny benchmark task jumps directly into a runner, CLI or league implementation. | Scope / Engineering | High | Medium | `10_NEXT` sets a boundary-definition task before implementation and explicitly forbids runner, CLI, file ingestion, league, real Tenhou and external data. | Open |
| Synthetic legal-action coverage is used as model ranking or LuckyJ comparison evidence. | Evaluation / Governance | High | Medium | `05M`, evidence log and algorithm ranking protocol state this is diagnostic P5 smoke evidence only, not model-strength, Tenhou or LuckyJ evidence. | Open |

## 2026-05-30 — Synthetic legal-action parse-failure coverage risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The synthetic `parse_failure` fixture case is mistaken for expanded action support or a canonicalizer. | Evaluation / Scope | Medium-High | Medium | Docs state the case uses `dahai` plus `tsumogiri = null` only to exercise the strict parse-failure branch; current supported scope remains `dahai` + strict matching. | Open |
| Null or unknown `tsumogiri` is accidentally treated as acceptable strict matching input. | Evaluation / Data Quality | Medium-High | Medium | Evaluator tests expect the project fixture to count the null-`tsumogiri` record as `parse_failure`, not legal or invalid. | Mitigated in tests |
| Fixture labels such as `expected_future_outcome = parse_failure` are mistaken for evaluator output or model predictions. | Governance / Evaluation | Medium-High | Medium | Existing tests verify labels are not used for computation; docs repeat labels are future expectations only. | Mitigated in implementation |
| Synthetic legality diagnostics are overclaimed as Tenhou evidence, model strength evidence or LuckyJ 10.68 comparison. | Evaluation / Governance | High | Medium | Evidence log, docs and envelope warnings state synthetic-only, not Tenhou, not real haifu, not model strength evidence and not LuckyJ comparison. | Open |

## 2026-05-29 — Synthetic legal-action metric evaluator risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Synthetic legal-action rates are mistaken for model strength, Tenhou evidence or LuckyJ comparison. | Evaluation / Governance | High | Medium | Result warnings, docs and evidence log state synthetic-only, not Tenhou, not real haifu, not model strength evidence and not LuckyJ 10.68 comparison. | Open |
| The narrow fixture evaluator is expanded into broad file ingestion, model-output evaluation, CLI, runner or league behavior. | Scope / Engineering | High | Medium | Current implementation accepts an in-memory fixture mapping only; `10_NEXT` restricts the next task to synthetic parse-failure fixture coverage. | Open |
| Strict `dahai` comparison is treated as a full canonicalizer. | Engineering / Evaluation | Medium-High | Medium | Docs and tests state current comparison is only actor/action_type/tile/tsumogiri; no reach/calls/kans/red-five/tile-normalization support exists. | Open |
| `expected_future_outcome` labels leak into evaluator logic. | Evaluation / Test Quality | Medium-High | Low-Medium | Unit test mutates labels and verifies computed counts/rates do not change. | Mitigated in implementation |
| Zero-denominator cases fabricate `0.0` or `1.0` rates. | Evaluation / Data Quality | High | Low | `LegalActionMetricResult` requires all rates to be `None` when `evaluated_decision_count == 0`. | Mitigated in implementation |

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

## 2026-05-29 — Akochan F2 real-exe workflow risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The real-exe workflow definition is mistaken for successful real `system.exe` compatibility evidence before it is run. | Governance / Evaluation | High | Medium | Keep candidate status tied to successful run IDs and logs. | Mitigated by successful run `26629344590` for fixed-sample wrapper validation |
| Workflow logs could expose too much third-party build output or sample stdout. | Governance | Low-Medium | Medium | Write only short summaries to GitHub Step Summary and do not upload artifacts. | Open |
| GitHub Actions temporary build succeeds but local macOS remains unable to run real Akochan. | Reproducibility | Medium | High | Treat evidence as Ubuntu-runner compatibility only; keep local macOS build limits documented. | Open |
| Real `mjai_log` stdout may be newline-delimited JSON, another multi-record JSON stream or an allowlisted mixed stream rather than a single JSON document. | Engineering | Medium | Medium | Wrapper supports strict JSON streams plus exactly the allowlisted `calculating review` status line. | Mitigated by successful run `26629344590` |
| The workflow accidentally persists third-party source or binaries. | License / Governance | High | Low | Use runner temp directories only and do not configure artifact upload or caches for Akochan outputs. | Open |
| Akochan `system.exe` depends on runtime config files such as `setup_mjai.json` being visible from the process working directory. | Engineering / Reproducibility | Medium-High | High | Wrapper uses explicit `working_dir`, `AKOCHAN_WORKING_DIR` or default executable directory as subprocess cwd; workflow sets runner-temp `AKOCHAN_WORKING_DIR`. | Mitigated by successful runs `26623247276` and `26629344590` |

## 2026-05-29 — Akochan F2 working-directory fix risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Local fake tests may pass while real Akochan still needs additional runtime files or cwd assumptions beyond `setup_mjai.json`. | Engineering / Reproducibility | Medium | Medium | Rerun `Akochan F2 Wrapper Real Exe Audit` against the Ubuntu-built real `system.exe` and record the run ID/logs before closing F2 real-exe compatibility. | Mitigated for fixed samples by successful run `26629344590` |
| `AKOCHAN_WORKING_DIR` could point to a directory that does not match the audited executable or commit. | Reproducibility / Governance | Medium | Medium | Require explicit environment setup in workflow, record `working_dir` in every audit log, and keep external commit/build environment in the audit record. | Open |

## 2026-05-29 — Akochan F2 real mjai_log parser risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Real `mjai_log` stdout is multi-record or mixed-format output that the current wrapper parser cannot represent. | Engineering / Reproducibility | Medium-High | High | Parser preserves raw stdout, records parsed records and warnings, supports strict JSON streams plus exactly `calculating review`, and raises bounded diagnostics on residue. | Mitigated for fixed samples by successful run `26629344590` |
| Parser fixes could silently discard non-JSON lines that matter for reproducibility or debugging. | Governance / Engineering | Medium | Medium | Strict parser rejects partial parses and unknown non-JSON lines, reports bounded stdout summaries, stdout SHA256, failure position and parsed-record count; keep raw stdout on success. | Mitigated for fixed samples by successful run `26629344590`; keep open for broader outputs |

## 2026-05-29 — Akochan F2 allowlisted mixed stdout parser risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Allowlisting a non-JSON `mjai_log` status line could accidentally hide unexpected runtime output. | Governance / Engineering | Medium-High | Medium | Only the exact line `calculating review` is allowlisted; every other non-JSON line still raises `AkochanOutputParseError` with bounded diagnostics and stdout SHA256. | Mitigated for fixed samples by successful run `26629344590`; keep open for broader outputs |
| The real `mjai_log` output may contain additional known status lines not covered by local fake tests. | Engineering / Reproducibility | Medium | Medium | Rerun the real-exe workflow and add only specific, reviewed status lines if logs prove they are necessary and safe. | Open |
| Local parser tests may pass while the real GitHub Actions output still has an unmodeled stdout shape. | Reproducibility | Medium | Medium | Require run ID/log review before closing F2 real-exe compatibility. | Mitigated by successful run `26629344590` for fixed samples |

## 2026-05-29 — Akochan F2 closeout risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Fixed-sample wrapper validation is mistaken for Akochan or mjlabai strength evidence. | Evaluation / Governance | High | Medium | Label run `26629344590` as fixed-sample integration evidence only; require F3+ offline/evaluation evidence before any strength claim. | Open |
| Akochan is expanded into broader evaluator/reviewer integration without rechecking license boundaries. | License / Scope | High | Medium | Keep Akochan at private/internal audit boundary; create a separate task and require Web/legal review before modification, redistribution, commercial use or public release. | Open |
| GitHub Actions Node.js 20 deprecation warning later breaks the workflow even though current F2 validation passed. | Infrastructure / Maintenance | Medium | Medium | Track workflow action/runtime updates; warning does not affect run `26629344590` but should be addressed before relying on repeated CI. | Open |

## 2026-05-29 — Stable-dan calculator risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| A deterministic stable-dan point estimate is mistaken for statistically reliable strength evidence. | Evaluation / Governance | High | Medium | Label the calculator as point-estimate infrastructure only; require bootstrap confidence intervals and sample-size reporting before comparing against LuckyJ. | Mitigated by bootstrap CI implementation; threshold helper still needed |
| `fourth_count == 0` is misreported as infinite or superior strength. | Evaluation | High | Medium | Calculator raises `StableDanUndefinedError` when `fourth_count` is zero. | Mitigated in implementation |
| Room aliases or weights are applied to the wrong Tenhou room. | Evaluation | Medium-High | Medium | Canonicalize supported room aliases and expose formula weights in `StableDanResult` for audit. | Open |

## 2026-05-29 — Stable-dan bootstrap CI risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Bootstrap lower/upper bounds are mistaken for proof that a model beats LuckyJ without an explicit threshold decision rule. | Evaluation / Governance | High | Medium | Next task is a threshold comparison helper using the bootstrap lower bound against LuckyJ 10.68. | Open |
| High undefined-resample rate makes the CI unstable or misleading. | Evaluation | Medium-High | Medium | `StableDanBootstrapResult` reports `undefined_resamples` and `undefined_rate`; docs require treating high undefined rate as unreliable. | Open |
| Bootstrap resamples with zero fourth-place count are silently converted to infinite stable dan. | Evaluation | High | Low | Implementation skips and counts undefined resamples; if all resamples are undefined, it raises `StableDanBootstrapUndefinedError`. | Mitigated in implementation |

## 2026-05-29 — Stable-dan threshold comparison risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| A helper outcome of `clear_pass` is treated as a full model-strength claim without sample-size and reporting context. | Evaluation / Governance | High | Medium | Next task defines minimum sample-size and reporting schema before project-level LuckyJ comparison claims. | Open |
| Point estimate above LuckyJ 10.68 is mistaken for a threshold pass. | Evaluation | High | Medium | Helper returns `point_estimate_only` with `clears_threshold=False` when lower bound does not exceed threshold. | Mitigated in implementation |
| High undefined rate is ignored when threshold lower bound looks strong. | Evaluation | Medium-High | Medium | Helper returns `unreliable` and `clears_threshold=False` when `undefined_rate > max_undefined_rate`. | Mitigated in implementation |

## 2026-05-29 — Stable-dan reporting schema risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Internal sample-size guardrails are mistaken for Tenhou official standards or statistical proof. | Governance / Evaluation | Medium-High | Medium | Report source note and docs label them as project-internal governance defaults only. | Open |
| A report with `clears_threshold=True` but insufficient sample size is used as a LuckyJ claim. | Evaluation / Governance | High | Medium | Report separates `clears_threshold` from `can_enter_threshold_review`; low sample adds a warning note. | Mitigated in implementation |
| Future callers feed inconsistent threshold comparison and bootstrap results into the report. | Engineering / Evaluation | Medium | Medium | Report builder validates matching point estimate, bounds, confidence level and resample counts before building a report. | Mitigated in implementation |

## 2026-05-29 — Stable-dan placement aggregation risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Placement input aliases are over-expanded and accidentally accept ambiguous or zero-based values. | Evaluation / Data Quality | Medium-High | Medium | Aggregator accepts only explicit `1`/`2`/`3`/`4` values and a small whitelist of aliases; zero-based, bool, float and unknown strings fail. | Mitigated in implementation |
| Placement aggregation helper is mistaken for a league harness or real Tenhou ingestion path. | Scope / Compliance | High | Medium | Document helper as offline input preparation only; it does not read accounts, platform data, logs, Tenhou, league or match runner outputs. | Open |
| Bad placement records are silently skipped, biasing stable-dan counts. | Evaluation / Data Quality | High | Medium | Missing keys, invalid records and invalid placements raise clear errors instead of being skipped. | Mitigated in implementation |
| Aggregated placement counts are used as strength evidence without bootstrap, threshold and sample-size report context. | Evaluation / Governance | High | Medium | Require composition with stable-dan calculator, bootstrap CI, threshold helper and reporting schema before any threshold review. | Open |

## 2026-05-29 — Stable-dan smoke fixture risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Synthetic smoke fixture output is mistaken for a model result or LuckyJ evidence. | Evaluation / Governance | High | Medium | Fixture and docs label it as synthetic-only code-path validation; report notes still say not model-strength evidence and not a Tenhou ranked result. | Open |
| A smoke test becomes a hidden CLI, file-ingestion path or league harness. | Scope | Medium-High | Medium | Keep the smoke test under `tests/`; it reads only the checked-in synthetic fixture and writes no output files. | Mitigated in implementation |
| The 100-record synthetic sample is treated as threshold-review ready. | Evaluation / Governance | High | Medium | Test asserts `can_enter_threshold_review=False` because the sample is below the project-internal `1000` game threshold-review minimum. | Mitigated in implementation |

## 2026-05-29 — Stable-dan API documentation risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Documentation examples drift from the actual Python API signature. | Documentation / Engineering | Medium | Medium | The API doc was written against the current `build_stable_dan_evaluation_report(...)` signature and notes that model/dataset metadata is not yet part of the report schema. | Open |
| API documentation is mistaken for an endorsement to build CLI or ingestion tooling. | Scope | Medium-High | Medium | Docs explicitly say API-only, no CLI, no file ingestion path, no league and no Tenhou integration. | Open |
| Synthetic example documentation is mistaken for strength evidence. | Evaluation / Governance | High | Medium | Docs label the fixture as synthetic only and repeat that point estimate, bootstrap, threshold and report examples are not model-strength evidence. | Open |

## 2026-05-29 — Stable-dan groundwork review risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Stable-dan subtrack current-scope completion is mistaken for full P5 completion. | Governance / Planning | High | Medium | `05I_STABLE_DAN_GROUNDWORK_REVIEW.md` explicitly says only the stable-dan subtrack is complete and P5 overall remains open. | Open |
| Stable-dan groundwork completion is mistaken for model-strength or LuckyJ evidence. | Evaluation / Governance | High | Medium | The review document repeats that there are no real model samples, no Tenhou ranked results and no final LuckyJ proof. | Open |
| The next metric-registry task expands into league, training or external-data ingestion. | Scope | High | Medium | `10_NEXT.md` limits the next task to P5 offline metric registry and result envelope schema; no league, training, self-play, Tenhou or P6-P12. | Open |

## 2026-05-29 — Offline evaluation result envelope schema risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Registry placeholder metrics are mistaken for implemented evaluators. | Evaluation / Governance | Medium-High | Medium | `05J_OFFLINE_EVALUATION_RESULT_SCHEMA.md` labels legal-action, invalid-action, parse-success and latency metrics as schema placeholders unless separate evaluator tasks implement them. | Open |
| Result envelope is mistaken for a runner or evidence generator. | Scope | High | Medium | The schema records results only; docs and tests confirm it does not run commands, read data, train, self-play, league or connect to Tenhou. | Open |
| High-risk safety flags are ignored in downstream reports. | Governance | Medium | Medium | Envelope preserves safety flags and adds warnings when high-risk flags are true. | Open |

## 2026-05-29 — Offline envelope smoke fixture risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| Synthetic envelope smoke result is mistaken for model-strength evidence. | Evaluation / Governance | High | Medium | The smoke test and evidence log label the input as synthetic-only and not strength evidence. | Open |
| Envelope smoke test is mistaken for a CLI, runner or data-ingestion path. | Scope | Medium-High | Medium | The test constructs an envelope in-process, writes no output files and reads only the checked-in synthetic fixture. | Open |
| Legal-action / invalid-action placeholder metrics are used before precise metric denominators are defined. | Evaluation | Medium-High | Medium | `05K_LEGAL_ACTION_METRIC_SPEC.md` now defines denominator rules; next task should define canonical action fixture schema before implementation. | Mitigated for metric definitions; canonical schema remains open |

## 2026-05-29 — Legal-action metric specification risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| `legal_action_rate` is mistaken for model-strength evidence. | Evaluation / Governance | High | Medium | `05K_LEGAL_ACTION_METRIC_SPEC.md` states that legality is necessary but not sufficient and cannot support LuckyJ comparison by itself. | Open |
| Parse failures or missing actions are incorrectly counted as invalid actions without explicit mode. | Evaluation / Metric Definition | Medium-High | Medium | The spec separates `invalid_action_count`, `parse_failure_count` and `missing_action_count`; strict-mode changes must be explicit future work. | Open |
| Skipped records silently hide denominator problems. | Evaluation / Data Quality | Medium-High | Medium | The spec requires skipped records to be excluded from denominator but reported through `skipped_count` and skipped categories. | Open |
| Canonical action matching is implemented inconsistently across future fixtures. | Engineering / Evaluation | Medium-High | Medium | `05L_ACTION_CANONICALIZATION_SCHEMA.md` now defines canonical fields and strict `dahai` matching before evaluator implementation. | Mitigated for schema; fixture smoke test remains open |

## 2026-05-29 — Action canonicalization schema risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The schema is mistaken for an implemented canonicalizer. | Scope / Engineering | Medium-High | Medium | `05L_ACTION_CANONICALIZATION_SCHEMA.md` explicitly says it is documentation only and no parser/canonicalizer was implemented. | Open |
| Strict matching rejects valid future representations when `tsumogiri` or tile notation differs across tools. | Evaluation / Compatibility | Medium | Medium | The schema records strict mode as default and leaves relaxed modes / tile normalization as explicit future tasks. | Open |
| Future fixture authors use real Tenhou or external logs as shortcut data. | Compliance / Data | High | Medium | The schema says the first fixture must be synthetic/local only; no Tenhou, external logs, platform data or strength evidence. | Open |
| Edge cases such as reach, calls, kans and red fives are underspecified for implementation. | Evaluation / Engineering | Medium | Medium | The schema records them as future edge cases; next tasks should start with minimal `dahai` fixture smoke tests before broader actions. | Open |

## 2026-05-29 — Synthetic legal-action fixture schema smoke risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| `expected_future_outcome` labels are mistaken for actual evaluator output. | Evaluation / Governance | High | Medium | The fixture and test docstring label outcomes as future labels only; the test does not compute legal/invalid rates or canonical equality. | Open |
| Schema smoke test is mistaken for a legal-action evaluator. | Scope / Engineering | High | Medium | Keep the task limited to JSON shape validation; define an explicit evaluator boundary before implementation. | Open |
| Synthetic fixture is mistaken for model-strength evidence. | Evaluation / Governance | High | Medium | Fixture/source notes and evidence log state synthetic-only, not Tenhou, not model output and not strength evidence. | Open |
| Dahai-only fixture scope hides future edge cases for reach, calls, kans and red fives. | Evaluation / Engineering | Medium | Medium | Keep `dahai` as the minimum smoke scope and require separate tasks for broader canonicalization and evaluator behavior. | Open |

## 2026-05-29 — Synthetic legal-action evaluator boundary risks

| Risk | Category | Severity | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| The future synthetic evaluator expands from fixture-only code into a broad evaluator, file ingestion path or runner. | Scope / Engineering | High | Medium | `05K_LEGAL_ACTION_METRIC_SPEC.md` limits the next implementation to the project-authored synthetic fixture and requires a separate boundary change before broader inputs. | Open |
| Synthetic legal-action rates are mistaken for model-strength evidence or LuckyJ comparison. | Evaluation / Governance | High | Medium | Boundary warnings require synthetic-only, not Tenhou data, not real haifu, not strength evidence and not LuckyJ comparison. | Open |
| Future implementation accidentally reads real Tenhou, external logs or platform data. | Compliance / Data | High | Medium | Boundary explicitly forbids real Tenhou, real haifu, platform data, online accounts and external logs. | Open |
| Future implementation silently fabricates rates when `evaluated_decision_count == 0`. | Evaluation / Data Quality | High | Low-Medium | Boundary requires all rates to be undefined when denominator is zero and preserves the count invariant. | Open |
| Future implementation treats `expected_future_outcome` as authoritative evaluator output. | Evaluation / Governance | Medium-High | Medium | Boundary states labels are smoke expectations only and not model predictions, evaluator output or strength evidence. | Open |
