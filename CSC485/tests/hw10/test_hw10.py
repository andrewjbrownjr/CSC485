import pytest
from CSC485.projects.hw10 import fruit_query

def test_lowercase():
  assert fruit_query.is_it_a_fruit('apple') == True

def test_uppercase():
  assert fruit_query.is_it_a_fruit('PEAR') == True

def test_some_uppercase():
  assert fruit_query.is_it_a_fruit('Banana') == True

def test_not_fruit():
  assert fruit_query.is_it_a_fruit('lettuce') == False

def test_bool():
  assert fruit_query.is_it_a_fruit(True) == False

def test_int():
  assert fruit_query.is_it_a_fruit(5) == False