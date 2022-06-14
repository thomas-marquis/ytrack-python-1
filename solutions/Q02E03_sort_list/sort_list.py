from operator import itemgetter
from typing import Literal


def sort_recipes(recipes: list[tuple[str, int]], by: Literal['title', 'persons']) -> list[tuple[str, int]]:
    if by not in ['title', 'persons']:
        raise ValueError('Invalid value for parameter by')
    return sorted(recipes, key=itemgetter(0 if by == 'title' else 1))
