# Project Day

Build Coding Agent | 04/09

# Current Version

`v0.6-recovery`

# Today's Project Goal

Add explicit state, retry budget, and recovery termination.

# Real Problem

Fail → retry → retry can repeat the same mistake forever.

# Real Case

The managed run has one denied command and one intentionally wrong patch/test
failure per case; all five cases are synthetic fixtures.

# Before

EP05 had bounded outer steps but no named recovery state or termination reason.

# Code Change

Added `RecoveryState`, `RecoveryController`, and retry/recovery fields to the
run manifest.

# Key Diff

`state.py` changes `acting → replanning → verified` or
`replanning → stopped` when the budget is exhausted.

# Run

`PYTHONPATH=src python3 scripts/run_version.py managed --episode 6 --output runs/manifests/ep06_runs.jsonl`

# Result

5/5 pass, 10 retries, 5 recovery successes; all final termination reasons are
`verified`.

# Bad Case

`tests/test_state.py` preserves a repeated-failure probe that stops after the
third failure instead of retrying without bound.

# One Core Knowledge Point

State + Recovery.

# Before / After

Before: fail → retry with no state.

After: fail → diagnose/update state → replan or stop.

# Current Capability Checklist

✅ Understand  
✅ Explore  
✅ Edit  
✅ Verify  
✅ Sandbox  
✅ Recovery  
❌ Eval

# Commit SHA

`e22bfa56c52858494a7c1c52b858d2b03c2977d5`

# Next Gap

Compare versions over a fixed regression harness rather than individual runs.

# Candidate Visual Evidence

- `docs/architecture/recovery-tree.mmd`
- `src/coding_agent/state.py`
- `runs/manifests/ep06_summary.json`
- `tests/test_state.py`
