class Exemplu:
    counter = 0
    def __init__(self, val=3):
        self.first = val
        Exemplu.counter += 1
        # patru = 44
    def set_second(self, val):
        self.second = val

# proprietate -> first
# clasa -> Exemplu
# obiect -> obiect_1, obiect_2, obiect_3


obiect_1 = Exemplu(1)
# print(obiect_1.counter, 'linia 16')
obiect_2 = Exemplu(2)
# print(obiect_1.counter, 'linia 18')
# print(obiect_2.counter, 'linia 19')

# obiect_3 = Exemplu(4)
# print(obiect_1.first)
# print(obiect_1.__dict__)
# obiect_1.patru = 55
# print(obiect_1.patru)
# print(obiect_1.counter)
# print(Exemplu.first)
# print(Exemplu.counter)
# obiect_1.set_second(999)
# print(obiect_1.second)
# obiect_1.third = 3
# print(obiect_1.third)
# print(obiect_1.__dict__)
# print(obiect_2.second)
# print(obiect_2.__dict__)
# print(obiect_2.first)

# print(obiect_3.first)

"""Rudolph este o pisica mare care doarme toata ziua.
clasa -> pisica
obiect -> Rudolph
proprietate -> mare
activitate -> doarme"""


class Pisica:

    nr_picioare = 4
    nr_pisici = 0
    nr_vieti = 9

    def __init__(self, size="mare"):
        # self.__marime = size
        self.marime = size
        # self.nr_pisici += 1
        Pisica.nr_pisici += 1

    def mananca(self, tip_mancare):
        self.mancare = tip_mancare

    def accidentare(self):
        Pisica.nr_vieti -= 1
        # return Pisica.nr_vieti - 1


Rudolph = Pisica()
# print(Rudolph.marime)
Max = Pisica("mic")
# print(Max.nr_picioare)
# print(Pisica.nr_picioare)
# print(Max.nr_pisici)
Max.accidentare()
# Rudolph.accidentare()
# print(Max.nr_vieti)
# print(Pisica.nr_vieti)
# print()
# print(Rudolph.nr_pisici)
print(Max.__dict__)
print(Pisica.__dict__)
# print(Max._Pisica__marime)
Max.mananca("bobite")
# print(Max.mancare)
Max.mancare_extra = "pliculet"
Max.mancare_extra_2 = "peste"
# print(Rudolph.mancare)
# print(Max.__dict__)
# print(Rudolph.__dict__)
