import requests
import pytest
from REST.helper import HelpersApi


base_url = 'https://dog.ceo/api'

list_count = pytest.mark.parametrize('count_request, count_expected',
                             [
                                 (0, 1),
                                 (50, 50),
                                 (51, 50)
                             ])


list_breed_and_subbreed = pytest.mark.parametrize('breed, subbreed',
                                                [
                                                    ('hound', 'afghan'),
                                                    ('australian', 'shepherd'),
                                                    ('bulldog', 'english')
                                                ])

class TestDogs:

    @list_count
    def test_check_count_links(self, count_request, count_expected):
        """ Max number returned is 50"""
        url = f'{base_url}/breeds/image/random/{count_request}'

        response = HelpersApi.get_request(url)
        assert len(response['message']) == count_expected, \
            f'Кол-во полученных ссылок {len(response['message'])}, но ожидалось: {count_expected}'

    def test_check_status_code_200(self):
        url = f'{base_url}/breeds/image/random'

        response = requests.get(url)
        assert response.status_code == 200

    def test_check_status(self):
        url = f'{base_url}/breeds/image/random'

        response = requests.get(url)
        assert response.json()['status'] == 'success', \
            f'Ожидаемый статус: success, но получен: {response.json()['status']}'

    def test_check_fields_response(self):
        url = f'{base_url}/breeds/image/random'

        body_response = HelpersApi.get_request(url)

        assert body_response['message'] is not None
        assert body_response['status'] == 'success', \
            f'Ожидаемый статус: success, но получен: {body_response['status']}'

    @list_breed_and_subbreed
    def test_message_contain_subbreed(self, breed, subbreed):
        url = f'{base_url}/breed/{breed}/{subbreed}/images/random'

        body_response = HelpersApi.get_request(url)
        assert breed in body_response['message'] and subbreed in body_response['message']
