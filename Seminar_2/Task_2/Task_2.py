# -*- coding: cp1251 -*-

text = '�������������������'
count = 0
maxcount = 0

for i in range(len(text)):
    if text[i] == '�':
        count += 1
        if count > maxcount:
            maxcount = count
    else:
        count = 0

print(maxcount)

