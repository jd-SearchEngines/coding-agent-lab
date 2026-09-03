"""Run every Season 1 version on the same fixed cases and write a scorecard."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from run_version import run

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = [("minimal", 1), ("explore", 2), ("edit", 3), ("verify", 4), ("managed", 6)]


def main() -> None:
    all_rows = []
    for version, episode in VERSIONS:
        rows = run(version, episode)
        output = ROOT / f"runs/manifests/eval_{version}.jsonl"
        with output.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row) + "\n")
        all_rows.extend(rows)

    summaries = []
    for version, _episode in VERSIONS:
        rows = [row for row in all_rows if row["requested_version"] == version]
        summaries.append(
            {
                "version": rows[0]["version"],
                "requested_version": version,
                "case_count": len(rows),
                "pass": sum(row["external_test_pass"] for row in rows),
                "false_finish": sum(row["false_finish"] for row in rows),
                "avg_steps": round(sum(row["steps"] for row in rows) / len(rows), 3),
                "avg_latency_ms": round(sum(row["latency_ms"] for row in rows) / len(rows), 3),
                "tool_failures": sum(row["tool_failures"] for row in rows),
                "permission_denials": sum(row["permission_denials"] for row in rows),
                "cost_usd": None,
                "model_runs": 0,
            }
        )
    summary_path = ROOT / "reports/season1/metrics_summary.csv"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)
    (ROOT / "runs/manifests/season1_eval.json").write_text(
        json.dumps({"config": "evals/configs/season1.json", "rows": all_rows}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(summary_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()

