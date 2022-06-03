'''
Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого класса, следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно
'''
import random
from random import choice


class Line:

    def __init__(self, a, b, c, d) -> None:
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:

    def __init__(self, a, b, c, d) -> None:
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:

    def __init__(self, a, b, c, d) -> None:
        self.sp = (a, b)
        self.ep = (c, d)

elements = []
classes = [Line, Rect, Ellipse]
for item in range(217):
    a = random.randrange(100)
    b = random.randrange(100)
    c = random.randrange(100)
    d = random.randrange(100)
    elements.append(choice(classes)(a, b, c, d))

for e in elements:
    if isinstance(e, Line):
        e.ep = (0, 0)
        e.sp = (0, 0)