for count in range(0, 10):
	score = input("PUT THE THING HERE = ")
	if(score <= 69):
		grade = "D"
	elif(score <= 79):
		grade = "C"
	elif(score <= 89):
		grade = "B"
	else:
		grade = "A"
	print "score = {}; grade = {}".format(score,grade)
