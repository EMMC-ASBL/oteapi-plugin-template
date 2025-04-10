"""Demo strategy class for text/json."""

from __future__ import annotations

import json
from typing import Literal, Annotated

from oteapi.datacache import DataCache
from oteapi.models import AttrDict, DataCacheConfig, ParserConfig
from oteapi.plugins import create_strategy
from pydantic import Field
from pydantic.dataclasses import dataclass


class JSONConfig(AttrDict):
    """JSON parse-specific Configuration Data Model."""

    datacache_config: Annotated[
        DataCacheConfig | None,
        Field(
            description=(
                "Configurations for the data cache for storing the downloaded file "
                "content."
            ),
        ),
    ] = None


class JSONParseConfig(ParserConfig):
    """File download strategy filter config."""

    mediaType: Annotated[
        Literal["application/jsonDEMO"],
        Field(
            description=ParserConfig.model_fields["mediaType"].description,
        ),
    ] = "application/jsonDEMO"

    configuration: Annotated[
        JSONConfig, Field(description="JSON parse strategy-specific configuration.")
    ] = JSONConfig()


class GetJSONParse(AttrDict):
    """Class for returning values from JSON Parse."""

    content: Annotated[dict, Field(description="Content of the JSON document.")]


@dataclass
class DemoJSONDataParseStrategy:
    """Parse strategy for JSON.

    **Registers strategies**:

    - `("mediaType", "application/jsonDEMO")`

    """

    parse_config: JSONParseConfig

    def initialize(self) -> AttrDict:
        """Initialize."""
        return AttrDict()

    def get(self) -> GetJSONParse:
        """Parse json."""
        downloader = create_strategy("download", self.parse_config)
        output = downloader.get()
        cache = DataCache(self.parse_config.configuration.datacache_config)
        content = cache.get(output["key"])

        if isinstance(content, dict):
            return GetJSONParse(content=content)

        return GetJSONParse(content=json.loads(content))
