import pytest

from src.rectangle import Rectangle
import random

list_for_parametrize = pytest.mark.parametrize('side_a, side_b, area_check',
                                                [pytest.param(3, 5, 15, id="Rectangle 3*5"),
                                                pytest.param(3.02, 5.5, 16.61, id="Rectangle 3.02*5.5")]
                                               )
list_for_error = pytest.mark.parametrize('side_a, side_b, error_message',
                                          [pytest.param(0, 5, "side_a and side_b must be above zero", id="ValueError"),
                                           pytest.param(4, 0, "side_a and side_b must be above zero", id="ValueError"),
                                           pytest.param(-1, 5.5, "side_a and side_b must be above zero", id="ValueError"),
                                           pytest.param(100, -5, "side_a and side_b must be above zero", id="ValueError")
                                           ]
                                        )

class TestRectangle:

    @list_for_parametrize
    def test_check_area_rectangle(self, side_a, side_b, area_check):
        r = Rectangle(side_a, side_b)
        assert r.get_area == area_check, \
            f'Стороны а:{side_a} и b: {side_b} площадь: {area_check}, но получен {r.get_area}'

    def test_check_perimeter_rectangle(self):
        side_a = random.randint(1,100)
        side_b = random.randint(1,100)
        expected_perimeter = 2 * (side_a + side_b)
        r = Rectangle(side_a, side_b)
        assert r.get_perimeter == expected_perimeter, \
            f'Стороны а:{side_a} и b: {side_b} периметр: {expected_perimeter}, но получен {r.get_perimeter}'

    @list_for_error
    def test_rectangle_negative(self, side_a, side_b, error_message):
        with pytest.raises(ValueError) as exc_info:
            Rectangle(side_a, side_b)
        assert str(exc_info.value)  == error_message, \
            f'Ожидаемое сообщение об ошибке:{error_message} но ожидаемое: {exc_info.value}'
