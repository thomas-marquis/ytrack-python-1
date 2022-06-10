def add(a: int | float, b: int | float) -> int | float:
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    return a * b


def power(a: int | float, b: int | float) -> int | float:
    return a ** b


def square(a: int | float) -> int | float:
    return power(a, 2)
