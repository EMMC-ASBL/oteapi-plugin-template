"""Demo function strategy class."""
# pylint: disable=no-self-use,unused-argument
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Dict, Optional

    from oteapi.models import FunctionConfig


@dataclass
class DemoFunctionStrategy:
    """Function Strategy."""

    function_config: "FunctionConfig"

    def initialize(
        self, session: "Optional[Dict[str, Any]]" = None
    ) -> "Dict[str, Any]":
        """Initialize strategy.

        This method will be called through the `/initialize` endpoint of the OTE-API
        Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            Dictionary of key/value-pairs to be stored in the sessions-specific
            dictionary context.

        """
        return {}

    def get(self, session: "Optional[Dict[str, Any]]" = None) -> "Dict[str, Any]":
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTE-API Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            Dictionary of key/value-pairs to be stored in the sessions-specific
            dictionary context.

        """
        return {}
