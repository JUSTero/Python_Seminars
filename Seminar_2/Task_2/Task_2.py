# -*- coding: cp1251 -*-

text = 'ממממממנננמנמנננננננ'
count = 0
maxcount = 0

for i in range(len(text)):
    if text[i] == 'נ':
        count += 1
        if count > maxcount:
            maxcount = count
    else:
        count = 0

print(maxcount)

