__author__ = 'Smirnov Boris Leonidovich'

import random

# 1) Написать программу, которая генерирует список со случайными значениями. (модуль random в помощь)

list = []
n = input("Введите желаемое количество элементов: ")
count = 0
while count < int(n):
    list.append(random.randint(0,100))
    count += 1
print(list)

# 2) Найдите сумму чисел списка, которые стоят на четных местах.

summ = 0

for i in range(0, len(list), 2):
    summ += list[i]

print (summ)

# 3) Сделать универсальное решение для того, чтобы можно было отсортировать словарь по значениям

# не вполне понятна задача

# 4) Сформировать пять списков разной длины и найти в них элементы, которые есть в каждом списке

n = int(input("Введите желаемое количество элементов: "))

list1, list2, list3, list4, list5 = [], [], [], [], []
count = 0
while count < n:
    list1.append(random.randint(0,40))
    count += 1
count = 0
while count < n+2:
    list2.append(random.randint(0,40))
    count += 1
count = 0
while count < n+3:
    list3.append(random.randint(0,40))
    count += 1
count = 0
while count < n+4:
    list4.append(random.randint(0,40))
    count += 1
count = 0
while count < n+5:
    list5.append(random.randint(0,40))
    count += 1

newList1, newList2, newList3, newList4, newList5 = set(list1), set(list2), set(list3), set(list4), set(list5)

print(newList1)
print(newList2)
print(newList3)
print(newList4)
print(newList5)

set = (newList1.intersection(newList2))
set = (set.intersection(newList3))
set = (set.intersection(newList4))
set = (set.intersection(newList5))
print(set)