# def move_to_left(mylist, k):
#     if type(k) != int or k <= 0:
#         return "Character entered is not valid. Please enter a positive number."
#     if k > len(mylist):
#         return "Number entered is greater than the list length"
#     mylist = mylist[-k:] + mylist[:-k]
#     return mylist
#
# print(move_to_left([], 5))
#
# # lista = [1, 2, 3, 4, 5, 6, 7], k=3 => output de afisat: [5, 6, 7, 1, 2, 3, 4]
# # lista = [-1, -100, 3, 99], k=2 => output de afisat: [3, 99, -1, -100]
#
# # print(move_to_left([1, 2, 3, 4, 5, 6, 7], 3))
#
# #print(move_to_left([-1, -100, 3, 99], 2))
# Sa se scrie o functie care, pe baza unei liste de lungime n returneaza elementul majoritar dintr-un sir
# sub forma unui sir de caractere. In cazul in care exista mai multe elemente majoritare, sirul de caractere
# se separa prin virgula.
# Exemple:
# lista = [3, 2, 3] Output: 3
# lista = [2, 2, 1, 1, 1, 2, 2] Output: 2
# lista = [1, 2, 3, 1, 2] Output: 1, 2
def functie (lista):
    if len(lista) == 0:
        return "Nu exista element majoritar"
    dictionar = dict()
    for i in lista:
        if i in dictionar:
            dictionar[i] += 1
            # print(i)
        else:
            dictionar[i] = 1
            # print(i, "else")
    max_value = 0
    for j in list(dictionar.values()):
        # print(j)
        if j > max_value:
            max_value = j
    val_maxime = ""
    for key, value in dictionar.items():
        # print(key)
        # print(value)
        if value == max_value:
            # print(key)
            val_maxime = val_maxime + str(key) + ","
    # return max_value
    return val_maxime[:-1]
# print(functie([3, 2, 3, 3, 3]))
# print(functie([1, 2, 3, 1, 2]))
# print(functie([]))
print(functie([["Alfa", "BMW"], 2, 3, 283.5, ["Alfa", "BMW"]]))
# def functie (lista):
#     dictionar = dict()
#     for i in lista:
#         if i in dictionar:
#             dictionar[i] += 1
#             # print(i)
#         else:
#             dictionar[i] = 1
#             # print(i, "else")
#     max_value = max(list(dictionar.values()))
#     print(max_value, "valoare maxima")
#
#     val_maxime = ""
#     for key, value in dictionar.items():
#         # print(key)
#         # print(value)
#         if value == max_value:
#             # print(key)
#             val_maxime = val_maxime + str(key) + ","
#
#     # return max_value
#     return val_maxime[:-1]
#
# # print(functie([3, 2, 3, 3, 3]))
# # print(functie([1, 2, 3, 1, 2]))
# print(functie([]))
