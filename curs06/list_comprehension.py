my_numbers = [1, 2, 4, 5]


def ridicare_la_patrat(lista_elemente):
    lista_noua = []
    for i in lista_elemente:
        if i % 2 == 0:
            lista_noua.append(i ** 2)
        elif i % 3 == 0:
            lista_noua.append(i ** 3)
        else:
            lista_noua.append('-')
    return lista_noua


# print(ridicare_la_patrat(my_numbers))

# lista_noua = [i ** 2 for i in my_numbers if i % 2 == 0]
lista_noua = [i ** 2 if i % 2 == 0 else '-' for i in my_numbers]
print(lista_noua)
