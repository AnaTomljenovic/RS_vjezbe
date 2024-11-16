def count_vowels_consonants(tekst):
    vowels = ("aeiouAEIOU")
    
    num_vowels = 0
    num_consonants = 0

    for znak in tekst:
        if znak.isalpha():
            if znak in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return {'vowels': num_vowels, 'consonants': num_consonants}