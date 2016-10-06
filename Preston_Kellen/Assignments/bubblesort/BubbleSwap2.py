def bubble_swap(swapstring):
    for desc in range(len(swapstring) -1, 0, -1):
        for x in range(desc):
            if swapstring[x] > swapstring[x+1]:
                (swapstring[x], swapstring[x+1]) = (swapstring[x+1], swapstring[x])
    return swapstring

swapstring = bubble_swap([8,4,2,9,5,6,7,6])

print swapstring
