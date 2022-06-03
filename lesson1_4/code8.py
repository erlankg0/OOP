# Реализиция Python класса узла, используемая для создания объектов узла

import re


class Node:
    def __init__(self, data) -> None:
        # Информационая область
        self.data = data
        # Ссылка на след объект
        self.next_obj = None

# Реализация Python связанного списка, используемая для создания объектов связанного списка


class ListObject:
    def __init__(self) -> None:
        # Записать головной узел, сохранить объект
        self.head = None

    def is_empty(self):
        return  self.head is None

    def add(self, item):
        # Создать объект узла
        node = Node(item)
        
