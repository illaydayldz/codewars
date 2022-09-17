def highest_rank(arr):
    counter = 0 
    num = arr[0]
    for number in arr:
        numberCount = arr.count(number)
        if numberCount > counter:
            counter = numberCount
            num = number

        if numberCount == counter:
            if number > num:
                counter = numberCount
                num = number
    return num 