import random
def coinToss(toss):
	head_count = 0
	tail_count = 0
	for var in range(toss+1):
		dice = int(round(random.random()))
		if dice == 1:
			head_count+=1
			print "Attempt #{}. You rolled a heads!. You have rolled {} head(s) and {} tail(s) in {} rolls thus far.".format(var, head_count, tail_count, var)
		else:
			tail_count+=1
			print "Attempt #{}. You rolled a tails!. You have rolled {} head(s) and {} tail(s) in {} rolls thus far.".format(var, head_count, tail_count, var)

coinToss(500)