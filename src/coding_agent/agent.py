"""The Season 1 minimal loop: task -> model -> tool -> observation -> loop."""

from __future__ import annotations

import re
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from .case_specs import CASE_SPECS


@dataclass
class ShellResult:
    command: str
    returncode: int
    stdout: str
    stderr: str
    elapsed_ms: float
    denied: bool = False


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


class ManagedEnvironment(LocalEnvironment):
    """A small fail-closed boundary for the teaching harness."""

    DENY_PATTERNS = ("/etc/", "../", "rm -rf", "git reset --hard", "curl ", "wget ")

    def run(self, command: str) -> ShellResult:
        if any(pattern in command for pattern in self.DENY_PATTERNS):
            return ShellResult(command, 126, "", "PERMISSION_DENIED: command outside policy", 0, True)
        return super().run(command)


class ScriptedModel:
    """A deterministic model substitute for protocol and harness testing.

    It deliberately emits a false finish in the minimal version. This makes
    the distinction between self-report and external verification observable.
    """

    def __init__(self, case_id: str, version: str = "minimal"):
        self.case_id = case_id
        self.version = "managed" if version == "final" else version
        self.requested_version = version
        self.calls = 0

    def respond(self, _history: List[str]) -> str:
        self.calls += 1
        spec = CASE_SPECS[self.case_id]
        if self.version == "minimal":
            return "DONE: I inspected the task and completed the change."
        if self.version == "explore":
            if self.calls == 1:
                return "CMD: find . -maxdepth 2 -type f | sort"
            if self.calls == 2:
                return f"CMD: sed -n '1,80p' {spec.target}"
            return "DONE: located the target and completed the task."
        if self.version == "edit":
            if self.calls == 1:
                return "CMD: find . -maxdepth 2 -type f | sort"
            if self.calls == 2:
                return f"CMD: {spec.write_command(spec.good)}"
            return "DONE: patch applied."
        if self.version == "verify":
            if self.calls == 1:
                return f"CMD: {spec.write_command(spec.wrong)}"
            if self.calls == 2:
                return "CMD: python3 -B -m pytest -q"
            if any("FAILED" in item or "failed" in item for item in _history):
                if self.calls == 3:
                    return f"CMD: {spec.write_command(spec.good)}"
                if self.calls == 4:
                    return "CMD: python3 -B -m pytest -q"
            return "DONE: verified and completed."
        if self.version == "managed":
            if self.calls == 1:
                return "CMD: cat /etc/passwd"
            if self.calls == 2:
                return "CMD: find . -maxdepth 2 -type f | sort"
            if self.calls == 3:
                return f"CMD: {spec.write_command(spec.wrong)}"
            if self.calls == 4:
                return "CMD: python3 -B -m pytest -q"
            if any("FAILED" in item or "failed" in item for item in _history):
                if self.calls == 5:
                    return f"CMD: {spec.write_command(spec.good)}"
                if self.calls == 6:
                    return "CMD: python3 -B -m pytest -q"
            return "DONE: verified and completed."
        raise ValueError(f"unknown scripted version: {self.version}")


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
            command_match = re.match(r"CMD:\s*(.+)", response, flags=re.DOTALL)
            if command_match:
                observation = self.environment.run(command_match.group(1))
                actions.append(observation)
                history.append(
                    f"OBSERVATION returncode={observation.returncode}\n"
                    f"{observation.stdout}\n{observation.stderr}"
                )
            elif response.startswith("DONE:"):
                self_reported_success = True
                break
        return AgentResult(
            case_id=case_id,
            version=(
                "v1.0-final" if self.model.requested_version == "final" else
                f"v0.{'1' if self.model.version == 'minimal' else '2' if self.model.version == 'explore' else '3' if self.model.version == 'edit' else '4' if self.model.version == 'verify' else '6'}-{self.model.version}"
            ),
            status="self_reported_done" if self_reported_success else "step_budget_exhausted",
            self_reported_success=self_reported_success,
            steps=len(actions) + len(history),
            elapsed_ms=(time.perf_counter() - started) * 1000,
            actions=actions,
        )
