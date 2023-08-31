"""Realizati un program care sa creeze o lista, concatenand o lista data, cu nr. de la 1 la n
exemplu:
list_var = ['p', 's']
n = 5
result = ['p1', 's1', 'p2', 's2', 'p3', 's3', 'p4', 's4', 'p5', 's5']
"""
from exercitiu1 import add_input

input_value = input("Elementele listei sunt separate prin virgula: ")
list_var = input_value.split(',')
n = add_input("Adauga un nr intreg: ")


def concatenare(nr: int, lista: list) -> list:
    result = []
    for i in range(1, nr+1):
        for j in lista:
            result.append(f"{j}{i}")
    return result


print(concatenare(n, list_var))
