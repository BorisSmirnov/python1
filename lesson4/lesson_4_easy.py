__author__ = 'Smirnov Boris Leonidovich'

# Все задачи текущего блока решите с помощью генераторов списков!

import random


# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


numbers = [random.randint(0, 10) for _ in range(10)]
print([x * x for x in numbers])

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


fruits_1 = ["apple", "orange", "lemon", "pear", "grapes", "watermelon", "melon", "lime"]
fruits_2 = ["kiwi", "mango", "apple", "lime", "слива", "melon", "grapes", "pomegranate"]
print([x for x in fruits_1 if x in fruits_2])

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


list_1 = [random.randint(-50, 100) for _ in range(50)]
list_2 = [x for x in list_1 if (x > 0) and (x % 3 == 0) and (x % 4 != 0)]

print(list_2)
