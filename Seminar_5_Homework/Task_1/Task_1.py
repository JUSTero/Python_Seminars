# -*- coding: cp1251 -*-
# 38. �������� ���������, ��������� �� ������ ��� ����� ���������� "���".
# ������� ������: '������ ������ ������� ��������� ��������'

text = '������ ������ ������� ��������� ��������'
print(text)

def del_some_words(text):
    text = list(filter(lambda x: '���' not in x, text.split()))
    return " ".join(text)

text = del_some_words(text)
print(text)
