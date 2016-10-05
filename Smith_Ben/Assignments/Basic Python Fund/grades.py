
def grades(count):
	if(count < 101 and count > 89):
		print 'Score: ' + str(count) + '; Your grade is A.'
	elif(count < 90 and count > 79):
		print 'Score: ' + str(count) + '; Your grade is B.'
	elif(count < 80 and count > 69):
		print 'Score: ' + str(count) + '; Your grade is C.'
	elif(count < 70 and count > 59):
		print 'Score: ' + str(count) + '; Your grade is D.'
	else:
		print 'Score: ' + str(count) + '; Your grade is F.'				
poop = 0
while poop < 10:
	x = input('What was your score?')
	grades(x)
	poop = poop + 1


