# -*- coding: cp1251 -*-
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def binary(num):
    binary = ''
    while num != 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary


number = int(input('Число для перевода в двоичное = '))

print(binary(number))