# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Enter x '))
y = int(input('Enter y '))

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print("The dot is in the 1st quadrant")
    elif x > 0 and y < 0:
        print("The dot is in the 2nd quadrant")
    elif x < 0 and y < 0:
        print("The dot is in the 3rd quadrant")
    else:
        print("The dot is in the 4th quadrant")
else:
    print('One of the coordinates is 0')