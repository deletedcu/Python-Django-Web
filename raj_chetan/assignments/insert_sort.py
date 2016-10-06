my_array = [4,7,3,5,2]

def insertionSort(arr):
	print arr
	for index in range(1,len(arr)):
		test_value = arr[index]
		position = index
		while position > 0 and arr[position-1] > test_value:
			arr[position] = arr[position-1]
			position -= 1

		arr[position] = test_value
		print arr


insertionSort(my_array)