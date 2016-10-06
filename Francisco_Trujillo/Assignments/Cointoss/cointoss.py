import random
heads = 0
tails = 0
toss= random.random()

num = input("Enter number of Tosses: ")
num+=1
for num in range (1, num):
    toss= random.random()
    if toss >=0.50:
        heads+=1
    else:
        tails+=1

    print 'Attempt'+ str(num) + " : Throwing a coin... It's a head! ... Got "+ str(heads) + "head(s) so far and "+str(tails)+ " tail(s) so far "

print "Attempt "+ str(heads+tails) + " : Throwing a coin... It's a head! ... Got "+ str(heads) + "head(s) so far and "+str(tails)+ " tail(s) so far. Ending the program, thank you!"
