"""Pytest fixtures and configuration."""
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture(scope="session")
def static_files() -> "Path":
    """Path to `static` folder containing static test files."""
    from pathlib import Path

    return (Path(__file__).resolve().parent / "static").resolve()
