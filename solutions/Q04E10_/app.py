from enum import Enum

from fastapi import FastAPI, HTTPException

from repositories.storage import Storage
from repositories.dock import SpaceDock
from models.spaceships import Interceptor, Bomber, Frigate, Destroyer, Cruiser

app = FastAPI()
dock = SpaceDock()
storage = Storage()


class ShipType(Enum):
    INTERCEPTOR = Interceptor
    BOMBER = Bomber
    FRIGATE = Frigate
    CRUISER = Cruiser
    DESTROYER = Destroyer


@app.post('/ship/{type}/build/{quantity}')
def build_ships(type: str, quantity: int):
    try:
        ship_class = ShipType[type]
    except KeyError:
        raise ValueError(f'ship type {type} does not exists')


@app.get('ship/fleet/{fleet_name}')
def get_fleet(fleet_name: str):
    pass


@app.get('/resource/stock')
def get_resource_stocks(type: str):
    match type.lower():
        case 'metal':
            return storage.metal
        case 'crystal':
            return storage.crystal
        case 'fuel':
            return storage.fuel
        case _:
            raise ValueError(f'resource type {type} does not exists')


@app.post('/resource/produce')
def produce_resources():
    pass
