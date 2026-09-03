from coding_agent.production import ProductionAgent


def test_production_capability_contract() -> None:
    capabilities = ProductionAgent.capabilities
    assert capabilities.verify is True
    assert capabilities.regression is True
    assert capabilities.cost is False

