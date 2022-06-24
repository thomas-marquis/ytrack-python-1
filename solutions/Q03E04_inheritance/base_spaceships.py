class Spaceship:
    is_alive: bool = True
    
    def __init__(self, attack: int, defense: int):
        self.attack = attack
        self.defense = defense
        
    def take_damages(self, damages: int):
        self.defense -= damages
        if self.defense <= 0:
            self.defense = 0
            self.is_alive = False


class Battleship(Spaceship):
    pass


class Fighter(Spaceship):
    pass
