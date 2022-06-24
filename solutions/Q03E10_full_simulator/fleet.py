from .base_spaceships import Spaceship, Fighter, Battleship


class Fleet:
    def __init__(self, name: str, ships: list[Spaceship]):
        self.name = name
        self.ships = ships

    def get_all_alive_ships(self):
        return [ship for ship in self.ships if ship.is_alive]

    def get_alive_battleships(self) -> list[Battleship]:
        return [ship for ship in self.ships if isinstance(ship, Battleship) and ship.is_alive]
    
    def get_alive_fighters(self) -> list[Fighter]:
        return [ship for ship in self.ships if isinstance(ship, Fighter) and ship.is_alive]
    
    def get_report(self):
        return {
            'alive_battleships': len(self.get_battleships()),
            'alive_fighters': len(self.get_fighters()),
            'dead_battleships': len([ship for ship in self.ships if isinstance(ship, Battleship) and not ship.is_alive]),
            'dead_fighters': len([ship for ship in self.ships if isinstance(ship, Fighter) and not ship.is_alive]),
        }
