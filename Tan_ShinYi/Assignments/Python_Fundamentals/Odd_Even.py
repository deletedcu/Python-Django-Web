for counter in range(1,2001,1):
    if counter%2 == 0:
        state = 'even'
    else:
        state = 'odd'

    print 'Number is {}. Thsi is an {} number.'.format(counter,state)
