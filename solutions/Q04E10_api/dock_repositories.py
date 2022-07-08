import os
import pickle
from abc import ABC, abstractmethod

from dock import SpaceDock
    

class SpaceDockRepository(ABC):
    @abstractmethod
    def save(self, dock: SpaceDock) -> None:
        pass
    
    @abstractmethod
    def load(self) -> SpaceDock:
        pass
    
    
class SpaceDockFileRepository:
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def save(self, dock: SpaceDock):
        with open(self._file_name, 'wb') as f:
            pickle.dump(dock, f)
            
    def load(self) -> SpaceDock:
        if not os.path.exists(self._file_name):
            return SpaceDock()
        
        with open(self._file_name, 'rb') as f:
            return pickle.load(f)


class SpaceDockInMemoryRepository(SpaceDockRepository):
    def __init__(self) -> None:
        self._dock = SpaceDock()
    
    def save(self, dock: SpaceDock) -> None:
        self._dock = dock
        
    def load(self) -> SpaceDock:
        return self._dock
