# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите целое число: "))


def multiply_n(user_element):
    i, mult, result = 1, 1, {}
    while i <= user_element:
        mult += round((1 + 1 / user_element)**user_element)
        result[i] = mult
        i += 1
    return result


print(f'Сумма последовательности чисел - {multiply_n(n)}')

