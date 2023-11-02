import json
import pytest
import requests

class TestApiGetThroughHttp:
    '''
    Testing the api's get endpoint through
    http requests
    '''

    @pytest.mark.parametrize('password', ['%%%%', '%%t%t', 'o---O'])
    def test_good_password_by_get(self, password):
        '''
        Testing that the api returns a 'good' response
        when given a strong password
        '''
        params = {'password': password}
        response = requests.get('http://127.0.0.1:5000/get_strength', params=params)
        assert response.status_code

        data = response.json()
        assert data.get('password') == password
        assert data.get('strength') == 'good'

    @pytest.mark.parametrize('password', ['password', 'letMeIn', 'not-a-hacker'])
    def test_bad_password_by_get(self, password):
        '''
        Testing that the api returns a 'bad' response
        when given a weak password
        '''
        params = {'password': password}
        response = requests.get('http://127.0.0.1:5000/get_strength', params=params)
        assert response.status_code == 200

        data = response.json()
        assert data.get('password') == password
        assert data.get('strength') == 'bad'

class TestApiPostThroughHttp:
    '''
    Testing the api's post endpoint through
    http requests
    '''

    @pytest.mark.parametrize('password', ['%%%%', '%%t%t', 'o---O'])
    def test_good_password_by_post(self, password):
        '''
        Testing that the api returns a 'good' response
        when given a strong password
        '''
        payload = {'password' : password}
        response = requests.post('http://127.0.0.1:5000/get_strength',json = payload)
        assert response.status_code == 200

        data = response.json()
        assert data.get('password') == password
        assert data.get('strength') == 'good'

    @pytest.mark.parametrize('password', ['password', 'letMeIn', 'not-a-hacker'])
    def test_bad_password_by_post(self, password):
        '''
        Testing that the api returns a 'bad' response
        when given a weak password
        '''
        payload = {'password': password}
        response = requests.post('http://127.0.0.1:5000/get_strength', json=payload)
        assert response.status_code == 200

        data = response.json()
        assert data.get('password') == password
        assert data.get('strength') == 'bad'
