ex = [6,5,3,1,8,7,2,4]
ex2 = [1,2,3,4,5,6,7,8]
import random
import time
new = []
for index in range(0,100):
    number = round(random.random() *1000)
    new.append(number)

def bubble(arr):
    start_time = time.time()
    length = len(arr)
    while (length > 0):
        for i in range (len(arr)):
            if (i == (len(arr) - 1)):
                break
            elif (arr[i] > arr[i + 1]):
                temp = arr[i]
                arr [i] = arr[i + 1]
                arr[i + 1] = temp
        length -= 1
    print arr
    print ("--- %s seconds ---" % (time.time() - start_time))
bubble(ex)
bubble(new)
