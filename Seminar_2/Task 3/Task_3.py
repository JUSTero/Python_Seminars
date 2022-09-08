# -*- coding: cp1251 -*-

N = int(input('Введите количество членов '))
num = 1

for i in range(N):
    print(f'{i + 1}. {num}')
    num *= -3

