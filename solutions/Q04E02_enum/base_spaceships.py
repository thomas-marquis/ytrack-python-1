from requirements import Requirements


class Spaceship:
    is_alive: bool = True
    requirements: Requirements
    
    def __init__(self, attack: int, defense: int):
        self.attack = attack
        self.defense = defense
        
    def take_damages(self, damages: int):
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
