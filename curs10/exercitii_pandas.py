import pandas

# a = [1, 7, 2]
# variabila = pandas.Series(a, index=["x", "y", "z"])
# print(variabila)

# taskuri = {"ziua1": 2, "ziua2": 4, "ziua3": 1}
# variabila = pandas.Series(taskuri, index=["ziua2", "ziua3"])
# print(variabila)

taskuri = {
    "zile": [2, 4, 5],
    "durata": [50, 40, 45]
}

variabila = pandas.DataFrame(taskuri, index=["ziua1", "ziua2", "ziua3"])
# print(variabila)
# print(variabila.loc["ziua1"])
# print(variabila.loc[[0, 1]])

df = pandas.read_csv('Exemplu.csv')
print(df)

