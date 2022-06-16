import datetime as dt

import pytest

from decorator import with_current_date

expected = dt.date.today()


def test_with_current_date_with_single_kwarg():
    @with_current_date
    def mock_func(current_date):
        assert current_date == expected
        
    mock_func()
    

def test_with_current_date_with_many_args_and_kwargs():
    @with_current_date
    def mock_func(a, b, c, current_date):
        assert current_date == expected
        assert a == 'foo'
        assert b == 'bar'
        assert c == 42
        
    mock_func('foo', 'bar', c=42)
