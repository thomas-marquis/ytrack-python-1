import datetime as dt


def build_menu(start_date: dt.date):
    recipes = []
    
    meals = []
    for i, recipe in enumerate(recipes):
        meals.append((start_date + dt.timedelta(days=i), recipe['title']))
        
    return meals
        