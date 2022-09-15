# -*- coding: cp1251 -*-
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def difference(list):
    min = list[0] % 1
    max = list[0] % 1
    for i in range(len(list)):
        if list[i] % 1 > max:
            max = list[i] % 1
        elif list[i] % 1 < min:
            min = list[i] % 1
    return round(max - min, 2)


numbers = []
N = int(input("Количество чисел = "))
for i in range(N):
    numbers.append(float(input()))

print(numbers)
print(difference(numbers))