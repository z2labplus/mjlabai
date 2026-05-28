# 09_EVIDENCE_LOG

## Rule

Every external claim must be logged with source, date checked, and project relevance.

Internal governance decisions that affect execution should also be noted here, but they are not external strength evidence.

## Evidence entries

### 2026-05-28 — LuckyJ target baseline

- Claim: Tencent LuckyJ reached Tenhou 10 dan and stable dan 10.68.
- Sources:
  - https://haobofu.github.io/
  - https://technode.com/2023/07/12/tencents-mahjong-ai-sets-new-gaming-record-on-international-mahjong-platform/
  - https://www.stcn.com/article/detail/918748.html
- Relevance: Defines the minimum target to exceed.
- Action: Keep as north-star benchmark until a stronger verified benchmark is selected.

### 2026-05-28 — Suphx route

- Claim: Suphx used deep reinforcement learning with global reward prediction, oracle guiding and run-time policy adaptation, and demonstrated strong Tenhou stable-rank performance.
- Sources:
  - https://www.microsoft.com/en-us/research/project/suphx-mastering-mahjong-with-deep-reinforcement-learning/
  - https://arxiv.org/abs/2003.13590
- Relevance: First core algorithm reference route.
- Action: Decompose into supervised baseline, self-play RL, value/risk models and runtime adaptation experiments.

### 2026-05-28 — ACH / LuckyJ-inspired route

- Claim: Actor-Critic Hedge modifies actor-critic policy optimization toward weighted cumulative counterfactual regret in a large-scale imperfect-information Mahjong setting.
- Source:
  - https://openreview.net/forum?id=DTXZqTNV5nW
- Relevance: Candidate technical direction for regret-minimization-inspired self-play.
- Action: Treat as research route; do not assume direct four-player Tenhou transfer without experiment.

### 2026-05-28 — Open-source baselines

- Claim: Mortal is an open-source Japanese mahjong AI powered by deep reinforcement learning.
- Source:
  - https://github.com/Equim-chan/Mortal
  - https://mortal.ekyu.moe/
- Relevance: Candidate baseline and implementation reference.

- Claim: Akochan is an open-source Japanese mahjong AI.
- Source:
  - https://github.com/critter-mj/akochan
- Relevance: Candidate reviewer/search/baseline reference.

- Claim: Kanachan is an open-source riichi mahjong AI project targeting Mahjong Soul rules and top AI strength.
- Source:
  - https://github.com/Cryolite/kanachan
- Relevance: Candidate architecture/data/reference route.

- Claim: Archer describes itself as a top-tier Mahjong AI development framework with Tenhou 10 dan experience.
- Source:
  - https://github.com/moxcomic/archer
- Relevance: Candidate Tenhou-oriented framework reference.

## 2026-05-28 — v0.3 algorithm table evidence notes

- LuckyJ target: Haobo Fu page reports LuckyJ reached Tenhou 10 dan on 2023-05-30, from scratch under 1500 matches, with stable rank 10.68 among players with more than 1000 games in Tenhou expert room. URL: https://haobofu.github.io/
- LuckyJ public news: TechNode reported Tencent LuckyJ reached Tenhou 10 dan and stable rank 10.68. URL: https://technode.com/2023/07/12/tencents-mahjong-ai-sets-new-gaming-record-on-international-mahjong-platform/
- Suphx method: arXiv/ar5iv paper describes global reward prediction, oracle guiding and run-time policy adaptation. URL: https://ar5iv.labs.arxiv.org/html/2003.13590
- Suphx performance/statistics: paper reports 5000+ Tenhou games, 10 dan, stable rank 8.74, and low fourth-place/deal-in statistics. URL: https://ar5iv.labs.arxiv.org/html/2003.13590
- ACH: OpenReview page describes Actor-Critic Hedge for large-scale imperfect-information 1-on-1 Mahjong, combining actor-critic with counterfactual-regret ideas. URL: https://openreview.net/forum?id=DTXZqTNV5nW
- Mortal: GitHub describes Mortal as a free open-source Japanese Mahjong AI powered by deep reinforcement learning. URL: https://github.com/Equim-chan/Mortal
- Akochan: GitHub describes akochan as an artificial intelligence for Japanese mahjong and documents build/selfmatch usage. URL: https://github.com/critter-mj/akochan
- Kanachan: GitHub describes a four-player Japanese riichi Mahjong AI framework for Mahjong Soul rules and a goal of beating NAGA/Suphx/top professionals. URL: https://github.com/Cryolite/kanachan
- Archer: GitHub describes Archer as a top-tier Mahjong AI development framework, claiming Tenhou 10 dan on Phoenix. URL: https://github.com/moxcomic/archer
- Tenhou stable-dan formulas: Tenhou manual lists four-player stable-rank-equivalent formulas for general, upper, tokujou and phoenix rooms. URL: https://tenhou.net/man/

## 2026-05-28 — v0.4 racing-funnel methodology note

- Claim: v0.4 does not add new external strength claims. It reorganizes existing Suphx / LuckyJ / Mortal / Akochan / Kanachan / Archer evidence into a staged racing-funnel process.
- Source: internal project methodology decision from discussion.
- Relevance: Prevents wasteful full training of all candidates and keeps algorithm selection tied to Tenhou stable dan, pt EV, average placement and fourth-place control.
- Action: Future external claims must still be logged with source, date checked and project relevance before changing candidate priority.

## 2026-05-28 — Mortal F1 initial reproducibility audit

