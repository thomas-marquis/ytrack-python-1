from base_spaceships import Battleship, Fighter, Spaceship


class Interceptor(Fighter):
    def __init__(self):
        super().__init__(attack=180, defense=1000)
        
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Fighter):    
            attack *= 2
            
        other_ship.take_damages(attack)
        return other_ship


class Bomber(Fighter):
    def __init__(self):
        super().__init__(attack=150, defense=2000)
    
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Battleship):
            attack *= 2
            
        other_ship.take_damages(attack)
        return other_ship
    
    
class Cruiser(Battleship):
    def __init__(self):
        super().__init__(attack=800, defense=3000)
        
        
class Frigate(Battleship):
    def __init__(self):
        super().__init__(attack=500, defense=2500)
        
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Fighter):
            attack *= 2
            
        other_ship.take_damages(attack)
        return other_ship
        
        
class Destroyer(Battleship):
    def __init__(self):
        super().__init__(attack=650, defense=5000)
        
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Battleship):
            attack *= 2
            
        other_ship.take_damages(attack)
        return other_ship
