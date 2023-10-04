import pytest
from CSC485.projects.hw11 import formal_names

#Part 1 test
def test_lowercase_1():
    '''
    Method to test if get_formal_name returns the formal name of
    a fruit with an all lowercase string input
    '''
    assert formal_names.get_formal_name('apple') == 'Malus domestica'

def test_uppercase_1():
    '''
    Method to test if get_formal_name returns the formal name of
    a fruit with an all uppercase string input
    '''
    assert formal_names.get_formal_name('APPLE') == 'Malus domestica'

def test_some_uppercase_1():
    '''
    Method to test if get_formal_name returns the formal name of a
    fruit with an input containing some uppercase letters and some lowercase letters
    '''
    assert formal_names.get_formal_name('Apple') == 'Malus domestica'

def test_not_a_fruit_1():
    '''
    Method to test if get_formal_name raises a KeyError when
    a string that is not the name of a fruit is input
    '''
    with pytest.raises(KeyError):
        formal_names.get_formal_name('this is not a fruit')

#Part 2 tests
def test_lowercase_2():
    '''
    Method to test if get_formal_name_2 returns the formal name of
    a fruit when the input is an all lowercase fruit name
    '''
    assert formal_names.get_formal_name_2('apple') == 'Malus domestica'

def test_uppercase_2():
    '''
    Method to test if get_formal_name_2 returns the formal name of
    a fruit when the input is an all uppercase fruit name
    '''
    assert formal_names.get_formal_name_2('APPLE') == 'Malus domestica'

def test_some_uppercase_2():
    '''
    Method to test if get_formal_name_2 returns the formal name of a fruit when
    the input is a fruit name with some uppercase and some lowercase letters
    '''
    assert formal_names.get_formal_name_2('Apple') == 'Malus domestica'

def test_not_a_fruit_2():
    '''
    Method to test if get_formal_name_2 raises a KeyError when
    the input is not the name of a valid fruit
    '''
    with pytest.raiss(KeyError):
        formal_names.get_formal_name_2('this is not a fruit')