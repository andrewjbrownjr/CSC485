import pytest
from CSC485.projects.hw12.compute_complexity import compute_complexity

@pytest.mark.parametrize('key',['@','~~~','##','$$$$$$','_______','----','+=+=+'])
def test_all_complexifiers(key):
    '''
    Method to test that compute_complexity returns 100 when
    the input string is only complexifiers
    '''
    assert compute_complexity(key) == 100

@pytest.mark.parametrize('key',['a@','#e$e','%%tt','op-_','@@gg@@gg','~~~lll'])
def test_half_complexifiers(key):
    '''
    Method to test that compute_complexity returns 50
    when half of the input string is complexifiers
    '''
    assert compute_complexity(key) == 50

@pytest.mark.parametrize('key',['@aaa','##eeeeee','oo#o','p-pp','&&&aaaaaaaaa'])
def test_quarter_complexifiers(key):
    '''
    Method to test that compute_complexity returns 25
    when a quarter of the string is complexifiers
    '''
    assert compute_complexity(key) == 25

@pytest.mark.parametrize('key',['@aaaaaaaaa','w#wwwwwwww','jj_jjjjjjj','ooooooooo$'])
def test_tenth_complexifiers(key):
    '''
    Method to test that compute_complexity returns 10 when
    a tenth of the input string is complexifiers
    '''
    assert compute_complexity(key) == 10

@pytest.mark.parametrize('key',['k','aaaaaaaaaa','llll','00000'])
def test_no_complexifiers(key):
    '''
    Method to test that compute_complexity returns 0 when
    none of the input string is complexifiers
    '''
    assert compute_complexity(key) == 0