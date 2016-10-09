arr = [5,8,7,9,3,2,6,1,4]

def sorter(x):
	temp =0
	lent = len(x)-1
	
	for t in x:
		for i in range(0,lent):
			if x[i] > x[i+1]:
				temp = x[i]
				x[i] = x[i+1]
				x[i+1] = temp
				

sorter(arr)
print (arr)