'''
Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки. Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление товара в корзину, представленного объектом gd;
remove(self, indx) - удаление товара из корзины по индексу indx;
get_list(self) - получение товаров корзины в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами. 

P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям
'''




class Cart:
    def __init__(self) -> None:
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)
    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        res = []
        for item in self.goods:
            res.append(f'{item.name}: {item.price}')
        return res


class Product:
    def __init__(self, name: str, price: int or float) -> None:
        self.name = name
        self.price = price


class TV(Product):
    pass


class Table(Product):
    pass


class Notebook(Product):
    pass


class Cup(Product):
    pass

cart = Cart()

tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)
lst = cart.get_list()
print(lst)