from CSC485.projects.hw10 import fruit_query

def test_answers():
  assert fruit_query.is_it_a_fruit('apple') == True
  assert fruit_query.is_it_a_fruit('PEAR') == True
  assert fruit_query.is_it_a_fruit('Banana') == True
  assert fruit_query.is_it_a_fruit('lettuce') == False
  assert fruit_query.is_it_a_fruit(True) == False
  assert fruit_query.is_it_a_fruit(5) == False