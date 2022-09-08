# -*- coding: cp1251 -*-
#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


N = int(input('Количество элементов = '))
numbers = []
numbers = [randint(-N, N + 1) for i in range(N)]
data = []
avr = 1



with open('TextFile1.txt') as TF:
    print(*TF)
    data = [(int(line.strip()) for line in TF)]
    print(data)
for i in data:
    avr = avr * numbers[i]
    print(i)

print(numbers)
print(avr)