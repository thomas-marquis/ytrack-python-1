import pytest

import string_processing


@pytest.mark.parametrize('sentence, expected', [
    (
        "Dites, on n'attend pas votre soeur ?",
        ['dites', 'on', 'n', 'attend', 'pas', 'votre', 'soeur'],
    ),
    (
        '',
        [],
    ),
    (
        'Coucou',
        ['coucou'],
    ),
    (
        "      je Ne pEnse pas   _-??   qu'il y ait de bonnes ou de mauvaises SITUATIONS.",
        ['je', 'ne', 'pense', 'pas', 'qu', 'il', 'y', 'ait', 'de', 'bonnes', 'ou', 'de', 'mauvaises', 'situations'],
    ),
    (
        "c'est-à-dire",
        ['c', 'est', 'à', 'dire'],
    ),
])
def test_tokenize(sentence: str, expected: list[str]):
    res = string_processing.tokenize(sentence)
    assert res == expected
