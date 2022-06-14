import datetime as dt


def save_menu(meals: list[tuple[dt.date, str]]):
    with open('menu.txt', 'w') as f:
        f.writelines([f'{dt.datetime.strftime(date, "%A %d %B %Y")}: {title}' for date, title in meals])
