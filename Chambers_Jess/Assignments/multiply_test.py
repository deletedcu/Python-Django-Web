def multiply(a,b):
    length = len(a)
    array_new = []
    for i in range(0,length):
        array_new.append(a[i] * b)
    print array_new
    #
    # for x in a: #x= a value in the array
    #     array_new.append(x*b)
    # print array_new

multiply([2,4,10,16], 5)
