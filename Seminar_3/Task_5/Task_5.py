# -*- coding: cp1251 -*-
# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import random
import time

def getrand(x, y):
    count = y - x
    result = int(time.time()) % count
    return result + x
print(getrand(100, 80))
