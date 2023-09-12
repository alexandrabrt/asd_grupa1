"""
r -> citim, nu adaugam, daca fisierul nu exista, apare eroare
w -> scriere, daca fisierul nu exista, il adauga, daca exista informatie in fisier, se rescrie
a -> scriere, daca exista ceva in fisier, adauga la final, daca fisierul nu exista, nu apare eroare
r+ -> scriere, citire, daca fisierul nu exista, apare eroare
"""
import io

# with open("data.txt", 'r'):
# with open("data1.txt", 'r') as item:
#     item.write("Hello\n")
#     item.write("Hello\n")
#     item.write('Hei\n')
# file = open('data.txt', 'r')
# try:
#     file.write('Hello')
# except io.UnsupportedOperation as error:
#     print(error)
#     file = open('data.txt', 'w')
#     file.write('Hello\n')
# finally:
#     file.close()

# with open('data.txt', 'r') as item:
#     try:
#         item.write('Hei')
#     except io.UnsupportedOperation as error:
#         print(error)
#         item = open('data.txt', 'w')
#         item.write('Hei\n')

# with open('data.txt', 'r') as file:
#     x = file.readlines()
#     print(x)
#     for line in x:
#         print(line)

# with open('data.txt', 'w') as file:
#     x = list(file)
#     print(x)
#     for line in x:
#         print(line)

with open('data.txt', 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break
        print(line)
