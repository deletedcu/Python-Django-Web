def grade(score):
        if score < 60:
            print 'Score: ' + str(score) + '; Your grade is undefined.'
        elif score > 101:
            print 'Score: ' + str(score) + '; Your grade is undefined.'
        elif score >= 60 and score <=69:
            print 'Score: ' + str(score) + '; Your grade is D.'
        elif score >= 70 and score <=79:
            print 'Score: ' + str(score) + '; Your grade is C.'
        elif score >= 80 and score <=89:
            print 'Score: ' + str(score) + '; Your grade is B.'
        elif score >= 90 and score <=100:
            print 'Score: ' + str(score) + '; Your grade is A.'

print 'Welcome to Scores and Grades'
count = 0
while count < 10:
    score = input('Please enter test score between 60-100.')
    grade(score)
    count = count + 1

print 'Sweet, you entered all the test scores! Bye!'
