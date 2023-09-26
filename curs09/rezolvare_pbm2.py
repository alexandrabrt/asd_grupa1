def functie1(lista: list) -> dict:
    dictionar = dict()
    for i in lista:
        if i in dictionar:
            dictionar[i] += 1
        else:
            dictionar[i] = 1
    max_value = 1
    for i in list(dictionar.values()):
        # print(i)
        if i > max_value:
            max_value = i
    value_maxima = ''
    for key, value in dictionar.items():
        if value == max_value:
            value_maxima = value_maxima + str(key) + ','
    return value_maxima[:-1]

print(functie1([1, 2, 3, 1, 2]))

#varianta 3

def functie1(lista: list) -> dict:
    dictionar = dict()
    for i in lista:
        if i in dictionar:
            dictionar[i] += 1
        else:
            dictionar[i] = 1
    max_value = max(list(dictionar.values()))
    # print(max_value, 'valoare maxima')
    for i in list(dictionar.values()):
        # print(i)
        if i > max_value:
            max_value = i
    value_maxima = ''
    for key, value in dictionar.items():
        if value == max_value:
            value_maxima = value_maxima + str(key) + ','
    return value_maxima[:-1]

print(functie1([1, 2, 3, 1, 2]))
