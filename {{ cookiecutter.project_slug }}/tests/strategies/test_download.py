"""Tests the download strategy for 'file://'."""
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path

    from oteapi.models import SessionUpdate

    from {{ cookiecutter.package_name }}.strategies.download import SessionUpdateFile


@pytest.mark.parametrize(
    "filename,mediaType",
    [("sample1.db", "application/vnd.sqlite3"), ("sample2.json", "application/json")],
    ids=["binary", "text"],
)
def test_download_file(filename: str, mediaType: str, static_files: "Path") -> None:
    """Test `file` download strategy on binary and text files.

    Test files are taken from filesamples.com.
    """
    from oteapi.datacache import DataCache

    from {{ cookiecutter.package_name }}.strategies.download import FileStrategy

    sample_file = static_files / filename
    assert sample_file.exists(), f"Test file not found at {sample_file} !"

    config = {
        "downloadUrl": sample_file.as_uri(),
        "mediaType": mediaType,
    }
    download_initialize: "SessionUpdate" = FileStrategy(config).initialize()
    download_get: "SessionUpdateFile" = FileStrategy(config).get(download_initialize)

    content: bytes = DataCache().get(download_get.key)

    # `download_initialize` is not actually a dictionary, but rather a SessionUpdate
    # instance. This means by definition `download_initialize` will not be equal to {}.
    # However, it has the ability to unpack similarly as a dictionary, when adding two
    # asterisks (*) prior to it: `**download_initialize`.
    # But since a bare statement `**download_initialize` is not allowed (it fails when
    # one does this) it needs to be packed into a dictionary, hence the surrounding {}.
    assert {**download_initialize} == {}

    if "sqlite" in mediaType:
        # binary
        assert content == sample_file.read_bytes()
    else:
        # text
        assert content.decode(encoding="utf8").replace(
            "\r", ""
        ) == sample_file.read_text(encoding="utf8")
