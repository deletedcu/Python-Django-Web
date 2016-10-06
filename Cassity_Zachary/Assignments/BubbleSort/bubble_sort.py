import random
import time
b = []
for x in range(0,100):
    b.append(int(random.random() * 10000))
maximum = len(b) - 1
start_time = time.time()
for i in range(0,maximum):
    for j in range(0,maximum):
        if(b[j] > b[j+1]):
            t = b[j]
            b[j] = b[j+1]
            b[j+1] = t
    maximum = maximum - 1
print b
print("Time spent : %s seconds!"% (time.time() - start_time))
