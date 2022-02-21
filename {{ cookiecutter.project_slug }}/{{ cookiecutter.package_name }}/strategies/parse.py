"""Demo strategy class for text/json."""
# pylint: disable=no-self-use,unused-argument
import json
from dataclasses import dataclass
from typing import TYPE_CHECKING

from oteapi.datacache import DataCache
from oteapi.models import SessionUpdate
from oteapi.plugins import create_strategy

if TYPE_CHECKING:
    from typing import Any, Dict, Optional

    from oteapi.models import ResourceConfig


@dataclass
class DemoJSONDataParseStrategy:
    """Parse Strategy.

    **Registers strategies**:

    - `("mediaType", "application/jsonDEMO")`

    """

    parse_config: "ResourceConfig"

    def initialize(
        self, session: "Optional[Dict[str, Any]]" = None
    ) -> SessionUpdate:
        """Initialize strategy.

        This method will be called through the `/initialize` endpoint of the OTE-API
        Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return SessionUpdate()

    def get(self, session: "Optional[Dict[str, Any]]" = None) -> SessionUpdate:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTE-API Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        downloader = create_strategy("download", self.parse_config)
        output = downloader.get()
        cache = DataCache(self.parse_config.configuration)
        content = cache.get(output["key"])

        if isinstance(content, dict):
            return SessionUpdate(**content)
        return SessionUpdate(**json.loads(content))
