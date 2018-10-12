__author__ = 'Smirnov Boris Leonidovich'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

class NewInt(int):
    def __gt__(self,other):
        if other == 999999: return True
        else: return self.__int()>other.__int__()

a=NewInt(0)

print(type(a))

print(a==a**2)
print(a==a*2)
print(a>999999)