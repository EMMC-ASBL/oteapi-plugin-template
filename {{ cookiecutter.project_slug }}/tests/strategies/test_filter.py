"""Tests the filter strategy."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oteapi.models import SessionUpdate

    from {{ cookiecutter.package_name }}.strategies.filter import SessionUpdateDemoFilter


def test_filter() -> None:
    """Test the DEMO filter strategy on a local file."""
    from random import randint

    from {{ cookiecutter.package_name }}.strategies.filter import DemoFilter

    demo_data = [randint(0, 100) for _ in range(5)]

    config = {
        "filterType": "filter/DEMO",
        "configuration": {"demo_data": demo_data},
    }
    filter_initialize: "SessionUpdateDemoFilter" = DemoFilter(config).initialize()
    filter_get: "SessionUpdate" = DemoFilter(config).get(filter_initialize)

    assert filter_initialize.key == demo_data
    assert {**filter_get} == {}
