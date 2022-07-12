from base_spaceships import Spaceship, Fighter, Battleship


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
            'alive_battleships': len(self.get_alive_battleships()),
            'alive_fighters': len(self.get_alive_fighters()),
            'dead_battleships': len([ship for ship in self.ships if isinstance(ship, Battleship) and not ship.is_alive]),
            'dead_fighters': len([ship for ship in self.ships if isinstance(ship, Fighter) and not ship.is_alive]),
        }
        
    @property
    def alive_ships(self):
        return self.get_all_alive_ships()
    
    @property
    def alive_fighters(self):
        return self.get_alive_fighters()
    
    @property
    def alive_battleships(self):
        return self.get_alive_battleships()
    
    @property
    def report(self):
        return self.get_report()

    def __add__(self, other: Spaceship | list[Spaceship]):
        self.ships += [other] if isinstance(other, Spaceship) else other
