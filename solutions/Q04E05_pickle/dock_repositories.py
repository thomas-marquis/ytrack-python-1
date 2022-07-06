import os
import pickle

from dock import SpaceDock
    
    
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
