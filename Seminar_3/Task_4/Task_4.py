# -*- coding: cp1251 -*-
# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), 
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, 
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
# my_dict = {'first_one': 'we can do it'}
# тесты
# k1=22, k2=31, k3=11, k4=91
# name='Елена', age=31, weight=61, eyes_color='grey'

biggest_dict = dict(first_one = 'we can do it')

def Biggest_Dict(dict, **kwargs):
    dict.update(**kwargs)

print(biggest_dict)

Biggest_Dict(biggest_dict, k1=22, k2=31, k3=11, k4=91)
print(biggest_dict)
Biggest_Dict(biggest_dict, name='Елена', age=31, weight=61, eyes_color='grey')
print(biggest_dict)