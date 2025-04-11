"""Demo transformation strategy class."""

from __future__ import annotations

import datetime
import sys
from typing import Annotated

from oteapi.models import AttrDict, TransformationConfig, TransformationStatus
from pydantic import Field
from pydantic.dataclasses import dataclass


class DummyTransformationContent(AttrDict):
    """Class for returning values from Dummy Transformation strategy."""

    result: Annotated[str, Field(description="The job ID.")]


@dataclass
class DummyTransformationStrategy:
    """Transformation Strategy.

    **Registers strategies**:

    - `("transformationType", "script/DEMO")`

    """

    transformation_config: TransformationConfig

    def initialize(self) -> AttrDict:
        """Initialize strategy.

        This method will be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return AttrDict()

    def get(self) -> DummyTransformationContent:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return DummyTransformationContent(result="a01d")

    def status(self, task_id: str) -> TransformationStatus:
        """Get job status.

        Parameters:
            task_id: The transformation job ID.

        Returns:
            An overview of the transformation job's status, including relevant
            metadata.

        """
        if sys.version_info < (3, 11):
            time_now = datetime.datetime.utcnow()
        else:
            time_now = datetime.datetime.now(datetime.UTC)

        return TransformationStatus(
            id=task_id,
            status="wip",
            messages=[],
            created=time_now,
            startTime=time_now,
            finishTime=time_now,
        )
