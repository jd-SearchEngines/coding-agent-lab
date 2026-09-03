# Season 1 Master Report

## 1. Project Goal

Build a small, runnable coding agent that turns a GitHub-Issue-shaped task into
understanding, exploration, editing, testing, verification, recovery, and an
auditable result. This is an engineering teaching project, not a leaderboard
claim.

## 2. Baseline Architecture

`Task → ScriptedModel → LocalEnvironment → Observation → bounded loop → DONE`

The baseline is shaped after the minimal loop of
[SWE-agent/mini-SWE-agent](https://github.com/SWE-agent/mini-swe-agent), with
upstream attribution and MIT notice preserved in `docs/UPSTREAM.md` and
`licenses/mini-swe-agent-LICENSE.md`.

## 3. Final Architecture

`Issue → Understand → Explore → Edit → External Verify → State/Recovery → Result`

Cross-cutting controls are permission policy, workspace boundary, timeout,
retry budget, action audit, latency/step fields, and fixed regression eval.
See `docs/architecture/final-capability-map.mmd`.

## 4. Episode-by-Episode Changes

| Version | Commit | Change |
|---|---|---|
| v0.1 | `0545336fdcdc776919991afb332916d2d52175f1` | minimal loop + baseline run |
| v0.2 | `73b464fb60b23b97b3dc5bb455292ba3e1c2d8b6` | bounded repo exploration |
| v0.3 | `6cc8e6be10313b180e8caf321fb15e99268319b8` | structured edit + diff |
| v0.4 | `e4931bf0daa1401bebf91a23534ba44bcc577b8d` | external verify + replan |
| v0.5 | `c089c029c2713a5ab0b47483dd5f9758ac13aea8` | command permission boundary |
| v0.6 | `e22bfa56c52858494a7c1c52b858d2b03c2977d5` | state + recovery budget |
| v0.7 | `ac4a4e3ebf4922793d7cbd5f01fea4b4cfa6e771` | regression harness |
| v1.0 | `f71c2a9f1e251cb964965a352b04e869a190e94c` | final benchmark |

## 5. Final Dataset

Five small Python fixtures live in `cases/case_001` through `case_005`. Every
case has task metadata and a pytest oracle. They are all `synthetic`; the
planned public-Issue corpus was not completed and is a known gap.

## 6. Baseline Metrics

The baseline run has 0/5 external passes, 5/5 self-reported successes, and 5
false finishes. See `runs/manifests/ep01_baseline.jsonl`.

## 7. Final Metrics

The v1.0 deterministic run has 5/5 external passes, 0 final false finishes,
5 permission denials, 10 failed tool actions, average 19 steps, and
`cost_usd=null`. See `runs/manifests/ep08_final_summary.json`.

## 8. Version Comparison

See `metrics_summary.csv`. The current machine-generated scorecard is:

| Version | Pass | False Finish | Avg Steps | Avg Latency (ms) | Cost |
|---|---:|---:|---:|---:|---|
| v0.1 minimal | 0/5 | 5 | 1.0 | 433.418 | null |
| v0.2 explore | 0/5 | 5 | 7.0 | 477.989 | null |
| v0.3 edit | 5/5 | 0 | 7.0 | 447.702 | null |
| v0.4 verify | 5/5 | 0 | 13.0 | 1274.155 | null |
| v0.6 managed | 5/5 | 0 | 19.0 | 1291.920 | null |

Latency is host/run dependent; cost is null because no provider token data
exists. The final benchmark is a fresh v1.0 alias of the managed composition.

## 9. Failure Taxonomy

See `failure_taxonomy.md`. Observed categories include verify failure, missing
context, wrong patch, tool failure, permission boundary, and recovery success.
Timeout and recovery failure were not observed in the final deterministic run.

## 10. Representative Bad Cases

- Baseline: self-report success while pytest fails, 5/5.
- Verify: wrong patch causes pytest failure, then a corrected patch passes, 5/5.
- Managed: `cat /etc/passwd` receives a permission denial, 5/5.
- State: repeated failures stop after retry budget in `tests/test_state.py`.

## 11. What Actually Improved

The externally measured change is the verify gate: false finishes drop from 5/5
to 0/5 once a failing test is observed and repaired. Exploration adds useful
context traces but alone does not improve task pass rate. Managed execution
adds visible boundary events without changing final pass rate on this easy set.

## 12. What Did Not Improve

The benchmark does not show whether a real LLM understands arbitrary repos,
whether public Issue tasks improve, or whether a production sandbox is secure.
It also does not measure cost because there are no provider tokens.

## 13. Cost / Latency Impact

Latency is persisted for each local run and shown in the CSV. Cost is `null`,
not zero. There is no legal provider-model run in this environment.

## 14. Production Gaps

Public Issue reproductions, provider-model trajectories, token/cost accounting,
strong sandbox/VM isolation, network policy, durable state/resume, cancellation,
multi-tenant authorization, human review, secret handling, and larger
regression coverage remain open.

## 15. Key Engineering Lessons

Self-report is not ground truth; context, edit, verify, permissions, state,
recovery, and regression are separate capabilities; failures are evidence;
and a deterministic harness can validate system mechanics without pretending to
measure model intelligence.

## 16. Final Architecture Diagram

`docs/architecture/final-capability-map.mmd`

