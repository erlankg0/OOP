'''
В программе объявлена переменная TYPE_OS и два следующих класса:

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name = "DialogWindows"


class DialogLinux:
    name = "DialogLinux"
Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:

dlg = Dialog(<название>)
Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.

Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 и объекты класса DialogLinux, если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS может меняться в последующих строчках программы. Имейте это в виду, при объявлении класса Dialog.

P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.
'''

TYPE_OS = 2  # 1 - Windows; 2 - Linux


class DialogWindows:
    name = 'DialogWindows'


class DialogLinux:
    name = 'DialogLinux'


class Dialog:
    obj = None

    def __new__(cls, *args, **kwargs):
        # print('CALL __new__')
        if cls.obj is None:
            if TYPE_OS == 1:
                cls.obj = super().__new__(DialogWindows)
                cls.obj.name = args[0]
                # print('Windows')
            else:
                cls.obj = super().__new__(cls)
                # print('LINUX')
                cls.obj.name = args[0]
            return cls.obj

    def __del__(self):
        # print('Call DEL')
        Dialog.obj = None

    def __init__(self, name: str):
        # print('CALL __init__')
        self.name = name


dgl = Dialog("Linux")
dgl1 = Dialog("Windows")
print(dgl.name)
print(True if isinstance(dgl, DialogLinux) else False)

print(dgl1.name)
print(True if isinstance(dgl, DialogWindows) else False)


