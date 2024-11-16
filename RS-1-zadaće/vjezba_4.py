broj = 0
while broj < 5:
    broj +=2
    print(broj)

"""Ispis:
2
4
6"""


broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1

"""Ova je petlja beskonačna jer se u svakoj iteraciji vrijednost varijable
broj poveća za 1 i nakon ispisa smanji za 1 tako da je uvijek vrijednost 0,
odnosno varijabla je nepromijenjena i petlja nema kraj."""


broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
      broj += 2

"""Kada broj postane manji od 5, povećanje vrijednosti (broj += 2) odgađa smanjenje prema 0.
Petlja ne završava u očekivanom broju koraka. Ovo uzrokuje beskonačnu petlju jer broj nikada neće biti 0."""