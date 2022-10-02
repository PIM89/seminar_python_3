# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

user_num = int(input('Задайте целое положительное число: '))

def negafibonachi(user_num):
    list_negafibonachi_positive = [0, 1]
    for i in range(user_num - 1):
        list_negafibonachi_positive.append(list_negafibonachi_positive[i] + list_negafibonachi_positive[i+1])
    list_negafibonachi_negative = [0, 1]
    for i in range(user_num - 1):
        list_negafibonachi_negative.append(list_negafibonachi_negative[i] - list_negafibonachi_negative[i+1])
    list_negafibonachi_negative.reverse()
    list_negafibonachi_negative.extend(list_negafibonachi_positive[1:])
    if user_num == 0:
        return '0'
    else: return list_negafibonachi_negative

print(f'Список чисел Фибоначи: {negafibonachi(user_num)}')
