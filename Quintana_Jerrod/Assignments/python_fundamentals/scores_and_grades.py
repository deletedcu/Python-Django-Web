
def scores_grades():
    print 'Enter 10 grades between 60 and 100'
    for element in range(0,10):
        a = input()
        grade = ''
        if (a > 89):
            grade = 'A'
        elif ( 90 > a > 79):
            grade = 'B'
        elif ( 80 > a > 69):
            grade = 'C'
        else:
            grade = 'D'
        print 'Score: {}; Your grade is {}'.format(a,grade)
scores_grades()

'''
second attempt below

def scores_grades():
    print 'Please input 10 grades between 60 and 100'
    for i in range (0, 10):
        score = input()
        grade = ''
        if score > 89:
            grade = 'A'
        elif 90 > score > 79:
            grade = 'B'
        elif 80 > score > 69:
            grade = 'C'
        else:
            grade = 'D'
        print 'Score: {}; Your grade is {}'.format(score, grade)
    print 'End of program. Bye!'
scores_grades()
'''
