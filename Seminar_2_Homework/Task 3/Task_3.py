# -*- coding: cp1251 -*-
# ������� ������ �� n ����� ������������������ $(1+\frac 1 n)^n$ � �������� �� ����� �� �����.

N = int(input('N = '))

for i in range(1, N + 1):
    print(round((1 + 1/i) ** i, 2), end = ' ')
print()