- Candidate: Mortal.
- Funnel stage after audit: F1 Reproduce blocked.
- Checked repository: `Equim-chan/Mortal`.
- Checked commit: `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
- Sources:
  - https://github.com/Equim-chan/Mortal
  - https://github.com/Equim-chan/Mortal/blob/main/README.md
  - https://github.com/Equim-chan/Mortal/blob/main/LICENSE
  - https://github.com/Equim-chan/Mortal/blob/main/docs/src/user/build.md
  - https://github.com/Equim-chan/Mortal/blob/main/docs/src/user/docker.md
  - https://github.com/Equim-chan/Mortal/blob/main/Dockerfile
  - https://github.com/Equim-chan/Mortal/blob/main/environment.yml
  - https://github.com/Equim-chan/Mortal/blob/main/.github/workflows/libriichi.yml
- Source facts:
  - README describes Mortal as a free/open-source Japanese mahjong AI powered by deep reinforcement learning.
  - Code license is AGPL-3.0-or-later; logo and other assets are CC BY-SA 4.0.
  - Repository is a Rust workspace with `libriichi` and `exe-wrapper`; Python inference code lives under `mortal/`.
  - Build documentation requires Python, an up-to-date Rust compiler, PyTorch, and `cargo build -p libriichi --lib --release`.
  - Docker inference path is designed for mjai inference, not training, and requires a trained model file mounted separately.
  - The mjai path consumes newline-separated JSON events and emits JSON reactions such as `dahai` or `none`, with optional metadata including q-values, mask bits, shanten and evaluation time.
- Local check facts:
  - `git clone --depth 1 https://github.com/Equim-chan/Mortal.git` failed because local shell DNS could not resolve `github.com`.
  - `git ls-remote https://github.com/Equim-chan/Mortal.git HEAD` failed for the same reason.
  - Local DNS lookup for `github.com` and `raw.githubusercontent.com` failed.
  - `python3 --version` returned Python 3.9.6.
  - `rustc`, `cargo`, `docker` and `conda` were not found.
  - PyTorch was not installed in the default Python environment.
- Result: minimal local inference sample was not run. This is an environment/artifact blocker, not evidence that Mortal itself is unsuitable.
- Action: resolve local source/toolchain/model-artifact blockers before retrying Mortal F1; do not proceed to F2 yet.

## 2026-05-28 — Mortal F1 blocker-resolution attempt

- Candidate: Mortal.
- Funnel stage after attempt: F1 Reproduce blocked.
- Source artifact:
  - URL pattern: `https://codeload.github.com/Equim-chan/Mortal/tar.gz/0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`
  - Retrieval method: `curl --resolve codeload.github.com:443:20.205.243.165`.
  - Local temporary path: `/tmp/mjlabai_mortal_src_zMLVHS/mortal.tar.gz`.
  - SHA256: `6531f46ba2f2b40a69528bf5362f9c89294ad72521aec4f59e208400c379e62c`.
  - Extracted top-level directory: `Mortal-0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
- Git access:
  - `git -c http.curloptResolve=github.com:443:20.205.243.166 ls-remote https://github.com/Equim-chan/Mortal.git HEAD` returned `0cff2b52982be5b1163aa9a62fb01f03ce91e0d2`.
  - `git clone` with the same local resolution path still failed to connect after timeout.
- Model artifact evidence:
  - README points to gist `cf3f01735d5d98f1e7be02e94b288c56` for trained model details.
  - Gist API URL: `https://api.github.com/gists/cf3f01735d5d98f1e7be02e94b288c56`.
  - Retrieval method: `curl --resolve api.github.com:443:20.205.243.168`.
  - Local temporary path: `/tmp/mjlabai_mortal_gist.json`.
  - Gist JSON SHA256: `6677ddb33bb10b51ef0e09529be72f144c3e7f19af717ad1432663a19a4e6e04`.
  - Gist `updated_at`: `2026-05-05T07:47:24Z`.
  - Relevant gist statement: as of the 2022-08-19 update, the author says there is currently no plan to release the trained model.
- Environment check:
  - Python 3.12.13 exists at `/opt/homebrew/bin/python3.12`; a temporary venv was created successfully.
  - PyTorch is missing in that venv.
  - `cargo build -p libriichi --lib --release` could not start because `cargo` was not found.
  - `docker` was not found.
  - `brew info rust` failed while fetching Homebrew formula API because `formulae.brew.sh` could not be resolved.
- Result:
  - Official mjai minimal inference sample was not run.
  - This remains blocked mainly by missing trained model artifact, plus unresolved Rust/Cargo and Docker/native dependency path.
- Action:
  - Do not promote Mortal to F2.
  - Next project decision: provide a lawful trained Mortal model artifact with source/version/usage/checksum, or pause Mortal as runnable baseline and audit another baseline.

## 2026-05-29 — Technical-plan-first execution decision

- Type: internal governance / technical planning decision.
- Claim: `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` is now the current technical execution charter; the project uses technical-plan-first execution and treats papers as future summaries.
- Source: user instruction and local docs update on 2026-05-29.
- Relevance: Keeps execution tied to reproducible baselines, Tenhou-oriented metrics, racing-funnel gates and documented Codex tasks.
- Evidence status: internal decision, not external model-strength evidence.
- Action: Follow `docs/12_technical_plan/12A_TECHNICAL_PLAN_v0.1.md` and keep `docs/10_next/10_NEXT.md` as the single next-task queue.
