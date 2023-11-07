class Persoana:

    def __init__(self, nume, varsta):
        self.__nume = nume
        self.__varsta = varsta


    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume_persoana):
        self.__nume = nume_persoana

    @property
    def varsta(self):
        return self.__varsta

    @varsta.setter
    def varsta(self, varsta_persoana):
        self.__varsta = varsta_persoana


persoana1 = Persoana("Ana", 12)

print(persoana1.varsta)
persoana1.varsta = 20
print(persoana1.varsta)
