"""Demo resource strategy class."""

from __future__ import annotations

from oteapi.models import AttrDict, ResourceConfig
from pydantic.dataclasses import dataclass


@dataclass
class DemoResourceStrategy:
    """Resource Strategy.

    **Registers strategies**:

    - `("accessService", "DEMO-access-service")`

    """

    resource_config: ResourceConfig

    def initialize(self) -> AttrDict:
        """Initialize strategy.

        This method will be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return AttrDict()

    def get(self) -> AttrDict:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return AttrDict()
