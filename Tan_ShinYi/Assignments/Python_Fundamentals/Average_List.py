a = [1, 2, 5, 10, 255, 3]
total=0

for i in range(len(a)):
    total += a[i]
print total/len(a)

'''
for count in a[0:6]:
    total += a[count]
print count/len(a)
'''
