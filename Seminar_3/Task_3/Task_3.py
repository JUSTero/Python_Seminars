# -*- coding: cp1251 -*-
# � ��������� ����� ��������� ���������� �����, � ����� ��� ������ ��������� ������ ���������� ���������� � ��� �������� � ����.

f = open('TestFile', 'r')
linecount = 1

for line in f:
    words = len(line.split())
    print(f'� {linecount} ������ {words} ���� � {len(line)} ��������')
    linecount += 1

f.close()
print(f'����� � �����: {linecount - 1} ')



