class Calculator:

    def __init__(self):
        self.number1 = self.verificare_numere(input("Insert number 1: "), 1)
        self.number2 = self.verificare_numere(input("Insert number 2: "), 2)
        self.op = self.verificare_operator(input("Insert operation sign: "))

    def verificare_numere(self, valoare_input, nr_input):
        while valoare_input.isdigit() is False:
            valoare_input = input(f"Insert number {nr_input}: ")
        return int(valoare_input)

    def verificare_operator(self, operator):
        while operator not in '*-+/' or len(operator) != 1:
            operator = input("Insert operation sign: ")
        return operator

    def adunare(self):
        return self.number1 + self.number2

    def scadere(self):
        return self.number1 - self.number2

    def inmultire(self):
        return self.number1 * self.number2

    def impartire(self):
        if int(self.number2) != 0:
            return self.number1 / self.number2
        return "Eroare"

    def calcul(self):
        if self.op == '+':
            return self.adunare()
        elif self.op == '-':
            return self.scadere()
        elif self.op == '*':
            return self.inmultire()
        return self.impartire()

    def __str__(self):
        return f"{self.number1} {self.op} {self.number2} = {self.calcul()}"


while True:
    obiect = Calculator()
    print(obiect)
    quit_q = input('Press Q to quit: ').lower()
    if quit_q == 'q':
        break
# obiect_2 = Calculator(1, 2, '-')
# obiect_3 = Calculator(1, 2, '*')
# obiect_4 = Calculator(1, 2, '/')
# obiect_5 = Calculator(1, 0, '/')
# print(obiect)
# print(obiect_2)
# print(obiect_3)
# print(obiect_4)
# print(obiect_5)

