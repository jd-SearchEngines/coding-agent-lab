"""Explicit state and bounded recovery decisions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RecoveryState:
    phase: str = "acting"
    retry_count: int = 0
    retry_budget: int = 2
    termination_reason: str | None = None

    def on_failure(self, reason: str) -> str:
        self.retry_count += 1
        if self.retry_count > self.retry_budget:
            self.phase = "stopped"
            self.termination_reason = f"retry_budget_exhausted: {reason}"
            return "stop"
        self.phase = "replanning"
        return "replan"

    def on_success(self) -> None:
        self.phase = "verified"
        self.termination_reason = "verified"


class RecoveryController:
    def __init__(self, retry_budget: int = 2):
        self.state = RecoveryState(retry_budget=retry_budget)

    def observe(self, returncode: int) -> str:
        if returncode == 0:
            self.state.on_success()
            return "finish"
        return self.state.on_failure(f"tool_returncode={returncode}")

