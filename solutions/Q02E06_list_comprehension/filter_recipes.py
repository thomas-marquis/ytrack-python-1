def filter_recipes(recipes: list[dict]) -> list[str]:
    return [rec['title'] for rec in recipes if rec['persons'] < 5]
