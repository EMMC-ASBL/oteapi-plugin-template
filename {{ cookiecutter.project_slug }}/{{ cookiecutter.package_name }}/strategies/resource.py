"""Demo resource strategy class."""
# pylint: disable=unused-argument
from typing import TYPE_CHECKING, Optional

from oteapi.models import AttrDict, DataCacheConfig, ResourceConfig, SessionUpdate
from oteapi.plugins import create_strategy
from pydantic import Field
from pydantic.dataclasses import dataclass

if TYPE_CHECKING:  # pragma: no cover
    from typing import Any, Dict


class DemoConfig(AttrDict):
    """Strategy-specific Configuration Data Model."""

    datacache_config: Optional[DataCacheConfig] = Field(
        None,
        description="Configuration for the data cache.",
    )


class DemoResourceConfig(ResourceConfig):
    """Demo resource strategy config."""

    # Require the resource to be a REST API with JSON responses that uses the
    # DemoJSONDataParseStrategy strategy.
    mediaType: str = Field(
        "application/jsonDEMO",
        const=True,
        description=ResourceConfig.__fields__["mediaType"].field_info.description,
    )

    accessService: str = Field(
        "DEMO-access-service",
        const=True,
        description=ResourceConfig.__fields__["accessService"].field_info.description,
    )
    configuration: DemoConfig = Field(
        DemoConfig(),
        description="Demo resource strategy-specific configuration.",
    )


class SessionUpdateDemoResource(SessionUpdate):
    """Class for returning values from Demo Resource strategy."""

    output: dict = Field(
        ...,
        description=(
            "The output from downloading the response from the given `accessUrl`."
        ),
    )


@dataclass
class DemoResourceStrategy:
    """Resource Strategy.

    **Registers strategies**:

    - `("accessService", "DEMO-access-service")`

    """

    resource_config: DemoResourceConfig

    def initialize(self, session: "Optional[Dict[str, Any]]" = None) -> SessionUpdate:
        """Initialize strategy.

        This method will be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return SessionUpdate()

    def get(
        self, session: "Optional[Dict[str, Any]]" = None
    ) -> SessionUpdateDemoResource:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        # Example of the plugin using a parse strategy to (fetch) and parse the data
        session = session if session else {}

        parse_config = self.resource_config.copy()
        if not parse_config.downloadUrl:
            parse_config.downloadUrl = self.resource_config.accessUrl

        session.update(create_strategy("parse", parse_config).initialize(session))
        session.update(create_strategy("parse", parse_config).get(session))

        if "content" not in session:
            raise ValueError(
                f"Expected the parse strategy for {self.resource_config.mediaType!r} "
                "to return a session with a 'content' key."
            )

        return SessionUpdateDemoResource(output=session["content"])
