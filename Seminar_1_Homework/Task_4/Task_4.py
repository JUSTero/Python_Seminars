# -*- coding: cp1251 -*-
# �������� ���������, ������� �� ��������� ������ ��������, ���������� �������� ��������� ��������� ����� � ���� �������� (x � y).

numquar = int(input('Enter number quarter '))
if numquar > 4 or numquar < 1:
    print('Number out of range')
elif numquar == 1:
    print(f'X > 0 and Y > 0')
elif numquar == 2:
    print(f'X > 0 and Y < 0')
elif numquar == 3:
    print(f'X < 0 and Y < 0')
else:
    print(f'X < 0 and Y > 0')