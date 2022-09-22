# -*- coding: cp1251 -*-
# �������� ��������� ��� ���� � ��������� ������� ������ ��������. 
# ������� ������: �� ����� ����� 2021 �������. 
# ������ ��� ������ ����� ��� ���� ����� �����. ������ ��� ������������ �����������. 
# �� ���� ��� ����� ������� �� ����� ��� 28 ������. 
# ��� ������� ��������� ��������� ���������� ��������� ���. 
# ������� ������ ����� ����� ������� ������, ����� ������� ��� ������� � ������ ����������?
# a) �������� ���� ������ ����
# �) ���������, ��� �������� ���� "�����������"

# ������� ������� ������ ��������:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, ������� ���������� ������, ������� �������� �� 1 �� 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, ������� ���������� ���������� ������: "))
    return x


def p_print(name, k, counter, value):
    print(f"����� {name}, �� ���� {k}, ������ � ���� {counter}. �������� �� ����� {value} ������.")

player1 = input("������� ��� ������� ������: ")
player2 = input("������� ��� ������� ������: ")
value = int(input("������� ���������� ������ �� �����: "))
flag = randint(0,2) # ���� �����������
if flag:
    print(f"������ ����� {player1}")
else:
    print(f"������ ����� {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"������� {player1}")
else:
    print(f"������� {player2}")
