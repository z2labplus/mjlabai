# 07B_TASK_BACKLOG

| Task | Stage | Priority | Depends on | Acceptance criteria | Status |
|---|---|---|---|---|---|
| Run rule-load test | setup | P0 | docs initialized | Codex summarizes rules without modifying files | Done |
| Apply algorithm racing funnel | 04/05/07 | P0 | rule-load passed | candidate stages and next lowest-cost experiments confirmed | Done |
| Mortal F1 reproducibility audit | 04/07 | P0 | racing funnel confirmed | install/build, license, minimal run, I/O notes, logging ability checked; no training | Blocked: source/toolchain/model artifact |
| Resolve Mortal F1 blockers and rerun mjai sample | 04/07/09 | P0 | Mortal F1 initial audit | Source clone works, minimal dependencies are available, model artifact is documented, official mjai sample runs without training | Blocked: no public trained model artifact |
| Decide Mortal F1 continuation path | 04/07/09 | P0 | Mortal model artifact unavailable | Lawful user-provided model artifact is recorded, or Mortal is paused as runnable baseline and next baseline F1 is selected | Planned |
| Define Mortal F2 adapter/legal-action task | 04/06 | P0 | Mortal F1 passes | state/action mapping, legal action validator and decision log schema specified | Planned |
| Verify Archer evidence | 04/09 | P1 | racing funnel confirmed | Tenhou claim, weights/logs/protocol/build path recorded before baseline use | Planned |
| Akochan F1 reproducibility audit | 04/07 | P1 | first baseline path started | build/self-match feasibility recorded | Planned |
| Kanachan transfer review | 02/03/04 | P1 | candidate table stable | schema/model/data ideas mapped to Tenhou transfer risks | Planned |
| Suphx method decomposition | 03/04/05 | P0 | evaluation harness draft | SL, self-play RL, GRP, oracle guiding and runtime adaptation experiment cards created | Planned |
| Implement Tenhou stable-dan calculator | 05 | P0 | metric spec | room-specific formulas and bootstrap requirement documented/tested | Planned |
| Create tiny benchmark harness | 05/06 | P0 | adapter spec | legal action rate, latency, fixed-position decisions and result table recorded | Planned |
| Define replay schema | 02 | P0 | benchmark metrics stable | `02B_REPLAY_SCHEMA.md` filled | Planned |
| Build legal action reconstruction test | 02 | P0 | schema | test plan exists | Planned |
