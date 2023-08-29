"""scrieti un program care sa extraga inversul dintr-un nr.
Exemplu: 7536 trebuie afisati 6 3 5 7"""

from exercitiu1 import add_input


def invers() -> str:
    value = add_input("Adauga nr: ")
    return ' '.join(str(value)[::-1])
#     lista = []
#     for i in str(value):
#         lista.insert(0, i)
#     return ' '.join(lista)


print(invers())
