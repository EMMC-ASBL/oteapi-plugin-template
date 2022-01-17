# pylint: disable=W0511, W0613
"""
Demo resource strategy class
"""
from dataclasses import dataclass
from typing import Any, Dict, Optional

from oteapi.models.resourceconfig import ResourceConfig
from oteapi.interfaces.factory import StrategyFactory
from oteapi.interfaces.idownloadstrategy import create_download_strategy


@dataclass
# TODO: Replace "demo-access-service" below with appropriate accessService
@StrategyFactory.register(("accessService", "demo-access-service"))
class DemoResourceStrategy:
    """Resource Interface"""

    resource_config: ResourceConfig

    def initialize(self, session: Optional[Dict[str, Any]] = None) -> Dict:
        """Initialize"""

        return {}

    def get(self, session: Optional[Dict[str, Any]] = None) -> Dict:
        """Manage mapping and return shared map"""

        # Example of the plugin using the download strategy to fetch the data
        download_strategy = create_download_strategy(self.resource_config)
        read_output = download_strategy.read({})
        print(read_output)

        return {}
