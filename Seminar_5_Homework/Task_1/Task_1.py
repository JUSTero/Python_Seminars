# -*- coding: cp1251 -*-
# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".
# Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'

text = 'ываабв лповап абвцукв алоабвабв ываываыв'
print(text)

def del_some_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_some_words(text)
print(text)
