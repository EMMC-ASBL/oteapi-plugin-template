"""Tests the resource strategy."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def test_resource(static_files: Path) -> None:
    """Test `file` download strategy on binary and text files.

    Test files are taken from filesamples.com.
    """
    import json

    from {{ cookiecutter.package_name }}.strategies.resource import DemoResourceStrategy

    config = {
        "downloadUrl": "https://example.com/sample2.json",
        "mediaType": "application/jsonDEMO",
        "accessService": "DEMO-access-service",
    }
    resource_initialize = DemoResourceStrategy(config).initialize()
    resource_get = DemoResourceStrategy(config).get()

    assert {**resource_initialize} == {}
    assert {**resource_get} == {}
