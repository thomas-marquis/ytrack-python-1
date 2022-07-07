from base_spaceships import Spaceship
from dock import SpaceDock
from exceptions import ResourceError


class SpaceYard:
    def __init__(self, dock: SpaceDock) -> None:
        self._dock = dock
        
    def build_ship(self, fleet_name: str, ship_class: type[Spaceship], quantity: int, available_metal: int, available_crystal: int):
        req = ship_class.requirements
        
        if req.metal * quantity > available_metal:
            raise ResourceError(f'Not enough metal to build {quantity} {ship_class.__name__}')
        if req.crystal * quantity > available_crystal:
            raise ResourceError(f'Not enough crystal to build {quantity} {ship_class.__name__}')

        new_ships = [ship_class() for _ in range(quantity)]
        
        self._dock[fleet_name] += new_ships
