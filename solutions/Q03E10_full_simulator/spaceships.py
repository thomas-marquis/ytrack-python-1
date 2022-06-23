from .base_spaceships import Battleship, Fighter, Spaceship


class Interceptor(Fighter):
    def __init__(self):
        super().__init__(attack=100, defense=200)
        
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Fighter):    
            attack *= 2
            
        other_ship.take_damages(attack)
        return other_ship


class Bomber(Fighter):
    def __init__(self):
        super().__init__(attack=300, defense=700)
    
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Fighter):
            attack *= 0.5
            
        other_ship.take_damages(attack)
        return other_ship
    
    
class Cruiser(Battleship):
    def __init__(self):
        super().__init__(attack=950, defense=5000)
        
        
class Frigate(Battleship):
    def __init__(self):
        super().__init__(attack=600, defense=3500)
        
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Fighter):
            attack *= 2
            
        other_ship.take_damages(attack)
        return other_ship
        
        
class Destroyer(Battleship):
    def __init__(self):
        super().__init__(attack=800, defense=4000)
        
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Battleship):
            attack *= 2
            
        other_ship.take_damages(attack)
        return other_ship
