import random

a = 0
b = 0

def coin_tosses():
    global a
    global b
    random_num = random.random()
    x_rounded = round(random_num)
    print x_rounded
    if x_rounded == 0:
        a = a + 1
        print 'Attempt # ' + str(index) + ': Throwing a coin... It is a tail!... Got ' + str(a) + ' head(s) so far and '  + str(b) + ' tail(s) so far' 
    else:
        b = b + 1
        print 'Attempt # ' + str(index) + ': Throwing a coin... It is a head!... Got ' + str(a) + ' head(s) so far and '  + str(b) + ' tail(s) so far'  
index = 1
while index <= 5000:
    coin_tosses()
    index = index + 1
    