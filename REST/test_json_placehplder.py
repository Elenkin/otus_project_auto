import pytest
from faker import Faker
from REST.helper import HelpersApi

faker = Faker()


base_url = 'https://jsonplaceholder.typicode.com/posts'

list_fields = pytest.mark.parametrize('field',
                             [
                                 'title',
                                 'body'
                             ])

list_post_id = pytest.mark.parametrize('post_id', [1, 2, 3, 4, 5])

class TestJsonPlaceholder:

    def test_create_resource(self):
        """ """
        random_word = faker.word()
        body = {
            'title': 'foo',
            'body': random_word,
            'userId': 1
        }
        response = HelpersApi.post_request(base_url, body)

        assert response['title'] == 'foo'
        assert response['body'] == random_word

    @list_fields
    def test_edit_resource(self, field):
        """ Проверяем редактирование полей"""
        url = f'{base_url}/1'
        random_word = faker.word()

        body = {
            field: random_word
        }
        response = HelpersApi.patch_request(url, body)

        assert response[field] == random_word

    @list_post_id
    def test_get_post_by_postid(self, post_id):
        url = f'{base_url}/comments'

        response = HelpersApi.get_request(url, params={'postId': post_id})
        for post in response:
            assert post['postId'] == post_id

    def test_filter_by_userid(self):
        """Basic filtering is supported through query parameters"""

        response = HelpersApi.get_request(base_url, params={'userId': 1})
        all_resource = all(item['userId'] == 1 for item in response)

        if all_resource:
            print("Все значения в поле 'userId' равны 1")
        else:
            print("Есть значения, отличные от 1")

    def test_check_max_count_posts(self):
        """ Max count posts 100"""

        response = HelpersApi.get_request(base_url)
        assert len(response) == 100
