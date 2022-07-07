import os
import pickle

import pytest
from behave import *
from fastapi.testclient import TestClient

from app import app

DOCK_FILE = 'fleets.pickle'


@given('ship name is "{ship_name}"')
def step_impl(context, ship_name):
    context.ship_name = ship_name


@given('quantity is "{quantity}"')
def step_impl(context, quantity):
    context.quantity = quantity


@given('metal stock is "{metal}"')
def step_impl(context, metal):
    context.metal = metal


@given('crystal stock is "{crystal}"')
def step_impl(context, crystal):
    context.crystal = crystal


@given('fleet name is "{fleet_name}"')
def step_impl(context, fleet_name):
    context.fleet_name = fleet_name


@when('call route /ship with POST')
def step_impl(context):
    client = TestClient(app)
    response = client.post('/ship', {
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


@then('ships should be created in space dock')
def step_impl(context):
    if not os.path.exists(DOCK_FILE):
        pytest.fail(f'file {DOCK_FILE} not exists')
        
    with open(DOCK_FILE, 'rb') as f:
        dock = pickle.load(f)


@then('ships should NOT be created in space dock')
def step_impl(context):
    pass


@then('return status code "{status_code}"')
def step_impl(context, status_code):
    assert context.response.status_code == status_code


@then('return fleet report')
def step_impl(context):
    assert context.response.json() == {
        'alive_battleships': 0,
        'alive_fighters': 0,
        'dead_battleships': 0,
        'dead_fighters': 0,
    }
