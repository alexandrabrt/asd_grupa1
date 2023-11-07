class Dog:

    legs_no = 4

    def __init__(self, name="Ben"):
        self.name = name

    def change_name(self, redenumire):
        self.name = redenumire
        return self.name

    def __str__(self):
        return str(self.name)


obiect_1 = Dog("Rex")
obiect_2 = Dog(123)
print(obiect_2)
# print(obiect_1.name)
# print(obiect_1.legs_no)
# print(Dog.legs_no)
# obiect_1.legs_no = 3
# Dog.legs_no = 2
# print(obiect_1.legs_no, obiect_1.name)
# print(obiect_2.legs_no, obiect_2.name)
# print(Dog.legs_no)
# print(obiect_1.change_name("Catel2"))
