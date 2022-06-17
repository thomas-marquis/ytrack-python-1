def filter_recipes(recipes: list[dict], max_persons: int) -> list[str]:
    return [rec['title'] for rec in recipes if rec['persons'] < max_persons]
