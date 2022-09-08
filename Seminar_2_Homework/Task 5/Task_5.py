# -*- coding: cp1251 -*-
# Реализуйте алгоритм перемешивания списка.
from random import randint


numbers = [randint(-10, 10) for i in range(5)]
print(numbers)
lenght = len(numbers)
for i in range(lenght):
    rand_i = randint(0, lenght - 1)
    temp = numbers[i]
    numbers[i] = numbers[rand_i]
    numbers[rand_i] = temp
print(numbers)

