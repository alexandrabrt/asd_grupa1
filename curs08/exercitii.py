# 1
# x = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'a': 4,
#     'd': 5
# }
# print(x['a'])


# 2
# x = list(range(1, 20))
# x = [i for i in x if i % 2 == 0]
# print(x)


# 3
# def a(param):
#     # param[4] = 'd'
#     param.update({4: 'd'})
#     return param

# x = dict()
# x.update({
#     1: 'a',
#     2: 'b',
#     3: 'c'
# })

# x = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }
# print(type(x))
#
# y = a(x)
# print(y)


# 4
# def functie1(lista_cuvinte):
#     lista = []
#     for n in lista_cuvinte:
#         lista.append((len(n), n))
#     lista.sort()
#     return lista[-1][0], lista[-1][1]
#
#
# rezultat = functie1(['pip', 'Exercitiu', 'Python', 'abecedar', 'masa'])
# print(rezultat)
# print(rezultat[1], rezultat[0])

# x = [('3', 'pip'), ('4', 'masa'), ('6', 'Python'), ('8', 'abecedar'), ('9', 'Exercitiu')]
# x.sort()
# print(x)


# 5
# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y+1]
#
#
# lista = [1, 2, 3]
# print(functie(lista))


# 6
# my_tuple = (1, 10, 100)
# t2 = my_tuple * 3
# print(len(t2))
# (1, 10, 100, 1, 10, 100, 1, 10, 100)
# Error
# 9
# 0

# 7
# def functie1():
#     # global var
#     var = 40
#     print('Variabila este definita?', var)
#
#
# def functie2():
#     print('Variabila este definita?', var)


# global var
# var = 30
# functie2()
# print(var)
# # print(functie1())
# functie1()
# # var = 50
# print(var)

"""
a. Variabila este definita? 30
b. Variabila este definita? 30
    None
    30
c. Error
d. Variabila este definita?

"""
# 8
# x = 10
# while x > 1:
#     # print(x)
#     # continue
#     x -= 1
#     # print(x)
#     continue
#     # if x == 3:
#     #     continue
#
# print(x)
"""
a. x = [1, 2, 3]
b. 1
c. 9
8
7
6
5
4
3
2
1 
d. Infinite loop
"""


# 9
# my_var = ['a', 'b', {'x': 1, 'z': {'key': 30, 'key': 40}, 'w': 3}, 10]
# print(my_var[2]['key'])
# print(my_var[2].get('key', 40))
# print(my_var)
# print(my_var['key'])
# print(my_var[2]['z']['key'])
"""
Cum afisezi valoarea 30 din structura urmatoare?
a. my_var[2]['key']
b. my_var['key']
c. my_var[2]['z']['key']

"""
# def inmultire(x):
#     return x * 2
#
# list_1 = [1, 5, 4, 6, 8, 11, 3, 12]
#
# list_3 = list(map(inmultire, list_1))
# print(list_3)


# lista_intregi = [1, 2, 3, 4, 5, 6, 7]
# lista_stringuri = ['unu', 'doi', 'trei', 'patru', 'cinci', 'sase', 'sapte']
# lista_3 = [9, 8, 3, 5, 6, 3]
#
# rezultat = list(zip(lista_intregi, lista_stringuri, lista_3))
# print(rezultat)
# for i in rezultat:
#     print(i)


# 10
# x = ['ab', 'cd', 'ed']
# for i, v in enumerate(x):
#     x[i] = v.title()
#
# print(x)

"""
a. ['ab', 'cd', 'ed']
b. none of the mentioned
c. [‘Ab’, ‘Cd’, 'Ed']
d. ['Ab', 'cd', 'ed']

"""


# 11

# i = 6
# while True:
#     if i // 3:
#         break
#     print(i)
#     i += 3

"""
a. 2 4 6 8 10 …
b. 2
c. error
d. Infinite loop

"""

# 12
# try:
#     i = int('Hello')
# except Exception as e:
#     print(e)

"""
a. None
b. Eroare
c. Hello!
d. “Hello!”
"""

# 13
# lista = [10 ** ex for ex in range(6)]
# print(lista)

"""
a. [1, 10, 100, 1000, 10000, 100000]
b. [0, 1, 2, 3, 4, 5]
c. 0, 1, 2, 3, 4, 5
d. Eroare

"""

# 14
# lista1 = list(set([1, 3, 2, 3, 4, 5, 6]))
# print(lista1)
# print(lista1[1, 5])
# print(slice(1, 5, 3))
# print(lista1[1:-2])
# del lista1[1:5]
# print(lista1)

# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(1, 2)
# print(a[x])
# print(a[1:2])
"""
a. [1 3 2 4 5 6]
b. [1 5]
c. [1]
d. [1 6]

"""
