# creates a program that will show the Letter Grade
def gradeTransform(grade):
    if grade >= 90:
        print 'Score '+str(grade)+'; your grade is A'
    elif grade >= 80:
        print 'Score '+str(grade)+'; your grade is B'
    elif grade >= 70:
        print 'Score '+str(grade)+'; your grade is C'
    elif grade >= 60:
        print 'Score '+str(grade)+'; your grade is D'
    else:
        print 'Score '+str(grade)+'; your grade is F'

print 'Hello Please enter your numerical grade to calculate your Letter Grade. To quit the program please type -1'
grade =input('What is your grade? ')
while grade !=-1:
    gradeTransform(grade)
    grade=input('What is your grade? ')
print('\nEnd of the program. Bye!')
