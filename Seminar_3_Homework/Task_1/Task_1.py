# -*- coding: cp1251 -*-
#������� ������ �� ���������� �����. �������� ���������, ������� ����� ����� ��������� ������, ������� �� �������� �������.


def sum(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum


numbers = []
N = int(input("���������� ����� = "))
for i in range(N):
    numbers.append(float(input()))

print("����� ����� ", sum(numbers))

