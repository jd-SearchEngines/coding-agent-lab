# Project Day

Build Coding Agent | 04/09

# Current Version

`v0.2-explore`

# Today's Project Goal

Make repository exploration explicit and bounded.

# Real Problem

Without locating the target file, a model cannot reliably act on a real repo.

# Real Case

Five synthetic fixtures in `cases/`, explicitly labeled in each README.

# Before

EP01 issued no tool action and false-finished all five cases.

# Code Change

Added `RepoExplorer` and scripted `find`/targeted `sed` actions.

# Key Diff

`src/coding_agent/explorer.py` constrains targeted reads to the workspace.

# Run

`PYTHONPATH=src python3 scripts/run_version.py explore --episode 2 --output runs/manifests/ep02_runs.jsonl`

# Result

All 5 cases generated bounded exploration traces; no files were changed and
external pass remained 0/5.

# Bad Case

Exploration alone still self-reports completion without a patch: 5 false
finishes remain.

# One Core Knowledge Point

Context Engineering.

# Before / After

Before: task → model → final.

After: task → search → targeted read → model → final.

# Current Capability Checklist

✅ Understand  
✅ Explore  
❌ Edit  
❌ Verify  
❌ Sandbox  
❌ Recovery  
❌ Eval

# Commit SHA

Filled after the episode commit.

# Next Gap

Turn located context into a constrained patch and retain the changed-file
record.

# Candidate Visual Evidence

- `src/coding_agent/explorer.py`
- `runs/manifests/ep02_runs.jsonl`
- `runs/manifests/ep02_summary.json`
- `reports/EP02/REPORT.md`

