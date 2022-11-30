#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import *
def create_list(arr_list, list_length):
    for i in range(list_length):
        arr_list.append(randint(-100, 100))

def find_sum(arr_list):
    total = 0
    for i in range(1, len(arr_list) + 1, 2):
        total += arr_list[i]
    return total

arr = []
create_list(arr, 6)
print(f'Посмотрите на сгенерированный список {arr}')
print(f'А вот сумма его нечетных элементов: {find_sum(arr)}')




