from operator import itemgetter
from typing import Literal


def sort_recipes(recipes: list[dict], by: Literal['title', 'persons']) -> list[dict]:
    if by not in ['title', 'persons']:
        raise ValueError('Invalid value for parameter by')
    return sorted(recipes, key=itemgetter(by))
