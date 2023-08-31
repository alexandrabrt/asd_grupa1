"""Scrieti un program care sa faca split dupa al n-lea element intr-o lista:

lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""
lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3


# def split_function(lista, nr):
#     result = []
#     for j in range(0, nr):
#         result.append(lista[j::nr])
#     return result


def split_function(lista, nr):
    return [lista[j::nr] for j in range(0, nr)]


print(split_function(lista_start, n))


# string = 'ana are mere'
# lista = []
# for i in string:
#     lista.append(i)
# lista = [i for i in string]
# lista_element = [1, 2, 3, 4, 5, 6]
# lista = []
# for i in lista_element:
#     if i % 2 == 0:
#         lista.append(i)
#     else:
#         lista.append(0)

# lista = [i for i in lista_element if i % 2 == 0]
# lista = [i if i % 2 == 0 else 0 for i in lista_element]
# print(lista)
