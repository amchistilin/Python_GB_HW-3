# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
from math import *
n = int(input('Введите число: '))
s1 = []
x1, x2 = 1, 1
for i in range(n):
    s1.append(abs(x1)) # [0, 1, -1, 2, -3, 5, -8, 13, -21]
    if i % 2 == 0:
        s1.insert(0, x1)
    elif i % 2 != 0:
        s1.insert(0, x1 * (-1))
    x1, x2 = x2, x1 + x2
s1.insert(len(s1) // 2, 0)

print(s1)

# def negative_list(arr):
#     s2 = []
#     for i in range(len(arr)):
#         s2.append(arr[i] * - 1)
#         s2.sort()
#     return s2
#
# neg_s1 = negative_list(s1)
#
# print(neg_s1 + [0] + s1)

