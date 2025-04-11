"""Demo strategy class for text/json."""

from __future__ import annotations

import json
from typing import Annotated, Literal

from oteapi.datacache import DataCache
from oteapi.models import (
    AttrDict,
    DataCacheConfig,
    HostlessAnyUrl,
    ParserConfig,
    ResourceConfig,
)
from oteapi.plugins import create_strategy
from pydantic import Field
from pydantic.dataclasses import dataclass


class JSONConfig(AttrDict):
    """JSON parse-specific Configuration Data Model."""

    downloadUrl: Annotated[
        HostlessAnyUrl | None,
        Field(description=ResourceConfig.model_fields["downloadUrl"].description),
    ]
    mediaType: Annotated[
        Literal["application/jsonDEMO"],
        Field(description=ResourceConfig.model_fields["mediaType"].description),
    ] = "application/jsonDEMO"

    datacache_config: Annotated[
        DataCacheConfig | None,
        Field(
            description=(
                "Configurations for the data cache for storing the downloaded file "
                "content."
            ),
        ),
    ] = None


class JSONParserConfig(ParserConfig):
    """File download strategy filter config."""

    parserType: Annotated[
        Literal["parser/jsonDEMO"],
        Field(description=ParserConfig.model_fields["parserType"].description),
    ] = "parser/jsonDEMO"

    configuration: Annotated[
        JSONConfig, Field(description="JSON parse strategy-specific configuration.")
    ]


class JSONParseContent(AttrDict):
    """Class for returning values from JSON Parse."""

    content: Annotated[dict, Field(description="Content of the JSON document.")]


@dataclass
class DemoJSONDataParseStrategy:
    """Parse strategy for JSON.

    **Registers strategies**:

    - `("parserType", "parser/jsonDEMO")`

    """

    parse_config: JSONParserConfig

    def initialize(self) -> AttrDict:
        """Initialize."""
        return AttrDict()

    def get(self) -> JSONParseContent:
        """Parse json."""
        downloader = create_strategy(
            "download", self.parse_config.configuration.model_dump()
        )
        output = downloader.get()
        cache = DataCache(self.parse_config.configuration.datacache_config)
        content = cache.get(output["key"])

        if isinstance(content, dict):
            return JSONParseContent(content=content)

        return JSONParseContent(content=json.loads(content))
