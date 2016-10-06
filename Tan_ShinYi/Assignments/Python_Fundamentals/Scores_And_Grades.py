scores=[]

def scores_and_grades():
    for counter in range(0,10,1):
        score=raw_input('Please enter a test score (60-100): ')
        while int(score)>100 or int(score)<60:
            score=raw_input('Error: Incorrect Input. Please enter a test score (0-100): ')
        score = int(score)
        scores.append(score)

    print 'Scores and Grades'
    grade='None'
    for counter in range(len(scores)):
        if scores[counter]>89:
            grade='A'
        elif scores[counter]>79:
            grade='B'
        elif scores[counter]>69:
            grade='C'
        else:
            grade='D'

        print 'Score: {}; Your grade is {}'.format(scores[counter], grade)

    print 'End of the program. Bye!'

scores_and_grades()
