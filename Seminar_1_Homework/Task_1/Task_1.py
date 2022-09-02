# -*- coding: cp1251 -*-
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Enter day of week '))
if day == 7 or day ==6:
    print("It's a holiday")
elif day > 7 or day < 1:
    print('There is no such day')
else:
    print('Weekday')
