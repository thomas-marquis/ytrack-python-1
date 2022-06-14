def create_recipe_v2(title: str, persons: int, *ingredients, **tags) -> dict:
    if not ingredients:
        raise ValueError('this recipe has no ingredients')
    
    return {
        'title': title,
        'persons': persons,
        'ingredients': ingredients,
        'tags': tags,
    }
