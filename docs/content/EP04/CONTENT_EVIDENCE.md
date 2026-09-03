# Project Day

Build Coding Agent | 04/09

# Current Version

`v0.4-verify`

# Today's Project Goal

Make external tests, rather than the model's DONE message, the success gate.

# Real Problem

An agent can say “completed” after a wrong patch.

# Real Case

Five synthetic fixtures in `cases/`; each has a deterministic pytest oracle.

# Before

EP03 direct edit stopped without in-loop verification.

# Code Change

Added `ExternalVerifier` plus failure-aware scripted replanning.

# Key Diff

`src/coding_agent/verification.py` returns a separate pass/fail result and
timeout code.

# Run

`PYTHONPATH=src python3 scripts/run_version.py verify --episode 4 --output runs/manifests/ep04_runs.jsonl`

# Result

5 final passes, 5 initial test failures, 5 recovery successes; the failed
attempts remain in the JSONL trace.

# Bad Case

The first patch is wrong by design. Without the verifier it would be a false
finish; with the verifier it becomes a replan signal.

# One Core Knowledge Point

Verify.

# Before / After

Before: LLM says complete → finish.

After: edit → test → failure observation → replan → test → finish.

# Current Capability Checklist

✅ Understand  
✅ Explore  
✅ Edit  
✅ Verify  
❌ Sandbox  
❌ Recovery  
❌ Eval

# Commit SHA

`e4931bf0daa1401bebf91a23534ba44bcc577b8d`

# Next Gap

Define what commands the agent is allowed to execute.

# Candidate Visual Evidence

- `docs/architecture/verification-loop.mmd`
- `runs/manifests/ep04_runs.jsonl`
- `tool_failures=5` and final `passed=5`
- `src/coding_agent/verification.py`
