def recursive(n):
    if(n < 10):
        return n

    nAsString = str(n)
    total = 0
    for number in nAsString:
        total += int(number)

    return recursive(total)

def digital_root(n):
    return recursive(n)