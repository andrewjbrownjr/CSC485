import pytest, json
from CSC485.projects.hw15.api import app

@pytest.fixture
def client_get_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_post_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestApiGetThroughCode:
    '''
    Testing the api's get endpoint through
    pytest fixtures
    '''

    @pytest.mark.parametrize('password', ['%%%%', '%%t%t', 'o---O'])
    def test_good_password_by_get(self, client_get_endpoint, password):
        '''
        Testing that the api returns a 'good' response when
        given a strong password
        '''
        response = client_get_endpoint.get(f'/get_strength?password={password}')
        assert response.status_code == 200

        data = json.loads(response.data.decode())
        assert data.get('password') == password
        assert data.get('strength') == 'good'

    @pytest.mark.parametrize('password', ['password', 'letMeIn', 'not-a-hacker'])
    def test_bad_password_by_get(self, client_get_endpoint, password):
        '''
        Testing that the api returns a 'bad' respone
        when given a weak password
        '''
        response = client_get_endpoint.get(f'/get_strength?password={password}')
        assert response.status_code == 200

        data = json.loads(response.data.decode())
        assert data.get('password') == password
        assert data.get('strength') == 'bad'

class TestApiPostThroughCode:
    '''
    Testing the api's post endpoint through
    pytest fixtures
    '''

    @pytest.mark.parametrize('password', ['%%%%', '%%t%t', 'o---O'])
    def test_good_password_by_post(self, client_post_endpoint, password):
        '''
        Testing that the api returns a 'good' response
        when given a strong password
        '''
        response = client_post_endpoint.get(f'/get_strength?password={password}')
        assert response.status_code == 200

        data = json.loads(response.data.decode())
        assert data.get('password') == password
        assert data.get('strength') == 'good'

    @pytest.mark.parametrize('password', ['password', 'letMeIn', 'not-a-hacker'])
    def test_bad_password_by_post(self, client_post_endpoint, password):
        '''
        Testing that the api returns a 'bad' response
        when given a weak password
        '''
        response = client_post_endpoint.get(f'/get_strength?password={password}')
        assert response.status_code == 200

        data = json.loads(response.data.decode())
        assert data.get('password') == password
        assert data.get('strength') == 'bad'
