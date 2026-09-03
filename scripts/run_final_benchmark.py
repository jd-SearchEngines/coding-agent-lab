"""Re-run the fixed Season 1 cases through the v1.0 composition."""

from __future__ import annotations

import json
from pathlib import Path

from run_version import run

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    rows = run("final", 8)
    output = ROOT / "runs/manifests/ep08_final.jsonl"
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")
    summary = {
        "episode": 8,
        "version": "v1.0-final",
        "case_count": len(rows),
        "passed": sum(row["external_test_pass"] for row in rows),
        "false_finish": sum(row["false_finish"] for row in rows),
        "avg_steps": round(sum(row["steps"] for row in rows) / len(rows), 3),
        "permission_denials": sum(row["permission_denials"] for row in rows),
        "cost_usd": None,
        "model_runs": 0,
        "runtime": "deterministic_scripted; provider LLM not configured",
    }
    (ROOT / "runs/manifests/ep08_final_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

