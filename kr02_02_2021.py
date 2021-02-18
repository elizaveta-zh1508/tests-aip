def task_1(two_dim_words):
    """
        Здесь должен быть ваш код.
        Переменная two_dim_words - ваш двумерный список.
        Заполнять список значениями не нужно.
        Финальное значение должно быть помещено в переменную sorted_words.
        """
    s = sorted(two_dim_words)
    sorted_words = sorted(s, key=len, reverse=True)

    return sorted_words


def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """
    words_1 = str(words).lower()
    words_2 = list(words_1.split(', '))
    if words_1.count('a') >= 2:
        a = [i.count('a') ** 2 for i in words_2]
        res = tuple(a)
    
    return res


def task_4_2(words):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """
    words = "Alaska", "auto", "arc", "agenda", "arugula", "caveman"
    res = {len(i) for i in words if len(i) > 3}

    return res


def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """
    v = "aoiuey"
    w = str(words).lower()
    for i in w:
        if i.endswith('a') is True:
            for chr in w:
                if chr in v:
                    w = w.replace(chr,'')
                    res = w
    return res


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """
    diff = sorted(list(set(lst1) - set(lst2)), reverse=False)


    return diff

def task_6(lst):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """
    new_spisok = set(lst)
    new_spisok_1 = sorted(new_spisok, reverse=True)
    res = tuple(new_spisok_1)

    return res

