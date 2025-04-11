"""Tests the demo parse strategy for JSON."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def test_json(static_files: Path) -> None:
    """Test `application/jsonDEMO` parse strategy on local file."""
    import json

    from {{ cookiecutter.package_name }}.strategies.parse import DemoJSONDataParseStrategy

    sample_file = static_files / "sample2.json"
    assert sample_file.exists(), f"Test file not found at {sample_file} !"

    config = {
        "parserType": "parser/jsonDEMO",
        "entity": "http://onto-ns.com/meta/1.0/test",
        "configuration": {
            "downloadUrl": sample_file.as_uri(),
            "mediaType": "application/jsonDEMO",
        },
    }
    parser_initialize = DemoJSONDataParseStrategy(config).initialize()
    parser_get = DemoJSONDataParseStrategy(config).get()

    test_data = json.loads(sample_file.read_text())

    assert {**parser_initialize} == {}
    assert parser_get.content == test_data
