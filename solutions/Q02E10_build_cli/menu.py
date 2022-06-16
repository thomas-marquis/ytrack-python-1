import datetime as dt

import datetime_utils


def build_menu(recipes: list[str], start_date: dt.date) -> list[tuple[dt.date, str]]:
    meals = []
    for i, recipe in enumerate(recipes):
        meals.append((start_date + dt.timedelta(days=i), recipe))
        
    return meals


def save_menu(meals: list[tuple[dt.date, str]]):
    with open('menu.txt', 'w') as f:
        f.writelines([f'{datetime_utils.format_date(date)}: {title}\n' for date, title in meals])
