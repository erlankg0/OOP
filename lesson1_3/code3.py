import sys

# здесь объявляется класс StreamData

class StreamData:
    def create(self, FIELDS, lst_in):
        self.fields = FIELDS
        self.lst_in = lst_in
        if len(self.fields) != len(self.lst_in):
            return False
        else:
            return True
        
class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()
print(f'data {data} res {result}')