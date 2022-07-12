class Spaceship:
    is_alive: bool = True
    
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


class Battleship(Spaceship):
    """Battle ship representation. Heavy spaceship with heigh level of defense and attack"""


class Fighter(Spaceship):
    """Star fighter representation. Small and fast spaceship with low level of defense."""
