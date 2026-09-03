from pathlib import Path

import pytest

from coding_agent.editor import StructuredEditor
from coding_agent.explorer import RepoExplorer


def test_explorer_reads_only_workspace(tmp_path: Path) -> None:
    target = tmp_path / "module.py"
    target.write_text("needle\n", encoding="utf-8")
    explorer = RepoExplorer(tmp_path)
    assert explorer.file_search("*.py") == ["module.py"]
    assert explorer.text_search("needle") == ["module.py"]
    with pytest.raises(ValueError):
        explorer.read_targeted("../outside.py")


def test_structured_editor_returns_diff_and_blocks_escape(tmp_path: Path) -> None:
    target = tmp_path / "module.py"
    target.write_text("old\n", encoding="utf-8")
    editor = StructuredEditor(tmp_path)
    diff = editor.replace_file("module.py", "new\n")
    assert "-old" in diff and "+new" in diff
    with pytest.raises(ValueError):
        editor.replace_file("../outside.py", "bad\n")

