# -*- coding: cp1251 -*-
#  ������� ������ �� N ���������, ����������� ������� �� ���������� [-N, N]. 
#  ������� ������������ ��������� �� ��������� ��������.
#  ������� �������� � ����� file.txt � ����� ������ ���� �����.

from random import randint


N = int(input('���������� ��������� = '))
numbers = []
numbers = [randint(-N, N + 1) for i in range(N)]
data = []
avr = 1



with open('TextFile1.txt') as TF:
    print(*TF)
    data = [(int(line.strip()) for line in TF)]
    print(data)
for i in data:
    avr = avr * numbers[i]
    print(i)

print(numbers)
print(avr)