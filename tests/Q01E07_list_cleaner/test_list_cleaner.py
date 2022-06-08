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
    res = shopping.remember_the_milk(input_list)
    
    is_you_remember_the_milk = 'milk' in res
    is_all_items_present = sorted(res) == sorted(expected)
    
    assert is_you_remember_the_milk, 'You forgot the milk !'
    assert is_all_items_present, 'You remember the milk, be forgot another element...'


def test_clean_list_should_handle_empty():
    res = shopping.clean_list([])
    assert res == [], 'should return an empty list'
