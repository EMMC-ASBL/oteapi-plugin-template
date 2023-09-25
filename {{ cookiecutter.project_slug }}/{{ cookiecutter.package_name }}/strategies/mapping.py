"""Demo mapping strategy class."""
# pylint: disable=unused-argument
from __future__ import annotations

from typing import TYPE_CHECKING

from oteapi.models import MappingConfig, SessionUpdate
from pydantic.dataclasses import dataclass

if TYPE_CHECKING:  # pragma: no cover
    from typing import Any


@dataclass
class DemoMappingStrategy:
    """Mapping Strategy.

    **Registers strategies**:

    - `("mappingType", "mapping/DEMO")`

    """

    mapping_config: MappingConfig

    def initialize(self, session: "dict[str, Any]" | None = None) -> SessionUpdate:
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

    def get(self, session: "dict[str, Any]" | None = None) -> SessionUpdate:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return SessionUpdate()
