def modulo(a: int | float, b: int | float) -> int | float:
    if b == 0:
        return 0
    return a % b


def divide(a: int | float, b: int | float) -> int | float:
    if b == 0:
        return 0
    return a / b


def integer_division(a: int | float, b: int | float) -> int | float:
    if b == 0:
        return 0
    return a // b
