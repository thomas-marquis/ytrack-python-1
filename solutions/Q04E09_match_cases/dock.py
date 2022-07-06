from fleet import Fleet


class SpaceDock:
    def __init__(self) -> None:
        self.fleets = {'default': Fleet('default', [])}

    def __setitem__(self, index, value):
        if not self.fleets.get(index):
            self.fleets[index] = Fleet(index, value)
            
    def __getitem__(self, index):
        if fleet := self.fleets.get(index):
            return fleet
        else:
            fleet = Fleet(index, [])
            self.fleets[index] = fleet
            return fleet

    def __delitem__(self, index):
        if not self.fleets.get(index):
            raise ValueError(f'Fleet {index} not exists in space dock')
        del self.fleets[index]
        
    def __str__(self) -> str:
        return ', '.join(f'{name}: {len(fleet.ships)} ships' for name, fleet in self.fleets.items())
    