"""Fail-closed command policy for the managed local environment."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PermissionDecision:
    allowed: bool
    reason: str


class CommandPolicy:
    denied_fragments = ("/etc/", "../", "rm -rf", "git reset --hard", "curl ", "wget ")

    def check(self, command: str) -> PermissionDecision:
        for fragment in self.denied_fragments:
            if fragment in command:
                return PermissionDecision(False, f"matched denied fragment: {fragment}")
        return PermissionDecision(True, "within local workspace policy")

