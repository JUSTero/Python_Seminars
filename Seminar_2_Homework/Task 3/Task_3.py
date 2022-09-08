# -*- coding: cp1251 -*-
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

N = int(input('N = '))

for i in range(1, N + 1):
    print(round((1 + 1/i) ** i, 2), end = ' ')
print()
