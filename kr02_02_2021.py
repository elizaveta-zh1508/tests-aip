import re
from operator import itemgetter


def task_1(two_dim_words):  # можно сделать тесты
    """
    Здесь должен быть ваш код.
    Переменная two_dim_words - ваш двумерный список.
    Новый список создавать не нужно.
    Финальное значение должно быть помещено в переменную sorted_words.
    """
    one_dim = []
    for cluster in two_dim_words:
        one_dim.extend(cluster)
    sorted_words = sorted(sorted(one_dim), key=len, reverse=True)
    return sorted_words


def task_2(school):  # проверить вручную
    option = int(input("Выберите действие:\n"
                       "1 - изменить кол-во учащихся в классе\n"
                       "2 - добавить новый класс\n"
                       "3 - удалить класс\n"
                       "4 - вывести кол-во учеников в школе\n"))
    if option == 1:
        group = input("Введите класс: ")
        num = int(input("Новое кол-во учеников: "))
        school[group] = num
        return school
    elif option == 2:
        group = input("Введите класс: ")
        num = int(input("Кол-во учеников: "))
        school[group] = num
        return school
    elif option == 3:
        group = input("Введите класс: ")
        school.pop(group)
        return school
    elif option == 4:
        students = sum(school.values())
        return students


def task_3(numbers):  # можно сделать тесты
    set_num = set(numbers)
    dict_num = {int(num): numbers.count(num) for num in set_num}
    top3 = sorted(set(dict_num.values()), reverse=True)[:3]
    dict_min = {key: value for key, value in dict_num.items() if value in top3}
    return dict_min


def task_4_1(words):  # можно сделать тесты
    """Элемент списка – квадрат кол-ва букв «а» в каждом слове (по порядку),
        если буква «а» встречается в слове минимум 2 раза"""
    res = [word.lower().count("a") ** 2 for word in words if word.lower().count("a") >= 2]
    return tuple(res)


def task_4_2(words):  # можно сделать тесты
    """Элементы списка – длины слов из списка words,
    в которых больше 3 букв"""
    res = [len(word) for word in words if len(word) > 3]
    return set(res)


def task_4_3(words):  # можно сделать тесты
    """Элементы списка – последовательности из согласных букв слов списка words,
    заканчивающихся на 'а'"""
    res = [re.sub(r"[aeiou]", "", word.lower()) for word in words if word.lower().endswith("a")]
    return res


def task_5(lst1, lst2):  # можно сделать тесты
    diff = sorted(set(lst1).difference(lst2))
    return diff


def task_6(lst):  # можно сделать тесты
    res = tuple(sorted(set(lst), reverse=True))
    return res


def task_7(shop):  # проверить вручную
    customers = sorted({i["name"] for i in shop.values()})
    for person in customers:
        items = set()
        print("NAME:", person)
        for i in shop.values():
            if i["name"] == person:
                items.add((i["item"], i["number"]))
        items = sorted(items, key=itemgetter(0))
        for i in items:
            print(i[0], i[1])

    return customers
