"""Tests the resource strategy."""

from __future__ import annotations


def test_resource() -> None:
    """Test `file` download strategy on binary and text files.

    Test files are taken from filesamples.com.
    """
    from {{ cookiecutter.package_name }}.strategies.resource import DemoResourceStrategy

    config = {
        "downloadUrl": "https://example.com/sample2.json",
        "mediaType": "application/jsonDEMO",
        "accessService": "DEMO-access-service",
    }
    resource_initialize = DemoResourceStrategy(config).initialize()
    resource_get = DemoResourceStrategy(config).get()

    assert {**resource_initialize} == {}
    assert {**resource_get} == {}
