from base_spaceships import Spaceship


class Simulator:
    @staticmethod
    def _duel_fight(attacker_ship: Spaceship, defender_ship: Spaceship) -> None:
        attacker_ship.fire_on(defender_ship)
        if defender_ship.is_alive:
            defender_ship.fire_on(attacker_ship)
