"""Creati un program in care utilizatorul sa introduca o adresa de email de formatul
litere_sau_cifre@litere_sau_cifre.litere.
Validati acest sir de caractere si informati utilizatorul de raspuns. @ sau .(punct) trebuie sa exista o singura data
in sirul de caractere
-> trebuie sa contina @ si . o singura data
-> tot ce este inainte de . contine litere_sau_cifre, cu exceptia @
-> tot ce urmeaza dupa . contine doar litere
-> trebuie sa avem caracter scris inainte de @
-> trebuie sa avem caracter(e) scris(e) intre @ si .
-> trebuie sa avem minim 2 litere dupa .
ana123@ana321.ro
"""
adresa_de_email = input("Adauga adresa de email: ").lower()
while adresa_de_email.count('@') != 1 or \
        adresa_de_email.count('.') != 1 or \
        adresa_de_email.index('@') > adresa_de_email.index('.') or \
        adresa_de_email.split('@')[0].isalnum() is False or \
        adresa_de_email.split('@')[1].split('.')[0].isalnum() is False or \
        adresa_de_email.split('.')[1].isalpha() is False or \
        len(adresa_de_email.split('.')[1]) < 2:
    adresa_de_email = input(f"Adresa de email adaugata este '{adresa_de_email}'. Adauga alta adresa: ")
# count = len(adresa_de_email.split('@')) - 1
# count = 0
# for i in adresa_de_email:
#     if i == '@':
#         count = count + 1

