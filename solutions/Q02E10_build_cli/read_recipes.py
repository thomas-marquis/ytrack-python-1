import json


def get_recipes(file_name: str) -> list[dict]:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = json.load(f)
    return content
