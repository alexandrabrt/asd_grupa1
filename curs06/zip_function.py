lista_intregi = [1, 2, 3, 4, 5, 6, 7]
lista_stringuri = ['unu', 'doi', 'trei', 'patru', 'cinci', 'sase', 'sapte']
lista_3 = [9, 8, 3, 5, 6, 3]

rezultat = list(zip(lista_intregi, lista_stringuri, lista_3))
print(rezultat)

# cnp = '12344567'
# cifra = '9875899'
# suma = 0
# for i in zip(list(cnp), list(cifra)):
#     suma = suma + int(i[0]) * int(i[1])
# print(suma)
