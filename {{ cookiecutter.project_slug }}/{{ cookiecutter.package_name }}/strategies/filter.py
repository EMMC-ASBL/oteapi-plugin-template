"""Demo filter strategy."""
# pylint: disable=no-self-use,unused-argument
from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from oteapi.models import SessionUpdate
from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from typing import Any, Dict, Optional

    from oteapi.models import FilterConfig


class DemoDataModel(BaseModel):
    """Demo filter data model."""

    demo_data: List[int] = Field([], description="List of demo data.")


class SessionUpdateDemoFilter(SessionUpdate):
    """Class for returning values from Download File strategy."""

    key: str = Field(..., description="Key to access the data in the cache.")



@dataclass
class DemoFilter:
    """Filter Strategy.

    **Registers strategies**:

    - `("filterType", "filter/DEMO")`

    """

    filter_config: "FilterConfig"

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

    def get(self, session: "Optional[Dict[str, Any]]" = None) -> SessionUpdateDemoFilter:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTE-API Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        model = DemoDataModel(**self.filter_config.configuration)
        return SessionUpdateDemoFilter(key=model.demo_data)
