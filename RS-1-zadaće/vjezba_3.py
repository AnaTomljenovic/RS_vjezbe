import random

tajni_broj = random.randint(1, 100)

broj_je_pogoden = False
broj_pokusaja = 0

print("Pogodite broj između 1 i 100!")

while not broj_je_pogoden:
    try:
        pretpostavka = int(input("Unesite svoj pretpostavljeni broj: "))
        broj_pokusaja += 1
        if pretpostavka < tajni_broj:
            print("Vaš broj je manji od traženog.")
        elif pretpostavka > tajni_broj:
            print("Vaš broj je veći od traženog.")
        else:
            print(f"Bravo, pogodili ste u {broj_pokusaja} pokušaja!")
            broj_je_pogoden = True
    except:
        print("Molim unesite cijeli broj.")