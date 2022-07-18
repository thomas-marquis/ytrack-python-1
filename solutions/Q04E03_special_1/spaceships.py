from base_spaceships import Battleship, Fighter, Spaceship
from requirements import Requirements


class BattleshipKiller:
    bonus = 2
    
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Battleship):    
            attack *= self.bonus
            
        other_ship.take_damages(attack)
        return other_ship


class FighterKiller:
    bonus = 2
    
    def fire_on(self, other_ship: Spaceship) -> Spaceship:
        attack = self.attack
        if isinstance(other_ship, Fighter):
            attack *= self.bonus
            
        other_ship.take_damages(attack)
        return other_ship


class Interceptor(FighterKiller, Fighter):
    requirements: Requirements = Requirements(metal=1_000, crystal=200)

    def __init__(self):
        super().__init__(attack=180, defense=1000)
        

class Bomber(BattleshipKiller, Fighter):
    requirements: Requirements = Requirements(metal=2_500, crystal=400)

    def __init__(self):
        super().__init__(attack=150, defense=2000)
    

class Cruiser(Battleship):
    requirements: Requirements = Requirements(metal=25_000, crystal=10_000)

    def __init__(self):
        super().__init__(attack=800, defense=3000)
        
        
class Frigate(FighterKiller, Battleship):
    requirements: Requirements = Requirements(metal=10_000, crystal=10_000)

    def __init__(self):
        super().__init__(attack=500, defense=2500)
        
        
class Destroyer(BattleshipKiller, Battleship):
    requirements: Requirements = Requirements(metal=35_000, crystal=20_000)
    
    def __init__(self):
        super().__init__(attack=650, defense=5000)
        