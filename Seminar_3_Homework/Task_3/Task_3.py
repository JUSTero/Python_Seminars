# -*- coding: cp1251 -*-
# ������� ������ �� ������������ �����. �������� ���������, ������� ����� ������� ����� ������������ � ����������� ��������� ������� ����� ���������.

def difference(list):
    min = list[0] % 1
    max = list[0] % 1
    for i in range(len(list)):
        if list[i] % 1 > max:
            max = list[i] % 1
        elif list[i] % 1 < min:
            min = list[i] % 1
    return round(max - min, 2)


numbers = []
N = int(input("���������� ����� = "))
for i in range(N):
    numbers.append(float(input()))

print(numbers)
print(difference(numbers))