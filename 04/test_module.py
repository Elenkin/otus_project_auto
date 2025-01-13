import requests

# Тестовая функция, проверяющая статус ответа по URL
def test_status_code(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(status_code), \
        f"Expected status code {status_code}, but got {response.status_code} for URL {url}"