head = 0
tail = 0
import random
for element in range (1, 5001):
    toss = round(random.random())
    if (toss == 1):
        head += 1
        toss_text='head'
    else:
        tail += 1
        toss_text = 'tail'
    print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(element,toss_text,head,tail)
print 'Ending the program, thank you!'
