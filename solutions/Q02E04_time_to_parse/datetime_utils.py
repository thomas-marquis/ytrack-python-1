import datetime as dt


def format_time(time_str: str):
    parsed = dt.datetime.strptime(time_str, '%d/%m/%Y')
    return parsed
