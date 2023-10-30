import pytest
from CSC485.projects.hw13 import strength_and_complexity

'''
    Testing compute_complexity and evaluate_strength

    compute_complexity
            -length of input
            -type of input
            -complexifiers in input
                    -number of complexifiers
                    -types of complexifiers
                    -order of complexifiers
            -complexity scores

    evaluate_strength
            -type of input
            -strong passwords
            -weak passwords
            -
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
        assert strength_and_complexity.compute_complexity(key) == 100

    @pytest.mark.parametrize('key', ['a@', '#e$e', '%%tt', 'op-_', '@@gg@@gg', '~~~lll'])
    def test_half_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 50
        when half of the input string is complexifiers
        '''
        assert strength_and_complexity.compute_complexity(key) == 50

    @pytest.mark.parametrize('key', ['@aaa', '##eeeeee', 'oo#o', 'p-pp', '&&&aaaaaaaaa'])
    def test_quarter_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 25
        when a quarter of the string is complexifiers
        '''
        assert strength_and_complexity.compute_complexity(key) == 25

    @pytest.mark.parametrize('key', ['@aaaaaaaaa', 'w#wwwwwwww', 'jj_jjjjjjj'])
    def test_tenth_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 10 when
        a tenth of the input string is complexifiers
        '''
        assert strength_and_complexity.compute_complexity(key) == 10

    @pytest.mark.parametrize('key', ['k', 'aaaaaaaaaa', 'llll', '00000'])
    def test_no_complexifiers(self, key):
        '''
        Method to test that compute_complexity returns 0 when
        none of the input string is complexifiers
        '''
        assert strength_and_complexity.compute_complexity(key) == 0


    def test_51_percent(self):
        '''
        Method to test that compute_complexity returns 51 when
        51% of the string is complexifiers
        '''
        key = '##################ttttttttttttttttt'
        assert strength_and_complexity.compute_complexity(key) == 51


    def test_49_percent(self):
        '''
        Method to test that compute_complexity returns 49 when
        49% of the string is complexifiers
        '''
        key = 'tttttttttttttttttt#################'
        assert strength_and_complexity.compute_complexity(key) == 49


    @pytest.mark.parametrize('key', [1, 324, [43, 'string'], ('str', 'int'), True])
    def test_not_a_string(self, key):
        '''
        Method to test that compute_complexity raises a TypeError
        when the input is not a string
        '''
        with pytest.raises(TypeError):
            strength_and_complexity.compute_complexity(key)

class TestEvaluateStrength:
    '''
    These methods will test evaluate_strength
    '''

    @pytest.mark.parametrize('strong_password', ['#', '$ee%%', '__a', 'p@@@p','o-oo-_-'])
    def test_strong_password(self, strong_password):
        '''
        Method to test that evaluate_strength returns true on passwords
        that are over 50% complexifiers
        '''
        assert strength_and_complexity.evaluate_strength(strong_password)

    @pytest.mark.parametrize('weak_password', ['a', 'password', 'pass#', '123$'])
    def test_weak_password(self, weak_password):
        '''
        Method to test that evaluate_strength returns false on
        passwords that are under 50% complexifiers
        '''
        assert not strength_and_complexity.evaluate_strength(weak_password)
