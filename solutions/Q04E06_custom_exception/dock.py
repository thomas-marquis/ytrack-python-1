import pickle

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
    
    
class SpaceDockFileRepository:
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def save(self, dock: SpaceDock):
        with open(self._file_name, 'wb') as f:
            pickle.dump(dock, f)
            
    def load(self) -> SpaceDock:
        with open(self._file_name, 'rb') as f:
            return pickle.load(f)


if __name__ == '__main__':
    from base_spaceships import Spaceship
    from spaceships import Interceptor
    dock = SpaceDock()
    i1 = Interceptor()
    i2 = Interceptor()
    dock['starfleet'] = [i1, i2]
    dock['starfleet'] += [i1, i2]
    print(dock)

    
    # dock_repo = SpaceDockRepository('fleets.pickle')
    # dock_repo.save(dock)
    # dock = dock_repo.load()
    # print(dock)