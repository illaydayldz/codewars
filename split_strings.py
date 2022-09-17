def solution(s):
    arr = []
    i = 0
    while i < len(s):

        if(i % 2 == 0):
            substring = s[i:i+2]
            if(len(substring) == 1):
                substring += "_"
            arr.insert(i, substring)

        i += 1
    
    return arr