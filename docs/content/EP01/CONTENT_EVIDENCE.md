# Project Day

Build Coding Agent | 04/09

# Current Version

`v0.1-minimal`

# Today's Project Goal

Test whether a minimal task/model/tool/observation loop is sufficient for a
small code task.

# Real Problem

The model can emit a completion message without changing code or running a
test. A self-report is an observation, not proof.

# Real Case

`case_001` through `case_005`; all are explicitly marked `synthetic` local
teaching fixtures.

# Before

The repository contains intentionally failing implementations.

# Code Change

Added the minimal linear loop and a deterministic scripted model.

# Key Diff

`src/coding_agent/agent.py` records model turns and the final self-report.

# Run

`PYTHONPATH=src python3 scripts/run_baseline.py`

# Result

See `runs/manifests/ep01_summary.json` and
`runs/manifests/ep01_baseline.jsonl`. The run recorded 5 self-reported
successes and 5 external test failures.

# Bad Case

Every case is a false finish: `self_reported_success=true` and
`external_test_pass=false`.

# One Core Knowledge Point

Minimal Agent Loop.

# Before / After

Before: no runnable agent or persisted evidence.

After: runnable bounded loop, self-report, and external result recorded
separately.

# Current Capability Checklist

✅ Understand (task input)  
❌ Explore  
❌ Edit  
❌ Verify  
❌ Sandbox  
❌ Recovery  
❌ Eval

# Commit SHA

`5be3c77f0246ff206c01e7302aa6e3675f924901`

# Next Gap

The agent must inspect a repository and make a constrained, observable edit.

# Candidate Visual Evidence

- `src/coding_agent/agent.py` loop
- `runs/manifests/ep01_baseline.jsonl`
- `runs/manifests/ep01_summary.json`
- false-finish terminal output in `REPORT.md`
