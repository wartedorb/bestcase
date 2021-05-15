import random

d = dict()

c = """
Правила:
НАРОД - 1 житель платит в год 1 д.е., потребляет 1 ед зерна
ЗЕМЛЯ - с 1 земли приходит 1 ед зерна
КАЗНА - за 1 д.е. можно купить 1 ед зерна + траты на случайные события

"""

d['Казна'] = 100
d['Смута'] = 0
d['Народ'] = 10
d['Земля'] = 10
d['Зерно'] = 10

print(c)


def stats(dicti):
    """статы"""
    for el in dicti:
        print(el, '-', dicti.setdefault(el))


def default_changes():
    d['Казна'] = d['Казна'] + d['Народ']
    d['Зерно'] = d['Зерно'] - d['Народ'] + d['Земля']
    stats(d)


def moves():
    print('Что хотите сделать в этом году, милорд?')
    print('0 - Ничего')
    print('1 - Покупка зерна')
    print('2 - Улучшить свой рейтинг среди жителей')
    print('3 - Исследование земель')
    a = list(input('Введите цифры действий: '))
    res = []
    for el in a:
        try:
            el = int(el)
            if 0 <= el <= 3:
                res.append(el)
            else:
                print('Милорд, такого мы пока сделать не можем')
                moves()
        except ValueError:
            print('Я вас не понял, милорд')
            moves()
    return res


def pokupka_zerna():
    print('Сколько хотите купить зерна, милорд? (1 д.е. = 1 з)')
    try:
        a = int(input())
        dengi = d['Казна']
        if a > dengi:
            print('Вы не можете столько купить, милорд')
        elif a < 0:
            print('Вам стоило лучше изучать математику, милорд')
        else:
            d['Казна'] = d['Казна'] - a
            d['Зерно'] = d['Зерно'] + a
    except ValueError:
        print('Я вас не понял милорд')


def issledovanie_zemel():
    print('Сколько хотите потратить на исследования? ( 1 д.е. - 50% шанс получения 1 земли)')


print('Начало ( 0 год ):')
stats(d)
c = 0
while True:
    c += 1
    print(c, 'ГОД:')
    default_changes()
    decision = moves()
    for number in decision:
        if number == 0:
            print('Как скажете, милорд')
        if number == 1:
            pokupka_zerna()

