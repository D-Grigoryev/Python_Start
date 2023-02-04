# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите целое число: "))


def multiply_n(user_element):
    temp, mult, result = 1, 1, []
    while temp <= user_element:
        mult *= temp
        temp += 1
        result.append(mult)

    return result


print(f'Набор произведений от 1 до {n} равен - {multiply_n(n)}')
