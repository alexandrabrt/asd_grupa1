dictionar = {"cheia1": 1, "cheia2": 2, 3: "valoare3", "cheia2bis": 2}
# print(type(dictionar))
# print(dictionar.keys())
# print(dictionar.values())
# print(dictionar.items())
# print(dictionar['cheia1'])
# print(dictionar['cheia11'])
# print(dictionar.get('cheia11', "Nu exista valoarea"))
# print(dictionar.get('cheia1', "Nu exista valoarea"))
# print(dictionar)
# dictionar['cheia11'] = "valoare"
dictionar.update({"cheia11": "valoare", "cheia12": 12})
# print(dictionar.pop("cheia11"))
# dictionar.popitem()
dictionar['cheia11'] = 'alfabet'
print(dictionar)
