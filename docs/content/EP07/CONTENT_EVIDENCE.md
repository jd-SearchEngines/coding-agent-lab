# Project Day

Build Coding Agent | 04/09

# Current Version

`v0.7-eval`

# Today's Project Goal

Prove version changes with a small fixed regression harness.

# Real Problem

One successful demo cannot establish that V2 is better than V1.

# Real Case

The same five synthetic cases are run across minimal, explore, edit, verify,
and managed versions.

# Before

Results lived in episode-specific runs with no common scorecard.

# Code Change

Added `evals/configs/season1.json`, the season evaluator, CSV metrics, and
failure taxonomy.

# Key Diff

`scripts/run_season1_eval.py` fixes dataset/version/verification settings and
writes both aggregate and per-case evidence.

# Run

`PYTHONPATH=src python3 scripts/run_season1_eval.py`

# Result

0/5 → 0/5 → 5/5 → 5/5 → 5/5 across the cumulative versions; false finishes
drop from 5 to 0 at the verified version. Costs are `null`.

# Bad Case

The minimal and explore versions still false-finish all 5 cases. The harness
keeps them in the comparison instead of selecting only successful versions.

# One Core Knowledge Point

Regression Eval.

# Before / After

Before: isolated demo result.

After: fixed cases → fixed verification → version comparison → taxonomy.

# Current Capability Checklist

✅ Understand  
✅ Explore  
✅ Edit  
✅ Verify  
✅ Sandbox  
✅ Recovery  
✅ Eval

# Commit SHA

`ac4a4e3ebf4922793d7cbd5f01fea4b4cfa6e771`

# Next Gap

Run the integrated v1.0 benchmark and document production gaps without
overclaiming the small synthetic corpus.

# Candidate Visual Evidence

- `reports/season1/metrics_summary.csv`
- `reports/season1/failure_taxonomy.md`
- `runs/manifests/season1_eval.json`
- `evals/configs/season1.json`
