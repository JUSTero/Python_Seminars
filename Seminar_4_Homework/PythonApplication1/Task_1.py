# -*- coding: cp1251 -*-
# ��������� ����� c �������� ��������� d

from cmath import pi


d = float(input('������� �������� '))
accuracy = 0
while d < 1:
    accuracy += 1
    d *= 10

print(round(pi, accuracy))
