# 1
# i = 2
# while True:
#     if i % 3 == 0:
#         break
#     print(i)
#     i += 2

"""

a. 2
b. 2 4
c. 2 4 6 8 10 ...
d. ValueError
"""


# 2
# my_list = [1, 2, 3, 4]
# try:
#     x = my_list[3]
# except IndexError:
#     msg = 'Indexul nu a fost gasit'
#     print(msg)
# except NameError:
#     msg = 'Variabila nu a fost definita'
# else:
#     msg = 'exceptie'
#     print(msg)
# finally:
#     msg = 'Totul a mers perfect'
# print(msg)
"""
a. Variabila nu a fost definita!
b. Indexul nu a fost gasit!
c. Totul a mers perfect
"""

# 3
# dictionar = {"pisica": "pisica1", "caine": "caine1", "cal": "cal1"}
# dictionar["pisica"] = "pisica2"
# print(dictionar)
"""
a. [‘pisica2’, ‘caine1’, ‘cal1’]
b.{‘pisica’: ‘pisica1’, ‘caine’: ‘caine1’, ‘cal’: ‘cal1’}
c.[‘pisica’, ‘caine’, ‘cal’]
d.{'pisica': 'pisica2', 'caine': 'caine1', 'cal': 'cal1'}
"""

# 4
# planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
# flatten_planets = []
# for sublist in planets:
#     for planet in sublist:
#         if len(planet) < 6:
#             flatten_planets.append(planet)
# print(flatten_planets)
"""
a. ['Venus', 'Mars', 'Pluto']
b. ['V','e','n','u','s',  'M','a','r','s',  'P','l','u','t','o']
c. [5, 4, 5]
d. ['Venus', 'Earth', 'Mars', 'Pluto']
"""
