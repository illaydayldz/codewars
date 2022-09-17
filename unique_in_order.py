def unique_in_order(iterable):
    arr = []
    if len(iterable) != 0:
        arr.append(iterable[0])
        i = 0
        while i < len(iterable):
            if(arr[len(arr) - 1] != iterable[i]):
                arr.append(iterable[i])

            i += 1

    return arr