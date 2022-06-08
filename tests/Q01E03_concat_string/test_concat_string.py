import pytest

import concat_string


@pytest.mark.parametrize('first, second, expected', [
    ('Je suis mon cher amis', 'très heureux de te voir', 'Je suis mon cher amis, très heureux de te voir'),
    ('No', 'I am your father', 'No, I am your father'),
])
def test_concat(first: str, second: str, expected: str):
    res = concat_string.concat(first, second)
    assert res == expected
