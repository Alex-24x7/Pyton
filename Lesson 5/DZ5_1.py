import os
clear = lambda: os.system('clear')  # При использовании MacOS или Linux
# clear = lambda: os.system('CLS')  # При использовании Windows
clear()

#____________________________________________________________________________________
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')