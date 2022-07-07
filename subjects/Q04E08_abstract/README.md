# Abstract classes

## Instructions

Go to file `dock_repositories.py` and create an abstract class `SpaceDockRepository` that declare 2 abstract methods:

* `save(self, dock: SpaceDock) -> None:`
* `load(self) -> SpaceDock:`

Exte



## Usage

Here is a possible `test.py` to test your functions:

```python
from ship_types import get_ship_class_by_name
from spaceships import Interceptor

if __name__ == '__main__':
    print(get_ship_class_by_name('interceptor') == Interceptor)
    print(get_ship_class_by_name('intERCEptoR') == Interceptor)
```

```bash
$ python test.py
True
True
```

## Notion

* [access to an enum item by name](https://docs.python.org/fr/3/library/enum.html#programmatic-access-to-enumeration-members-and-their-attributes)
* [Handle exceptions](https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7197031-gerez-les-exceptions)
