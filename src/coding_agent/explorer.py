"""Bounded repository exploration primitives."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path


class RepoExplorer:
    def __init__(self, root: Path):
        self.root = Path(root)

    def file_search(self, pattern: str) -> list[str]:
        return sorted(str(path.relative_to(self.root)) for path in self.root.rglob(pattern))

    def text_search(self, needle: str, files: Iterable[Path] | None = None) -> list[str]:
        candidates = files or self.root.rglob("*.py")
        hits = []
        for path in candidates:
            if path.is_file() and needle in path.read_text(encoding="utf-8"):
                hits.append(str(path.relative_to(self.root)))
        return sorted(hits)

    def read_targeted(self, relative_path: str, max_lines: int = 80) -> str:
        path = (self.root / relative_path).resolve()
        if self.root.resolve() not in path.parents:
            raise ValueError("path outside workspace")
        return "\n".join(path.read_text(encoding="utf-8").splitlines()[:max_lines])
