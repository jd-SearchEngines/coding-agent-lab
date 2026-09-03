# Video Master Evidence

## Title

《从100行Coding Agent到工业级Agent：一个真实项目完整复盘》

## Hook Evidence

In v0.1, all five cases self-reported success, while external pytest passed
0/5. The raw evidence is `runs/manifests/ep01_baseline.jsonl`; this is the
central conflict: “Agent says done” versus “repository test says fail”.

## Baseline Architecture

`Task → Model → Tool → Observation → Loop → Final`

Commit: `0545336fdcdc776919991afb332916d2d52175f1`.

## Biggest 3 Failures

1. Self-report false finish: 5/5 baseline cases.
2. Wrong patch: verify and managed versions each retain five initial pytest
   failures before replanning.
3. Unsafe intent: managed version blocks five `/etc/passwd` attempts.

## Important Turning Points

- EP02 makes repository search/read observable, but proves exploration alone is
  not enough: still 0/5.
- EP03 adds bounded editing and reaches 5/5 on this fixed fixture set.
- EP04 makes external verification a gate and preserves failure/replan traces.
- EP05–EP06 add permission and bounded recovery rather than silent retries.
- EP07 turns anecdotes into a fixed scorecard; EP08 re-runs it as v1.0.

## Representative Case

`case_001` is the clearest small repair: a broken `normalize_name` function,
an intentionally wrong first patch, a failing pytest observation, a corrected
patch, and a passing pytest. It is synthetic, not a historical GitHub Issue.

## Baseline vs Final

| | v0.1 minimal | v1.0 final |
|---|---:|---:|
| External pass | 0/5 | 5/5 |
| False finish | 5 | 0 |
| Permission denials | 0 | 5 blocked |
| Cost | null | null |
| Model provider runs | 0 | 0 |

## Final Architecture

`Issue → Understand → Explore → Edit → Verify → Replan/Recover → Result`,
surrounded by permission, timeout, retry, audit, observability, and regression
controls. Diagram: `docs/architecture/final-capability-map.mmd`.

## Production Trade-offs

Each guard adds steps and latency: current average steps rise from 1 to 19.
The managed policy improves observability and safety for the probe but is only a
string policy, not a secure production sandbox. Cost is unknown, not free.

## What Model Solved

In this repository, the scripted model emits the deterministic sequence of
explore, patch, test, and replan actions. No conclusion about a real LLM's
reasoning ability is supported because provider credentials were unavailable.

## What Harness Solved

The harness solved reproducibility, external test gating, changed-file capture,
permission denial, retry termination, per-case traces, and version comparison.

## What Still Fails

There is no public-Issue corpus, provider-backed trajectory, token/cost
telemetry, strong sandbox, durable resume, network isolation, human review, or
large-scale regression benchmark.

## Final Engineering Conclusion

The same model loop is not automatically a production coding agent. The model
can propose actions, but the surrounding system must decide what context it
gets, what it may execute, whether a patch actually works, how failures update
state, when to stop, and how to compare versions. This project's evidence
supports that systems lesson within a five-case deterministic fixture set; it
does not support a claim of production readiness.

