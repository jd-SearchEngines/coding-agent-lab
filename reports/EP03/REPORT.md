# EP03 report — 会改代码为什么不等于会修 Bug？

## Evidence status

`PASS_WITH_LIMITS`: the structured editor is real, path-bounded, and emits a
unified diff. The deterministic edit version passes 5/5 after one direct edit;
this is harness evidence, not LLM quality evidence.

## Change

Added `StructuredEditor` with workspace-bound path validation and diff capture.
The scripted edit agent first explores the file and then applies a complete
targeted replacement, preserving a changed-file record in the run manifest.

## Run and result

Command: `PYTHONPATH=src python3 scripts/run_version.py edit --episode 3 --output runs/manifests/ep03_runs.jsonl`

Result: 5 cases, 5 external passes, 0 false finishes, 5 changed target files.
The raw JSONL preserves the commands and verification output. The case_003
fixture constraint was corrected before this run because its prior expected
string exceeded its stated limit; that correction is part of the test-data
history, not a hidden Agent repair.

## Bad case and gap

The direct edit version has no external verification inside the loop and can
self-report after a bad patch. EP04 adds a failing test observation and a
replan. The dataset is still synthetic.

