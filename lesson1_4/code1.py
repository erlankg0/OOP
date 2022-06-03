'''
Инициализатор и финализатор
есть магические методы 
синтаксиз
__имя метода__

в частности существует 2 метода

первый сразу же реализуется 
__init__(self) - инициализатор объекта класса
второй же реализуется перед его удалением
__del__(self) - финализатор  класса
'''


class Point:
    color = 'RED'
    cirlce = 2

    def __init__(self, a, b):
        print("Call init")
        self.x = a
        self.y = b

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get__coords(self):
        return f'{self.x} {self.y}'

    def __del__(self):
        print("Call del")


pt = Point(10, 4)
print(pt.__dict__)
