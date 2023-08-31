"""Realizati un program care sa gaseasca al doilea cel mai mic numar din lista.

list_1 = [-8, 1, 2, -2, 0] -> ec.: -2

list_2 = [1, 1, 0, 0, 2, -2, -2] -> ex.: 0

list_3 = [1, -1, 0, -9, 4, -5]

list_4 = [1, 4, 0, 23, 6, 34]"""

# list_1 = [-8, 1, 2, -2, 0]
# list_4 = [1, 4, 0, 23, 6, 34]
list_1 = [1, 1, 0, 0, 2, -2, -2]
# list_1 = [1, -1, 0, -9, 4, -5]
# list_1 = [1, -1, 0, -9, 4, -5]
# def min_number(lista):
#     lista = list(set(lista))
#     min_value = lista[0]
#     second_value = lista[-1]
#     for i in lista:
#         if min_value >= i:
#             min_value = i
#     for i in lista:
#         if min_value != i:
#             second_value = min_value
#     return second_value


def second_min_element(lista: list) -> int:
    lista = list(set(lista))
    min_val = lista[0]
    second_min_val = lista[-1]
    if len(lista) > 1:
        for i in lista:
            if i < min_val:
                second_min_val = min_val
                min_val = i
            elif i < second_min_val and i != min_val:
                second_min_val = i
    return second_min_val


print(second_min_element(list_1))



