def binary_array_to_number(arr):
    
    arr2 = arr[::-1]
    j = 0
    islem = 0
    for i in arr2:
        islem +=  i * ( 2 ** j)
        j +=1
        
    return islem