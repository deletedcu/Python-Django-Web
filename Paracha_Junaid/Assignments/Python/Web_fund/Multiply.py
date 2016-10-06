def multi(x,y):
	return x*y
def multiplier(a,x):
	i = 0
	while (i < len(a)):
		a[i] = multi(a[i],x)
		i += 1
	return a

a = [2,4,10,16]
b = multiplier(a,5)
print b