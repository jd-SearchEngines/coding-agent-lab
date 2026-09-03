# Project Day

Build Coding Agent | 04/09

# Current Version

`v0.3-edit`

# Today's Project Goal

Separate generating code from modifying the correct existing file.

# Real Problem

A patch can be syntactically valid yet target the wrong file or violate the
existing test contract.

# Real Case

`case_001` through `case_005`, synthetic and locally reproducible.

# Before

EP02 located files but changed nothing.

# Code Change

Added `StructuredEditor`, safe target resolution, and unified diff capture.

# Key Diff

`src/coding_agent/editor.py` emits a standard `a/...` / `b/...` diff and blocks
paths outside the workspace.

# Run

`PYTHONPATH=src python3 scripts/run_version.py edit --episode 3 --output runs/manifests/ep03_runs.jsonl`

# Result

5/5 external tests passed; 5 target files changed; cost is `null` because this
was a deterministic local run.

# Bad Case

The version can still declare completion without running a test inside its
loop. That verification gap is deliberately carried into EP04.

# One Core Knowledge Point

Action / Code Editing.

# Before / After

Before: locate-only, no patch.

After: targeted edit with a path check and diff evidence.

# Current Capability Checklist

✅ Understand  
✅ Explore  
✅ Edit  
❌ Verify  
❌ Sandbox  
❌ Recovery  
❌ Eval

# Commit SHA

`6cc8e6be10313b180e8caf321fb15e99268319b8`

# Next Gap

Do not trust a successful-looking patch until an external test runs.

# Candidate Visual Evidence

- `src/coding_agent/editor.py`
- `tests/test_exploration_and_edit.py`
- `runs/manifests/ep03_runs.jsonl`
- before/after changed-file list
