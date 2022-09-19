# -*- coding: cp1251 -*-
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

divider = 0
N = int(input('Заданное число '))
i = 2
while i <= int(N):
    if N % i == 0:
        divider = i
        N = N // i
        i = 2
        print(divider)
    else:
        i += 1
