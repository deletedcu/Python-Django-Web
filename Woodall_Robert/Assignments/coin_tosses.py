'''

Create a program that simulates tossing a coin 5,000 times. 
Your program should display how many times the head/tail appears.

'''

import random

head_count = 0
tail_count = 0
string_result = 'invalid'

print('Lets start tossing that coin...')

for index in range(1, 5001):
	toss_result = round(random.random())

	if (toss_result == 1): # heads
		head_count += 1
		string_result = 'heads'
	else:
		tail_count += 1
		string_result = 'tails'

	print('Coin Toss {}: {} -> [ total heads: {}, total tails {}]'.format(index, string_result, head_count, tail_count))

print('5000 tosses, you must be tired...let\'s stop now.')
