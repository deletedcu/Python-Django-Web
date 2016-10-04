def scoresAndgrades(score):
	score = int(score)
	print 'Scores and Grades'
	if score < 70:
		print 'Score: ', str(score), '; Your grade is D'
	elif score < 80 and score >= 70:
		print 'Score ', str(score), '; Your grade is C'
	elif score < 90 and score >= 80:
		print 'Score ', str(score), '; Your grade is B'
	elif score <= 100 and score >= 90:
		print 'Score ', str(score), '; Your grade is A'
i = 0
while i < 10:
	user_input = raw_input('score: ')
	scoresAndgrades(user_input)
	i = i + 1
print 'End of the program. Bye!'
