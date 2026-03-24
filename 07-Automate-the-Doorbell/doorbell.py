from typing import ClassVar, Mapping, Sequence, Tuple

from typing_extensions import Self
from viam.components.board import Board
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.easy_resource import EasyResource
from viam.resource.types import Model, ModelFamily
from viam.services.generic import Generic
from viam.services.vision import VisionClient
from viam.utils import ValueTypes

# IMPORTANT: Do not change the class name or the MODEL triplet below.
# The platform uses these auto-generated values to identify your module.
# Changing them will break your inline module.
class MyGenericService(Generic, EasyResource):
    MODEL: ClassVar[Model] = Model(
        ModelFamily("viam-devrel", "ring-doorbell"), "generic-service"
    )

    board: Board
    detector: VisionClient

    @classmethod
    def validate_config(
        cls, config: ComponentConfig
    ) -> Tuple[Sequence[str], Sequence[str]]:
        # Declare board-1 and person-detector as required dependencies
        return ["board-1", "person-detector"], []

    @classmethod
    def new(
        cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]
    ) -> Self:
        self = cls(config.name)
        self.board = dependencies[Board.get_resource_name("board-1")]
        self.detector = dependencies[VisionClient.get_resource_name("person-detector")]
        return self

    async def do_command(
        self, command: Mapping[str, ValueTypes], **kwargs
    ) -> Mapping[str, ValueTypes]:
        # Get the GPIO pin connected to the LED
        led_pin = await self.board.gpio_pin_by_name("11")

        # Ask the vision service for detections from the camera
        detections = await self.detector.get_detections_from_camera("camera-1")

        # Check if any detection is a "Person" with sufficient confidence
        person_detected = any(
            d.class_name.lower() == "person" and d.confidence > 0.5
            for d in detections
        )

        # Light the LED if a person is detected, turn it off otherwise
        await led_pin.set(high=person_detected)

        return {"person_detected": person_detected}
