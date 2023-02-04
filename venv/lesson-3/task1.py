"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
dict_1 = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
list_1 = ['зима', 'весна', 'лето', 'осень']


def seasons_dict(number, dic):
    return [k for (k, n) in dic.items() if number in n]


def seasons_list(number, lis):
    ret = 0;
    if 3 <= number < 6:
        ret = lis[1]
    elif 6 <= number < 9:
        ret = lis[2]
    elif 9 <= number < 12:
        ret = lis[3]
    else:
        ret = lis[0]
    return ret


print(*seasons_dict(10, dict_1))
print(seasons_list(11, list_1))
