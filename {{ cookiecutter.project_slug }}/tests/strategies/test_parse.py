"""Tests the demo parse strategy for JSON."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from oteapi.models import SessionUpdate

    from {{ cookiecutter.package_name }}.strategies.parse import SessionUpdateJSONParse


def test_json(static_files: "Path") -> None:
    """Test `application/jsonDEMO` parse strategy on local file."""
    import json

    from {{ cookiecutter.package_name }}.strategies.parse import DemoJSONDataParseStrategy

    sample_file = static_files / "sample2.json"
    assert sample_file.exists(), f"Test file not found at {sample_file} !"

    config = {
        "downloadUrl": sample_file.as_uri(),
        "mediaType": "application/jsonDEMO",
    }
    parser_initialize: "SessionUpdate" = DemoJSONDataParseStrategy(config).initialize()
    parser_get: "SessionUpdateJSONParse" = DemoJSONDataParseStrategy(config).get(
        parser_initialize
    )

    test_data = json.loads(sample_file.read_text())

    assert {**parser_initialize} == {}
    assert parser_get.content == test_data
