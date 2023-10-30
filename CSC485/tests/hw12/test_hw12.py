import pytest
from CSC485.projects.hw12.compute_complexity import compute_complexity
'''
Testing compute complexity by categories of how much of the string
is made up of complexifiers. Each category is tested using strigns
containing different complexifiers, different string lengths, and
different sequences of characters in the strings.
'''


class TestComputeComplexity:
    '''
    These methods will test compute_complexity
    '''
    @pytest.mark.parametrize('key', ['@', '~~~', '##', '$$$$$$', '_______', '----'])
    def test_all_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 100 when
        the input string is only complexifiers
        '''
        assert compute_complexity(key) == 100

    @pytest.mark.parametrize('key', ['a@', '#e$8', '%%tt', 'op-_', '@@5g@@gg', '~~~lll'])
    def test_half_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 50
        when half of the input string is complexifiers
        '''
        assert compute_complexity(key) == 50

    @pytest.mark.parametrize('key', ['@aaa', '##ee7eee', 'oo#o', 'p-pp', '&&&aaaa0aaaa'])
    def test_quarter_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 25
        when a quarter of the string is complexifiers
        '''
        assert compute_complexity(key) == 25

    @pytest.mark.parametrize('key', ['@aa2a4aaaa', 'w#www96www', 'ooooooooo$'])
    def test_tenth_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 10 when
        a tenth of the input string is complexifiers
        '''
        assert compute_complexity(key) == 10

    @pytest.mark.parametrize('key', ['k', 'aaaaaaaaaa', 'llll', '012345'])
    def test_no_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 0 when
        none of the input string is complexifiers
        '''
        assert compute_complexity(key) == 0

    def test_51_percent(self):
        '''
        Method to test that compute_complexity returns 51 when
        51% of the string is complexifiers
        '''
        key = '##################ttttttttttttttttt'
        assert compute_complexity(key) == 51

    def test_49_percent(self):
        '''
        Method to test that compute_complexity returns 49 when
        49% of the string is complexifiers
        '''
        key = 'tttttttttttttttttt#################'
        assert compute_complexity(key) == 49

    @pytest.mark.parametrize('key', [1, 324, [43, 'string'], ('str', 'int'), True])
    def test_not_a_string(self, key):
        '''
        Method to test that compute_complexity raises a TypeError
        when the input is not a string
        '''
        with pytest.raises(TypeError):
            compute_complexity(key)
