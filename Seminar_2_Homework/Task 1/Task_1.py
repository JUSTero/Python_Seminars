# -*- coding: cp1251 -*-
# ???????? ?????????, ??????? ????????? ?? ???? ???????????? ????? ? ?????????? ????? ??? ????.

number = float(input('??????? ????? '))
sum = 0
while number % 1 > 0:                    # ??????? ??????? ????? ???? ??? ????
    number *= 10
while number > 0:                        # ??????? ????? ????
    sum += number % 10
    number //= 10
print(int(sum))
