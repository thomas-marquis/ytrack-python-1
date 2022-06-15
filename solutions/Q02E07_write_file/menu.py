import datetime_utils


def save_menu(meals: list[tuple[dt.date, str]]):
    with open('menu.txt', 'w') as f:
        f.writelines([f'{datetime_utils.format_date(date)}: {title}' for date, title in meals])
