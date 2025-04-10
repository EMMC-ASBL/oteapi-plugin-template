"""Demo resource strategy class."""

from __future__ import annotations

from typing import Literal, Annotated

from oteapi.models import AttrDict, DataCacheConfig, ResourceConfig
from oteapi.plugins import create_strategy
from pydantic import Field
from pydantic.dataclasses import dataclass


class DemoConfig(AttrDict):
    """Strategy-specific Configuration Data Model."""

    datacache_config: Annotated[
        DataCacheConfig | None,
        Field(
            description="Configuration for the data cache.",
        ),
    ] = None


class DemoResourceConfig(ResourceConfig):
    """Demo resource strategy config."""

    # Require the resource to be a REST API with JSON responses that uses the
    # DemoJSONDataParseStrategy strategy.
    mediaType: Annotated[
        Literal["application/jsonDEMO"],
        Field(
            description=ResourceConfig.model_fields["mediaType"].description,
        ),
    ] = "application/jsonDEMO"

    accessService: Annotated[
        Literal["DEMO-access-service"],
        Field(
            description=ResourceConfig.model_fields["accessService"].description,
        ),
    ] = "DEMO-access-service"

    configuration: Annotated[
        DemoConfig,
        Field(
            description="Demo resource strategy-specific configuration.",
        ),
    ] = DemoConfig()


class GetDemoResource(AttrDict):
    """Class for returning values from Demo Resource strategy."""

    output: Annotated[
        dict,
        Field(
            description=(
                "The output from downloading the response from the given `accessUrl`."
            )
        ),
    ]


@dataclass
class DemoResourceStrategy:
    """Resource Strategy.

    **Registers strategies**:

    - `("accessService", "DEMO-access-service")`

    """

    resource_config: DemoResourceConfig

    def initialize(self) -> AttrDict:
        """Initialize strategy.

        This method will be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return AttrDict()

    def get(self) -> GetDemoResource:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        # Example of the plugin using a parse strategy to (fetch) and parse the data
        parse_config = self.resource_config.model_copy()
        if not parse_config.downloadUrl:
            parse_config.downloadUrl = self.resource_config.accessUrl

        strategy = create_strategy("parse", parse_config)
        session = strategy.initialize()
        session.update(strategy.get())

        if "content" not in session:
            raise ValueError(
                f"Expected the parse strategy for {self.resource_config.mediaType!r} "
                "to return a session with a 'content' key."
            )

        return GetDemoResource(output=session["content"])
