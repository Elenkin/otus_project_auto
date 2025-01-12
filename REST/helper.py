import requests


class HelpersApi:

    @staticmethod
    def get_request(url, params=None):
        r = requests.get(url, params)
        body = r.json()
        return body

    @staticmethod
    def post_request(url, json, params=None):
        r = requests.post(url, json, params)
        body = r.json()
        return body

    @staticmethod
    def patch_request(url, json):
        r = requests.patch(url, json)
        body = r.json()
        return body
