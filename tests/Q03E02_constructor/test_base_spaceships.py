import random

import pytest

from base_spaceships import Spaceship

_UNDEFINED = object()


class TestSpaceship:
    def test_should_be_instance_attributes(self):
        attr_should_not_exists = getattr(Spaceship, 'attack', _UNDEFINED)
        if attr_should_not_exists is not _UNDEFINED:
            pytest.fail('attack should be an instance attribuTe, not a class attribute')

        attr_should_not_exists = getattr(Spaceship, 'defense', _UNDEFINED)
        if attr_should_not_exists is not _UNDEFINED:
            pytest.fail('defense should be an instance attribuTe, not a class attribute')

    def test_constructor(self):
        attack = random.randint(100, 1000)
        defense = random.randint(1000, 5000)
        spaceship = Spaceship(attack, defense)
        
        assert spaceship.attack == attack, 'Pass attack as constructor first argument'
        assert spaceship.defense == defense, 'Pass defense as constructor second argument'
        assert spaceship.is_alive is True, 'is_alive should be always True'
        assert Spaceship.is_alive is True, 'is_alive should be a class attribute'
        
    def test_constructor_with_kwargs(self):
        attack = random.randint(100, 1000)
        defense = random.randint(1000, 5000)
        spaceship = Spaceship(attack=attack, defense=defense)
        
        assert spaceship.attack == attack, 'Pass attack as constructor attack argument'
        assert spaceship.defense == defense, 'Pass defense as constructor defense argument'
        assert spaceship.is_alive is True, 'is_alive should be always True'
        assert Spaceship.is_alive is True, 'is_alive should be a class attribute'
