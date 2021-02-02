def list_of_words(two_dim_words):
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
