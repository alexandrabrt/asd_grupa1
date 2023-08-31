" se da un string de la tastatura. sa se calculeze suma digitilor din acel string "

cuvant = input('Adauga un cuvant: ')


def suma_cifre(word: str) -> str:
    variabila = ''
    suma = 0
    for i in word:
        if i.isdigit():
            suma += int(i)
            variabila += i
    return f"{' + '.join(variabila)} = {suma}"


print(suma_cifre(cuvant))
