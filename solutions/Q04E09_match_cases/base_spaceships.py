from requirements import Requirements


class Spaceship:
    is_alive: bool = True
    requirements: Requirements
    
    def __init__(self, attack: int, defense: int):
        self.attack = attack
        self.defense = defense
        
    def take_damages(self, damages: int):
        """Take damages and decrease the ship defense amount. If ship defense reach 0, ship is dead."""
        if damages < 0:
            raise ValueError('damages value should be a positive integer')
        self.defense -= damages
        if self.defense <= 0:
            self.defense = 0
            self.is_alive = False
        
    def fire_on(self, other_ship: 'Spaceship') -> 'Spaceship':
        other_ship.take_damages(self.attack)
        return other_ship
    

class Battleship(Spaceship):
    pass


class Fighter(Spaceship):
    pass
