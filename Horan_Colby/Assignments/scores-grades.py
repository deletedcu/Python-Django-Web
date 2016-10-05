x = 0
print 'Enter a test score between 60 and 100:'
while x < 10:
	score = input()
	if (score < 60):
		print "Score:", score, "You can't follow directions, and you are stupid"
	elif (score >= 60 and score < 70):
		print "Score:", score, 'Your grade is D'
	elif (score >= 70 and score < 80):
		print "Score:", score, 'Your grade is C'
	elif (score >= 80 and score < 90):
		print "Score:", score, 'Your grade is B'
	else:
		print "Score:", score, 'Your grade is A'
	x = x + 1
print 'End of the program. KayBaiiiiiiiiiiii!'