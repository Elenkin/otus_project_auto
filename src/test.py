import math
from abc import ABC

from src.figure import Figure

pi = math.pi

class Circle(Figure, ABC):
    def init(self, r: int):
        if r <=0 :
           raise ValueError('r must be above zero')

        self.r = r

    # декоратор - тогда метод можно вызызвать на классе как атрибут
    @property
    def get_area(self):

        area = pi * self.r**2
        return area

    @property
    def get_perimeter(self):
        perimeter = 2 * pi * self.r
        return perimeter


c1 = Circle(13)
c2 = Circle(10)

#
# print(c1.get_area)
# print(c2.get_area)
# total_area = c1.area(c2)
# print(total_area)

print(c1.get_perimeter)
print(c2.get_perimeter)
# total_perimeter= c1.add_perimeter(c2)
# print(total_perimeter)