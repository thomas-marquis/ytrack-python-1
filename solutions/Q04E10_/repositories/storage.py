from exceptions import ResourceError
from models.building import Building


class ResourceStorage:
    def __init__(self, resource_name: str, capacity: int, stock: int) -> None:
        self._resource_name = resource_name
        self._capacity = capacity
        self._current_stock = stock
    
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @capacity.setter
    def capacity(self, new_capacity: int) -> None:
        if not new_capacity >= 0:
            raise ValueError('Expected positive number for capacity')
        self._capacity = int(new_capacity)
    
    @property
    def current_stock(self) -> int:
        return self.current_stock
    
    def store(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError('Impossible to store a negative resource quantity')
        self.current_stock = min(self.current_stock + quantity, self._capacity)

    def use(self, quantity: int):
        if quantity < 0:
            raise ValueError('Expected positive number for used quantity')
        remaining = self.current_stock - quantity
        if remaining < 0:
            raise ResourceError(f'Not enough {self._resource_name}')
        self._current_stock = remaining


class Storage(Building):
    def __init__(self) -> None:
        self._metal_storage = ResourceStorage('metal', 0, 0)
        self._crystal_storage = ResourceStorage('crystal', 0, 0)
        self._fuel_storage = ResourceStorage('fuel', 0, 0)
    
    @property
    def metal(self):
        return self._metal_storage.current_stock
    
    @property
    def crystal(self):
        return self._crystal_storage.current_stock
    
    @property
    def fuel(self):
        return self._fuel_storage.current_stock
    
    def level_up(self):
        super().level_up()
        self._metal_storage.capacity = self.level * 10_000 * 1.2
        self._crystal_storage.capacity = self.level * 5_000 * 1.1
        self._fuel_storage.capacity = self.level * 8_000 * 1.2
    
    def store(self, resource_name: str, quantity: int) -> None:
        resource_storage = self._get_resource_storage(resource_name)
        resource_storage.store(quantity)
            
    def use(self, resource_name: str, quantity: int) -> None:
        resource_storage = self._get_resource_storage(resource_name)
        resource_storage.use(quantity)

    def _get_resource_storage(self, resource_name: str) -> ResourceStorage:
        match resource_name:
            case 'metal':
                return self._metal_storage
            case 'crystal':
                return self._crystal_storage
            case 'fuel':
                return self._fuel_storage
            case _:
                raise ValueError(f'Invalid resource {resource_name}')
