# Project Day

Build Coding Agent | 04/09

# Current Version

`v1.0-final`

# Today's Project Goal

Re-run the fixed dataset through the complete production-oriented composition.

# Real Problem

Model + tool loop is not a production agent without evidence, boundaries,
state, and regression controls.

# Real Case

The same five synthetic fixture cases used throughout Season 1.

# Before

`v0.1-minimal`: 0/5 external passes and 5 false finishes.

# Code Change

Added the explicit `ProductionAgent` composition boundary and final benchmark.

# Key Diff

`ProductionCapabilities` records capabilities and known non-capabilities such
as provider cost telemetry (`false` / `null` in this run).

# Run

`PYTHONPATH=src python3 scripts/run_final_benchmark.py`

# Result

5/5 external passes, 0 false finishes, 5 permission denials, 10 tool failures,
and `cost_usd=null`.

# Bad Case

The final run still includes the denied `/etc/passwd` attempt and wrong-patch
test failures; they are recovered/blocked and remain in the manifest.

# One Core Knowledge Point

Minimal → Production Coding Agent capability map.

# Before / After

Before: model + shell + self-report.

After: understand → explore → edit → verify → state/recover, under permission
and timeout boundaries, with audit and regression evidence.

# Current Capability Checklist

✅ Understand  
✅ Explore  
✅ Edit  
✅ Verify  
✅ Sandbox (minimal policy)  
✅ State  
✅ Recovery  
✅ Eval  
⚠️ Cost telemetry unavailable (`null`)  
⚠️ Provider LLM run blocked

# Commit SHA

Filled after the final benchmark commit.

# Next Gap

Replace synthetic fixtures with public Issue reproductions and execute a legal
provider-backed run with token/cost telemetry.

# Candidate Visual Evidence

- `docs/architecture/final-capability-map.mmd`
- `runs/manifests/ep08_final.jsonl`
- `runs/manifests/ep08_final_summary.json`
- `src/coding_agent/production.py`

