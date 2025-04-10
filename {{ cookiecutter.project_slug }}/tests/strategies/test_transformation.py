"""Tests the transformation strategy."""

from __future__ import annotations


def test_transformation() -> None:
    """Test the DEMO transformation strategy on a local file."""
    from datetime import datetime

    from {{ cookiecutter.package_name }}.strategies.transformation import DummyTransformationStrategy

    config = {"transformationType": "script/DEMO"}

    transformation_initialize = DummyTransformationStrategy(config).initialize()
    assert {**transformation_initialize} == {}

    transformation = DummyTransformationStrategy(config)

    assert {**transformation.get()} == {"result": "a01d"}

    test_task_id = "a01d"
    static_status_demo_data = {
        "id": test_task_id,
        "status": "wip",
        "messages": [],
    }
    dynamic_status_demo_data = ("created", "startTime", "finishTime")

    transformation_status = transformation.status(test_task_id)
    for key, value in static_status_demo_data.items():
        assert hasattr(transformation_status, key)
        assert getattr(transformation_status, key) == value

    for datetime_fields in dynamic_status_demo_data:
        assert hasattr(transformation_status, datetime_fields)
        assert isinstance(getattr(transformation_status, datetime_fields), datetime)
