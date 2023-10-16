"""Demo transformation strategy class."""
from datetime import datetime
from typing import Any, Optional, Annotated

from oteapi.models import SessionUpdate, TransformationConfig, TransformationStatus
from pydantic import Field
from pydantic.dataclasses import dataclass


class SessionUpdateDummyTransformation(SessionUpdate):
    """Class for returning values from Dummy Transformation strategy."""

    result: Annotated[str, Field(description="The job ID.")]


@dataclass
class DummyTransformationStrategy:
    """Transformation Strategy.

    **Registers strategies**:

    - `("transformationType", "script/DEMO")`

    """

    transformation_config: TransformationConfig

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

    def run(
        self, session: Optional[dict[str, Any]] = None
    ) -> SessionUpdateDummyTransformation:
        """Run a transformation job.

        This method will be called through the `/initialize` endpoint of the OTEAPI
        Services.

        Parameters:
            session: A session-specific dictionary context.

        Returns:
            An update model of key/value-pairs to be stored in the
            session-specific context from services.
            As a minimum, the dictionary will contain the job ID.

        """
        return SessionUpdateDummyTransformation(result="a01d")

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
