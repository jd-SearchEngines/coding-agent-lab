"""The Season 1 minimal loop: task -> model -> tool -> observation -> loop."""

from __future__ import annotations

import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class ShellResult:
    command: str
    returncode: int
    stdout: str
    stderr: str
    elapsed_ms: float


@dataclass
class AgentResult:
    case_id: str
    version: str
    status: str
    self_reported_success: bool
    steps: int
    elapsed_ms: float
    actions: List[ShellResult] = field(default_factory=list)


class LocalEnvironment:
    """A deliberately small command environment used by the baseline."""

    def __init__(self, root: Path, timeout_s: float = 10.0):
        self.root = Path(root)
        self.timeout_s = timeout_s

    def run(self, command: str) -> ShellResult:
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                command,
                shell=True,
                cwd=self.root,
                text=True,
                capture_output=True,
                timeout=self.timeout_s,
            )
            return ShellResult(
                command, completed.returncode, completed.stdout, completed.stderr,
                (time.perf_counter() - started) * 1000,
            )
        except subprocess.TimeoutExpired as exc:
            return ShellResult(
                command, 124, exc.stdout or "", f"TIMEOUT after {self.timeout_s}s",
                (time.perf_counter() - started) * 1000,
            )


class ScriptedModel:
    """A deterministic model substitute for protocol and harness testing.

    It deliberately emits a false finish in the minimal version. This makes
    the distinction between self-report and external verification observable.
    """

    def __init__(self, case_id: str):
        self.case_id = case_id
        self.calls = 0

    def respond(self, _history: List[str]) -> str:
        self.calls += 1
        if self.calls == 1:
            return "DONE: I inspected the task and completed the change."
        return "DONE: completed"


class MinimalAgent:
    def __init__(self, model: ScriptedModel, environment: LocalEnvironment, max_steps: int = 8):
        self.model = model
        self.environment = environment
        self.max_steps = max_steps

    def run(self, task: str, case_id: str) -> AgentResult:
        del task
        started = time.perf_counter()
        history: List[str] = []
        actions: List[ShellResult] = []
        self_reported_success = False
        for _ in range(self.max_steps):
            response = self.model.respond(history)
            history.append(response)
            if response.startswith("DONE:"):
                self_reported_success = True
                break
        return AgentResult(
            case_id=case_id,
            version="v0.1-minimal",
            status="self_reported_done" if self_reported_success else "step_budget_exhausted",
            self_reported_success=self_reported_success,
            steps=len(actions) + len(history),
            elapsed_ms=(time.perf_counter() - started) * 1000,
            actions=actions,
        )

