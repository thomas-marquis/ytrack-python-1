import datetime as dt


def build_menu(recipes: list[dict], start_date: dt.date) -> list[tuple[dt.date, str]]:
    meals = []
    for i, recipe in enumerate(recipes):
        meals.append((start_date + dt.timedelta(days=i), recipe['title']))
        
    return meals
