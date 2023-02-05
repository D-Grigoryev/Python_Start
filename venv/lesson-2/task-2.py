"""
Задание 2.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.
Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

num_inp = int(input('Ведите целое положительное число: '))


def find_max_number(num):
    more = 0
    smaller = 0
    if num > 999:
        while num > 0:
            more = num % 10
            num = num // 10
            if more < smaller:
                more = smaller
            else:
                smaller = more
    return more


print(f'Самая большая цыфра в числе {num_inp} - {find_max_number(num_inp)}')
