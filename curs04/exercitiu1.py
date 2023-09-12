"""Se cer 2 nr intregi de la tastatura. Sa se calculeze produsul daca produsul dintre cele 2 numere este
mai mic sau egal cu 1000, altfel, sa se returneze suma acestora."""
# input_1 = input("Alege primul nr: ")
# while not input_1.isnumeric():
#     input_1 = input("Alege primul nr: ")
#
# input_2 = input("Alege al doilea nr: ")
# while not input_2.isnumeric():
#     input_2 = input("Alege al doilea nr: ")


def add_input(text_value: str) -> int:
    input_value = input(text_value)
    while not input_value.isnumeric():
        input_value = input(text_value)
    return int(input_value)

# print('tra la la la')


def product_or_sum() -> str:
    input_1 = add_input("Alege primul nr: ")
    input_2 = add_input("Alege al doilea nr: ")
    rezultat = input_1 + input_2
    text = f"Suma este: {rezultat}"

    if (rezultat := input_1 * input_2) and rezultat <= 1000:
        text = f"Produsul este: {rezultat}"
    return text
    # print(text)


# x = product_or_sum()
# print(x)
# print(product_or_sum())
if __name__ == '__main__':
    print(product_or_sum())
# varianta 1

# input_1 = add_input("Alege primul nr: ")
# input_2 = add_input("Alege al doilea nr: ")
#
#
# def product_or_sum(first_input: int, second_input: int) -> str:
#     rezultat = first_input + second_input
#     text = f"Suma este: {rezultat}"
#
#     if (rezultat := first_input * second_input) and rezultat <= 1000:
#         text = f"Produsul este: {rezultat}"
#     return text


# print(product_or_sum(input_1, input_2))



