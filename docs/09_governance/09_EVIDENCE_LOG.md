# 09_EVIDENCE_LOG

## Rule

Every external claim must be logged with source, date checked, and project relevance.

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
