"""Scrieti un program ce va numara cate caractere are un sir de caractere dat de utilizator. Aceasta numarare sa se
realizeze cu ajutorul unui for fara a utiliza len(). La final afisati rezultatul"""
# sir = input("Adauga un sir de caractere: ")
count = 0
# for i in sir:
#     print(i)
#     count = count + 1 # count += 1
while count == 0:
    sir = input("Adauga un sir de caractere: ")
    for i in sir:
        print(i)
        count = count + 1
# print(f"Utilizatorul a introdus de la tastatura sirul '{sir}' care are lungimea {count}")
# print(f"Utilizatorul a introdus de la tastatura sirul \"{sir}\" care are lungimea {count}")
# print(f'Utilizatorul a introdus de la tastatura sirul "{sir}" care are lungimea {count}')
print(f"Utilizatorul a introdus de la tastatura sirul \'{sir}\' care are lungimea {count}")
# print("Utilizatorul a introdus de la tastatura sirul \"" + sir + "\" care are lungimea " + str(count))
