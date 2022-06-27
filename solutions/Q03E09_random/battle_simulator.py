import random

from base_spaceships import Spaceship


class Simulator:
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
