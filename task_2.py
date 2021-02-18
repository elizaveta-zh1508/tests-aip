while True:
    school = {"1а": "32", "1б": "24", "1в": "27"}
    print('Выберите действие, которое хотите совершить (указать номер):', '1) измененить количество учащихся в одном из классов', '2) добавить новый класс', '3) удалить класс из базы', '4) подсчитать общее количество учащихся в школе', sep='\n')
    act = int(input())
    if act == 1:
        print('Введите номер класса: ')
        number = input()
        print('На какое число изменить? ')
        numbers = int(input())
        school[number] = numbers
        print(school)
    elif act == 2:
        print('Введите номер класса, который хотите добавить: ')
        number_2 = input()
        print('Введите количество учеников: ')
        numbers_2 = int(input())
        school[number_2] = numbers_2
        
        print(school)
    elif act == 3:
        print('Введите номер класса, который хотите удалить: ')
        number_3 = input()
        if 'number_3' in school:
            del school[number_3]
            print(school)
        else:
            print(school)
    elif act == 4:
        num = 0
        for name in school.values():
            num += int(name)
        print(num)
    else:
        print('Действия под таким номером не существует. Попробуйте еще раз.')
