# -*- coding: cp1251 -*-
# �������� ���������, ������� ����� ������������ ��� ����� ������. ����� ������� ������ � ��������� �������, ������ � ������������� � �.�.

def average(list):
    size = len(list) - 1
    avr = []
    for i in range(len(list) // 2):
        avr.append(list[i] * list[size - i])
    return avr


numbers = []
N = int(input("���������� ����� = "))
for i in range(N):
    numbers.append(float(input()))

print(numbers)
print(average(numbers))
