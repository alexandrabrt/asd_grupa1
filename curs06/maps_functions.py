list_1 = [1, 5, 4, 6, 8, 11, 3, 12]


# def iterare(x):
#     lista_noua = []
#     for i in x:
#         lista_noua.append(i*2)
#     return lista_noua


# print(iterare(list_1))

def inmultire(x):
    return x * 2


# list_3 = list(map(lambda x: x * 2, list_1))
# list_3 = list(map(inmultire, list_1))
# print(list_3)

numere = (1, 2, 3, 4)
rezultat = set(map(lambda x: x + x, numere))
print(rezultat)
