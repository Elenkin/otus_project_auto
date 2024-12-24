import math
import pytest

from src.circle import Circle
pi = math.pi
import random

list_for_error = pytest.mark.parametrize('radius, error_message',
                                          [pytest.param(0, "r must be above zero", id="ValueError"),
                                           pytest.param(-1, "r must be above zero", id="ValueError")
                                           ]
                                        )

class TestCircle:

    def test_check_area_circle(self):
        radius = random.randint(1, 100)
        r = Circle(radius)
        area_check = pi * radius ** 2
        assert r.get_area == area_check, \
            f'Радиус:{radius} и площадь: {area_check}, но получен {r.get_area}'

    def test_check_perimeter_circle(self):
        radius = random.randint(1, 100)
        expected_perimeter = 2 * pi * radius
        r = Circle(radius)
        assert r.get_perimeter == expected_perimeter, \
            f'Радиус:{radius} и периметр: {expected_perimeter}, но получен {r.get_perimeter}'

    @list_for_error
    def test_circle_negative(self, radius, error_message):
        with pytest.raises(ValueError) as exc_info:
            Circle(radius)
        assert str(exc_info.value)  == error_message, \
            f'Ожидаемое сообщение об ошибке:{error_message} но ожидаемое: {exc_info.value}'