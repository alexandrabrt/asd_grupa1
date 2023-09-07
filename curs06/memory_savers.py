# lambda
# def suma(a, b):
#     return a + b

# suma = lambda a, b, c: a + b + c

players = [{
    "first_name": "Ion",
    "last_name": "Barbu",
    "age": 23
    },
    {
        "first_name": "Pavel",
        "last_name": "Popescu",
        "age": 35
    },
    {
        "first_name": "Andrei",
        "last_name": "Liviu",
        "age": 12
    }]

sortare = sorted(players, key=lambda jucator: jucator['first_name'])
print(sortare)
