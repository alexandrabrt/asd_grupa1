class ClasaA:
    def __init__(self, atribut_A):
        self.atribut_A = atribut_A


class ClasaB:
    def __init__(self, atribut_B):
        self.atribut_B = atribut_B


class ClasaC(ClasaA, ClasaB):
    def __init__(self, atribut_A, atribut_B):
        super(ClasaA, self).__init__(atribut_B)  # Apelăm constructorul din ClasaA
        super(ClasaC, self).__init__(atribut_A)  # Apelăm constructorul din ClasaC


obiect_C = ClasaC("Valoare_B", "Valoare_A")
print(obiect_C.atribut_A)
print(obiect_C.atribut_B)
