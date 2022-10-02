# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# o [2, 3, 4, 5, 6] => [12, 15, 16];
# o [2, 3, 5, 6] => [12, 15]

from random import randint

user_num = int(input('Введите размерность списка: '))
user_list = []
for i in range(user_num):
    user_list.append(randint(-user_num, user_num))
print(user_list)


def sum_elem(user_list):
    user_list_result = []
    for i in range(len(user_list)//2):
        user_list_result.append(user_list[i] * user_list[-i-1])
    if len(user_list) % 2 != 0:
        user_list_result.append(user_list[(len(user_list)//2)]**2)
    return user_list_result

print(f'Произведение пар чисел списка равно: {sum_elem(user_list)}')