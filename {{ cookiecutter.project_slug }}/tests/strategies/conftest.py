"""Pytest fixtures for `strategies/`."""

from __future__ import annotations

import pytest


@pytest.fixture(scope="session", autouse=True)
def load_plugins() -> None:
    """Load pip installed plugin strategies."""
    from oteapi.plugins.factories import load_strategies

    load_strategies(test_for_uniqueness=False)
