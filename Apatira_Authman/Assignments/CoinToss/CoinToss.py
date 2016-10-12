def CoinToss():
	import random
	newArr = []	
	tails = 0
	heads = 0
	for count in range(1000):
		random_num = random.random()
		newArr.append(round(random_num))
	for count in range(len(newArr)):
		if(newArr[count] > 0):
			heads += 1
		elif(newArr[count] == 0):
			tails += 1
	print 'Number of Head Tosses: ', heads
	print 'Number of Tails Tosses: ', tails
	

