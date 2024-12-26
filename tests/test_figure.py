import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

rectangle = Rectangle(5, 22)
circle = Circle(40)
triangle = Triangle(7, 10, 12)
square = Square(55)


list_for_area = pytest.mark.parametrize('figure, other_figure, expected_area',
                             [
                                 (rectangle, triangle, 145),
                                 (rectangle, circle, 5137),
                                 (rectangle, square, 3135),
                                 (square, circle, 8052),
                                 (square, triangle, 3060)

                             ])

list_for_perimeter = pytest.mark.parametrize('figure, other_figure, expected_perimeter',
                             [
                                 (rectangle, triangle, 83),
                                 (rectangle, circle, 305),
                                 (rectangle, square, 274),
                                 (square, circle, 471),
                                 (square, triangle, 249)

                             ])
list_for_error = pytest.mark.parametrize('figure, other_figure',
                             [
                                 (rectangle, "test"),
                                 (triangle, True),
                                 (circle, -1),
                                 (square, 0),
                             ])

class TestFigure:

    @list_for_area
    def test_check_add_area_figure(self, figure, other_figure, expected_area):

        add_area_figure = round(figure.add_area(other_figure))
        assert add_area_figure == expected_area, \
            f'Сумма площадей фигур: {expected_area}, но получено {add_area_figure}'

    @list_for_perimeter
    def test_check_add_perimeter_figure(self, figure, other_figure, expected_perimeter):

        add_perimeter_figure = round(figure.add_perimeter(other_figure))
        assert add_perimeter_figure == expected_perimeter, \
            f'Сумма периметров фигур: {expected_perimeter}, но получено: {add_perimeter_figure}'

    @list_for_error
    def test_figure_negative(self, figure, other_figure):
        with pytest.raises(ValueError, match="Should be a Figure"):
            figure.add_perimeter(other_figure)
