import random

from base_spaceships import Spaceship
from fleet import Fleet


class Simulator:
    def __init__(self, offensive_fleet: Fleet, defensive_fleet: Fleet):
        self._offensive_fleet = offensive_fleet
        self._defensive_fleet = defensive_fleet

    def fight(self) -> None:
        # fight between battleships
        self._simulate_fight(attacker_ships=self._offensive_fleet.get_alive_battleships(),
                             defender_ships=self._defensive_fleet.get_alive_battleships())

        # fight between fighters
        self._simulate_fight(attacker_ships=self._offensive_fleet.get_alive_fighters(),
                             defender_ships=self._defensive_fleet.get_alive_fighters())

        # fight between all ships
        self._simulate_fight(attacker_ships=self._offensive_fleet.get_all_alive_ships(),
                             defender_ships=self._defensive_fleet.get_all_alive_ships())

    def get_report(self) -> dict:
        return {
            self._offensive_fleet.name: self._offensive_fleet.get_report(),
            self._defensive_fleet.name: self._defensive_fleet.get_report(),
        }

    @staticmethod
    def _duel_fight(self, attacker_ship: Spaceship, defender_ship: Spaceship) -> None:
        attacker_ship.fire_on(defender_ship)
        if defender_ship.is_alive:
            defender_ship.fire_on(attacker_ship)

    def _simulate_fight(self, attacker_ships: list[Spaceship], defender_ships: list[Spaceship]):
        if not defender_ships:
            return
        for off_ship in attacker_ships:
            def_ship = random.choice(defender_ships)
            if off_ship.is_alive and def_ship.is_alive:
                self._duel_fight(off_ship, def_ship)
