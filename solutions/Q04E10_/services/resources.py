from abc import ABC, abstractmethod

from models.building import Building
from repositories.storage import Storage


class AbstractResourceProducer(Building, ABC):
    resource_name: str
    
    def __init__(self, storage: Storage) -> None:
        self._storage = storage
        
    @abstractmethod
    def produce(self) -> None:
        """Produce and store resource"""


class MetalMine(AbstractResourceProducer):
    resource_name: str = 'metal'

    def produce(self) -> None:
        self._storage.store(self.resource_name, self.level * 100)


class Crystallizer(AbstractResourceProducer):
    resource_name: str = 'crystal'

    def produce(self) -> None:
        self._storage.store(self.resource_name, self.level * 50)


class Refinery(AbstractResourceProducer):
    resource_name: str = 'fuel'

    def produce(self) -> None:
        self._storage.store(self.resource_name, self.level * 80)
