'''

Create a program that prompts the user ten times for a test score between 60 and 100. 
Each time a score is generated, your program should display what is the grade of that score. 

'''

def determineLetterGrade(score):
	grade = 'invalid'

	if score < 60:
		grade = 'F'
	elif score >= 60 and score < 70:
		grade = 'D'
	elif score >= 70 and score < 80:
		grade = 'C'
	elif score >= 80 and score < 90:
		grade = 'B'
	elif score >= 90 and score <= 100:
		grade = 'A'

	return grade

print('Scores and Grades\n')

for index in range(10):
	score = raw_input('Enter Score: ')
	print('Your grade is ' + determineLetterGrade(int(score)))

print('\nEnd of the program. Bye!')
