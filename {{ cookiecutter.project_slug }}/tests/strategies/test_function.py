"""Tests the function strategy."""

from __future__ import annotations


def test_function() -> None:
    """Test the DEMO function strategy on a local file."""
    from {{ cookiecutter.package_name }}.strategies.function import DemoFunctionStrategy

    config = {"functionType": "function/DEMO"}
    function_initialize = DemoFunctionStrategy(config).initialize()
    function_get = DemoFunctionStrategy(config).get()

    assert {**function_initialize} == {}
    assert {**function_get} == {}
