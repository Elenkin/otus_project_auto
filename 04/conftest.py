import pytest


def pytest_addoption(parser):
    """Регистрация параметров командной строки"""
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="URL to check"
    )

    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        help="Expected status code"
    )

# Фикстура для параметров командной строки
@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

