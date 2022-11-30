# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)

n = int(input('Введите число: '))

def interpretator(num):
    res = []
    while num != 0:
        res.append(num % 2)
        num //= 2
    return res

print(*interpretator(n), sep='')
