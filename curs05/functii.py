def functie_suma(a: int, b: int, e: int = 1, *args, **kwargs) -> int:
    print(kwargs, type(kwargs))
    s = a + b + e
    for i in args:
        s += i
    for i in kwargs.values():
        s += i
    return s


# suma = functie_suma(1, 2, 3, 4, 5, 6, 7, 8)
# suma = functie_suma(2, 3, 4, c=3, d=4)
# suma = functie_suma(b=2, a=3, c=3, d=4)
# suma = functie_suma(c=3, d=4, b=2, a=3)
suma = functie_suma(2, 3, 4, 5, c=3, d=4)
print(suma)
