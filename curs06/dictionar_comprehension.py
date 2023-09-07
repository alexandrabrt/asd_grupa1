my_dict = {1: 'car', 2: 'bike'}


# dictionar = {}
# for i in range(1, 11):
#     dictionar[i] = i * i
# print(dictionar)
dictionar = {i ** 2: v for i, v in my_dict.items()}

# dictionar = {i: i * i for i in range(1, 11)}
print(dictionar)
