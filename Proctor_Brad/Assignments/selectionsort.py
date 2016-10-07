import random
b = []
for x in range(0,100):
    b.append(int(random.random()*10000))

counter = 0
start = 0
end = 100
for i in range(0,100):
    for j in range(start,100):
        if b[j] < b[i]:
            temp = b[i]
            b[i] = b[j]
            b[j] = temp
            counter += 1
    start += 1

print b
print 'Number of if/else checks:',counter
