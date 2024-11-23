# Klase i objekti

# 1.
from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža

    def ispis(self):
        for atribut, vrijednost in self.__dict__.items():
          print(f"{atribut}: {vrijednost}")

    def starost(self):
        print(f"Starost:", datetime.now().year - self.godina_proizvodnje, "godine")

automobil = Automobil("Volvo", "XC60", 2020, 87000)

automobil.ispis()
automobil.starost()

# 2.
import math

class Kalkulator:
    def zbroj(self, a, b):
        return a + b

    def oduzimanje(self, a, b):
        return a - b

    def mnozenje(self, a, b):
        return a * b

    def dijeljenje(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Dijeljenje s 0 nije moguće."

    def potenciranje(self, a, b):
        return a ** b

    def korijen(self, a, b):
        if a < 0 and b % 2 == 0:
            return a ** (1 / b)
        else:
            return "Parni korijen negativnog broja ne može se izračunati."
        
# 3.
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]

for student in studenti_objekti:
    print(f"{student.ime} {student.prezime}, Godine: {student.godine}, Ocjene: {student.ocjene}")

for student in studenti_objekti:
    print(f"Prosječna ocjena studenta {student.ime} {student.prezime}: {student.prosjek()}")

najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())
print(f"Najbolji student je {najbolji_student.ime} {najbolji_student.prezime}.")

# 4.
class Krug():
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return round(2 * self.r * math.pi, 2)
    
    def povrsina(self):
        return round(self.r ** 2 * math.pi)
    
krug = Krug(7)

print(krug.opseg())
print(krug.povrsina())

# 5.
class Radnik():
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Povećanje plaće radnika {radnik.ime} za {povecanje}.")

radnik = Radnik("Ivan Ivanović", "voditelj", 1700)
manager = Manager("Lucija Lucić", "menadžer", 2100, "Financije")

radnik.work()
manager.give_raise(radnik, 100)