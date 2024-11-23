class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_str = ", ".join([f"{p['naziv']} x {p['kolicina']}" for p in self.proizvodi])
        print(f"Naručeni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(lista):
    if not lista:
        print("Greška: Lista ne smije biti prazna!")
        return None
    
    if not isinstance(lista, list):
        print("Greška: Argument mora biti lista.")
        return None
    
    if not all(isinstance(p, dict) for p in lista):
        print("Greška: Svaki element u listi mora biti rječnik.")
        return None
    
    kljucevi = {"naziv", "cijena", "kolicina"}
    for p in lista:
        if not kljucevi.issubset(p.keys()):
            print(f"Greška: Proizvod {p} ne sadrži sve potrebne ključeve: {kljucevi}")
            return None
        
    nedostupno = [p for p in lista if p["kolicina"] <= 0]

    if nedostupno:
        [print(f"Proizvod {p.naziv} je nedostupan.") for p in nedostupno]
        return None
    
    ukupna_cijena = sum([p["cijena"] * p["kolicina"] for p in lista])

    return Narudzba(lista, ukupna_cijena)

narudzbe = []
