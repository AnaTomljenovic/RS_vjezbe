# verzija s for petljom
broj = int(input("Unesite broj za izračun faktorijela: "))

faktorijel = 1

for i in range(1, broj + 1):
    faktorijel *= i

print(f"Faktorijel broja {broj} je {faktorijel}.")

# verzija s while petljom
broj = int(input("Unesite broj za izračun faktorijela: "))

faktorijel = 1
trenutni = 1

while trenutni <= broj:
    faktorijel *= trenutni
    trenutni += 1

print(f"Faktorijel broja {broj} je {faktorijel}.")