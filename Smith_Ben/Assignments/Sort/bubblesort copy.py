import random
import time
b = []
for x in range(0,100):
	b.append(int(random.random()*10000))

maximum = len(b) - 1

for i in range(0,maximum):
	start_time = time.time()
	for j in range(0,maximum):
		if b[j] > b[j + 1]:
			temp = b[j]
			b[j] = b[j + 1]
			b[j + 1] = temp
	maximum -= 1

print b	
print ("---%s seconds---" % (time.time() - start_time))

