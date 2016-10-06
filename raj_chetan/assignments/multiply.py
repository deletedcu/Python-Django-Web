a = [2,4,10,16]
def multiply(arr, num):
	new_list = []
	for var in arr:
		new_list.append(var*num)
	return new_list
print multiply(a, 5)

'''	
	for var in range(len(arr)):
		arr[var] *= 5
	return arr
'''