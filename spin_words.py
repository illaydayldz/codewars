def spin_words(sentence):
    newsentence = sentence.split(" ")

    for word in newsentence:
        if len(word) >=  5:
            newword =  word[::-1]
            sentence = sentence.replace(word,newword)
    return sentence