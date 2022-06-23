from .base_spaceships import Spaceship


class Simulator:
    def _duel_fight(self, attacker_ship: Spaceship, defender_ship: Spaceship) -> None:
        attacker_ship.fire_on(defender_ship)
        defender_ship.fire_on(attacker_ship)
