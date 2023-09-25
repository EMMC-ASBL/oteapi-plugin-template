"""Demo strategy class for text/json."""
# pylint: disable=unused-argument
from __future__ import annotations

import json
from typing import TYPE_CHECKING

from oteapi.datacache import DataCache
from oteapi.models import AttrDict, DataCacheConfig, ResourceConfig, SessionUpdate
from oteapi.plugins import create_strategy
from pydantic import Field
from pydantic.dataclasses import dataclass

if TYPE_CHECKING:  # pragma: no cover
    from typing import Any, Literal


class JSONConfig(AttrDict):
    """JSON parse-specific Configuration Data Model."""

    datacache_config: DataCacheConfig | None = Field(
        None,
        description=(
            "Configurations for the data cache for storing the downloaded file "
            "content."
        ),
    )


class JSONParseConfig(ResourceConfig):
    """File download strategy filter config."""

    mediaType: "Literal['application/jsonDEMO']" = Field(
        "application/jsonDEMO",
        description=ResourceConfig.model_fields["mediaType"].description,
    )
    configuration: JSONConfig = Field(
        JSONConfig(), description="JSON parse strategy-specific configuration."
    )


class SessionUpdateJSONParse(SessionUpdate):
    """Class for returning values from JSON Parse."""

    content: dict = Field(..., description="Content of the JSON document.")


@dataclass
class DemoJSONDataParseStrategy:
    """Parse strategy for JSON.

    **Registers strategies**:

    - `("mediaType", "application/jsonDEMO")`

    """

    parse_config: JSONParseConfig

    def initialize(self, session: "dict[str, Any]" | None = None) -> SessionUpdate:
        """Initialize."""
        return SessionUpdate()

    def get(self, session: "dict[str, Any]" | None = None) -> SessionUpdateJSONParse:
        """Parse json."""
        downloader = create_strategy("download", self.parse_config)
        output = downloader.get()
        cache = DataCache(self.parse_config.configuration.datacache_config)
        content = cache.get(output["key"])

        if isinstance(content, dict):
            return SessionUpdateJSONParse(content=content)
        return SessionUpdateJSONParse(content=json.loads(content))
