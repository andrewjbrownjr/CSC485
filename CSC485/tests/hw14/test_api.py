import json
import pytest
from CSC485.projects.hw14.api import app  # this is the flask app


# this is a pytest fixture
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestApi:
    # this is a simplified happy path test
    def test_expect_good(self, client):
        # call the API, get the server response
        response = client.get('/get_strength?password=%%%%%%%')
        assert response.status_code == 200

        # convert the json payload to a dict
        data = json.loads(response.data.decode())
        assert data.get('password') == '%%%%%%%'
        assert data.get('strength') == 'good'


    @pytest.mark.parametrize('password', ['%%%%', '%%t%t', 'o---O'])
    def test_expect_good_parametrized(self, client, password):
        response = client.get(f'/get_strength?password={password}')
        assert response.status_code == 200

        data = json.loads(response.data.decode())
        assert data.get('password') == password
        assert data.get('strength') == 'good'


    @pytest.mark.parametrize('password', ['password', 'letMeIn', 'not-a-hacker'])
    def test_expect_bad(self, client, password):
        response = client.get(f'/get_strength?password={password}')
        assert response.status_code == 200

        data = json.loads(response.data.decode())
        assert data.get('password') == password
        assert data.get('strength') == 'bad'


    # this is an example very negative test
    def test_api_error(self, client):
        # disambiguate
        password = '#password'

        with pytest.raises(ZeroDivisionError):
            response = client.get(f"/get_strength?password={password}")


    @pytest.mark.parametrize('password', [5, 67, ['list1', 'list2'], ('tuple', 'yes')])
    def test_api_not_string(self, client, password):
        with pytest.raises(TypeError):
            client.get(f"/get_strength?password={password}")
