# EP07 report — 怎么证明 V2 真的比 V1 好？

## Evidence status

`PASS_WITH_LIMITS`: a fixed 5-case regression harness compares five cumulative
versions and preserves per-case traces. It is intentionally small and local;
it is not SWE-bench or a production quality benchmark.

## Run and result

Command: `PYTHONPATH=src python3 scripts/run_season1_eval.py`

The scorecard is `reports/season1/metrics_summary.csv`. Raw runs are in
`runs/manifests/eval_*.jsonl` and the aggregate replay is
`runs/manifests/season1_eval.json`. The deterministic scorecard records:

| Version | Pass | False finish | Avg steps | Cost |
| --- | ---: | ---: | ---: | --- |
| v0.1 minimal | 0/5 | 5 | 1.0 | null |
| v0.2 explore | 0/5 | 5 | 7.0 | null |
| v0.3 edit | 5/5 | 0 | 7.0 | null |
| v0.4 verify | 5/5 | 0 | 13.0 | null |
| v0.6 managed | 5/5 | 0 | 19.0 | null |

Latency is intentionally read from the machine-generated CSV and can vary by
host; cost is null because no provider token usage exists.

## Gap

The dataset has five synthetic cases and no provider-backed model runs. A
larger public-issue corpus, cross-host latency controls, and real token/cost
telemetry are still required for stronger claims.

