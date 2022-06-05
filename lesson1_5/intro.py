'''
Пример паттрена Singleton
'''


class Point:
    def __new__(cls, *args, **kwargs):
        print("Вызов __new__ для" + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("Вызов __init__ для" + str(self))
        self.x = x
        self.y = y


p = Point(1, 3)


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port) -> None:
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Connection on DataBase: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("DataBase closed")

    def read(self):
        return 'Reading DataBase'

    def write(self, data):
        print('Writing DataBase {}'.format(data))


db = DataBase("Erlan", '123321', 80)
db1 = DataBase("Daniel", '123321', 40)
print(id(db))
print()
print(id(db1))
db.connect()
db1.connect()