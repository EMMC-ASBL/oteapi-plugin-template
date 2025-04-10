"""Demo filter strategy."""

from __future__ import annotations

from typing import Annotated, Literal

from oteapi.datacache import DataCache
from oteapi.models import AttrDict, DataCacheConfig, FilterConfig
from pydantic import Field
from pydantic.dataclasses import dataclass


class DemoDataModel(AttrDict):
    """Demo filter data model."""

    demo_data: Annotated[list[int], Field(description="List of demo data.")]

    datacache_config: Annotated[
        DataCacheConfig | None,
        Field(
            description=(
                "Configurations for the data cache for storing the downloaded file "
                "content."
            ),
        ),
    ] = None


class DemoFilterConfig(FilterConfig):
    """Demo filter strategy filter config."""

    filterType: Annotated[
        Literal["filter/DEMO"],
        Field(
            description=FilterConfig.model_fields["filterType"].description,
        ),
    ] = "filter/DEMO"

    configuration: Annotated[
        DemoDataModel, Field(description="Demo filter data model.")
    ]


class DemoFilterContent(AttrDict):
    """Class for returning values from Download File strategy."""

    key: Annotated[str, Field(description="Key to access the data in the cache.")]


@dataclass
class DemoFilter:
    """Filter Strategy.

    **Registers strategies**:

    - `("filterType", "filter/DEMO")`

    """

    filter_config: DemoFilterConfig

    def initialize(self) -> DemoFilterContent:
        """Initialize strategy.

        This method will be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        cache = DataCache(self.filter_config.configuration.datacache_config)

        if cache.config.accessKey and cache.config.accessKey in cache:
            key = cache.config.accessKey
        else:
            key = cache.add(self.filter_config.configuration.demo_data)

        return DemoFilterContent(key=key)

    def get(self) -> AttrDict:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return AttrDict()
