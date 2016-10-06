import random
import time

my_arr = [int(1000*random.random()) for i in xrange(20)]

def bubble_sort(arr):
	start = time.time()
	counter = 0
	for do_times in range(len(arr)):
		counter +=1
		for count in range(0, len(arr)-counter):
			if arr[count] > arr[count+1]:
				(arr[count], arr[count+1]) = (arr[count+1], arr[count])
			print arr
	end = time.time()
	print end - start
bubble_sort(my_arr)