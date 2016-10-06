def scores_and_grades(grade):
	user_input = int(grade)
	if 60 > user_input or user_input > 100:
		print 'grade must be above 60'
	if 60 <= user_input < 70:
		print 'Score: ' + str(user_input) + '; Your grade is D'
	elif 70 <= user_input < 80:
		print 'Score: ' + str(user_input) + '; Your grade is C'
	elif 80 <= user_input < 90:
		print 'Score: ' + str(user_input) + '; Your grade is B' 
	elif 90 <= user_input <= 100:
		print 'Score: ' + str(user_input) + '; Your grade is A'
index = 0

while index <= 10:
	input_grade = raw_input()
	index= index + 1
	scores_and_grades(input_grade)
