# -*- coding: cp1251 -*-
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def average(list):
    size = len(list) - 1
    avr = []
    for i in range(len(list) // 2):
        avr.append(list[i] * list[size - i])
    return avr


numbers = []
N = int(input("Количество чисел = "))
for i in range(N):
    numbers.append(float(input()))

print(numbers)
print(average(numbers))
