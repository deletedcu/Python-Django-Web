def count():
	for x in range(1, 2001):
		if x % 2 == 1:
			print 'Number is', x, 'This is an odd number.'
		else:
			print 'Number is', x, 'This is an even number.'
print count()