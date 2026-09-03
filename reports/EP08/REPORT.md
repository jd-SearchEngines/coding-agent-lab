# EP08 report — 工业级 Coding Agent 到底多了什么？

## Evidence status

`PASS_WITH_LIMITS`: the final composition re-ran the fixed five-case benchmark
and passed 5/5 with zero final false finishes. This is a small deterministic
teaching benchmark, not production validation or a claim of superiority over
OpenHands or SWE-agent.

## Final result

Command: `PYTHONPATH=src python3 scripts/run_final_benchmark.py`

The final manifest is `runs/manifests/ep08_final.jsonl` and the summary is
`runs/manifests/ep08_final_summary.json`. The run records 5/5 passes, 0 false
finishes, 5 permission denials, 10 tool failures, and `cost_usd=null`.

## What actually improved

External verification is the largest measured improvement: false finishes fall
from 5/5 in the minimal version to 0/5 after the verify loop. The managed
version additionally makes permission denials and recovery events observable.

## What did not improve / remains open

The corpus is synthetic, the scripted model is not an LLM, and no provider
tokens/costs were available. Production-grade sandboxing, durable state,
multi-tenant isolation, model quality, public Issue coverage, cancellation,
and human review remain gaps.

