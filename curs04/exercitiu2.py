"""scrieti un program care itereaza prin primele 10 numere. La fiecare iteratie afiseaza suma dintre iteratorul curent
si urmatorul iterator din sir."""
import exercitiu1


# from exercitiu1 import add_input as functie

# nr = input("Alege iteratorul final: ")
# while not nr.isnumeric():
#     nr = input("Alege iteratorul final: ")


def iterare():
    nr = exercitiu1.add_input("Alege iteratorul final: ")
    lista = []
    for i in range(1, int(nr) + 1):
        if i < int(nr):
            suma = 2 * i + 1
            lista.append(f"{i} + {i + 1} = {suma}")
    return '\n'.join(lista)


if __name__ == '__main__':
    print(iterare())

"""
    suma din sirul: de exemplu [12, 25, 36, 78, 1, 23, 5, 41]
    12 + 25
    25 + 36
    36 + 78
"""

# sir = [12, 25, 36, 78, 1, 23, 5, 41]


# def add_sir(sir_value: list) -> str:
#     text = []
#     if len(sir_value) > 1:
#         # for index, value in enumerate(sir):
#         for index in range(len(sir_value)):
#             if index < len(sir_value) - 1:
#                 suma = sir_value[index] + sir_value[index + 1]
#                 text.append(f"{sir_value[index]} + {sir_value[index + 1]} = {suma}")
#         return "\n".join(text)
#
#
# print(add_sir(sir))
