import random

b = []
for x in range(0,100):
	b.append(int(random.random()*10000))

minimum = 0

for j in range(0,100):
	for i in range(minimum,100):
		if b[i] < b[j]:
			temp = b[i]
			b[i] = b[j]
			b[j] = temp
	minimum += 1

print b	
