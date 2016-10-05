def scores():
	for var in range (5):
		user_val = int(raw_input("Please enter a integer score in the range 60-100: "))
		if 90<=user_val<=100:
			print 'Score', user_val, 'Your grade is an A'
		elif 80<=user_val<90:
			print 'Score', user_val, 'Your grade is a B'
		elif 70<=user_val<80:
			print 'Score', user_val, 'Your grade is a C'
		elif 60<=user_val<70:
			print 'Score', user_val, 'Your grade is a D'
		else:
			print "You are terrible at following directions. You get an F"

scores()