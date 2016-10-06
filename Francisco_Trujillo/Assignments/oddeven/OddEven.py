# Program will go from 1 to 2000 and it will indicate whether the number is odd or even
def oddEven():
    for count in range (1,2001):
        if count%2==0:
            print 'Number is '+ str(count)+ '. This is an Even number'
        else:
            print 'Number is '+ str(count)+ '. This is an Odd number'

print oddEven()
