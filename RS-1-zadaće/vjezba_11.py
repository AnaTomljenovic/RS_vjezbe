def grupiraj_po_paritetu(lista):
    rezultat = {
        'parni': [broj for broj in lista if broj % 2 == 0],
        'neparni': [broj for broj in lista if broj % 2 != 0]
    }
    return rezultat