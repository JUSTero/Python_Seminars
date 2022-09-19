# -*- coding: cp1251 -*-
# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.

f = open('TestFile', 'r')
linecount = 1

for line in f:
    words = len(line.split())
    print(f'В {linecount} строке {words} слов и {len(line)} символов')
    linecount += 1

f.close()
print(f'Строк в файле: {linecount - 1} ')



