# -*- coding: cp1251 -*-
#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


N = int(input('Количество элементов = '))
numbers = [randint(-N, N + 1) for i in range(N)]                # Заполнение списка случайными числами
multipliers = [randint(0, N - 1) for i in range(4)]             # Заполнение списка множителей для записи в файл
mult = []                                                       
print(numbers)
avr = 1
with open('file.txt','w') as data:                              # Запись множителей в файл
    for i in range(4):
        data.writelines(f'{str(multipliers[i])}')
with open('file.txt','r') as path:                              # Чтение сножителей из файла
    for i in range(4):
        mult.append(int(path.read(1)))                          # Запись множителей в список
    print(mult)
for i in mult:                                                  # Нахождение произведения чисел, стоящих на индексах множителей
    avr *= numbers[i]
print(avr)

