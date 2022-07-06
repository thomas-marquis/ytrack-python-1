from models.base_spaceships import Spaceship
from models.fleet import Fleet


class SpaceDock:
    def __init__(self) -> None:
        self.fleets = {'default': Fleet('default', [])}

    def __setitem__(self, index, value):
        if not self.fleets.get(index):
            self.fleets[index] = Fleet(index, value)

    def __getitem__(self, index):
        return self.fleets.get(index)

    def __delitem__(self, index):
        if not self.fleets.get(index):
            raise ValueError(f'Fleet {index} not exists in space dock')
        del self.fleets[index]
        
    def __str__(self) -> str:
        return ', '.join(f'{name}: {len(ships)} ships' for name, ships in self.fleets.items())

    def __contains__(self, value: Fleet):
        return value.name in self.fleets
    
