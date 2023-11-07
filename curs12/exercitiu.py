
class Animal:

    animal = 2
    # patruped = 2

    def __init__(self, varsta):
        self.varsta = varsta


class Patruped(Animal):

    # patruped = 1

    def __init__(self, name, varsta):
        super().__init__(varsta)
        self.name = name


class Carnivor:

    patruped = 3

    def __init__(self, tip_carne):
        self.carne = tip_carne


class Caine(Patruped, Carnivor):

    nr_picioare = 4
    patruped = 5

    def __init__(self, name, varsta, tip_carne):
        Patruped.__init__(self, name, varsta)
        Carnivor.__init__(self, tip_carne)
        self.tip_carne = carne

    #     Animal.__init__(self, varsta)
    #     self.name = name
        # self.varsta = varsta
        # self.nr_picioare = 3

    def __str__(self):
        # return f"{self.name}"
        return self.name

    def botez_nou_caine(self, name):
        self.name = name
        return self.name


exemplu_caine = Caine("Rex", 2, "porc")
# print(exemplu_caine.varsta)
# print(exemplu_caine.name)
# print(exemplu_caine.carne)
# print(exemplu_caine.__dict__)
# print(exemplu_caine.patruped)
print(exemplu_caine.tip_carne)
# print(exemplu_caine.nr_picioare)
# print(Caine.nr_picioare)
# print(exemplu_caine.__dict__)
# print(Caine.__dict__)
# print(exemplu_caine.botez_nou_caine("Ben"))
# print(exemplu_caine)
