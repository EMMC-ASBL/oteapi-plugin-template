"""Demo filter strategy."""
# pylint: disable=no-self-use,unused-argument
from typing import TYPE_CHECKING, List, Optional

from oteapi.datacache import DataCache
from oteapi.models import AttrDict, DataCacheConfig, FilterConfig, SessionUpdate
from pydantic import Field
from pydantic.dataclasses import dataclass

if TYPE_CHECKING:  # pragma: no cover
    from typing import Any, Dict


class DemoDataModel(AttrDict):
    """Demo filter data model."""

    demo_data: List[int] = Field(..., description="List of demo data.")
    datacache_config: Optional[DataCacheConfig] = Field(
        None,
        description=(
            "Configurations for the data cache for storing the downloaded file "
            "content."
        ),
    )


class DemoFilterConfig(FilterConfig):
    """Demo filter strategy filter config."""

    filterType: str = Field(
        "filter/DEMO",
        const=True,
        description=FilterConfig.__fields__["filterType"].field_info.description,
    )
    configuration: DemoDataModel = Field(..., description="Demo filter data model.")


class SessionUpdateDemoFilter(SessionUpdate):
    """Class for returning values from Download File strategy."""

    key: str = Field(..., description="Key to access the data in the cache.")


@dataclass
class DemoFilter:
    """Filter Strategy.

    **Registers strategies**:

    - `("filterType", "filter/DEMO")`

    """

    filter_config: DemoFilterConfig

    def initialize(
        self, session: "Optional[Dict[str, Any]]" = None
    ) -> SessionUpdateDemoFilter:
        """Initialize strategy.

        This method will be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        cache = DataCache(self.filter_config.configuration.datacache_config)
        if cache.config.accessKey and cache.config.accessKey in cache:
            key = cache.config.accessKey
        else:
            key = cache.add(self.filter_config.configuration.demo_data)
        return SessionUpdateDemoFilter(key=key)

    def get(self, session: "Optional[Dict[str, Any]]" = None) -> SessionUpdate:
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
