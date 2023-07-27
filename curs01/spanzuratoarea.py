# onomatopee
cuvant = 'onomatopee'.lower()
cuvant_de_ghicit = list(cuvant)
for index, valoare in enumerate(cuvant):
    if cuvant_de_ghicit[0] != valoare and cuvant_de_ghicit[-1] != valoare:
        cuvant_de_ghicit[index] = '_'
cuvant_de_afisat = ' '.join(cuvant_de_ghicit)
print(cuvant_de_afisat)
nr_total_vieti = 7
litere_incercate = set()
while nr_total_vieti > 0:
    litera = input("Alege o litera: ").lower()
    if len(litera) != 1:
        print("Te rog introdu un singur caracter")
        continue
    if not litera.isalpha():
        print('Nu ai voie decat litere')
        continue
    if litera in cuvant:
        for index, valoare in enumerate(cuvant):
            if litera == valoare:
                cuvant_de_ghicit[index] = litera
        cuvant_de_afisat = ' '.join(cuvant_de_ghicit)
        print(cuvant_de_afisat)
        if '_' not in cuvant_de_ghicit:
            print('Ai castigat')
            break
    else:
        if litera not in litere_incercate:
            nr_total_vieti -= 1 # nr_total_vieti = nr_total_vieti - 1
            if nr_total_vieti == 0:
                print(f'Ai pierdut! Cuvantul era: {cuvant}')
                break
            else:
                print(f'Nr vieti: {nr_total_vieti}')
            litere_incercate.add(litera)
        print(f"Lista literelor incercate este: {', '.join(litere_incercate)}")


