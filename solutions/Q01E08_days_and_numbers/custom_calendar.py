days_by_index = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}
index_by_days = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7,
}


def day_from_number(day_number: int) -> str | None:
    return days_by_index.get(day_number)


def day_to_number(day: str) -> int | None:
    return index_by_days.get(day)
