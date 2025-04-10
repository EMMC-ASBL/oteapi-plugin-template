"""Demo transformation strategy class."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

from oteapi.models import AttrDict, TransformationConfig, TransformationStatus
from pydantic import Field
from pydantic.dataclasses import dataclass


class RunDummyTransformation(AttrDict):
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

    def get(self) -> AttrDict:
        """Execute the strategy.

        This method will be called through the strategy-specific endpoint of the
        OTEAPI Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.

        """
        return AttrDict()

    def run(self) -> RunDummyTransformation:
        """Run a transformation job.

        This method will be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.
            As a minimum, the dictionary will contain the job ID.

        """
        return RunDummyTransformation(result="a01d")

    def status(self, task_id: str) -> TransformationStatus:
        """Get job status.

        Parameters:
            task_id: The transformation job ID.

        Returns:
            An overview of the transformation job's status, including relevant
            metadata.

        """
        return TransformationStatus(
            id=task_id,
            status="wip",
            messages=[],
            created=datetime.utcnow(),
            startTime=datetime.utcnow(),
            finishTime=datetime.utcnow(),
        )
