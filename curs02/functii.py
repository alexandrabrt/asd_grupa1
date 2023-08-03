def functie(a: int, b: int = 5) -> (int, int):
    """
    :param a: primul parametru de intrare
    :param b: al doilea parametru de intrare
    :return: suma a doua numere, diferenta a doua numere
    """
    return a + b, a - b
    # print("suma")


suma, diferenta = functie(3, b=6)

print(suma, diferenta)
