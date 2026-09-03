"""Run EP01 without an LLM and preserve the self-report/evidence split."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from coding_agent.agent import LocalEnvironment, MinimalAgent, ScriptedModel

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    cases = sorted((ROOT / "cases").glob("case_*/workspace"))
    output = ROOT / "runs/manifests/ep01_baseline.jsonl"
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    with output.open("w", encoding="utf-8") as handle:
        for workspace in cases:
            case_id = workspace.parent.name
            with tempfile.TemporaryDirectory(prefix=f"{case_id}-") as temp:
                run_root = Path(temp)
                shutil.copytree(workspace, run_root, dirs_exist_ok=True)
                started = time.perf_counter()
                result = MinimalAgent(
                    ScriptedModel(case_id), LocalEnvironment(run_root)
                ).run("complete the issue", case_id)
                verification = subprocess.run(
                    ["python3", "-B", "-m", "pytest", "-q"],
                    cwd=run_root,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                row = {
                    "episode": 1,
                    "case_id": case_id,
                    "version": result.version,
                    "model_runtime": "deterministic_scripted",
                    "self_reported_success": result.self_reported_success,
                    "external_test_pass": verification.returncode == 0,
                    "false_finish": result.self_reported_success and verification.returncode != 0,
                    "steps": result.steps,
                    "latency_ms": round((time.perf_counter() - started) * 1000, 3),
                    "cost_usd": None,
                    "verification_output": (verification.stdout + verification.stderr)[-4000:],
                }
                handle.write(json.dumps(row) + "\n")
                rows.append(row)
    summary = {
        "episode": 1,
        "version": "v0.1-minimal",
        "case_count": len(rows),
        "passed": sum(row["external_test_pass"] for row in rows),
        "failed": sum(not row["external_test_pass"] for row in rows),
        "self_reported_success": sum(row["self_reported_success"] for row in rows),
        "false_finish": sum(row["false_finish"] for row in rows),
        "model_runs": 0,
        "runtime_note": "No provider credentials; deterministic scripted protocol run only.",
    }
    (ROOT / "runs/manifests/ep01_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
