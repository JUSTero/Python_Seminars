# -*- coding: cp1251 -*-
# ���� ����� ������� ����� ������� ������� � ����. ��� ����� �� �������� ������� biggest_dict(**kwargs), 
# ������� ��������� �������������� ���������� ���������� �����: �������� � ��������� ��������� �� ������� my_dict, 
# ��������� ����� �� ������ �������� �first_one� �� ��������� �we can do it�. ����������� ��� �������.
# my_dict = {'first_one': 'we can do it'}
# �����
# k1=22, k2=31, k3=11, k4=91
# name='�����', age=31, weight=61, eyes_color='grey'

biggest_dict = dict(first_one = 'we can do it')

def Biggest_Dict(dict, **kwargs):
    dict.update(**kwargs)

print(biggest_dict)

Biggest_Dict(biggest_dict, k1=22, k2=31, k3=11, k4=91)
print(biggest_dict)
Biggest_Dict(biggest_dict, name='�����', age=31, weight=61, eyes_color='grey')
print(biggest_dict)