'''

Create a function called 'multiply' that reads each value in a list 
and returns a list where each value has been multiplied by 5.

'''

def multiply(input, multiplier):
	newList = []

	for index in range(len(input)):
		newList.append(input[index] * multiplier)

	return newList

a = [2, 4, 10, 16]
b = multiply(a, 5)
print b
