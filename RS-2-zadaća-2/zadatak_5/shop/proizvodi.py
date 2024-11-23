class Proizvod():
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv} Cijena: {self.cijena} Količina: {self.kolicina}")

proizvodi = []

proizvodi.append(Proizvod("Čokolada", 1.79, 7))
proizvodi.append(Proizvod("Keksi", 2.49, 11))

def dodaj_proizvod(naziv, cijena, kolicina):
    proizvodi.append(Proizvod(naziv, cijena, kolicina))

dodaj_proizvod("Bomboni", 1.99, 4)

[proizvod.ispis() for proizvod in proizvodi]
