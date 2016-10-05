import time, random

#my_array = [9,8,7,6,5,6,7]
my_array = [int(1000*random.random()) for i in xrange(100)]

def selection_sort(arr):
	print "start array:", arr
	start_time = time.time()
	capture = 0
	min_val = arr[0]
	how_many_ifs = 0
	for i in range(len(arr)-1):
		min_val = arr[i]
		capture = i
		for j in range(i,(len(arr))):
			if min_val > arr[j]:
				capture = j
				min_val = arr[j]
				how_many_ifs +=1
			#print i, j, i, arr, min_val, capture
		(arr[i],arr[capture]) = (arr[capture],arr[i])
	print time.time()-start_time
	print "ending array:", arr	
	print "how many ifs?", how_many_ifs


selection_sort(my_array)