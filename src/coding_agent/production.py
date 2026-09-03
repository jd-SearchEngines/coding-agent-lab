"""Composition boundary for the production-oriented Season 1 version."""

from __future__ import annotations

from dataclasses import dataclass

from .agent import MinimalAgent


@dataclass(frozen=True)
class ProductionCapabilities:
    understand: bool = True
    explore: bool = True
    edit: bool = True
    verify: bool = True
    sandbox: bool = True
    state: bool = True
    recovery: bool = True
    eval: bool = True
    audit: bool = True
    timeout: bool = True
    cost: bool = False
    latency: bool = True
    observability: bool = True
    regression: bool = True


class ProductionAgent(MinimalAgent):
    """The final composition currently delegates to the managed loop.

    Keeping this as an explicit boundary makes future provider/model wiring
    observable without claiming that the teaching policy is production-safe.
    """

    capabilities = ProductionCapabilities()

