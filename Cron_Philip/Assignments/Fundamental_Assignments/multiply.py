def multiply( indexlist, multiplier ):
    result = []
    for index in range(len(indexlist)):
        result.append(multiplier * indexlist[index])

    return result

a = [2,4,10,16]
b = multiply(a, 5)
print b
