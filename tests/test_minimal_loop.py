from pathlib import Path

from coding_agent.agent import LocalEnvironment, MinimalAgent, ScriptedModel


def test_minimal_loop_records_self_report(tmp_path: Path) -> None:
    result = MinimalAgent(ScriptedModel("case_001"), LocalEnvironment(tmp_path)).run(
        "fix the issue", "case_001"
    )
    assert result.self_reported_success is True
    assert result.status == "self_reported_done"
    assert result.steps == 1


def test_environment_runs_in_workspace(tmp_path: Path) -> None:
    result = LocalEnvironment(tmp_path).run("pwd")
    assert result.returncode == 0
    assert str(tmp_path) in result.stdout

