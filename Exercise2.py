#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import *
def create_list(arr_list, list_length):
    for i in range(list_length):
        arr_list.append(randint(-10, 10))

def sum_pairs(arr_list):
    res = []
    for i in range(0, int(len(arr_list) / 2 + 1)):
        res.append(arr_list[i] * arr_list[len(arr)-i-1])
    return res



arr = []
create_list(arr, 5)
print(arr)
print(sum_pairs(arr))
