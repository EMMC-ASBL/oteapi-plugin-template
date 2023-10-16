"""Demo download strategy class for file."""
from typing import Any, Optional

from oteapi.datacache import DataCache
from oteapi.models import AttrDict, DataCacheConfig, ResourceConfig, SessionUpdate
from oteapi.utils.paths import uri_to_path
from pydantic import Field, FileUrl, field_validator
from pydantic.dataclasses import dataclass


class FileConfig(AttrDict):
    """File-specific Configuration Data Model."""

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
    datacache_config: Optional[DataCacheConfig] = Field(
        None,
        description=(
            "Configurations for the data cache for storing the downloaded file "
            "content."
        ),
    )


class FileResourceConfig(ResourceConfig):
    """File download strategy filter config."""

    downloadUrl: FileUrl = Field(
        ..., description="The file URL, which will be downloaded."
    )
    configuration: FileConfig = Field(
        FileConfig(), description="File download strategy-specific configuration."
    )

    @field_validator("downloadUrl", mode="after")
    @classmethod
    def ensure_path_exists(cls, value: FileUrl) -> FileUrl:
        """Ensure `path` is defined in `downloadUrl`."""
        if not value.path:
            raise ValueError("downloadUrl must contain a `path` part.")
        return value


class SessionUpdateFile(SessionUpdate):
    """Class for returning values from Download File strategy."""

    key: str = Field(..., description="Key to access the data in the cache.")


@dataclass
class FileStrategy:
    """Strategy for retrieving data from a local file.

    **Registers strategies**:

    - `("scheme", "fileDEMO")`

    """

    download_config: FileResourceConfig

    def initialize(self, session: Optional[dict[str, Any]] = None) -> SessionUpdate:
        """Initialize."""
        return SessionUpdate()

    def get(self, session: Optional[dict[str, Any]] = None) -> SessionUpdateFile:
        """Read local file."""
        filename = uri_to_path(self.download_config.downloadUrl).resolve()

        if not filename.exists():
            raise FileNotFoundError(f"File not found at {filename}")

        cache = DataCache(self.download_config.configuration.datacache_config)
        if cache.config.accessKey and cache.config.accessKey in cache:
            key = cache.config.accessKey
        else:
            key = cache.add(
                filename.read_text(encoding=self.download_config.configuration.encoding)
                if self.download_config.configuration.text
                else filename.read_bytes()
            )

        return SessionUpdateFile(key=key)
