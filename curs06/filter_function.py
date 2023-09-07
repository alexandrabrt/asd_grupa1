list_1 = [1, 5, 4, 6, 8, 11, 3, 12]


# def filtrare(x):
#     lista_forloop = []
#     for i in x:
#         if i % 2 == 0:
#             lista_forloop.append(i)
#     return lista_forloop
# print(filtrare(list_1))

list_2 = list(filter(lambda x: x % 2 == 0, list_1))
print(list_2)


