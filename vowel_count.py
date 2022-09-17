def get_count(sentence):
    volwes = "aeiou"
    newsentence = sentence.lower()

    sayac = 0
    for i in newsentence:
        
        if  i  in volwes:
            sayac += 1
    return sayac