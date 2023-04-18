# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

len_array = int(input('Введите количество элементов в массиве: '))
array = [random.randrange(10) for i in range(len_array)]
print(array)
serch_number = int(input('Введите число для поска в массиве: '))

# solution - regular level:
# min_val = array[0]
# min_diff = abs(array[0] - serch_number)

# for i in range(1, len(array)):    
#     if abs(array[i] - serch_number) < min_diff:
#         min_diff = abs(array[i] - serch_number)
#         min_val = array[i]
# print(min_val)

# solution - expert level:    
print(min(array, key=lambda num: abs(num - serch_number)))
