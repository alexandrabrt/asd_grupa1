# class Clasa:
#
#     def __init__(self, variabila_instanta):
#         self.__variabila_instanta = variabila_instanta
#
#     @staticmethod
#     def metoda_statica():
#         return "Aceasta este o metoda statica"
#
#
# obiect = Clasa(20)
# print(obiect.metoda_statica())
#
# print(Clasa.metoda_statica())



# class Masina:
#
#     numar_masini = 0
#
#     def __init__(self, marca, model):
#         self.marca = marca
#         self.model = model
#         Masina.numar_masini += 1
#
#     # def afiseaza_numar_masini(self):
#     #     return f"Numarul total de masini: {self.numar_masini}"
#
#     @classmethod
#     def afiseaza_numar_masini(cls):
#         return f"Numarul total de masini: {cls.numar_masini}"
#
#
# masina1 = Masina("Dacia", "1310")
# masina2 = Masina("Trabant", "222")

# print(masina1.numar_masini)
# print(masina1.afiseaza_numar_masini())
# print(Masina.afiseaza_numar_masini())


"""getteri, setteri, deleteri"""
#
class Persoana:

    def __init__(self, nume, varsta):
        self.__nume = nume
        self.__varsta = varsta

    def get_nume(self):
        return self.__nume

    def set_nume(self, nume_persoana):
        return nume_persoana

    def get_varsta(self):
        return self.__varsta

    def set_varsta(self, varsta_persoana):
        self.__varsta = int(varsta_persoana)
        return self.__varsta


persoana1 = Persoana("Ana", 12)

print(persoana1.get_nume())
print(persoana1.get_varsta())

persoana1.set_varsta("20")
print(type(persoana1.get_varsta()))
