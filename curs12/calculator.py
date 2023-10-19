class Calculator:

    def __init__(self, input_1, input_2, operator):
        self.number1 = input_1
        self.number2 = input_2
        self.op = operator

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


obiect = Calculator(1, 2, '+')
# obiect_2 = Calculator(1, 2, '-')
# obiect_3 = Calculator(1, 2, '*')
# obiect_4 = Calculator(1, 2, '/')
# obiect_5 = Calculator(1, 0, '/')
# print(obiect)
# print(obiect_2)
# print(obiect_3)
# print(obiect_4)
# print(obiect_5)

