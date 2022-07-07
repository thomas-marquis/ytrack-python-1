from enum import Enum

from base_spaceships import Spaceship
from spaceships import Interceptor, Bomber, Frigate, Cruiser, Destroyer


class ShipType(Enum):
    INTERCEPTOR = Interceptor
    BOMBER = Bomber
    FRIGATE = Frigate
    CRUISER = Cruiser
    DESTROYER = Destroyer


def get_ship_from_by_name(ship_name: str) -> type[Spaceship]:
    try:
        return ShipType[ship_name.upper()]
    except KeyError:
        raise ValueError(f'Ship {ship_name} does not exist')