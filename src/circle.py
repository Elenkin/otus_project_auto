import math
from figure import Figure

pi = math.pi

class Circle(Figure):
    def __init__(self, r: int):
        if r <=0 :
           raise ValueError('r must be above zero')

        self.r = r

    @property
    def get_area(self):

        area = pi * self.r**2
        return area

    @property
    def get_perimeter(self):
        perimeter = 2 * pi * self.r
        return perimeter
