# EP01 report — 100行代码真的能做 Coding Agent 吗？

## Evidence status

`PASS_WITH_LIMITS`: the minimal loop and deterministic run are real and
reproducible. No provider-backed LLM run was available, so this is not evidence
of LLM task-solving quality.

## Change

The baseline has the smallest useful shape: task input, model response, shell
environment, observation history, a bounded loop, and a final self-report.

## Run

Command: `PYTHONPATH=src python3 scripts/run_baseline.py`

The raw per-case manifest is `runs/manifests/ep01_baseline.jsonl`; the summary
is `runs/manifests/ep01_summary.json`. Each case is copied to a fresh workspace
and independently verified with `pytest -q` after the agent stops.

## Result

The baseline self-reports success for every case while making no code change.
External tests fail for every case. This produces a real false-finish signal,
not a synthetic metric typed into the report.

## Gap

The baseline has no repo exploration, structured edit, external verification,
permission boundary, recovery, or regression harness. The dataset is currently
five local synthetic fixtures; a public historical issue reproduction remains a
known gap.

