def brojanje_riječi(tekst):
    riječi = tekst.split()
    
    brojač = {}
    
    for riječ in riječi:
        if riječ in brojač:
            brojač[riječ] += 1
        else:
            brojač[riječ] = 1
    
    return brojač