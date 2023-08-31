"""se da un cuvant de la tastatura. sa se indice cate vocale si cate consoane contine."""

string = input("Adauga un cuvant: ")


def nr_vocale(word: str) -> (int, int):
    vocale = 'aeiou'
    counter_vocale, counter_consoane = 0, 0
    for i in word:
        if i in vocale:
            # counter_vocale = counter_vocale + 1
            counter_vocale += 1
        elif i.isalpha():
            # counter_consoane = counter_consoane + 1
            counter_consoane += 1
    return counter_vocale, counter_consoane


print(nr_vocale(string))




