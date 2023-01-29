"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3
Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
elem_user = input('Вводите целые числа через пробел: ')


def create_list(elements):
    nums = []
    for el in elem_user:
        i = 0
        if el in ' ':
            continue
        else:
            nums.append(el)
            i += 1
    return nums


def change_position(lis):
    for i in range(0, len(lis) - 1, 2):
        # print(range(0, len(lis) - 1, 2))
        lis[i], lis[i + 1] = lis[i + 1], lis[i]
        print(lis[i])
    return lis


print(f'{change_position(create_list(elem_user))}')
