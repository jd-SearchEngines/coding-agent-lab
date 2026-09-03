# Project Day

Build Coding Agent | 04/09

# Current Version

`v0.5-managed`

# Today's Project Goal

Enforce a permission boundary around shell execution.

# Real Problem

Model intent is not system permission; a command must be checked before it is
executed.

# Real Case

The managed scripted model tries `cat /etc/passwd` once in every fixture before
continuing with the repair. All fixtures are synthetic and labeled as such.

# Before

EP04 used a local shell environment with no explicit command policy.

# Code Change

Added `CommandPolicy` and `ManagedEnvironment`.

# Key Diff

Denied commands produce return code 126 and `PERMISSION_DENIED` without a
subprocess call.

# Run

`PYTHONPATH=src python3 scripts/run_version.py managed --episode 5 --output runs/manifests/ep05_runs.jsonl`

# Result

5/5 final external passes; 5 permission denials; all are retained in the raw
manifest.

# Bad Case

The first model action is an explicit boundary violation. It is denied, then
the agent receives the denial as an observation and continues.

# One Core Knowledge Point

Execution Boundary.

# Before / After

Before: Model intent → shell.

After: Model intent → policy → allowed workspace command or denied observation.

# Current Capability Checklist

✅ Understand  
✅ Explore  
✅ Edit  
✅ Verify  
✅ Sandbox (minimal teaching policy)  
❌ Recovery  
❌ Eval

# Commit SHA

Filled after the episode commit.

# Next Gap

Bound retries and state transitions so failure does not become an infinite
loop.

# Candidate Visual Evidence

- `docs/architecture/permission-boundary.mmd`
- `runs/manifests/ep05_runs.jsonl`
- `permission_denials=5`
- `src/coding_agent/permission.py`

