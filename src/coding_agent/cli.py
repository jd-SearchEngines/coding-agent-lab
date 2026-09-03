"""Small CLI for running one deterministic baseline task."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agent import LocalEnvironment, MinimalAgent, ScriptedModel


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("task")
    parser.add_argument("--case-id", default="case_001")
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    args = parser.parse_args()
    result = MinimalAgent(ScriptedModel(args.case_id), LocalEnvironment(args.workspace)).run(
        args.task, args.case_id
    )
    print(json.dumps(result.__dict__, default=lambda value: value.__dict__, indent=2))

