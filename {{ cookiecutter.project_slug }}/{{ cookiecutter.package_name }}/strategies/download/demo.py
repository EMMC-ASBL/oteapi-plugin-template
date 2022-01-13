"""Download strategy class for http/https"""
from dataclasses import dataclass
from typing import TYPE_CHECKING

import requests

from oteapi.cache import DataCache
from oteapi.models.resourceconfig import ResourceConfig
from oteapi.strategies.factory import StrategyFactory

if TYPE_CHECKING:
    from typing import Any, Dict, Optional


@dataclass
@StrategyFactory.register(("scheme", "http"), ("scheme", "https"))
class HTTPSStrategy:
    """Strategy for retrieving data via http."""

    resource_config: ResourceConfig

    def initialize(
        self, session: Optional[Dict[str, Any]] = None
    ) -> Dict:
        """Initialize"""
        return {}

    def get(self, session: Optional[Dict[str, Any]] = None) -> Dict:
        """Download via http/https and store on local cache."""
        cache = DataCache(self.resource_config.configuration)
        if cache.config.accessKey and cache.config.accessKey in cache:
            key = cache.config.accessKey
        else:
            req = requests.get(self.resource_config.downloadUrl, allow_redirects=True)
            key = cache.add(req.content)

        return {"key": key}
