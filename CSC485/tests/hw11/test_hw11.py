import pytest
from CSC485.projects.hw11 import formal_names
'''
'''
class TestFormalNames:
    '''
    Tests for get_formal_name from part 1
    '''
    @pytest.mark.parametrize('fruit1',['apple','Apple','APPLE','aPpLe'])
    def test_is_a_fruit_1(self, fruit1):
        '''
        Method to test if get_formal_name returns the formal name of
        a fruit with a fruit as the input string
        '''
        assert formal_names.get_formal_name(fruit1) == 'Malus domestica'


    def test_not_a_fruit_1(self):
        '''
        Method to test if get_formal_name raises a KeyError when
        a string that is not the name of a fruit is input
        '''
        with pytest.raises(KeyError):
            formal_names.get_formal_name('this is not a fruit')


class TestFormalNames2:
    '''
    Tests for get_formal_name_2 from part 2
    '''
    @pytest.mark.parametrize('fruit2',['apple','APPLE','Apple','aPpLe'])
    def test_is_a_fruit_2(self, fruit2):
        '''
        Method to test if get_formal_name_2 returns the formal name of
        a fruit when the input is a fruit
        '''
        assert formal_names.get_formal_name_2(fruit2) == 'Malus domestica'

    def test_not_a_fruit_2(self):
        '''
        Method to test if get_formal_name_2 raises a KeyError when
        the input is not the name of a valid fruit
        '''
        with pytest.raises(KeyError):
            formal_names.get_formal_name_2('this is not a fruit')