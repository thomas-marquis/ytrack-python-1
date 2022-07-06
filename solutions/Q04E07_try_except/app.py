from dock import SpaceDock, SpaceDockRepository
from ship_types import ShipType


dock_repository = SpaceDockRepository('fleet.pickle')


def build_ships(type: str, quantity: int):
    try:
        ship_class = ShipType[type]
        
        
    except KeyError:
        raise ValueError(f'ship type {type} does not exists')


def get_fleet(fleet_name: str):
    dock: SpaceDock = dock_repository.load()
    try:
        fleet = dock[fleet_name]
    except:
        raise ValueError(f'fleet {fleet_name} not found')
    return fleet.get_report()
