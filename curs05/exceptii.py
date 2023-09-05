value = input('Introdu un nr: ')
try:
    b = int(value)
    a = None
    variabila = None
    lista = [0, 1, 2]
    if a is not None:
        raise NameError
    elif lista[3] == 2:
        raise IndexError
except (ValueError, IndexError) as e:
    print('Ai introdus un string')
    value = input('Introdu un nr: ')
    print(type(e).__name__)
    if type(e).__name__ == 'IndexError':
        print('IndexError')
    elif type(e).__name__ == 'ValueError':
        print('ValueError')
    # variabila = 5
except NameError:
    print('Nu ai declarat variabila')
# except IndexError:
#     print('Exceptie de index')
except Exception:
    print('Alta exceptie')
else:
    print('Nu avem exceptie')
finally:
    print('Se executa oricum')
print(variabila)

