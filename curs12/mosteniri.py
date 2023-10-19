# class Exemplu:
#     varia = 1
#
#     def __init__(self):
#         self.nume = 'Ana'
#         Exemplu.varia += 1
#         # self.varia = 'Maria'
#
#
# obiect = Exemplu()
# # print(obiect.varia)
# obiect_1 = Exemplu()
# # print(obiect_1.varia)
# # print(obiect.__dict__)
# # print(Exemplu.__dict__)
# print(hasattr(Exemplu, 'varia'))
# print(hasattr(Exemplu, 'nume'))
# print(hasattr(obiect, 'nume'))
# print(hasattr(obiect, 'varia'))


# class Super:
#     def __init__(self, name):
#          self.name = str(name).upper()
#
#     def __str__(self):
#         return f"My name is {self.name}"
#
#
# class Middle:
#
#     def __init__(self, prenume):
#         self.prenume = prenume
#         self.name = "Ana"
#
#
# class Sub(Middle, Super):
#
#     def __init__(self, name, prenume):
#         # Super.__init__(self, name)
#         # super().__init__()
#         super(Sub, self).__init__(name)
#         print(self.prenume, 'linia 34')
#         # self.name = name
#
#     def __str__(self):
#         return f"Numele meu este {self.name} {self.prenume}"


class Super:
    def __init__(self, atribut1, atribut2):
        self.name = 11
        self.atribut1 = atribut1
        self.atribut2 = atribut2
    def __str__(self):
        return f"My name is {self.name}"
class Middle:
    def __init__(self, atribut1):
        self.prenume = 12
        self.name = 13
        self.atribut1 = atribut1.upper()
class Sub(Middle, Super):

    def __init__(self, atribut1, atribut2):
        super().__init__(atribut1, atribut2)
    # def __str__(self):
    #     return f"Numele meu este {self.name} {self.prenume}"

obiect = Sub("Atribut100", "Atribut2")
print(obiect.atribut1, obiect.atribut2)


