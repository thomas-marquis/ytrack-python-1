import json


def get_recipes():
    with open('recipes_data.json', 'r') as f:
        content = json.dump(f)
    return content
