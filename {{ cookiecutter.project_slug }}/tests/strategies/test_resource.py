"""Tests the resource strategy."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from oteapi.models import SessionUpdate

    from {{ cookiecutter.package_name }}.strategies.resource import SessionUpdateDemoResource


def test_resource(static_files: "Path") -> None:
    """Test `file` download strategy on binary and text files.

    Test files are taken from filesamples.com.
    """
    import json

    from {{ cookiecutter.package_name }}.strategies.resource import DemoResourceStrategy

    sample_file = static_files / "sample2.json"
    assert sample_file.exists(), f"Test file not found at {sample_file} !"

    config = {
        "accessUrl": sample_file.as_uri(),
        "mediaType": "application/jsonDEMO",
        "accessService": "DEMO-access-service",
    }
    resource_initialize: "SessionUpdate" = DemoResourceStrategy(config).initialize()
    resource_get: "SessionUpdateDemoResource" = DemoResourceStrategy(config).get(
        resource_initialize
    )

    test_data = json.loads(sample_file.read_text())

    assert {**resource_initialize} == {}
    assert {**resource_get} == {"output": test_data}
