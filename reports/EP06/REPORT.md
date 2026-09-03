# EP06 report — Agent 失败以后为什么不能无脑 Retry？

## Evidence status

`PASS_WITH_LIMITS`: the final deterministic run contains tool failures,
permission failures, replanning, and successful recovery. A unit-level probe
also proves repeated failures terminate at a bounded retry budget.

## Change

Added `RecoveryState` and `RecoveryController`. Failure transitions now carry a
retry count and either choose `replan` or stop with an explicit reason. The
current scripted agent demonstrates this protocol through its failed-test and
permission observations.

## Run and result

Command: `PYTHONPATH=src python3 scripts/run_version.py managed --episode 6 --output runs/manifests/ep06_runs.jsonl`

Result: 5/5 external passes, 10 failed tool actions, 10 recorded retries, 5
recovery successes, and `termination_reason=verified` for every case. The
state unit probe stops after three failures with a retry-budget reason.

## Gap

The scripted model's plan is deterministic and does not yet diagnose arbitrary
provider failures. Real LLM runtime traces, cancellation, and durable resume
are still production gaps.

