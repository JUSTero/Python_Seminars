# -*- coding: cp1251 -*-
# 1. �������� ���������, ������� ����� �� ���� ��������� ����� N � �������� ����� �� -N �� N

num = int(input('������� ����� '))

if num < 0:
    num *= -1
print (range(-num, num))