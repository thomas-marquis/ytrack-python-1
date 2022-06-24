import random

from base_spaceships import Spaceship


class Simulator:
    def _duel_fight(self, attacker_ship: Spaceship, defender_ship: Spaceship) -> None:
        attacker_ship.fire_on(defender_ship)
        defender_ship.fire_on(attacker_ship)
        
    def _simulate_fight(self, attackers_ships: list[Spaceship], defender_ships: list[Spaceship]):
        for off_ship in attackers_ships:
            if defender_ships and off_ship.is_alive:
                def_ship = random.choice(defender_ships)
                self._duel_fight(off_ship, def_ship)
            else:
                break
