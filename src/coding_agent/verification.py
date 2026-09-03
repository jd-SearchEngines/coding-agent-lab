"""External verification is an independent observer of agent claims."""

from __future__ import annotations

import subprocess
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class VerificationResult:
    passed: bool
    returncode: int
    stdout: str
    stderr: str
    elapsed_ms: float


class ExternalVerifier:
    def __init__(self, timeout_s: float = 30.0):
        self.timeout_s = timeout_s

    def run(self, root: Path, command: str = "python3 -B -m pytest -q") -> VerificationResult:
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                command,
                shell=True,
                cwd=root,
                text=True,
                capture_output=True,
                timeout=self.timeout_s,
                check=False,
            )
            return VerificationResult(
                completed.returncode == 0,
                completed.returncode,
                completed.stdout,
                completed.stderr,
                (time.perf_counter() - started) * 1000,
            )
        except subprocess.TimeoutExpired as exc:
            return VerificationResult(
                False, 124, exc.stdout or "", f"TIMEOUT after {self.timeout_s}s",
                (time.perf_counter() - started) * 1000,
            )
