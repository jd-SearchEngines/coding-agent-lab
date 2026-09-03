# EP02 report — 它为什么看不懂一个真实 Repo？

## Evidence status

`PASS_WITH_LIMITS`: repository exploration is implemented and the run proves
the target file can be located and read with bounded commands. The explore-only
version intentionally does not edit, so external task success remains 0/5.

## Before / after

The EP01 baseline never issued a repository command and produced 5 false
finishes. EP02 adds a file listing and targeted file read before the final
self-report. It selects one target file per case rather than injecting an
entire repository into context.

## Run and result

Command: `PYTHONPATH=src python3 scripts/run_version.py explore --episode 2 --output runs/manifests/ep02_runs.jsonl`

All 5 cases produced an exploration trace containing `find` and `sed`. The
agent still changed no files, so this experiment demonstrates context location,
not end-to-end repair. That limitation is the result, not a hidden success.

## Gap

The case set is local synthetic data, not historical public GitHub issues. The
next stage adds structured edits and records changed files/diff evidence.

