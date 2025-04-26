from random import randint
from time import sleep


def generate(value1, value2):
    return randint(value1, value2)


a = int(input("Введите число от: "))
b = int(input("Введите число до: "))

result = generate(a, b)

print(f'Подбираем число в диапозоне от {a} до {b}...')
sleep(2)
print(f"Случайное число: {result}")
