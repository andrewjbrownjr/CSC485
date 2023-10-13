import pytest
from CSC485.projects.hw10 import fruit_query


def test_lowercase():
    '''
    Method to test if is_it_a_fruit returns true with an all
    lowercase input that is a valid fruit name
    '''
    assert fruit_query.is_it_a_fruit('apple')


def test_uppercase():
    '''
    Method to test if is_it_a_fruit returns true with an all
    uppercase input that is a valid fruit name
    '''
    assert fruit_query.is_it_a_fruit('PEAR')


def test_some_uppercase():
    '''
    Method to test if is_it_a_fruit returns true with an input with some
    uppercase input and some lowercase input that is a valid fruit name
    '''
    assert fruit_query.is_it_a_fruit('Banana')


def test_not_fruit():
    '''
    Method to test if is_it_a_fruit returns false when the input
    is not the name of a valid fruit
    '''
    assert not fruit_query.is_it_a_fruit('lettuce')


def test_bool():
    '''
    Method to test if is_it_a_fruit returns false
    when the input is a boolean
    '''
    assert not fruit_query.is_it_a_fruit(True)


def test_int():
    '''
    Method to test if is_it_a_fruit returns false
    when the input is an integer
    '''
    assert not fruit_query.is_it_a_fruit(5)
