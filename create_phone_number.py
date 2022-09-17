def create_phone_number(n):
    
    listToStr = ''.join (map (str, n))

    partone ="(" + listToStr[:3]

    parttwo =  ") "+ listToStr[3:6]

    partthree = "-" + listToStr[6:10]
    
    result = (partone +  parttwo + partthree)
    
    return result