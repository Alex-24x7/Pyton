import os
clear = lambda: os.system('clear')  # При использовании MacOS или Linux
# clear = lambda: os.system('CLS')  # При использовании Windows
clear()

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# x = input('Введите число: ')

# def summa(x):                            #Функция нахождения суммы чисел в заданном числе
#     if float(x) < 0:                            #Проверка на знак перед числом
#         x = float(x) * (-1)
#     number = 0

#     for i in str(x):
#         if i != '.':
#             number += int(i)
#     return number

# print(f'Сумма чисел равна: {summa(x)}')


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int(input('Введите число: '))

# f = 1
# for i in range(N):
#     i +=1
#     f = i * f
#     print(f, end=" ")


# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму

# n = int(input('Введите количество чисел в списке: '))

# def numbers(n):
#     summ = 0
#     for i in range(n):
#         a = int(input(f'Введи число {i + 1}: '))
#         a = (1+1/a)**a
#         summ = a + summ
#         i += 1
#     return summ

# print('Сумма чисел равна:',round((numbers(n)), 2))