'''

Part 1:
Create a function called  draw_stars() that takes a list of numbers 
and prints out '*'' for the number of times of the given value.

Part 2:
Modify the function above. 
Allow a list containing integers and strings to be passed to the  
draw_stars() function. When a string is passed, instead of  displaying *,
display the first letter of the string for as long as the string length.

'''

def drawStars(input):
	for value in input:
		if type(value) is int:
			print('*' * value)
		elif type(value) is str:
			print(value[:1].lower() * len(value))


x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
drawStars(x)
drawStars(y)
