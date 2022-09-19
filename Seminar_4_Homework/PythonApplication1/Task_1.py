# -*- coding: cp1251 -*-
# Вычислить число c заданной точностью d

from cmath import pi


d = float(input('Введите точность '))
accuracy = 0
while d < 1:
    accuracy += 1
    d *= 10

print(round(pi, accuracy))
