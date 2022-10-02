# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

user_num = int(input('Введите размерность списка: '))
user_list = []
for i in range(user_num):
    user_list.append(round(random.random()*10, 2))
print(user_list)

def difference_max_min(user_list):
    max = user_list[0] % 1
    min = user_list[0] % 1
    for i in range(len(user_list)):
        if max < user_list[i] % 1:
            max = user_list[i] % 1
        if min > user_list[i] % 1:
            min = user_list[i] % 1
    return round(max - min, 2)

print(difference_max_min(user_list))
