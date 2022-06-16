import pytest
import re

import recipes

ingredients = ['Pate à pizza', 'Frourne d\'Ambert', 'Comté', 'Emental', 'Mozzarella']


def test_create_recipe_v2():
    title = 'x' * 149
    res = recipes.create_recipe_v2(title, 49, *ingredients, regime='vegan')
    expected = {'title': title, 'persons': 49, 'ingredients': tuple(ingredients), 'tags': {'regime': 'vegan'}}
    assert res == expected, 'This function should return a dictionary with 3 keys: title, persons and ingredients'


def test_create_recipe_v2_should_raise_value_error_when_empty_ingredients():
    with pytest.raises(ValueError, match=re.compile('^this recipe has no ingredients$', flags=re.I)):
        recipes.create_recipe_v2('tacos à la grec', 12)


def test_create_recipe_v2_should_raise_value_error_when_title_too_long():
    with pytest.raises(ValueError, match=re.compile('^title is too long$', flags=re.I)):
        recipes.create_recipe_v2('x'*151, 12, *ingredients)


def test_create_recipe_v2_should_raise_value_error_when_too_many_persons():
    with pytest.raises(ValueError, match=re.compile('^invalid persons number$', flags=re.I)):
        recipes.create_recipe_v2('tacos à la grec', 51, *ingredients)


def test_create_recipe_v2_should_raise_value_error_when_zero_persons():
    with pytest.raises(ValueError, match=re.compile('^invalid persons number$', flags=re.I)):
        recipes.create_recipe_v2('tacos à la grec', 0, *ingredients)
