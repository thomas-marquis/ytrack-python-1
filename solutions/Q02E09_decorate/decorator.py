import datetime as dt


def with_current_date(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs, current_date=dt.date.today())
    return inner
