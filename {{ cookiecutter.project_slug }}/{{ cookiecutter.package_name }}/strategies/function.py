"""Demo function strategy class."""

from typing import Any, Optional

from oteapi.models import FunctionConfig, SessionUpdate
from pydantic.dataclasses import dataclass


@dataclass
class DemoFunctionStrategy:
    """Function Strategy.

    **Registers strategies**:

    - `("functionType", "function/DEMO")`

    """

    function_config: FunctionConfig

    def initialize(self, session: Optional[dict[str, Any]] = None) -> SessionUpdate:
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

    def get(self, session: Optional[dict[str, Any]] = None) -> SessionUpdate:
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
