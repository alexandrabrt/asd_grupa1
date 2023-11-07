# def decorator_simplu(functie_decorata):
#     print(f"Apelam functia {functie_decorata.__name__}")
#     # return True
#
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"
#
#
# @decorator_simplu
# def functie_complexa():
#     return "Noapte buna"

# print(functie_simpla())

# def decorator_depozit(functie_decorata):
#     def ambalaj_metoda(parametru_functie):
#         print(f"Ambalam produse din {functie_decorata.__name__} care contine cartea {parametru_functie}")
#         return functie_decorata(parametru_functie)
#     return ambalaj_metoda
#
#
# @decorator_depozit
# def impachetare_carti(nume):
#     return nume


# @decorator_depozit
# def impachetare_perne(tip_perna):
#     return "perne"

# print(impachetare_carti("Ion"))
# print(impachetare_perne("fulgi"))
# def decorator_depozit(parametru_decorat):
#     def ambalaj(functia_decorata):
#         def ambalaj_intern(denumire_carte):
#             print(f"Ambalam produse din {functia_decorata.__name__} cu material {parametru_decorat} care contine cartea {denumire_carte}")
#             return functia_decorata(denumire_carte)
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit("hartie")
# def impachetare_carti(nume):
#     return nume


# print(impachetare_carti("Ion"))



# def decorator_depozit(parametru_decorat):
#     def ambalaj(functia_decorata):
#         def ambalaj_intern(*denumire_carte):
#             print(f"Ambalam produse din {functia_decorata.__name__} cu material {parametru_decorat} care contine cartea {denumire_carte}")
#             return functia_decorata(denumire_carte)
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozit("hartie")
# def impachetare_carti(*nume):
#     return nume
#
#
# @decorator_depozit("hartie")
# def impachetare_2_carti(autor):
#     return autor

# print(impachetare_2_carti("Marin sorescu"))
# print(impachetare_2_carti("Marin sorescu", "Marin preda"))
# print(impachetare_carti("Ion", "Baltagul"))

import time, datetime

def calculeaza_timpul(functia_decorata):
    def functie_interioara(*param):
        inceput = time.time()
        data_inceput = datetime.datetime.now()
        suma = functia_decorata(*param)
        sfarsit = time.time()
        data_sfarsit = datetime.datetime.now()
        print(f"Ora inceput: {data_inceput} \nOra sfarsit: {data_sfarsit}\nTimp total de executie: {sfarsit - inceput}")
        return suma
    return functie_interioara


# @calculeaza_timpul
# def adunare(*args):
#     suma = 0
#     for i in args:
#         suma += i
#     return suma
# print(adunare(1, 2, 3))

@calculeaza_timpul
def adunare(number):
    suma = 0
    for i in range(number+1):
        suma += i
    return suma


print(adunare(100000000))


