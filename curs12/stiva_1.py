"""
farfurie_3
farfurie_2
farfurie_1
First In Last Out => FILO (LIFO)
Last In First Out -> LIFO

om1, om2, om3
First In First Out -> FIFO
"""

stiva = []


def push(val):
    stiva.append(val)


def pop():
    value = stiva[-1]
    stiva.pop()
    return value


push(3)
push(2)
push(1)
print(stiva)
print(pop())
print(pop())
print(pop())
