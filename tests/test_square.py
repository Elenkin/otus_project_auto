import pytest

from src.square import Square
import random

list_for_error = pytest.mark.parametrize('side_a, error_message',
                                          [pytest.param(0, "side_a and side_b must be above zero", id="ValueError"),
                                           pytest.param(-1, "side_a and side_b must be above zero", id="ValueError")
                                           ]
                                        )

class TestSquare:

    def test_check_area_square(self):
        side_a = random.randint(1, 100)
        r = Square(side_a)
        area_check = side_a * side_a
        assert r.get_area == area_check, \
            f'Стороны а:{side_a} и площадь: {area_check}, но получен {r.get_area}'

    def test_check_perimeter_square(self):
        side_a = random.randint(1,100)
        expected_perimeter = 2 * (side_a + side_a)

        r = Square(side_a)
        assert r.get_perimeter == expected_perimeter, \
            f'Сторона:{side_a} и периметр: {expected_perimeter}, но получен {r.get_perimeter}'

    @list_for_error
    def test_square_negative(self, side_a, error_message):
        with pytest.raises(ValueError) as exc_info:
            Square(side_a)
        assert str(exc_info.value)  == error_message, \
            f'Ожидаемое сообщение об ошибке:{error_message} но ожидаемое: {exc_info.value}'
