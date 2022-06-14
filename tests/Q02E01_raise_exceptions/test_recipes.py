import pytest
import re

import recipes


def test_create_recipe_should_raise_value_error():
    ingredients = ['Pate à pizza', 
                   'Frourne d\'Ambert', 
                   'Comté',
                   'Emental',
                   'Mozzarella']
    res = recipes.create_recipe('pizza 4 fromages', 1, ingredients)
    expected = {'title': 'pizza 4 fromages', 'persons': 1, 'ingredients': ingredients}
    assert res == expected


def test_create_recipe_should_raise_value_error():
    with pytest.raises(ValueError, match=re.compile('this recipe has no ingredients', flags=re.I)):
        recipes.create_recipe('tacos à la grec', 12, [])
