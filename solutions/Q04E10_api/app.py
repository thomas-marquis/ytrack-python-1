import os

from fastapi import FastAPI, HTTPException

from dock import SpaceDock
from dock_repositories import SpaceDockRepository, SpaceDockFileRepository, SpaceDockInMemoryRepository
from ship_types import ShipType
from space_yard import SpaceYard

app = FastAPI()


def init_dock_repository() -> SpaceDockRepository:
    match os.getenv('DOCK_REPOSITORY', 'IN_MEMORY').lower():
        case 'in_memory':
            return SpaceDockFileRepository('fleet.pickle')
        case 'file':
            return SpaceDockInMemoryRepository()
        case other:
            raise ValueError(f'Repository {other} does not exist')


@app.post('/ship/{ship_name}/fleet/{fleet_name}/build/{quantity}')
def build_ships(ship_name: str, fleet_name: str, quantity: int, metal: int, crystal: int):
    dock_repository = init_dock_repository()
    dock = dock_repository.load()
    space_yard = SpaceYard(dock)
    try:
        ship_class = ShipType[type]
        space_yard.build_ship(fleet_name, )
    except KeyError:
        raise HTTPException(404, f'ship type {type} does not exists')


@app.get('ship/fleet/{fleet_name}')
def get_fleet(fleet_name: str):
    dock: SpaceDock = dock_repository.load()
    try:
        fleet = dock[fleet_name]
    except:
        raise HTTPException(404, f'fleet {fleet_name} not found')
    return fleet.get_report()
