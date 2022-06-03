'''
Объявите в программе следующие несколько классов:

CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.

Обеспечить возможность создания объектов каждого класса командами:

cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory, максимум N - по числу слотов памяти на материнской плате (по умолчанию N = 4).

Объекты классов должны иметь, следующие локальные свойства: 

для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число слотов памяти; mem_slots - список из объектов класса Memory (максимум total_mem_slots штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской плате в виде следующего списка из четырех строк:

['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']

Создайте объект mb класса MotherBoard с одним CPU и двумя слотами памяти.

P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.

'''


class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume) -> None:
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu: CPU, mem_slots: list, total_mem_slots: int = 4,) -> None:
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = mem_slots

    def get_config(self):
        return [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            f'Память: {"; ".join(f"{str(x.name)} - {str(x.volume)}" for x in self.mem_slots)}'
        ]


cpu = CPU("Intel i3", 2700)
memory1, memory2 = Memory('Asus', 1333), Memory('Asus', 1333)
mb = MotherBoard('MSI', cpu, (memory1, memory2), total_mem_slots=2)
print(mb.get_config())
