# Lambda izrazi

# 1.
#def kvadriraj(x):
#    return x ** 2

kvadriraj = lambda x: x ** 2
print(kvadriraj(-3))

# 2.
#def zbroji_pa_kvadriraj(a, b):
#   return (a + b) ** 2

zbroji_pa_kvadriraj = lambda a, b: (a + b) ** 2
print(zbroji_pa_kvadriraj(4, 5))

# 3.
#def kvadriraj_duljinu(niz):
#    return len(niz) ** 2

kvadriraj_duljinu_izraza = lambda niz: len(niz) ** 2
print(kvadriraj_duljinu_izraza("Niz."))

# 4.
#def pomnozi_i_potenciraj(x, y):
#    return (y * 5) ** x

pomnozi_i_potenciraj = lambda x, y: (y * 5) ** x
print(pomnozi_i_potenciraj(3, 2))

# 5.
#def paran_broj(x):
#    if x % 2 == 0:
#        return True
#    else:
#        return None

paran_broj = lambda x: True if x % 2 == 0 else None
print(paran_broj(1))