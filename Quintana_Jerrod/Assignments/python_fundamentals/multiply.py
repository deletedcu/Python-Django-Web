a = [2,4,10,16]

def multiply(arr, num):
    for element in range(0,len(arr)):
        arr[element] = arr[element]*num
    return arr
b = multiply(a, 5)
print b

'''
second attempt below

def multiply(list, num):
    for i in range (len(list)):
        list[i] = list[i] * 5
    print list
multiply(a, 5)
'''
