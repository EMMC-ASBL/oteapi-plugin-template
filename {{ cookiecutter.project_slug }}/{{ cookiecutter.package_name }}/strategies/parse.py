"""Demo strategy class for text/json."""

import json
from typing import Any, Literal, Optional, Annotated

from oteapi.datacache import DataCache
from oteapi.models import AttrDict, DataCacheConfig, ResourceConfig, SessionUpdate
from oteapi.plugins import create_strategy
from pydantic import Field
from pydantic.dataclasses import dataclass


class JSONConfig(AttrDict):
    """JSON parse-specific Configuration Data Model."""

    datacache_config: Annotated[
        Optional[DataCacheConfig],
        Field(
            description=(
                "Configurations for the data cache for storing the downloaded file "
                "content."
            ),
        ),
    ] = None


class JSONParseConfig(ResourceConfig):
    """File download strategy filter config."""

    mediaType: Annotated[
        Literal["application/jsonDEMO"],
        Field(
            description=ResourceConfig.model_fields["mediaType"].description,
        ),
    ] = "application/jsonDEMO"

    configuration: Annotated[
        JSONConfig, Field(description="JSON parse strategy-specific configuration.")
    ] = JSONConfig()


class SessionUpdateJSONParse(SessionUpdate):
    """Class for returning values from JSON Parse."""

    content: Annotated[dict, Field(description="Content of the JSON document.")]


@dataclass
class DemoJSONDataParseStrategy:
    """Parse strategy for JSON.

    **Registers strategies**:

    - `("mediaType", "application/jsonDEMO")`

    """

    parse_config: JSONParseConfig

    def initialize(self, session: Optional[dict[str, Any]] = None) -> SessionUpdate:
        """Initialize."""
        return SessionUpdate()

    def get(self, session: Optional[dict[str, Any]] = None) -> SessionUpdateJSONParse:
        """Parse json."""
        downloader = create_strategy("download", self.parse_config)
        output = downloader.get()
        cache = DataCache(self.parse_config.configuration.datacache_config)
        content = cache.get(output["key"])

        if isinstance(content, dict):
            return SessionUpdateJSONParse(content=content)

        return SessionUpdateJSONParse(content=json.loads(content))
