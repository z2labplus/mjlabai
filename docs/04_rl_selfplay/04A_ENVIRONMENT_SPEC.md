# 04A_ENVIRONMENT_SPEC

| Component | Requirement | Status |
|---|---|---|
| Legal action engine | Must exactly enforce rules | Planned |
| Scoring engine | Must match target ruleset | Planned |
| Hidden information | Must not leak unseen tiles | Planned |
| Opponent policies | Support league/self-play opponents | Planned |
| Logging | Full decision trace reproducible | Planned |
| Synthetic transition contract smoke | Prove one authoritative strict-action match and immutable state progression | Implemented in `src/mjlabai/environment/synthetic_transition_smoke.py`; not a rules engine |
| Proven local riichi environment path | Pin a maintained licensed environment exposing legal actions, state transition and observation | MahJax `v0.1.2` / commit `3f9cee1` / Apache-2.0 selected in `04J`; public init/observe/legal-step integration review-closed in `04K`; bounded single-round decision next |
| Bounded single-round environment rollout | Prove repeated authoritative legal transitions reach one terminal raw outcome under a hard cap | Exact 256-cap JIT/lowest-legal rollout review-closed in `04M` after global-seat-score fix; seed 0 terminates after 94 transitions |
| Bundled rule-policy environment bridge | Prove a pinned non-learned policy can select legal actions and reach one terminal raw outcome | Exact four-seat MahJax bundled rule-policy round review-closed in `04N`; seed 0 terminates after 54 legal transitions |
| Project model-output environment bridge | Encode only public decision-time observation and mask 87 project-owned linear model scores by environment legality | Exact 630-feature untrained linear-policy round approved in `04N`; direct implementation next |

## Invalid environment examples

- Hidden tiles leaked to the policy.
- Scoring does not match target Tenhou rules.
- Legal actions differ from real riichi rules.
- Opponents are too weak to expose high-dan mistakes.
