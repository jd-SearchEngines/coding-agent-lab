from coding_agent.state import RecoveryController


def test_recovery_replans_then_stops_at_budget() -> None:
    controller = RecoveryController(retry_budget=2)
    assert controller.observe(1) == "replan"
    assert controller.observe(1) == "replan"
    assert controller.observe(1) == "stop"
    assert controller.state.phase == "stopped"
    assert controller.state.termination_reason.startswith("retry_budget_exhausted")


def test_recovery_marks_verified() -> None:
    controller = RecoveryController()
    assert controller.observe(0) == "finish"
    assert controller.state.termination_reason == "verified"

