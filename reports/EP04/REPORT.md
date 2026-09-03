# EP04 report — Agent 说修好了，你凭什么相信？

## Evidence status

`PASS_WITH_LIMITS`: an independent external verifier and a failure-triggered
replan are implemented. The deterministic version recovered all five cases.
This does not establish provider-model quality.

## Before / after

EP03 could apply a good patch but had no in-loop evidence. EP04 deliberately
applies the known-wrong patch first, runs pytest, observes failure, applies the
correct patch, and runs pytest again before finishing.

## Run and result

Command: `PYTHONPATH=src python3 scripts/run_version.py verify --episode 4 --output runs/manifests/ep04_runs.jsonl`

Result: 5/5 final external passes, 5/5 initial verification failures, 5/5
recovery successes, and 0 final false finishes. `tool_failures=5` is expected
and is preserved in the manifest as the turning point.

## Gap

The verifier currently runs local pytest with a fixed timeout and has no
production sandbox. EP05 adds a fail-closed command boundary.

