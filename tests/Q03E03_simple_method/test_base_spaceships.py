import pytest

from base_spaceships import Spaceship

attack, defense = 100, 1000


@pytest.fixture
def spaceship():
    return Spaceship(attack, defense)


class TestSpaceship:
    def test_constructor(self, spaceship):
        assert spaceship.attack == attack, 'Pass attack as constructor first argument'
        assert spaceship.defense == defense, 'Pass defense as constructor second argument'
        assert spaceship.is_alive, 'is_alive should be always True'
        assert Spaceship.is_alive is True, 'is_alive should be a class attribute'

    def test_take_damages(self, spaceship):
        spaceship.take_damages(100)
        assert spaceship.defense == 900, 'Incorrect defense value'
        assert spaceship.attack == 100, 'this method does not modify the attack attribute'
        assert spaceship.is_alive, 'This spaceship is still alive'
        
    def test_take_damages_should_have_docstring(self):
        docstring = Spaceship.take_damages.__doc__
        if docstring:
            docstring_size = len(docstring)
            assert docstring_size >= 50, 'docstring is too short'
        else:
            pytest.fail('Add some docstring to the method')
        
    def test_take_damages_null_damages(self, spaceship):
        spaceship.take_damages(0)
        assert spaceship.defense == 1000, 'Incorrect defense value'
        assert spaceship.is_alive, 'This spaceship is still alive'

    def test_take_damages_should_be_destroyed(self, spaceship):
        spaceship.take_damages(1500)
        assert spaceship.defense == 0, 'Incorrect defense value. 0 expected'
        assert not spaceship.is_alive, 'This spaceship should be destroyed'

    def test_take_damages_should_be_just_destroyed(self, spaceship):
        spaceship.take_damages(1000)
        assert spaceship.defense == 0, 'Incorrect defense value. 0 expected'
        assert not spaceship.is_alive, 'This spaceship should be destroyed'
        
    def test_take_damages_should_raise_if_negative(self, spaceship):
        with pytest.raises(ValueError):
            spaceship.take_damages(-1000)
