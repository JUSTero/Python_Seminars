# -*- coding: cp1251 -*-
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from math import *

x1 = int(input('Enter x1 '))
y1 = int(input('Enter y1 '))
x2 = int(input('Enter x2 '))
y2 = int(input('Enter y2 '))


print(round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2))
