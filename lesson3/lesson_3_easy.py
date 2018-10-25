__author__ = 'Smirnov Boris Leonidovich'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    number = number * (10 ** ndigits) + 0.5
    number = number // 1
    return number / (10 ** ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_list = str(ticket_number)
    if len(ticket_list) != 6:
        return False
    left_ticket  = ticket_list[:3]
    right_ticket = ticket_list[3:]
    left_sum = 0
    right_sum = 0
    for i in left_ticket:
        left_sum = left_sum + int(i)
    for i in right_ticket:
        right_sum = right_sum + int(i)
    return left_sum == right_sum


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
