"""Run one deterministic agent version over the fixed Season 1 dataset."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from coding_agent.agent import LocalEnvironment, ManagedEnvironment, MinimalAgent, ScriptedModel

ROOT = Path(__file__).resolve().parents[1]


def tree_hash(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob("*")):
        if path.is_file():
            result[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def run(version: str, episode: int) -> list[dict]:
    rows = []
    for workspace in sorted((ROOT / "cases").glob("case_*/workspace")):
        case_id = workspace.parent.name
        with tempfile.TemporaryDirectory(prefix=f"{version}-{case_id}-") as temp:
            run_root = Path(temp)
            shutil.copytree(workspace, run_root, dirs_exist_ok=True)
            before = tree_hash(run_root)
            environment = ManagedEnvironment(run_root) if version == "managed" else LocalEnvironment(run_root)
            started = time.perf_counter()
            agent_result = MinimalAgent(
                ScriptedModel(case_id, version), environment, max_steps=12
            ).run("complete the issue", case_id)
            verification = subprocess.run(
                ["python3", "-B", "-m", "pytest", "-q"],
                cwd=run_root,
                text=True,
                capture_output=True,
            )
            after = tree_hash(run_root)
            rows.append(
                {
                    "episode": episode,
                    "case_id": case_id,
                    "version": agent_result.version,
                    "requested_version": version,
                    "model_runtime": "deterministic_scripted",
                    "self_reported_success": agent_result.self_reported_success,
                    "external_test_pass": verification.returncode == 0,
                    "false_finish": agent_result.self_reported_success and verification.returncode != 0,
                    "steps": agent_result.steps,
                    "tool_failures": sum(action.returncode != 0 for action in agent_result.actions),
                    "permission_denials": sum(action.denied for action in agent_result.actions),
                    "changed_files": sorted(key for key in after if before.get(key) != after[key]),
                    "latency_ms": round((time.perf_counter() - started) * 1000, 3),
                    "cost_usd": None,
                    "actions": [
                        {
                            "command": action.command,
                            "returncode": action.returncode,
                            "denied": action.denied,
                            "stdout": action.stdout[-2000:],
                            "stderr": action.stderr[-2000:],
                        }
                        for action in agent_result.actions
                    ],
                    "verification_output": (verification.stdout + verification.stderr)[-4000:],
                }
            )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", choices=["minimal", "explore", "edit", "verify", "managed"])
    parser.add_argument("--episode", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = run(args.version, args.episode)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")
    summary = {
        "episode": args.episode,
        "version": args.version,
        "case_count": len(rows),
        "passed": sum(row["external_test_pass"] for row in rows),
        "failed": sum(not row["external_test_pass"] for row in rows),
        "self_reported_success": sum(row["self_reported_success"] for row in rows),
        "false_finish": sum(row["false_finish"] for row in rows),
        "avg_steps": round(sum(row["steps"] for row in rows) / len(rows), 3),
        "avg_latency_ms": round(sum(row["latency_ms"] for row in rows) / len(rows), 3),
        "tool_failures": sum(row["tool_failures"] for row in rows),
        "permission_denials": sum(row["permission_denials"] for row in rows),
        "cost_usd": None,
        "model_runs": 0,
    }
    summary_path = args.output.with_name(args.output.stem.replace("_runs", "") + "_summary.json")
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
