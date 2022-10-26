import os
clear = lambda: os.system('clear')  # При использовании MacOS или Linux
# clear = lambda: os.system('CLS')  # При использовании Windows
clear()

# def f(x):
#     return x**2

# print(f(2))
# print(f(3))


from math import pi

d =  int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')