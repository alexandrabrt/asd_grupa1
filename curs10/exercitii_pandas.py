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

# df = pandas.read_csv('Exemplu.csv')
# print(df)

df = pandas.read_csv('date_test.csv')
df.fillna(0, inplace=True)
# dict_to_replace = {": ": 0, ":": 0}
# df.replace(dict_to_replace, inplace=True)
# df.replace(': ', 0, inplace=True)
# df.replace(':', 0, inplace=True)
# print(df.corr())
# print(df.describe())
# print(df)
# df.to_csv('test1.csv')
# import matplotlib.pyplot as plot
# df.plot(kind='scatter', x='AT', y='BE')
# df['AT'].plot(kind='hist')
# plot.show()
# print(df.head(2))
# print(df.tail(2))
# df.loc[2, 'AL'] = 45
# print(df.transpose())
# print(df.AL.tolist())
for item, row in df.iterrows():
    print(row)
