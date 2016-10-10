'''
Create a function that counts from 1 to 2000 
and specifies the value as odd or even

'''

def oddOrEven():
	for index in range(1, 2001):
		if (index % 2) == 0:
			print 'Number is ' + str(index) + '. This is an even number'
		else:
			print 'Number is ' + str(index) + '. This is an odd number'

oddOrEven()
