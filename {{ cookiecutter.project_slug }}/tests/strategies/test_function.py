"""Tests the function strategy."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from oteapi.models import SessionUpdate


def test_function() -> None:
    """Test the DEMO function strategy on a local file."""
    from {{ cookiecutter.package_name }}.strategies.function import DemoFunctionStrategy

    config = {"functionType": "function/DEMO"}
    function_initialize: "SessionUpdate" = DemoFunctionStrategy(config).initialize()
    function_get: "SessionUpdate" = DemoFunctionStrategy(config).get(
        function_initialize
    )

    assert {**function_initialize} == {}
    assert {**function_get} == {}
