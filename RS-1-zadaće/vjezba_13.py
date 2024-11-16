# 1.
def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

# 2.
def maks_i_min(lista):
    maksimum = lista[0]
    minimum = lista[0]
    for broj in lista:
        if broj > maksimum:
            maksimum = broj
        if broj < minimum:
            minimum = broj
    return (maksimum, minimum)

# 3.
def presjek(skup_1, skup_2):
    rezultat = {element for element in skup_1 if element in skup_2}
    return rezultat