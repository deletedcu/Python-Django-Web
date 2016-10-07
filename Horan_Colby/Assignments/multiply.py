def multiply(a, num):
	for x in range(0, len(a)):
		a[x] = a[x] * num
	return a
a = [2, 4, 10,16]
print multiply(a, 5)	