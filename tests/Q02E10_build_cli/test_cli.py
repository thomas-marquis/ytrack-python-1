import subprocess

import pytest

expected_case_1 = (
'''Wednesday 15 June 2022: Croissant de la mer
Thursday 16 June 2022: Galette de légumes
Friday 17 June 2022: Galettes des rois
Saturday 18 June 2022: Rochers aux coco
Sunday 19 June 2022: Spaghetti Napolitaine révisé''')


@pytest.mark.parametrize('command, expected', [
    ('python cli.py --start 15/06/2022 --max-persons 5', expected_case_1),
])
def test_cli(command: str, expected: str):
    process = subprocess.Popen(command)
    process.wait()
    with open('menu.txt', 'r') as f:
        res = f.read().strip()

    assert process.returncode == 0, 'your program terminated with error'
    assert res == expected
