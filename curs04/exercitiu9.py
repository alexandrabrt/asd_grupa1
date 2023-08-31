"""Realizati un program care sa sorteze o lista de dictionare folosind functia Lambda.

models = [{'make':'Huawei', 'model':2, 'color':'Black'}, {'make':'Apple', 'model':'14', 'color':'Gold'},
        {'make':'Samsung', 'model': 7, 'color':'Blue'}]"""

#
# def suma(a, b):
#     return a + b

# suma = lambda a, b: a + b
# print(suma(1, 2))

models = [{'make': 'Huawei', 'model': 2, 'color': 'Black'},
          {'make': 'Apple',  'model': 14, 'color': 'Gold'},
          {'make': 'Apple',  'model': 14, 'color': 'Pink'},
          {'make': 'Samsung', 'model': 7, 'color': 'Black'}]
# sorted_models = sorted(models, key=lambda model: model['model'])
# print(sorted_models)


# def sortare(dict_list: list, key: str = 'color') -> list:
#     nr = len(dict_list)
#     lista = []
#     new_list = []
#     for i in range(nr):
#         lista.append(dict_list[i][key])
#     for i in sorted(list(set(lista))):
#         for j in dict_list:
#             if j[key] == i:
#                 new_list.append(j)
#     return new_list

def sortare(dict_list: list, key: str = 'color') -> list:
    nr = len(dict_list)

    lista = [dict_list[i][key] for i in range(nr)]
    # new_list = []
    # for i in sorted(list(set(lista))):
    #     for j in dict_list:
    #         if j[key] == i:
    #             new_list.append(j)
    new_list = [j for i in sorted(list(set(lista))) for j in dict_list if j[key] == i]
    # new_list = [j if j[key] == i else {} for i in sorted(list(set(lista))) for j in dict_list ]
    return new_list


print(sortare(models, 'color'))

