# # print(dir(__builtins__))
# global a
a = 1
b = 2


class Exemplu:
    pass


if __name__ == '__main__':
    print(a, 'a')
#
#
# def functie(param1):
#     global a
#     print(a, 'inainte')
#     a = 2
#     print(a, 'in functie')
#     return param1
#
#
# def functie1():
#     global a
#     print(a, 'inainte in functie1')
#     a = 3
#     print(a, 'in functie1')
#     return True
#
#
# print(a, '14')
# functie1()
# print(a, 'a')
# functie(1)
# print(a, 'dupa functie1')


# def functie():
#     def functie1():
#         print('functie secundara', msg)
#     msg = 'Mesaj'
#     functie1()
#     msg = 'Mesaj1'
#     print(msg)

#
# def functie():
#     def functie1():
#         # global msg
#         # msg = 4
#         if msg == 'Mesaj':
#             print('Ana are mere')
#         # msg2 = msg
#         # msg = 4
#         print('functie secundara', msg)
#     msg = 'Mesaj'
#     functie1()
#     msg = 'Mesaj1'
#     print(msg)


# def functie():
#     print('Ana are pere')

# functie()
