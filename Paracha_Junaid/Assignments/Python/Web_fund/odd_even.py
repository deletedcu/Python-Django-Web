
def even_odd (x):
	if x % 2 == 0:
		return ('even')
	return ('odd')
i = 1
while i < 2000:
	print 'Number is '+str(i)+'. This is an ' + even_odd(i)+' number.'
	i = i+1


