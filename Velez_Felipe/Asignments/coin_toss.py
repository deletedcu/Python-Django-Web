import random
coin = 0
num_of_tails = 0
num_of_heads = 0

def toss_coin():
	global num_of_tails
	global num_of_heads
	# global index
	toss = round(coin)
	if toss == 0:
		num_of_tails = num_of_tails + 1
		print "attempt # " + str(index) + ": Throwing a coin... It is a tail!... Got " + str(num_of_tails) +" tail(s) so far and " + str(num_of_heads) + "head(s) so far"
	else:
		num_of_heads = num_of_heads + 1
		print "attempt #  " + str(index) + ": Throwing a coin... It is a head!... Got " + str(num_of_tails) +" tail(s) so far and " + str(num_of_heads) + "head(s) so far"
	# print coin
	# print toss

index =1
while index <= 5000:
	coin = random.random()
	toss_coin()
	index= index + 1