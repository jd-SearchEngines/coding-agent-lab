# EP05 report — 它开始执行 Shell 了，我敢把电脑交给它吗？

## Evidence status

`PASS_WITH_LIMITS`: a real managed run blocked five explicit workspace-escape
attempts and still completed the five local repairs. This is a teaching policy,
not a claim of OS-grade sandbox isolation.

## Change

Added `CommandPolicy` and `ManagedEnvironment`. Denied commands return a
permission observation without invoking the shell. Allowed commands remain
workspace-scoped subprocesses.

## Run and result

Command: `PYTHONPATH=src python3 scripts/run_version.py managed --episode 5 --output runs/manifests/ep05_runs.jsonl`

Result: 5/5 external passes, 5 permission denials, 10 tool failures total
(the five denials plus five intentional first-test failures), and 0 false
finishes. The per-action evidence records `denied=true` for the boundary case.

## Gap

The policy is string-based and intentionally minimal. It is not a replacement
for a container, VM, OS MAC policy, network egress control, or production
approval workflow.

