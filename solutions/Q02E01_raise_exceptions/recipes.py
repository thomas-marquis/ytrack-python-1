def create_recipe(title: str, persons: int, ingredients: list[str]) -> dict:
    if len(title) > 150:
        raise ValueError('Title is too long')
    if not persons or persons > 50:
        raise ValueError('Invalid persons number')
    if not ingredients:
        raise ValueError('This recipe has no ingredients')
    
    return {
        'title': title,
        'persons': persons,
        'ingredients': ingredients,
    }
