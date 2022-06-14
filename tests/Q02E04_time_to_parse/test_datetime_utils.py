import datetime as dt

import pytest

import datetime_utils


@pytest.mark.parametrize('dt_str, expected', [
    ('01/01/2001', dt.datetime(2001, 1, 1)),
    ('06/12/2022', dt.datetime(2022, 12, 6)),
])
def test_format_time(dt_str: str, expected: dt.datetime):
    res = datetime_utils.format_time(dt_str)
    assert res == expected
