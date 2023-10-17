class Stiva:

    def __init__(self):
        self.stiva = []

    def push(self, val):
        self.stiva.append(val)

    def pop(self):
        return self.stiva.pop()


obiect_1 = Stiva()
obiect_2 = Stiva()
obiect_2.push(4)
obiect_1.push(3)
obiect_1.push(2)
obiect_1.push(1)
print(obiect_1.stiva)
print(obiect_2.stiva)
print(obiect_1.pop())
print(obiect_2.pop())
