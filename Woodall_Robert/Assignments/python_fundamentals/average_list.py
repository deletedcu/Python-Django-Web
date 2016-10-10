# Create a program that prints the average of the values in the list
a = [1, 2, 5, 10, 255, 3]
sumOfList = 0

for value in a:
	sumOfList += value

print sumOfList / len(a)
