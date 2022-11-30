#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
import random
from random import *
def create_list(arr_list, list_length):
    for i in range(list_length):
        arr_list.append(round(uniform(0, 10), 2))

def fractional_list(arr_list):
    new_arr = []
    for i in range(len(arr_list)):
        new_arr.append(arr_list[i] - int(arr_list[i]))
    return new_arr

arr = []
create_list(arr, 5)
print(arr)
print(max(arr) - min(arr))