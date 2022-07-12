import pytest

from base_spaceships import Spaceship, Battleship, Fighter

_UNDEFINED = object()
attack, defense = 100, 1000


@pytest.fixture
def battleship():
    return Battleship(attack, defense)


@pytest.fixture
def fighter():
    return Fighter(attack, defense)


class TestBattleship:
    def test_inherited(self):
        is_inherited = issubclass(Battleship, Spaceship)
        assert is_inherited, 'Battleship should be inherited from Spaceship'
        
    def test_take_damages_should_have_docstring(self):
        docstring = Battleship.__doc__
        if docstring:
            docstring_size = len(docstring)
            assert docstring_size >= 50, 'class docstring is too short'
        else:
            pytest.fail('Add some docstring to the class')
    
    def test_do_nothing_more(self, battleship):
        class_elements = [elt for elt in battleship.__dir__() if not elt.startswith('__')]
        assert class_elements == ['attack', 'defense', 'is_alive', 'take_damages'], 'The Battleship class should do nothing more than Spaceship class'
    
    def test_constructor(self, battleship):
        assert battleship.attack == attack, 'Pass attack as constructor first argument'
        assert battleship.defense == defense, 'Pass defense as constructor second argument'
        assert battleship.is_alive, 'is_alive should be always True'
        assert Battleship.is_alive is True, 'is_alive should be a class attribute'

    def test_should_be_instance_attributes(self):
        attr_should_not_exists = getattr(Battleship, 'attack', _UNDEFINED)
        if attr_should_not_exists is not _UNDEFINED:
            pytest.fail('attack should be an instance attribute, not a class attribute')

        attr_should_not_exists = getattr(Battleship, 'defense', _UNDEFINED)
        if attr_should_not_exists is not _UNDEFINED:
            pytest.fail('defense should be an instance attribute, not a class attribute')

    def test_take_damages(self, battleship):
        battleship.take_damages(100)
        assert battleship.defense == 900, 'Incorrect defense value'
        assert battleship.is_alive, 'This spaceship is still alive'
        
    def test_take_damages_should_have_docstring(self):
        docstring = Battleship.take_damages.__doc__
        if docstring:
            docstring_size = len(docstring)
            assert docstring_size >= 50, 'take_damages docstring is too short'
        else:
            pytest.fail('Add some docstring to the take_damages method')

    def test_take_damages_should_be_destroyed(self, battleship):
        battleship.take_damages(1500)
        assert battleship.defense == 0, 'Incorrect defense value. 0 expected'
        assert not battleship.is_alive, 'This spaceship should be destroyed'

    def test_take_damages_should_be_just_destroyed(self, battleship):
        battleship.take_damages(1000)
        assert battleship.defense == 0, 'Incorrect defense value. 0 expected'
        assert not battleship.is_alive, 'This spaceship should be destroyed'
        
    def test_take_damages_null_damages(self, battleship):
        battleship.take_damages(0)
        assert battleship.defense == 1000, 'Incorrect defense value'
        assert battleship.is_alive, 'This spaceship is still alive'
        
    def test_take_damages_should_raise_if_negative(self, battleship):
        with pytest.raises(ValueError):
            battleship.take_damages(-1000)

        

class TestFighter:
    def test_inherited(self):
        is_inherited = issubclass(Fighter, Spaceship)
        assert is_inherited, 'Fighter should be inherited from Spaceship'
    
    def test_take_damages_should_have_docstring(self):
        docstring = Fighter.__doc__
        if docstring:
            docstring_size = len(docstring)
            assert docstring_size >= 50, 'class docstring is too short'
        else:
            pytest.fail('Add some docstring to the class')
    
    def test_do_nothing_more(self, fighter):
        class_elements = [elt for elt in fighter.__dir__() if not elt.startswith('__')]
        assert class_elements == ['attack', 'defense', 'is_alive', 'take_damages'], 'The Fighter class should do nothing more than Spaceship class'
    
    def test_constructor(self, fighter):
        assert fighter.attack == attack, 'Pass attack as constructor first argument'
        assert fighter.defense == defense, 'Pass defense as constructor second argument'
        assert fighter.is_alive, 'is_alive should be always True'
        assert Fighter.is_alive is True, 'is_alive should be a class attribute'

    def test_should_be_instance_attributes(self):
        attr_should_not_exists = getattr(Fighter, 'attack', _UNDEFINED)
        if attr_should_not_exists is not _UNDEFINED:
            pytest.fail('attack should be an instance attribute, not a class attribute')

        attr_should_not_exists = getattr(Fighter, 'defense', _UNDEFINED)
        if attr_should_not_exists is not _UNDEFINED:
            pytest.fail('defense should be an instance attribute, not a class attribute')

    def test_take_damages(self, fighter):
        fighter.take_damages(100)
        assert fighter.defense == 900, 'Incorrect defense value'
        assert fighter.is_alive, 'This spaceship is still alive'
        
    def test_take_damages_should_have_docstring(self):
        docstring = Fighter.take_damages.__doc__
        if docstring:
            docstring_size = len(docstring)
            assert docstring_size >= 50, 'take_damages docstring is too short'
        else:
            pytest.fail('Add some docstring to the take_damages method')

    def test_take_damages_should_be_destroyed(self, fighter):
        fighter.take_damages(1500)
        assert fighter.defense == 0, 'Incorrect defense value. 0 expected'
        assert not fighter.is_alive, 'This spaceship should be destroyed'

    def test_take_damages_should_be_just_destroyed(self, fighter):
        fighter.take_damages(1000)
        assert fighter.defense == 0, 'Incorrect defense value. 0 expected'
        assert not fighter.is_alive, 'This spaceship should be destroyed'
        
    def test_take_damages_null_damages(self, fighter):
        fighter.take_damages(0)
        assert fighter.defense == 1000, 'Incorrect defense value'
        assert fighter.is_alive, 'This spaceship is still alive'
        
    def test_take_damages_should_raise_if_negative(self, fighter):
        with pytest.raises(ValueError):
            fighter.take_damages(-1000)

