# Comprehension sintaksa

# 1.
parni_kvadrati = [x ** 2 for x in range(20, 51) if x % 2 == 0]
print(parni_kvadrati) # [400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 
#                        1936, 2116, 2304, 2500]

# 2.
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", 
"pjesma", "otorinolaringolog"]
duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if "a" in rijec]
print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]

# 3.
kubovi = [{x: x ** 3} if x % 2 != 0 else {x: x} for x in range(1, 11)]
print(kubovi) # [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9: 
#                 729}, {10: 10}]

# 4.
import math
korijeni = {x: round(math.sqrt(x), 2) for x in range(50, 500, 50)}
print(korijeni) # {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32, 
#                  350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}

# 5.
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
zbrojeni_bodovi = [{student["prezime"]: sum(student["bodovi"])} for student in studenti]
print(zbrojeni_bodovi) # [{'Ivić': 152}, {'Marković': 127}, {'Anić': 55}, {'Petrić': 362}, 
#                         {'Ivić': 236}, {'Matić': 266}]