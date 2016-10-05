def odd_even():
    for number in range (1, 2001):
        if (number % 2 == 0):
            print 'Number is {}. This is an even number.'.format(number)
        else:
            print 'Number is {}. This is an odd number.'.format(number)
odd_even()

'''
this is my second attempt
def odd_even():
    for i in range (1, 2001):
        number = ''
        if i % 2 == 0:
            number = 'even'
        else:
            number = 'odd'
        print 'Number is {}. This is an {} number.'.format(i, number)
odd_even()
'''
