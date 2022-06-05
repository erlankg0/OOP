'''
Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
P.S. В программе на экран ничего выводить не нужно. 

'''


class SingletonFive:
    _count = 0  # Этот класс должен формировать только первые пять объектов
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._count <= 4:
            cls._instance = super().__new__(cls)
            cls._count += 1
        return cls._instance

    def __init__(self, name) -> None:
        self.name = name


objs = [SingletonFive(str(x)) for x in range(10)]
for i in objs:
    print(id(i))