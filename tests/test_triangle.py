import pytest

from src.triangle import Triangle

list_for_parametrize = pytest.mark.parametrize('side_a, side_b, side_c',
                                                [pytest.param(3, 5, 4)]
                                               )
list_for_error = pytest.mark.parametrize('side_a, side_b, side_c, error_message',
                                          [pytest.param(39, 42, 89, "The sum of any two sides must be greater than the third side", id="ValueError"),
                                           pytest.param(4, 0, 10, "side_a, side_b and side_c must be above zero", id="ValueError"),
                                           pytest.param(-1, 5.5, 10, "side_a, side_b and side_c must be above zero", id="ValueError"),
                                           pytest.param(100, -5, 10, "side_a, side_b and side_c must be above zero", id="ValueError")
                                           ]
                                        )

class TestTriangle:

    @list_for_parametrize
    def test_check_area_triangle(self, side_a, side_b, side_c, area_check=6):
        r = Triangle(side_a, side_b, side_c)
        assert r.get_area == area_check, \
            f'Стороны а:{side_a}, b: {side_b}, c:{side_c} площадь: {area_check}, но получен {r.get_area}'

    @list_for_parametrize
    def test_check_perimeter_triangle(self, side_a, side_b, side_c):
        expected_perimeter = side_a + side_b + side_c
        r = Triangle(side_a, side_b, side_c)
        assert r.get_perimeter == expected_perimeter, \
            f'Стороны а:{side_a}, b: {side_b}, c: {side_c} периметр: {expected_perimeter}, но получен {r.get_perimeter}'

    @list_for_error
    def test_triangle_negative(self, side_a, side_b, side_c, error_message):
        with pytest.raises(ValueError) as exc_info:
            Triangle(side_a, side_b, side_c)
        assert str(exc_info.value)  == error_message, \
            f'Ожидаемое сообщение об ошибке:{error_message} но ожидаемое: {exc_info.value}'
