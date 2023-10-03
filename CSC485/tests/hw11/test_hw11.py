import pytest
from CSC485.projects.hw11 import formal_names

#Part 1 test
def test_lowercase_1():
    assert formal_names.get_formal_name('apple') == 'Malus domestica'

def test_uppercase_1():
    assert formal_names.get_formal_name('APPLE') == 'Malus domestica'

def test_some_uppercase_1():
    assert formal_names.get_formal_name('Apple') == 'Malus domestica'

def test_not_a_fruit_1():
    with pytest.raises(ValueError):
        formal_names.get_formal_name('this is not a fruit')

#Part 2 tests
def test_lowercase_2():
    assert formal_names.get_formal_name_2('apple') == 'Malus domestica'

def test_uppercase_2():
    assert formal_names.get_formal_name_2('APPLE') == 'Malus domestica'

def test_some_uppercase_2():
    assert formal_names.get_formal_name_2('Apple') == 'Malus domestica'

def test_not_a_fruit_2():
    with pytest.raiss(ValueError):
        formal_names.get_formal_name_2('this is not a fruit')