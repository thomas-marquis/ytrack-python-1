from enum import Enum

from spaceships import Interceptor, Bomber, Frigate, Cruiser, Destroyer


class ShipType(Enum):
    INTERCEPTOR = Interceptor
    BOMBER = Bomber
    FRIGATE = Frigate
    CRUISER = Cruiser
    DESTROYER = Destroyer


def get_ship_class_by_name(ship_name: str) -> ShipType:
    try:
        return ShipType[ship_name.upper()]
    except KeyError:
        raise ValueError(f'Ship {ship_name} does not exist')
