def grade(x):
	if 101>x>=90:
		return 'Your Grade is A'
	elif 89>=x>=80:
		return 'Your Grade is B'
	elif 79>=x>=70:
		return 'Your Grade is C'
	elif 69>=x>=60:
		return 'Your Grade is D'
	return 'not a correct value'

y = ['Score and Grade']
for i in range (0,10):
	a = input('Enter a score between 60 and 100. ->')
	x = ('Score: '+ str(a)+ ';'+ grade(a))
	y.append(x)
	i+=1

print '\n'.join(y)
print 'End of the program. Bye!'
