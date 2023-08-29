from exercitiu1 import add_input

"""Sa da de la tastatura un string. Sa se elimine caracterele din string pornind de la 0 pana la n,
unde n e dat si el de la tastatura"""


def split_value() -> str:
    string_input = input('Adauga un string: ')
    final_value = add_input("Adauga indexul final de eliminat: ")
    if len(string_input) <= final_value:
        final_value = add_input("Adauga indexul final de eliminat: ")
    return string_input[final_value:]


print(split_value())
