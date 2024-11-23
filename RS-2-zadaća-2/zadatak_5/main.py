# Moduli i paketi

from shop import proizvodi as pro
from shop import narudzbe

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in proizvodi:
    pro.dodaj_proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])
    p = pro.Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])
    p.ispis()

narudzba = narudzbe.napravi_narudzbu(lista=proizvodi)
narudzba.ispis_narudzbe()
