x = [4,6,1,3,5,7,25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(x):
	index = 0
	while index < len(x):
		if type(x[index])is str:
			first_letter = x[index].lower()
			print first_letter[0] * len(first_letter)
		else:
			print "*" * x[index]
		index = index + 1
draw_stars(y)


	