# -*- coding: cp1251 -*-
#  ������� ������ �� N ���������, ����������� ������� �� ���������� [-N, N]. 
#  ������� ������������ ��������� �� ��������� ��������.
#  ������� �������� � ����� file.txt � ����� ������ ���� �����.

from random import randint


N = int(input('���������� ��������� = '))
numbers = [randint(-N, N + 1) for i in range(N)]                # ���������� ������ ���������� �������
multipliers = [randint(0, N - 1) for i in range(4)]             # ���������� ������ ���������� ��� ������ � ����
mult = []                                                       
print(numbers)
avr = 1
with open('file.txt','w') as data:                              # ������ ���������� � ����
    for i in range(4):
        data.writelines(f'{str(multipliers[i])}')
with open('file.txt','r') as path:                              # ������ ���������� �� �����
    for i in range(4):
        mult.append(int(path.read(1)))                          # ������ ���������� � ������
    print(mult)
for i in mult:                                                  # ���������� ������������ �����, ������� �� �������� ����������
    avr *= numbers[i]
print(avr)

