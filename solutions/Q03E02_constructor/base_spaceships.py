class Spaceship:
    is_alive: bool = True
    
    def __init__(self, attack: int, defense: int):
        self.attack = attack
        self.defense = defense
