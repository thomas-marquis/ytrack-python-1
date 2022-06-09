import pytest

import punishment


@pytest.mark.parametrize('first_part, second_part, nb_lines, expected', [
    (
        'Je ne jetterai plus de cacahuètes', 
        'sur le professeur', 
        3,
        'Je ne jetterai plus de cacahuètes sur le professeur. '
        'Je ne jetterai plus de cacahuètes sur le professeur. '
        'Je ne jetterai plus de cacahuètes sur le professeur.',
    ),
    (
        'Je ne jetterai plus de cacahuètes', 
        'sur le professeur      ', 
        3,
        'Je ne jetterai plus de cacahuètes sur le professeur. '
        'Je ne jetterai plus de cacahuètes sur le professeur. '
        'Je ne jetterai plus de cacahuètes sur le professeur.',
    ),
    (
        'Je ne jetterai plus de cacahuètes', 
        '     sur le professeur', 
        3,
        'Je ne jetterai plus de cacahuètes sur le professeur. '
        'Je ne jetterai plus de cacahuètes sur le professeur. '
        'Je ne jetterai plus de cacahuètes sur le professeur.',
    ),
    (
        'Je ne jetterai plus de cacahuètes', 
        'sur le professeur', 
        0,
        '',
    ),
])
def test_do_punishment(first_part: str, second_part: str, nb_lines: int, expected: str):
    res = punishment.do_punishment(first_part, second_part, nb_lines)
    assert res == expected, f'{first_part=}, {second_part=}, {nb_lines=} => {expected=}'
