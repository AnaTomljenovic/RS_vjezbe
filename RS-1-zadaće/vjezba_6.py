for i in range(1, 2):
    print(i)

# Petlja nema smisla zato što ispisuje samo 1 broj (1).

for i in range(1, 10, 2):
    print(i)

# Ispisuje samo neparne brojeve jer je step 2:
# Ispis: 1,3,5,7,9

for i in range(10, 1, -1):
    print(i)

# Vrijednost se smanjuje za -1 pri svakom pokretanju.
# Ispis: 10,9,8,7,6,5,4,3,2