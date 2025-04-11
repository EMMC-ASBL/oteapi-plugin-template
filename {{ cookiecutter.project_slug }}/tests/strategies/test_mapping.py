"""Tests the mapping strategy."""

from __future__ import annotations


def test_mapping() -> None:
    """Test the DEMO mapping strategy on a local file."""
    from {{ cookiecutter.package_name }}.strategies.mapping import DemoMappingStrategy

    config = {"mappingType": "mapping/DEMO"}
    mapping_initialize = DemoMappingStrategy(config).initialize()
    mapping_get = DemoMappingStrategy(config).get()

    assert {**mapping_initialize} == {}
    assert {**mapping_get} == {}
