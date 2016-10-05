import random
tails = 0
heads = 0
for count1 in range(1, 5001):
	x = random.random()
	round(x)
	if(x == 0):
		heads += 1
		print 'Attempt #' + count1 ': Throwing a coin... Its a head!  .... Got ' + heads + 'head(s) so far and' + tails + 'tail(s) so far'
	else: 	
		tails += 1
		print 'Attempt #' + count1 ': Throwing a coin... Its a head!  .... Got ' + heads + 'head(s) so far and' + tails + 'tail(s) so far'
