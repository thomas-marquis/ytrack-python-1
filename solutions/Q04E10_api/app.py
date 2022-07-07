import os

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from dock import SpaceDock
from dock_repositories import SpaceDockRepository, SpaceDockFileRepository, SpaceDockInMemoryRepository
from exceptions import ResourceError
from ship_types import get_ship_class_by_name
from space_yard import SpaceYard

app = FastAPI()


def init_dock_repository() -> SpaceDockRepository:
    match os.getenv('DOCK_REPOSITORY', 'IN_MEMORY').lower():
        case 'file':
            return SpaceDockFileRepository('fleets.pickle')
        case 'in_memory':
            return SpaceDockInMemoryRepository()
        case other:
            raise ValueError(f'Repository {other} does not exist')


dock_repository = init_dock_repository()


class BuildShipRequest(BaseModel):
    metal_stock: int
    crystal_stock: int
    fleet_name: str
    ship_name: str
    quantity: int


@app.post('/ship', status_code=status.HTTP_201_CREATED)
def build_ships(body: BuildShipRequest):
    dock = dock_repository.load()
    space_yard = SpaceYard(dock)
    
    try:
        ship_class = get_ship_class_by_name(body.ship_name).value
        space_yard.build_ship(fleet_name=body.fleet_name, 
                              ship_class=ship_class, 
                              quantity=body.quantity,
                              available_metal=body.metal_stock,
                              available_crystal=body.crystal_stock)
        dock_repository.save(dock)
    except ValueError as err:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(err))
    except ResourceError as err:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(err))


@app.get('/ship/fleet/{fleet_name}')
def get_fleet(fleet_name: str):
    dock: SpaceDock = dock_repository.load()
    fleet = dock[fleet_name]
    return fleet.get_report()
