# -*- coding: cp1251 -*-
# ������� ����������� ����� N. �������� ���������, ������� �������� ������ ������� ���������� ����� N.

import math

divider = 0
N = int(input('�������� ����� '))
i = 2
while i <= int(N):
    if N % i == 0:
        divider = i
        N = N // i
        i = 2
        print(divider)
    else:
        i += 1
