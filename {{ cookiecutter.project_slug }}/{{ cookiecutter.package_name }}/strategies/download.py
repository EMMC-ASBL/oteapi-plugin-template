"""Demo download strategy class for file."""
# pylint: disable=no-self-use,unused-argument
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Optional

from oteapi.datacache import DataCache
from pydantic import BaseModel, Extra, Field

if TYPE_CHECKING:
    from typing import Any, Dict

    from oteapi.models.resourceconfig import ResourceConfig


class FileConfig(BaseModel):
    """File Specific Configuration"""

    text: bool = Field(
        False,
        description=(
            "Whether the file should be opened in text mode. If `False`, the file will"
            " be opened in bytes mode."
        ),
    )
    encoding: Optional[str] = Field(
        None,
        description=(
            "Encoding used when opening the file. The default is platform dependent."
        ),
    )


@dataclass
class DemoFileStrategy:
    """Strategy for retrieving data via local file."""

    download_config: "ResourceConfig"

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
        if (
            self.download_config.downloadUrl is None
            or self.download_config.downloadUrl.scheme != "file"
        ):
            raise ValueError(
                "Expected 'downloadUrl' to have scheme 'file' in the configuration."
            )
        filename = Path(self.download_config.downloadUrl.host).resolve()

        cache = DataCache(self.download_config.configuration)
        if cache.config.accessKey and cache.config.accessKey in cache:
            key = cache.config.accessKey
        else:
            config = FileConfig(
                **self.download_config.configuration, extra=Extra.ignore
            )
            key = cache.add(
                filename.read_text(encoding=config.encoding)
                if config.text
                else filename.read_bytes()
            )

        return {"key": key}
