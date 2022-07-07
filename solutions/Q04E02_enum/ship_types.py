from enum import Enum

from spaceships import Interceptor, Bomber, Frigate, Cruiser, Destroyer


class ShipType(Enum):
    INTERCEPTOR = Interceptor
    BOMBER = Bomber
    FRIGATE = Frigate
    CRUISER = Cruiser
    DESTROYER = Destroyer
