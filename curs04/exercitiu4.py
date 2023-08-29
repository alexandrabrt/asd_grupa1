"""sa se scrie o functie care sa returneze True in cazul in care primul si ultimul element dintr-o lista sunt la fel.
Altfel, returnati False."""

lista = [12, 34, 23, 5, 1]  # False
lista_2 = [12, 3, 56, 2, 12]  # True
lista_3 = [1]


def verify_elements(element_list: list) -> bool:
    if len(element_list) > 1:
        if element_list[0] == element_list[-1]:
            return True
    return False


print(verify_elements(lista))
print(verify_elements(lista_2))
print(verify_elements(lista_3))
