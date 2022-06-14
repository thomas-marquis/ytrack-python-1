import json

import read_recipes


def test_get_recipes():
    with open('recipes_data.json', 'r') as f:
        expected = json.dump(f)

    res = read_recipes.get_recipes()
    
    assert res == expected
