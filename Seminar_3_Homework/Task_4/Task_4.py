# -*- coding: cp1251 -*-
# �������� ���������, ������� ����� ��������������� ���������� ����� � ��������.

def binary(num):
    binary = ''
    while num != 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary


number = int(input('����� ��� �������� � �������� = '))

print(binary(number))