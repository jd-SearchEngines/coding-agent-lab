from pathlib import Path

from coding_agent.verification import ExternalVerifier


def test_external_verifier_is_independent(tmp_path: Path) -> None:
    (tmp_path / "test_ok.py").write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    result = ExternalVerifier().run(tmp_path)
    assert result.passed is True
    assert result.returncode == 0

