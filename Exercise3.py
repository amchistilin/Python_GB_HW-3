#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
import random
from random import *
def create_list(arr_list, list_length):
    for i in range(list_length):
        arr_list.append(round(uniform(0, 10), 2))


def fractional_list(arr_list):
    new_l = []
    for i in range(len(arr_list)):
        new_l.append(round(arr_list[i] - int(arr_list[i]), 2))
    return new_l

l1 = []
create_list(l1, 7)
l2 = fractional_list(l1)
print(l1)
print(l2)
print(f'Ответ: {max(l2) - min(l2)}')






