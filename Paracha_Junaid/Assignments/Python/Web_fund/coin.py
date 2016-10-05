head=0
tail=0
print 'starting the Program'
for i in range (1,51):
	import random
	random_num = round(random.random())
	if random_num == 0:
		head += 1
		print "Attempt#"+str(i)+" Throwing a coin... It's head! ...Got " + str(head) + "head(s) so far and "+str(tail)+" tail(s) so far"
		i+=1
	else: 
		tail += 1
		print "Attempt#"+str(i)+" Throwing a coin... It's tail! ...Got " + str(head) + "head(s) so far and "+str(tail)+" tail(s) so far"
		i+=1
print 'ending the program'