def good_vs_evil(good,evil):
    def islem(x):
        return x[0] * x[1]

    
    good, evil = map(int, good.split(' ')), map(int, evil.split(' '))
    good_total = sum(map(islem, zip(good, [1,2,3,3,4,10])))
    evil_total = sum(map(islem, zip(evil, [1,2,2,2,3,5,10])))
    if good_total > evil_total:
         return "Battle Result: Good triumphs over Evil"
    elif good_total < evil_total:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
         return"Battle Result: No victor on this battle field"