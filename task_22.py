# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

user_num = int(input('Введите размерность списка: '))
user_list = []
for i in range(user_num):
    user_list.append(randint(-user_num, user_num))
print(user_list)

def sum_uneven_number(user_list):
    sum = 0
    for i in range(1, len(user_list), 2):
        sum += user_list[i]
    return sum

print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum_uneven_number(user_list)}')
