import pytest

import shopping


@pytest.mark.parametrize('case, input, expected', [
    (
        'list should be formatted correctly (read instructions ;) )',
        ['tomatoes', 'pastas', 'milk', 'salt'], 
        ['1/ Tomatoes', '2/ Pastas', '3/ Milk', '4/ Salt'],
    ),
    (
        'uppercase for the first letter only',
        ['milk', 'SalT'], 
        ['1/ Milk', '2/ Salt'],
    ),
])
def test_clean_list(case: str, input: list[str], expected: list[str]):
    res = shopping.clean_list(input)
    assert res == expected, case


@pytest.mark.parametrize('input_list, expected', [
    (['tomatoes', 'pastas', 'milk', 'salt'], ['1/ Tomatoes', '2/ Pastas', '3/ Milk', '4/ Salt']),
    (['tomatoes', 'pastas', 'salt'], ['1/ Tomatoes', '2/ Pastas', '3/ Salt', '4/ Milk']),
    (['milk'], ['1/ Milk']),
    (['milke'], ['1/ Milke', '2/ Milk']),
])
def test_clean_list_should_remember_the_milk(input_list: list[str], expected: list[str]):
    res = shopping.clean_list(input_list)
    assert res == expected


def test_clean_list_should_handle_empty():
    res = shopping.clean_list([])
    assert res == [], 'should return an empty list'
