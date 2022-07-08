import os
import pickle
from collections import Counter

from behave import *
from fastapi.testclient import TestClient

from app import app


@given('ship name is "{ship_name}"')
def step_impl(context, ship_name):
    context.ship_name = str(ship_name)


@given('quantity is "{quantity}"')
def step_impl(context, quantity):
    context.quantity = int(quantity)


@given('metal stock is "{metal}"')
def step_impl(context, metal):
    context.metal = int(metal)


@given('crystal stock is "{crystal}"')
def step_impl(context, crystal):
    context.crystal = int(crystal)


@given('fleet name is "{fleet_name}"')
def step_impl(context, fleet_name):
    context.fleet_name = str(fleet_name)


@when('call route /ship with POST')
def step_impl(context):
    client = TestClient(app)
    response = client.post('/ship', json={
        'metal_stock': context.metal,
        'crystal_stock': context.crystal,
        'fleet_name': context.fleet_name,
        'quantity': context.quantity,
        'ship_name': context.ship_name,
    })
    context.response = response


@when('call route /ship/fleet/<fleet_name> with GET')
def step_impl(context):
    client = TestClient(app)
    response = client.get(f'/ship/fleet/{context.fleet_name}')
    context.response = response


@then('space dock should be empty')
def step_impl(context):
    if os.path.exists(context.dock_file):
        with open(context.dock_file, 'rb') as f:
            dock = pickle.load(f)
            
        actual_dock_type = type(dock).__name__.lower()
        assert actual_dock_type == 'spacedock', (f'Invalid type for SpaceDock: {actual_dock_type}. '
                                                f'You must serialize a valid SpaceDOck in file {context.dock_file}')
            
        actual_fleets = {}
        for actual_fleet in dock.fleets.values():
            actual_ship_types: list[str] = [type(ship).__name__.lower() for ship in actual_fleet.ships]
            ship_types_counter = Counter(actual_ship_types)
            actual_fleets[actual_fleet.name] = dict(ship_types_counter)
            
        expected_fleets = {'default': {}}
            
        assert actual_fleets == expected_fleets, f'SpaceDock should be empty: {actual_fleets=}, {expected_fleets=}'

@then('following ships should be in space dock')
def step_impl(context):
    expected_fleets = {}
    for row in context.table:
        fleet = row['fleet']
        if not expected_fleets.get(fleet):
            expected_fleets[fleet] = {}
        ship = row['ship']
        if ship:
            expected_fleets[fleet][ship.lower()] = int(row['number'])
        
    # table:
    # | fleet     | ship        | number |
    # | default   |             |        |
    # | attackers | interceptor | 100    |
    # expected_fleets = {
    #     'default': {},
    #     'attackers': {'interceptor': 100},
    # }
        
    if not os.path.exists(context.dock_file):
        assert False, f'File {context.dock_file} does not exist'
        
    with open(context.dock_file, 'rb') as f:
        dock = pickle.load(f)
        
    actual_dock_type = type(dock).__name__.lower()
    assert actual_dock_type == 'spacedock', (f'Invalid type for SpaceDock: {actual_dock_type}. '
                                             f'You must serialize a valid SpaceDOck in file {context.dock_file}')
        
    actual_fleets = {}
    for actual_fleet in dock.fleets.values():
        actual_ship_types: list[str] = [type(ship).__name__.lower() for ship in actual_fleet.ships]
        ship_types_counter = Counter(actual_ship_types)
        actual_fleets[actual_fleet.name] = dict(ship_types_counter)
        
    assert actual_fleets == expected_fleets, f'Unexpected SpaceDock content: {actual_fleets=}, {expected_fleets=}'


@then('return status code "{status_code}"')
def step_impl(context, status_code):
    expected_code = int(status_code)
    actual_code = context.response.status_code
    assert actual_code == expected_code, f'{actual_code=}, {expected_code=}'


@then('return fleet report')
def step_impl(context):
    expected_response = {
        'alive_battleships': 0,
        'alive_fighters': 0,
        'dead_battleships': 0,
        'dead_fighters': 0,
    }
    actual_response = context.response.json()
    assert actual_response == expected_response, f'Unexpected fleet report: {actual_response=}, {expected_response=}'
