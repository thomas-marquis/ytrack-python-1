import subprocess

import pytest

expected_case_1 = (
'''Wednesday 15 June 2022: Croissant de la mer
Thursday 16 June 2022: Galette de légumes
Friday 17 June 2022: Galettes des rois
Saturday 18 June 2022: Rochers aux coco
Sunday 19 June 2022: Spaghetti Napolitaine révisé''')


@pytest.mark.parametrize('command, expected, expected_code', [
    ('python cli.py --start 15/06/2022 --max-persons 5', expected_case_1, 0),
    ('python cli.py -s 15/06/2022 -p 5', expected_case_1, 0),
])
def test_cli(command: str, expected: str, expected_code: int):
    process = subprocess.Popen(command)
    
    process.wait()
    with open('menu.txt', 'r') as f:
        res = f.read().strip()
    actual_code = process.returncode

    assert actual_code == expected_code, f'your program terminated with exit code {actual_code}'
    assert res == expected
