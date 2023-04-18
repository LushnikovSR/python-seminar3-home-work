# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

len_array = int(input('Введите количество элементов в массиве: '))
array = [random.randrange(10) for i in range(len_array)]
print(array)
serch_number = int(input('Введите число для поска в массиве: '))
# methods solution:
print(array.count(serch_number))

# List Comprehension solution:
# print(len([el for el in array if el == serch_number]))