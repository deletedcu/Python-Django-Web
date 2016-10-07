import random
import datetime

# NEEDS TO BE OPTIMIZED TO FIND MIN AND MAX AND SWAP AFTER EACH ITERATION
# Playing catch up so will accomplish above when time exists

def selection_sort(list):
	start = datetime.datetime.now()

	for i in range(len(list)):
		minIndex = i

		for j in range(i, len(list)):
			if list[j] < list[minIndex]:
				minIndex = j

		#print('List before swap: ' + str(list))
		# swap values at minIndex and i
		(list[minIndex], list[i]) = (list[i], list[minIndex])
		#print('List after swap: ' + str(list))

	end = datetime.datetime.now()

	return end - start

# create list of random values
sampleList = []

for index in range(10000):
	sampleList.append(random.randint(0, 10001))

print('sampleList before sort: ' + str(sampleList))
execution_time = selection_sort(sampleList)
print('sampleList after sort: ' + str(sampleList))
print('\ntotal execution time (hh:mm:ss.microsecs): ' + str(execution_time))