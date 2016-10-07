import random
import datetime

def bubble_sort(list):
	start = datetime.datetime.now()

	for i in range(len(list)):
		for j in range(len(list) - 1):
			if (list[j] > list[j + 1]):
				(list[j], list[j + 1]) = (list[j + 1], list[j]) # tuple swap

	end = datetime.datetime.now()

	return end - start

# create list of random values
sampleList = []

for index in range(100):
	sampleList.append(random.randint(0, 10001))

print('sampleList before bubble_sort():\n' + str(sampleList))
executionTime = bubble_sort(sampleList)
print('\nsampleList after bubble_sort():\n' + str(sampleList))
print('\ntotal execution time (hh:mm:ss.microsecs): ' + str(executionTime))
