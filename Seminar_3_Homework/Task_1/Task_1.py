# -*- coding: cp1251 -*-
#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


def sum(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum


numbers = []
N = int(input("Количество чисел = "))
for i in range(N):
    numbers.append(float(input()))

print("Сумма равна ", sum(numbers))

