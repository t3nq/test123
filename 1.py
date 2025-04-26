from random import randint
from time import sleep


class Randomizer:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.result = self.__get_genereted_value()

    def __get_genereted_value(self):
        return randint(self.value1, self.value2)

    def get_info(self):
        return f"Случайное число: {self.result}"


a = int(input("Введите число от: "))
b = int(input("Введите число до: "))

rand = Randomizer(a, b)

print(f'Подбираем число в диапозоне от {a} до {b}...')
sleep(2)
print(rand.get_info())
