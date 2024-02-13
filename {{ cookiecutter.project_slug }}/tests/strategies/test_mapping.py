"""Tests the mapping strategy."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oteapi.models import SessionUpdate


def test_mapping() -> None:
    """Test the DEMO mapping strategy on a local file."""
    from {{ cookiecutter.package_name }}.strategies.mapping import DemoMappingStrategy

    config = {"mappingType": "mapping/DEMO"}
    mapping_initialize: "SessionUpdate" = DemoMappingStrategy(config).initialize()
    mapping_get: "SessionUpdate" = DemoMappingStrategy(config).get(mapping_initialize)

    assert {**mapping_initialize} == {}
    assert {**mapping_get} == {}
