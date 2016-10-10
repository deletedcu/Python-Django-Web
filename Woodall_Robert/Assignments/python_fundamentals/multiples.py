'''

Part 1:
Create a program that prints all the odd numbers from 1 to 1000. Use the for loop and don't use array to do this exercise.

Part 2:
Create another program that prints all the multiples of 5 from 5 to 1000000

'''

print "Printing odd values from 1 - 1000..."

for counter in range(1, 1000):
	if (counter % 2) != 0:
		print counter

print "\nPrinting multiples of 5 from 5 - 1000000..."

for counter in range(5, 1000001):
	if (counter % 5) == 0:
		print counter
		