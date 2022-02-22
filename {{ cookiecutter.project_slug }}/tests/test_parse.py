"""Test parse strategies."""


def test_json() -> None:
    """Test `application/jsonDEMO` demo parse strategy."""
    from oteapi.models import ResourceConfig

    from {{ cookiecutter.package_name }}.strategies.parse import DemoJSONDataParseStrategy

    data = {
        "firstName": "Joe",
        "lastName": "Jackson",
        "gender": "male",
        "age": 28,
        "address": {"streetAddress": "101", "city": "San Diego", "state": "CA"},
        "phoneNumbers": [{"type": "home", "number": "7349282382"}],
    }

    config = ResourceConfig(
        downloadUrl="https://filesamples.com/samples/code/json/sample2.json",
        mediaType="application/jsonDEMO",
    )
    parser = DemoJSONDataParseStrategy(config)
    parsed_data = parser.get()

    assert parsed_data.dict() == data
