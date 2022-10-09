import os
clear = lambda: os.system('clear')
clear()
# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# a = int(input('Первое число: '))
# b = int(input('Второе число: '))

# if a*a == b:
#     print('Да')
# elif b*b == a:
#     print('Да')
# else:
#     print('Нет')


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# i=0
# max = int(input('Введите число 1: '))
# while i < 4:
#     a = int(input(f'Введите число {i+2}: '))
#     if a > max:
#         max = a
#     i+=1
# print('Максимальное число:', max)

# some_list = []
# for _ in range(5):
#     number = int(input())
#     some_list.append(number)
# maxx = some_list[0]
# for element in some_list:
#     if element in some_list:
#         maxx = element
# print(maxx)

# print(max(map(int, input().split())))

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n = int(input('Введите целое число: '))
# some_list = []
# for number in range(-n, n+1):
#     some_list.append(number)
# print(some_list, sep=',')

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# a = float(input())
# print(f'Нет' if a*10 %10 == 0 else int(a*10 %10))

# n = input()
# if '.' in n:
#     index_t = n.find('.')
#     print(n[index_t + 1])
# else:
#     print('нет')

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int(input())
print('Да' if (n%5==0 and n%10==0 or n%15==0) and (n%30!=0) else 'Нет')