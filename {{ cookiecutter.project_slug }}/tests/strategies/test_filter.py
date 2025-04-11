"""Tests the filter strategy."""

from __future__ import annotations


def test_filter() -> None:
    """Test the DEMO filter strategy on a local file."""
    from random import randint

    from oteapi.datacache import DataCache

    from {{ cookiecutter.package_name }}.strategies.filter import DemoFilter

    demo_data = [randint(0, 100) for _ in range(5)]

    config = {
        "filterType": "filter/DEMO",
        "configuration": {"demo_data": demo_data},
    }
    filter_initialize = DemoFilter(config).initialize()
    filter_get = DemoFilter(config).get()

    content = DataCache().get(filter_initialize.key)

    assert content == demo_data
    assert {**filter_get} == {}
