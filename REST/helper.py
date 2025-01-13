import requests


class HelpersApi:

    @staticmethod
    def get_request(url, params=None):
        r = requests.get(url, params)

        # Проверяем статус код
        if r.status_code == 200:
            body = r.json()
            return body
        else:
            return {'error': f'Request failed with status code {r.status_code}'}

    @staticmethod
    def post_request(url, json, params=None):
        r = requests.post(url, json, params)
        if r.status_code == 200:
            body = r.json()
            return body
        else:
            return {'error': f'Request failed with status code {r.status_code}'}

    @staticmethod
    def patch_request(url, json):
        r = requests.patch(url, json)
        if r.status_code == 200:
            body = r.json()
            return body
        else:
            return {'error': f'Request failed with status code {r.status_code}'}
