# -*- coding: cp1251 -*-
# �������� ���������, ������� ��������� �� ���� �����, ������������ ���� ������, � ���������, �������� �� ���� ���� ��������.

day = int(input('Enter day of week '))
if day == 7 or day ==6:
    print("It's a holiday")
elif day > 7 or day < 1:
    print('There is no such day')
else:
    print('Weekday')
