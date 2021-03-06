'''
Объявите в программе класс Video с двумя методами:

create(self, name) - для создания нового видео с именем name (метод сохраняет имя name в локальном атрибуте объекта класса Video);
play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").

Объявите еще один класс с именем YouTube, объекты которого создаются командой:

yt = YouTube()
В самом классе объявите два метода:

add_video(self, video) - для добавления нового видео (метод помещает объект video класса Video в список);
play(self, video_indx) - для проигрывания видео из списка по указанному индексу (индексация с нуля).

В каждом объекте этого класса должен быть локальный атрибут videos, представляющий собой список, в котором сохраняются объекты класса Video. Изначально список пуст.

Метод play() класса YouTube должен обращаться к объекту класса Video по индексу в списке videos и, затем, вызывать метод play() класса Video.

Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП". После этого создайте объект youtube класса YouTube, добавьте в него эти два видео и воспроизведите сначала первое, а затем, второе видео.

Sample Input:


Sample Output:

воспроизведение видео Python
воспроизведение видео Python ООП
'''

"""
* getattr(obj name, [, default]) - возращает значения атрибута объекта;
* hasattr(obj, name) - проверяет на наличие атрибута name в obj; 
* setattr(obj, name, value) - задает значения атрибута (если атрибута не 
  существует, то он создается)
* delattr(obj, name) - удаляет атрибут с именем name

* __doc__ - содержит строку с описанием класса.
* __dict__ - содержит набор атрибутов экземпляра класса.
"""


class Video:
    name = None

    # для создания нового видео с именем name (метод сохраняет имя name в локальном атрибуте объекта класса Video);
    def create(self, name):
        self.name = name

    # для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").
    def play(self) -> str:
        return f'воспроизведение видео {self.name}'


class YouTube:
    # для добавления нового видео (метод помещает объект video класса Video в список);
    videos = []

    def add_video(self, video: Video):
        self.videos.append(video.play())

    # для проигрывания видео из списка по указанному индексу (индексация с нуля).

    def play(self, video_index):
        print(f'{self.videos[video_index]}')


v1 = Video()
v1.create('Python')
v2 = Video()
v2.create('Python ООП')
yt = YouTube()
yt.add_video(v1)
yt.add_video(v2)
yt.play(0)
yt.play(1)
