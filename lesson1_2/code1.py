from ctypes.wintypes import POINT
from turtle import color


class Point:
    color = 'red'
    circle = 2


x = Point()
y = Point()
y.color = 'Black'
y.circle = 5
print(x.color)
print(id(y), ' ', id(x))

class Dictionary:
    rus = 'Питон'
    eng = 'Python'
    
print(getattr(Dictionary, 'rus_word', False))

"""
* getattr(obj name, [, default]) - возращает значения атрибута объекта;
* hasattr(obj, name) - проверяет на наличие атрибута name в obj; 
* setattr(obj, name, value) - задает значения атрибута (если атрибута не 
  существует, то он создается)
* delattr(obj, name) - удаляет атрибут с именем name

* __doc__ - содержит строку с описанием класса.
* __dict__ - содержит набор атрибутов экземпляра класса.
"""