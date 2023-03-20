# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N
# целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import sample

list_size = int(input("Введите кол-во элементов в массиве: "))
list = sample(range(1, list_size + 100), list_size)
print(list)

find_number = int(input('Введите число для поиска: '))

index_of_closest = 0
minimum_difference = abs(list[0] - find_number)

for i in range(0, len(list)):
    this_difference = abs(list[i] - find_number)
    if this_difference < minimum_difference:
        index_of_closest = i
        minimum_difference = this_difference

print('Ближайшее число', list[index_of_closest])
