def obrni_rjecnik(rjecnik):
    obrnuti_rjecnik = {}
    for kljuc, vrijednost in rjecnik.items():
        obrnuti_rjecnik[vrijednost] = kljuc
    return obrnuti_rjecnik