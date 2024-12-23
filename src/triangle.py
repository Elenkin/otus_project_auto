import math

from figure import Figure


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int):

        list_value_side = [a, b, c]
        for value in list_value_side:
            if value <=0 :
                raise ValueError('side_a, side_b and side_c must be above zero')

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('The sum of any two sides must be greater than the third side')

        self.a = a
        self.b = b
        self.c = c

    @property
    def get_area(self):
        #полупериметр

        p = self.get_perimeter / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area

    @property
    def get_perimeter(self):
        perimeter = (self.a + self.b + self.c)
        return perimeter
