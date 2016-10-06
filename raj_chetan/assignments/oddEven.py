def oddEven(num):
	for var in range(1,num+1):
		if var%2==0:
			print 'the current number is', var, "This is an even number"
		else:
			print 'the current number is', var, "This is an odd number"
oddEven(100)