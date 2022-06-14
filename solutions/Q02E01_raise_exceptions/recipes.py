def create_recipe(title: str, persons: int, ingredients: list[str]) -> dict:
    if not ingredients:
        raise ValueError('this recipe has no ingredients')
    
    return {
        'title': title,
        'persons': persons,
        'ingredients': ingredients,
    }
