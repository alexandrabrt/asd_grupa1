"""
utilizatorul cere de la tastatura 2 cifre si un operator (+, -, *, /)
"""
def definire_operator(counter_parametru):
    operator = input(f"Adauga {counter_parametru} numar tau: ")
    while operator.isdigit() is False:
        operator = input(f"Adauga {counter_parametru} numar: ")
    return operator


operator_1 = definire_operator("primul")
operator_2 = definire_operator("al doilea")
# operator_1 = input("Adauga primul numar: ")
# while operator_1.isdigit() is False:
#     operator_1 = input("Adauga primul numar: ")
#
#
# operator_2 = input("Adauga al doilea numar: ")
# while operator_2.isdigit() is False:
#     operator_2 = input('Adauga al doilea numar: ')


operand = input("Adauga operandul (+, -, *, /): ")

# while operand not in ['+', '-', '*', '/']:
#     operand = input("Adauga operandul (+, -, *, /): ")
while operand not in '+-*/' or len(operand) != 1:
    if len(operand) != 1:
        print('Ai introdus mai multe caractere')
    operand = input("Adauga operandul (+, -, *, /): ")

if operand == '+':
    rezultat = int(operator_1) + int(operator_2)
elif operand == '-':
    rezultat = int(operator_1) - int(operator_2)
elif operand == '*':
    rezultat = int(operator_1) * int(operator_2)
else:
    while operator_2.isdigit() is False or int(operator_2) == 0 :
        operator_2 =  input(f'Ai introdus valoarea {operator_2}. Adauga al doilea numar: ')
    rezultat = int(operator_1) / int(operator_2)

print(f"{operator_1} {operand} {operator_2} = {rezultat}")

