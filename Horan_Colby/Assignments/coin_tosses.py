import random
heads = 0
tails = 0
for x in range(1,5001):
	coin = random.random()
	coinround = round(coin)
	if (coinround == 1):
		coinround = 'heads'
		heads = heads + 1
	else:
		coinround = 'tails'
		tails = tails + 1
	print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} heads so far and {} tails so far".format(x, coinround, heads, tails)




