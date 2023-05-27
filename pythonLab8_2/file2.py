def lab4_1(list1):
    a = max(list1)
    c = list1.index(a)
    print("{0} {1} {2} {3}".format("Найбільший елемент списку:", a, "індекс", c))


def lab4_2(spisok):
    dictonary = {}
    for key, vals in spisok.items():
        dictonary[vals] = key
    return dictonary
