
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input(f'Enter x ')
y = input(f'Enter y ')
z = input(f'Enter z ')

res1 = not(x or y or z)
res2 = not x and not y and not z
res = res1 == res2

if res == True:
    print('The statement is true')
else:
    print('The statement is false')
