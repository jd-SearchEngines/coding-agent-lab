"""Constrained text editing and diff capture for an existing workspace."""

from __future__ import annotations

import difflib
from pathlib import Path


class StructuredEditor:
    def __init__(self, root: Path):
        self.root = Path(root).resolve()

    def _safe_path(self, relative_path: str) -> Path:
        path = (self.root / relative_path).resolve()
        if self.root not in path.parents:
            raise ValueError("edit target outside workspace")
        return path

    def replace_file(self, relative_path: str, content: str) -> str:
        path = self._safe_path(relative_path)
        before = path.read_text(encoding="utf-8") if path.exists() else ""
        path.write_text(content, encoding="utf-8")
        return "".join(
            difflib.unified_diff(
                before.splitlines(True),
                content.splitlines(True),
                fromfile=f"a/{relative_path}",
                tofile=f"b/{relative_path}",
            )
        )

