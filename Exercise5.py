# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
n = int(input())
s1 = []
x1, x2 = 1, 1
for i in range(n):
    s1.append(x1)
    x1, x2 = x2, x1 + x2

def negative_list(arr):
    s2 = []
    for i in range(len(arr)):
        s2.append(arr[i] * - 1)
        s2.sort()
    return s2

neg_s1 = negative_list(s1)

print(neg_s1 + [0] + s1)

